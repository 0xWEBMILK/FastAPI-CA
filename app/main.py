from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import uvicorn

from app.controllers.user_controller import user_router
from app.configs.database import get_session_stub, init


def main():
    app = FastAPI()

    engine = create_engine("postgresql+psycopg2://postgres:Ddz180905@localhost/postgres", echo=True)
    session = sessionmaker(bind=engine)
    init(engine)

    def new_session():
        with session() as s:
            yield s
            s.commit()

    app.dependency_overrides[get_session_stub] = new_session

    app.include_router(user_router)

    uvicorn.run(app, host='0.0.0.0', port=8000)

if __name__ == '__main__':
    main()