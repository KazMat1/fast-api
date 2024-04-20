from typing import Optional
from pydantic import BaseModel, Field

class TaskBase(BaseModel):
    title: Optional[str] = Field(None, example="クリーニングを取りに行く")

class Task(TaskBase):
    id: int
    done: bool = Field(False, description="完了フラグ")

    class Config:
        orm_mode = True

class TaskCreateRequest(TaskBase):
    pass

class TaskCreateResponse(TaskCreateRequest):
    id: int

    class Config:
        orm_mode = True

class TaskUpdateRequest(TaskCreateRequest):
    pass

class TaskUpdateResponse(TaskCreateResponse):
    pass
