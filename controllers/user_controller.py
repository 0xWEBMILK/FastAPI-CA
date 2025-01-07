from fastapi import APIRouter, Depends
from app.configs.database import get_db_connection
from app.repositories.user_repository import UserRepository
from app.interactors.user_interactor import UserInteractor


user_router = APIRouter()

@user_router.post('/create')
def create(name, email, password, session = Depends(get_db_connection)):
    user_repository = UserRepository(session)
    user_interactor = UserInteractor(user_repository)

    return user_interactor.create(name, email, password)
