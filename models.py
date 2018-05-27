from mongoengine import *

class Hacker(Document):
    username = StringField(max_length=25, required=True, primary_key = True)
    completed_challenges = IntField(min_value = 0, default = 0)

    #counted in seconds
    time_since_last_challenge =  IntField(min_value = 0)
    is_doing_challenge = BooleanField(default = False)

#class Challenges(Document):

