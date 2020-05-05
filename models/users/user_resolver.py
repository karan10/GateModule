import uuid

from dto.user import User
from models.users.in_mem_user import InMemUser


class UserResolver:
    user_resolver = None

    def __init__(self, file_system):
        if file_system == 'inMem':
            self.user = InMemUser()

    def get_all(self):
        return self.user.get_all()

    def get(self, user_id: uuid):
        return self.user.get(user_id)

    def add(self, user: User):
        return self.user.add(user)

    @staticmethod
    def new():
        if not UserResolver.user_resolver:
            UserResolver.user_resolver = UserResolver('inMem')
        return UserResolver.user_resolver


