from database import get_session
from sqlalchemy.future import select
from models import User


async def get_user_by_email(email: str):
    async with get_session() as session:
        result = await session.execute(select(User).filter_by(email=email))
        return result.scalar_one_or_none()
