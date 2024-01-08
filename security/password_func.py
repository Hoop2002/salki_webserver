from fastapi import status, HTTPException
from dotenv import load_dotenv
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError, InvalidHashError, VerificationError
import os
import logging
import secrets
import string

logging.basicConfig(level=logging.INFO)
hasher = PasswordHasher()
load_dotenv()

SECRET_KEY = os.getenv("PASS_SECRET_KEY")


async def password_generator(length=16, uppercase=True, digits=True, characters=False):
    alphabet = string.ascii_lowercase
    if uppercase:
        alphabet += string.ascii_uppercase
    if digits:
        alphabet += string.digits
    if characters:
        alphabet += string.punctuation

    password = "".join(secrets.choice(alphabet) for _ in range(length))

    return password


async def hash_password(password: str):
    password = password + SECRET_KEY
    return hasher.hash(password)


async def verify_password(hashed_password: str, password: str) -> bool:
    password_with_secret = password + SECRET_KEY
    try:
        hasher.verify(hash=hashed_password, password=password_with_secret)
        return True
    except VerifyMismatchError:
        logging.warning("Пароль не совпадает с хэшем.")
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Неверный пароль"
        )
    except InvalidHashError:
        logging.error("Пароль был неправильно сохранён в базе.")
        return HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Внутренняя ошибка сервера",
        )
    except VerificationError as ve:
        logging.error(f"Ошибка проверки пароля: {ve}")
        return HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Внутренняя ошибка сервера",
        )
