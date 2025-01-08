from fastapi import APIRouter, Depends
from app.repositories.user_repository import UserRepository
from app.interactors.user_interactor import UserInteractor
from app.configs.database import get_session_stub

user_router = APIRouter()

@user_router.post('/create')
def create(name, email, password, session = Depends(get_session_stub)):

    user_repository = UserRepository(session)
    user_interactor = UserInteractor(user_repository)

    user_interactor.create(name, email, password)

    return 200
