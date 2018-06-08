from mongoengine import *

class User_db(Document):
    id = StringField(max_length=25, required=True, primary_key = True)
    password = StringField(required=True)
    
    #no default??
    completed = IntField(min_value = 0)

    #counted in seconds
    counter =  IntField(min_value = 0)
    
    is_admin = BooleanField(required=True, default=False)

    actives = ListField(IntField(min_value = 0))


class Challenge_db(Document):
    id = IntField(min_value=0, required=True, primary_key=True)
    title = StringField(required=True)
    body = StringField(required=True)


