from fastapi import APIRouter, HTTPException, status, Request, Depends
from models import RequestUserSignUp, ResponseToken, RequestUserSignIn
from .func import create_user, get_user_by_email, get_admin_token_auth

from security import (
    hash_password,
    verify_password,
    password_generator,
    create_user_token,
    get_user_via_JWT,
)

router = APIRouter()


@router.post("/api/v1/sign-up")
async def user_sign_up(user_data: RequestUserSignUp, request: Request):
    token = request.headers.get("Authorization", False)
    if not token:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Token missing",
        )

    check_token = await get_admin_token_auth(token=token)

    if not check_token:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Wrong token",
        )

    data = user_data.model_dump()
    user = await get_user_by_email(data["email"])

    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Пользователь с таким email уже существует",
        )

    user_obj = await create_user(data)

    return user_obj


@router.post("/api/v1/sign-in")
async def user_sign_in(user_data: RequestUserSignIn, request: Request):
    token = request.headers.get("Authorization", False)
    if not token:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Token missing",
        )

    check_token = await get_admin_token_auth(token=token)

    if not check_token:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Wrong token",
        )

    data = user_data.model_dump()
    user = await get_user_by_email(data["email"])

    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Неправильный email или пароль",
        )

    await verify_password(user.password_hash, password=data["password"])

    token = await create_user_token(user.user_id)

    return ResponseToken(access_token=token)


@router.post("/api/v1/sign-out")
async def user_sign_out(user: str = Depends(get_user_via_JWT)):
    # TODO delete or blacklist jwt token
    return {"message": "Successfully logged out"}


@router.post("/test/test")
async def user_test(user: str = Depends(get_user_via_JWT)):
    return {}
