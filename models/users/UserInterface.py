import abc
import uuid

from dto.user import User


class UserInterface(abc.ABC):
    @abc.abstractmethod
    def get_all(self):
        pass

    @abc.abstractmethod
    def get(self, user_id: uuid):
        pass

    @abc.abstractmethod
    def add(self, user: User):
        pass
