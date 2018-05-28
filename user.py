from flask_login import UserMixin
from models import User_db

class User(UserMixin):

    def __init__(self, uname):
        self.username = uname

        #time since last challenge accepted
        #the right hand side queries 'fooddb' database
        self.counter = User_db.objects.get(username= uname).counter

        #number of challenges completed
        self.completed = User_db.objects.get(username = uname).completed

        self.is_doing_challenge = User_db.objects.get(username = uname).is_doing_challenge
    
    def is_authenticated():
        print("user.is_authenticated")

    def is_active():
        print("user.is_active")

    def is_anonymous():
        print("user.is_anonymous")

    def get_id():
        print("user.get_id")
