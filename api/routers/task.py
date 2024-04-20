from fastapi import APIRouter
from typing import List
from api.consts.router_const import TASK_PATH, TASK_ID_PATH
import api.schemas.task as task_schema

router = APIRouter()

@router.get(TASK_PATH, response_model=List[task_schema.Task])
async def list():
    return [task_schema.Task(id=1, title='一つ目のTodoタスク')]

@router.post(TASK_PATH, response_model=task_schema.TaskCreateResponse)
async def create(task_body: task_schema.TaskCreateRequest):
    return task_schema.TaskCreateResponse(id=1, **task_body.dict())

@router.put(TASK_ID_PATH, response_model=task_schema.TaskUpdateResponse)
async def update(task_id: int, task_body: task_schema.TaskUpdateRequest):
    return task_schema.TaskUpdateResponse(id=1, **task_body.dict())

@router.delete(TASK_ID_PATH, response_model=None)
async def delete(task_id: int):
    return
