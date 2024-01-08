from jose import jwt, ExpiredSignatureError, JWTError
from fastapi import status, HTTPException
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("TOKEN_SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
EXPIRATION_TIME = timedelta(hours=int(os.getenv("EXPIRATION_TIME")))


async def create_user_token(data: dict):
    expiration = datetime.utcnow() + EXPIRATION_TIME
    data.update({"exp": expiration})
    token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return token
