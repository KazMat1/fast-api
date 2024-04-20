from fastapi import APIRouter
from consts.router_const import TASK_DONE_PATH

router = APIRouter()

@router.put(TASK_DONE_PATH)
async def mark_as_done():
    pass

@router.delete(TASK_DONE_PATH)
async def unmark_as_done():
    pass
