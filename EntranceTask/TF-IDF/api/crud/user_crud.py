from api.schemas.user_schema import UserCreate
from models.user import users
from api.utils.security import hash_password
from typing import Optional
from api.db import database

async def create_user(user: UserCreate) -> Optional[dict]:
    hashed_pw = hash_password(user.password)
    query = users.insert().values(username=user.username, password_hash=hashed_pw, email=user.email)
    try:
        last_record_id = await database.execute(query)
        return {"id": last_record_id, "username": user.username, "email": user.email}
    except Exception as e:
        print(f"User creation error: {e}")
        return None

async def get_user_by_id(user_id: int) -> Optional[dict]:
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)

async def get_user_by_username(username: str) -> Optional[dict]:
    query = users.select().where(users.c.username == username)
    return await database.fetch_one(query)

async def get_user_by_useremail(email: str) -> Optional[dict]:
    query = users.select().where(users.c.email == email)
    return await database.fetch_one(query)

async def update_user(user_id: int, new_data: dict) -> Optional[dict]:
    if "password" in new_data:
        new_data["password_hash"] = hash_password(new_data.pop("password"))
    query = users.update().where(users.c.id == user_id).values(**new_data).returning(*users.c)
    return await database.fetch_one(query)

async def delete_user(user_id: int) -> Optional[dict]:
    query = users.delete().where(users.c.id == user_id).returning(*users.c)
    return await database.fetch_one(query)
