class UserInteractor:
    def __init__(self, repository):
        self.repository = repository

    def create(self, name, email, password):
        return self.repository.create(name, email, password)