from database import get_session
from models import User
from security import hash_password


async def create_user(data: dict):
    async with get_session() as session:
        password = data.pop("password")
        password_hash_ = await hash_password(password)
        data.update({"password_hash": password_hash_})

        created_user = User(**data)    
        session.add(created_user)
        
        await session.commit()
        await session.flush(created_user)

        return created_user
