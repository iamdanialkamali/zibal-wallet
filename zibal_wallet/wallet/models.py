from mongoengine import *


class Wallet(Document):
    id = ObjectIdField()
    name = StringField()
    credit = FloatField()


class Transaction(Document):
    id = ObjectIdField()
    source_wallet_id = ObjectIdField()
    destination_wallet_id = ObjectIdField(default=None)
    amount = FloatField(min_value=0)
