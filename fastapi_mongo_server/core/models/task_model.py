from bson import ObjectId
from typing import Optional
from fastapi_mongo_server.core.models.objectid_model import PyObjectId
from pydantic import BaseModel, ConfigDict, Field, EmailStr


class TaskModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True, arbitrary_types_allowed=True, json_encoders={ObjectId: str}, json_schema_extra = {
            "example": {
                "task": "This is an example task",
                "helpTest": "This is additonal text about the task outside of the main text",
                "complexTask": False
            }
        }
    )

    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    task: str
    helpText: Optional[str]
    complexTask: Optional[bool] = False


class UpdateTaskModel(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True, json_encoders={ObjectId: str}, json_schema_extra = {
                "example": {
                "task": "This is an example task",
                "helpTest": "This is additonal text about the task outside of the main text",
                "complexTask": False
                }
            }
        )

    task: str
    helpText: Optional[str]
    complexTask: Optional[bool] = False