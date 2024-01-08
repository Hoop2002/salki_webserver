from pydantic import BaseModel, EmailStr
from typing import Dict, Any, List
from datetime import datetime


class RequestUserSignUp(BaseModel):
    email: EmailStr
    username: str
    password: str
