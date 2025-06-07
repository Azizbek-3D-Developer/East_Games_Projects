from api.schemas.user_schema import UserCreate
from models.user import users
from api.utils.security import hash_password
from databases import Database
from typing import Optional
from api.db import database

async def create_user(user: UserCreate) -> Optional[dict]:
    hashed_pw = hash_password(user.password)
    query = users.insert().values(username=user.username, password_hash=hashed_pw, email = user.email)
    try:
        last_record_id = await database.execute(query)
        return {"id": last_record_id, "username": user.username, "email": user.email}
    except Exception as e:
        print(f"User creation error: {e}")
        return None

async def get_user_by_username(username: str) -> Optional[dict]:
    query = users.select().where(users.c.username == username)
    user = await database.fetch_one(query)
    return user


async def get_user_by_useremail(email: str) -> Optional[dict]:
    query = users.select().where(users.c.email == email)
    user = await database.fetch_one(query)
    return user