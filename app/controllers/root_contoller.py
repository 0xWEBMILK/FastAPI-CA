from fastapi import APIRouter

root_router = APIRouter()

@root_router.get('/')
def root():
    return 'Hello world!'

@root_router.get('/home')
def home():
    return 'Saluut!!!'