class UserInteractor:
    def __init__(self, repository):
        self.repository = repository

    def create(self, name, email, password, money):
        return self.repository.create(name, email, password, money)

    def read(self, name):
        return self.repository.read(name)

    def update(self, name, money):
        return self.repository.update(name, money)

    def delete(self, name):
        return self.repository.delete(name)