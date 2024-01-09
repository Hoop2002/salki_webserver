from jose import jwt, ExpiredSignatureError, JWTError
from fastapi import status, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from dotenv import load_dotenv
from models.response_models import TokenData
import os

load_dotenv()

SECRET_KEY = os.getenv("TOKEN_SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
EXPIRATION_TIME = timedelta(days=int(os.getenv("EXPIRATION_TIME")))
KID = "1"

user_oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/sign-in")


async def create_user_token(user_id: str) -> str:
    expiration = datetime.utcnow() + EXPIRATION_TIME

    data = {
        "sub": user_id,
        "exp": expiration,
        "iss": "salki.org",
    }
    headers = {"kid": KID}

    token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM, headers=headers)

    return token


async def verify_user_token(token: str = Depends(user_oauth2_scheme)) -> str:
    try:
        payload = jwt.decode(token, key=SECRET_KEY, algorithms=[ALGORITHM])
        token_data = TokenData(**payload)
        return token_data.model_dump()
    except ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Токен просрочен"
        )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Недействительный токен"
        )


from routers.auth.func.get_user import get_user_by_id


async def get_user_via_JWT(token: str = Depends(user_oauth2_scheme)):
    decoded_data = await verify_user_token(token)
    if not decoded_data:
        raise HTTPException(status_code=400, detail="Invalid token")

    user = await get_user_by_id(decoded_data["sub"])

    if not user:
        raise HTTPException(status_code=400, detail="User not found")

    return user
