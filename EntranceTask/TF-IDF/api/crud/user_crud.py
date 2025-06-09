from api.schemas.user_schema import UserCreate
from models.user import users
from api.utils.security import hash_password
from typing import Optional
from api.db import database
from api.utils.logger import logger

# Creating the user
async def create_user(user: UserCreate) -> Optional[dict]:
    # encoding the password
    hashed_pw = hash_password(user.password)
    query = users.insert().values(username=user.username, password_hash=hashed_pw, email=user.email)
    try:
        # inserting new user into database
        last_record_id = await database.execute(query)
        return {"id": last_record_id, "username": user.username, "email": user.email}
    except Exception as e:
        print(f"User creation error: {e}")
        logger.error(f"User creation error: {e}")
        return None

# Get by id 
async def get_user_by_id(user_id: int) -> Optional[dict]:
    # search for the id
    query = users.select().where(users.c.id == user_id)
    try:
        result = await database.fetch_one(query)
        return result 
    except Exception as e:
        print(f"Error in get by id in users: {e}")
        logger.error(f"Error in get by id in users: {e}")
        return None

# Get user by username  
async def get_user_by_username(username: str) -> Optional[dict]:
    # search for the username
    query = users.select().where(users.c.username == username)
    try:
        result = await database.fetch_one(query)
        return result 
    except Exception as e:
        print(f"Error in get by username in users: {e}")
        logger.error(f"Error in get by username in users: {e}")
        return None

# Get user by useremail
async def get_user_by_useremail(email: str) -> Optional[dict]:
    # search for the useremail
    query = users.select().where(users.c.email == email)
    try:
        result = await database.fetch_one(query)
        return result 
    except Exception as e:
        print(f"Error in get by useremail in users: {e}")
        logger.error(f"Error in get by useremail in users: {e}")
        return None

# Update the user
async def update_user(user_id: int, new_data: dict) -> Optional[dict]:
    try:
        if "password" in new_data:
            new_data["password_hash"] = hash_password(new_data.pop("password"))
        query = users.update().where(users.c.id == user_id).values(**new_data).returning(*users.c)
        result = await database.fetch_one(query)
        return result 
    except Exception as e:
        print(f"User update error: {e}")
        logger.error(f"User update error: {e}")
        return None

# Delete the user
async def delete_user(user_id: int) -> Optional[dict]:
    try:
        query = users.delete().where(users.c.id == user_id).returning(*users.c)
        result = await database.fetch_one(query)
        return result 
    except Exception as e:
        print(f"User delete error: {e}")
        logger.error(f"User delete error: {e}")
        return None
