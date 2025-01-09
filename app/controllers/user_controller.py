from fastapi import APIRouter, Depends
from app.repositories.user_repository import UserRepository
from app.interactors.user_interactor import UserInteractor
from app.configs.database import get_session_stub

user_router = APIRouter()

@user_router.post('/create')
def create(name: str, email: str, password: str, money: int, session = Depends(get_session_stub)):

    user_repository = UserRepository(session)
    user_interactor = UserInteractor(user_repository)

    user_interactor.create(name, email, password, money)

    return 200

@user_router.get('/read')
def read(name: str = None, session = Depends(get_session_stub)):
    user_repository = UserRepository(session)
    user_interactor = UserInteractor(user_repository)

    result = user_interactor.read(name)

    return result

@user_router.put('/update')
def update(name: str, money: int, session = Depends(get_session_stub)):
    user_repository = UserRepository(session)
    user_interactor = UserInteractor(user_repository)

    user_interactor.update(name, money)

    return 200

@user_router.delete('/delete')
def delete(name: str, session = Depends(get_session_stub)):
    user_repository = UserRepository(session)
    user_interactor = UserInteractor(user_repository)

    user_interactor.delete(name)

    return 200