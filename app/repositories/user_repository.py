from app.entities.user_entity import User

class UserRepository:
    def __init__(self, session):
        self.session = session

    def create(self, name, email, password):
        user = User(
            name=name,
            email=email,
            password=password
        )

        self.session.add(user)