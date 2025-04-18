from typing import Annotated
from fastapi import APIRouter, Depends
from schema import UserLoginSchema
from service import UserService
from dependency import get_user_service

router = APIRouter(prefix="/user", tags=["user"])

@router.post("", response_model=UserLoginSchema)
async def create_user(body: UserLoginSchema, user_service: Annotated[(UserService, Depends(get_user_service))]):
    return user_service.create_user(body.username, body.password)