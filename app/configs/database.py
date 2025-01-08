from app.entities.base_entity import Base


def get_session_stub():
    raise NotImplementedError

def init(engine):
    Base.metadata.create_all(engine)