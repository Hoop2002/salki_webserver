from fastapi import APIRouter, HTTPException, status, Request
from models import RequestUserSignUp, ResponseToken
from .func import create_user, get_user_by_email, get_admin_token_auth

from security import hash_password, verify_password, password_generator

router = APIRouter()


@router.post("/api/v1/sign-up")
async def user_sign_up(user_data: RequestUserSignUp, request: Request):
    token = request.headers.get("Authorization", False)
    if not token:
        return HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Token invalid",
        )

    check_token = await get_admin_token_auth(token=token)

    if not check_token:
        return HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Token invalid",
        )

    data = user_data.model_dump()
    user = await get_user_by_email(data["email"])

    if user:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Пользователь с таким email уже существует",
        )

    return {}


@router.post("/api/v1/sign-in")
async def user_sign_in(user_data: RequestUserSignUp, request: Request):
    token = request.headers.get("Authorization", False)
    if not token:
        return HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Token invalid",
        )

    check_token = await get_admin_token_auth(token=token)

    if not check_token:
        return HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Token invalid",
        )
    return ResponseToken(access_token="fake")


@router.post("/api/v1/sign-out")
async def user_sign_out(user_data: RequestUserSignUp, request: Request):
    token = request.headers.get("Authorization", False)
    if not token:
        return HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Token invalid",
        )

    check_token = await get_admin_token_auth(token=token)

    if not check_token:
        return HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Token invalid",
        )
    return ResponseToken(access_token="fake")
