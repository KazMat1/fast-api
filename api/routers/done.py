from fastapi import APIRouter
from api.consts.router_const import TASK_DONE_PATH

router = APIRouter()

@router.put(TASK_DONE_PATH, response_model=None)
async def mark_as_done(task_id: int):
    return

@router.delete(TASK_DONE_PATH, response_model=None)
async def unmark_as_done(task_id: int):
    return
