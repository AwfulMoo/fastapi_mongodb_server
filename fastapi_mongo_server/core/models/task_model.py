from bson import ObjectId
from typing import Optional
from fastapi_mongo_server.core.models.objectid_model import PyObjectId
from pydantic import BaseModel, Field


class TaskModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    task: str
    helpText: Optional[str]
    adultTask: Optional[bool] = False

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        json_schema_extra = {
            "example": {
                "task": "This is an example task",
                "helpTest": "This is additonal text about the task outside of the main text",
                "adultTask": False
            }
        }


class UpdateTaskModel(BaseModel):
    task: str
    helpText: Optional[str]
    adultTask: Optional[bool] = False

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        json_schema_extra = {
            "example": {
                "task": "This is an example task",
                "helpTest": "This is additonal text about the task outside of the main text",
                "adultTask": False
            }
        }
