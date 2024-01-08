from sqlalchemy import select
from database import get_session
from models import TokenAuth


async def get_admin_token_auth(token: str):
    async with get_session() as session:
        stmt = select(TokenAuth).filter_by(token=token)
        result = await session.execute(stmt)
        return result.scalar_one_or_none()
