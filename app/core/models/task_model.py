from bson import ObjectId
from typing import Optional
from app.core.models.objectid_model import PyObjectId
from pydantic import BaseModel, Field


class TaskModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    task: str
    helpText: Optional[str]
    adultTask: Optional[bool] = False

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
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
        schema_extra = {
            "example": {
                "task": "This is an example task",
                "helpTest": "This is additonal text about the task outside of the main text",
                "adultTask": False
            }
        }
