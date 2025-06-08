from pydantic import BaseModel, Field, validator
import re
from typing import Optional

class UserCreate(BaseModel):
    email: str = Field(
        ...,
        title="Email",
        description="User email, must be a valid Gmail address",
        max_length=50,
        example="user@gmail.com",
        pattern=r"^[a-zA-Z0-9._%+-]+@gmail\.com$"
    )
    username: str = Field(
        ...,
        title="Username",
        description="Unique username, minimum 3 and maximum 30 characters",
        min_length=3,
        max_length=30,
        example="john_doe")
    password: str = Field(
        ...,
        title="Password",
        description="Password with minimum length of 6 characters",
        min_length=6,
        example="strongpassword123"
    )

class UserUpdate(BaseModel):
    email: Optional[str] = Field(
        None,
        max_length=50,
        example="user@gmail.com"
    )
    username: Optional[str] = Field(
        None,
        min_length=3,
        max_length=30,
        example="john_doe"
    )
    password: Optional[str] = Field(
        None,
        min_length=6,
        example="newpassword123"
    )

    @validator("email")
    def validate_gmail(cls, v):
        if v and not re.match(r"^[a-zA-Z0-9._%+-]+@gmail\.com$", v):
            raise ValueError("Only Gmail addresses are allowed")
        return v
class UserRead(BaseModel):
    id: int = Field(..., title="User ID", example=1)
    username: str = Field(..., title="Username", example="john_doe")
    email: str = Field(..., title="Email", example="user@gmail.com")

    class Config:
        from_attributes  = True
