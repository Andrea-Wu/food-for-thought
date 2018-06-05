from mongoengine import *

class User_db(Document):
    username = StringField(max_length=25, required=True, primary_key = True)
    password = StringField(required=True)
    completed = IntField(min_value = 0, default = 0)

    #counted in seconds
    counter =  IntField(min_value = 0, default=0)

#class Challenges(Document):

