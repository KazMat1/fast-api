from fastapi import APIRouter
from consts.router_const import TASK_PATH, TASK_ID_PATH

router = APIRouter()

@router.get(TASK_PATH)
async def list():
    pass

@router.post(TASK_PATH)
async def create():
    pass

@router.put(TASK_ID_PATH)
async def update():
    pass

@router.delete(TASK_ID_PATH)
async def delete():
    pass
