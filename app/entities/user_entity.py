from app.entities.base_entity import Base
from sqlalchemy.orm import Mapped, mapped_column

class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str]
    password: Mapped[str]

    money: Mapped[int]