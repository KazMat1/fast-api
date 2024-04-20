from fastapi import APIRouter, Depends

from api.consts.router_const import TASK_DONE_PATH
import api.services.done as done_service
import api.schemas.done as done_schema
from api.db import get_db
import api.utils.handler as response_handler

from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

@router.put(TASK_DONE_PATH, response_model=done_schema.DoneResponse)
async def mark_as_done(task_id: int, db: AsyncSession = Depends(get_db)):
    done = await done_service.get_done(db, task_id)
    response_handler.conflict(done)

    return await done_service.create_done(db, task_id);

@router.delete(TASK_DONE_PATH, response_model=None)
async def unmark_as_done(task_id: int, db: AsyncSession = Depends(get_db)):
    done = await done_service.get_done(db, task_id);
    response_handler.not_found(done)

    return await done_service.delete_done(db, done)
