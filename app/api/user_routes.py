from fastapi import APIRouter, Depends
from app.service.user_service import UserService
from app.data.db import get_db

router = APIRouter()

@router.post("/users/")
async def create_user(username: str, email: str, service: UserService = Depends(UserService)):
    return service.create_user(username, email)

@router.get("/users/{user_id}")
async def get_user(user_id: int, service: UserService = Depends(UserService)):
    return service.get_user(user_id)

@router.get("/users/")
async def get_all_users(service: UserService = Depends(UserService)):
    return service.get_all_users()
