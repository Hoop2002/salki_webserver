from fastapi import APIRouter, HTTPException, status
from models import RequestUserSignUp, ResponseToken

router = APIRouter()


@router.post("/api/v1/sign-up", response_model=ResponseToken)
async def user_sign_up(user_data: RequestUserSignUp):
    return {}
