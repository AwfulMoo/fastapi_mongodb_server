from bson import ObjectId
from typing import List, Optional
from fastapi_mongo_server.core.models.objectid_model import PyObjectId
from pydantic import BaseModel, Field, EmailStr


class UserModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    username: str
    email: EmailStr
    questionsSeen: List[str]

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        json_schema_extra = {
            "example": {
                "username": "Jane Doe",
                "email": "jdoe@example.com",
                "questionsSeen": [123456789, 987654321],
            }
        }


class UpdatedUserModel(BaseModel):
    username: Optional[str]
    email: Optional[EmailStr]
    questionsSeen: Optional[List[int]]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        json_schema_extra = {
            "example": {
                "username": "Jane Doe",
                "email": "jdoe@example.com",
                "questionsSeen": [123456789, 987654321],
            }
        }
