from database import get_session
from models import User
from sqlalchemy import insert


async def create_user(data: dict):
    async with get_session() as session:
        stmt = insert(User).values(data).returning(User)
        output = await session.execute(stmt)
        output_ = output.scalar_one_or_none()
        return output_
