from app.entities.base_entity import Base


def get_session_stub():
    raise NotImplementedError

def database_metadata_init(engine):
    Base.metadata.create_all(engine)