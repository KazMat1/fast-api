from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
import api.services.task as task_service
from api.consts.router_const import TASK_PATH, TASK_ID_PATH
from api.consts.response_const import RESPONSE
import api.utils.handler as response_handler
from api.db import get_db
import api.schemas.task as task_schema

router = APIRouter()

@router.get(TASK_PATH, response_model=List[task_schema.Task])
async def list(db: AsyncSession = Depends(get_db)):
    return await task_service.get_task_with_done(db)

@router.post(TASK_PATH, response_model=task_schema.TaskCreateResponse)
async def create(task_body: task_schema.TaskCreateRequest, db: AsyncSession = Depends(get_db)):
    return await task_service.create_task(db, task_body)

@router.put(TASK_ID_PATH, response_model=task_schema.TaskUpdateResponse)
async def update(task_id: int, task_body: task_schema.TaskUpdateRequest, db: AsyncSession = Depends(get_db)):
    task = await task_service.get_task(db, task_id)
    response_handler.not_found(task)

    return await task_service.update_task(db, task_body, task)

@router.delete(TASK_ID_PATH, response_model=None)
async def delete(task_id: int, db: AsyncSession = Depends(get_db)):
    task = await task_service.get_task(db, task_id)
    response_handler.not_found(task)

    return await task_service.delete_task(db, task)
