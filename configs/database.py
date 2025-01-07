from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


def get_db_connection():
    engine = create_engine("postgresql+psycopg2://postgres:Ddz180905@localhost/postgres", echo=True)
    session = sessionmaker(bind=engine)

    return session