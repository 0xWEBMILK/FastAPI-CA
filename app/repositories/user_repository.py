from app.entities.user_entity import User
from app.utils.hashing import password_hash


class UserRepository:
    def __init__(self, session):
        self.session = session

    def create(self, name: str, email: str, password: str, money: int):
        user = User(
            name=name,
            email=email,
            password=password_hash(password),
            money=money,
        )

        query = self.session.query(User).filter_by(name=name).first()

        if query is not None:
            return query

        self.session.add(user)

    def read(self, name: str):
        if name is not None:
            user = self.session.query(User).filter_by(name=name).first()

            return user

        users = self.session.query(User).all()
        return users

    def update(self, name: str, money: int):
        user = self.session.query(User).filter_by(name=name).first()
        user.money = money

    def delete(self, name: str):
        user = self.session.query(User).filter_by(name=name).first()
        self.session.delete(user)