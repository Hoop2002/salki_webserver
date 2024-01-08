from pydantic import BaseModel, EmailStr
from typing import Dict, Any, List
from datetime import datetime


class ResponseToken(BaseModel):
    access_token: str
    token_type: str = "bearer"


class RequestUserSignUp(BaseModel):
    email: EmailStr
    password: str
