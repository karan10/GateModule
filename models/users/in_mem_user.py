import uuid

from models.users.UserInterface import UserInterface
from dto.user import User


class InMemUser(UserInterface):
    def __init__(self):
        self.user_list = [
            {'id': uuid.uuid4(), 'age': 26, 'gender': 'f', 'past_order_amount': 500}
        ]

    def get_all(self):
        return self.user_list

    def get(self, user_id: uuid.UUID):
        return list(filter(lambda x: x['id'] == user_id, self.user_list))

    def add(self, user: User):
        user.id = uuid.uuid4()
        self.user_list.append(user.__dict__)
        return user.id
