from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import uvicorn

from app.controllers.user_controller import user_router
from app.configs.database import get_session_stub, database_metadata_init


def main():
    app = FastAPI()

    engine = create_engine("wo-wo-wo-wo-wo-wo", echo=True)
    session = sessionmaker(bind=engine)
    database_metadata_init(engine)


    def new_session():
        # This function creates a new session using a context manager, ensuring proper resource management and transaction handling.
        # - The 'with' statement ensures that the session is automatically closed when the context exits.
        # - The function yields the session to allow operations within its scope.
        # - If operations succeed, the changes are committed using s.commit().
        # - If an exception occurs, the changes are rolled back using s.rollback(), maintaining data integrity.
        # - The session is guaranteed to close in the 'finally' block, even in case of errors, preventing resource leaks.
        with session() as s:
            try:
                yield s
                s.commit()
            except Exception as e:
                s.rollback()
                raise e
            finally:
                s.close()


    app.dependency_overrides[get_session_stub] = new_session

    app.include_router(user_router)

    uvicorn.run(app, host='0.0.0.0', port=8000)

if __name__ == '__main__':
    main()