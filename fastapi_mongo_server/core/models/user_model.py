from bson import ObjectId
from typing import List, Optional
from fastapi_mongo_server.core.models.objectid_model import PyObjectId
from pydantic import BaseModel, ConfigDict, Field, EmailStr


class UserModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True, arbitrary_types_allowed=True, json_encoders={ObjectId: str}, json_schema_extra = {
            "example": {
                "username": "Jane Doe",
                "email": "jdoe@example.com",
                "questionsSeen": [123456789, 987654321],
            }
        }
    )

    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    username: str
    email: EmailStr
    questionsSeen: List[str]


class UpdatedUserModel(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True, json_encoders={ObjectId: str}, json_schema_extra = {
                "example": {
                    "username": "Jane Doe",
                    "email": "jdoe@example.com",
                    "questionsSeen": [123456789, 987654321],
                }
            }
        )

    username: Optional[str]
    email: Optional[EmailStr]
    questionsSeen: Optional[List[int]]