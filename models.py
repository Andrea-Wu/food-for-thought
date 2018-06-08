from mongoengine import *

class User_db(Document):
    id = StringField(max_length=25, required=True, primary_key = True)
    password = StringField(required=True)
    
    #no default??
    completed = IntField(min_value = 0)

    #counted in seconds
    counter =  IntField(min_value = 0)

    
    
    authenticated = BooleanField(required=True, default=False)


#class Challenges(Document):

