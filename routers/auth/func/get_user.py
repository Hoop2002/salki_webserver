from database import get_session
from sqlalchemy.future import select
from models import User


async def get_user_by_email(email: str):
    async with get_session() as session:
        result = await session.execute(select(User).filter_by(email=email))
        return result.scalar_one_or_none()


async def get_user_by_id(user_id: str):
    async with get_session() as session:
        result = await session.execute(select(User).filter_by(user_id=user_id))
        return result.scalar_one_or_none()
