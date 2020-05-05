#
# from collections import namedtuple
# fields = ('id', 'age', 'gender', 'past_order_amount')
# User = namedtuple('User', fields, defaults=(None,) * len(fields))

# from recordtype import recordtype
#
# Book = recordtype('Book', 'author title genre year price instock')
import json


class User(object):
    def __init__(self, j):
        self.__dict__ = json.loads(j)

