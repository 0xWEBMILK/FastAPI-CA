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

        with self.session.begin() as conn:
            conn.add(user)
            conn.commit()

        return 200