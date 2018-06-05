from flask_login import UserMixin
from models import User_db

class User(UserMixin):

    def __init__(self, username, password):
        self.username = username
        self.password = password

        #time since last challenge accepted
        #the right hand side queries 'fooddb' database
        try:
            self.counter = User_db.objects.get(username= username).counter
        except:
            self.counter = 0

        #number of challenges completed
        try:
            self.completed = User_db.objects.get(username = username).completed
        except:
            self.completed = 0

    
    def is_authenticated(self):
        print("user.is_authenticated")
        return True #CHANGE

    def is_active(self):
        print("user.is_active")
        return True 

    def is_anonymous(self):
        print("user.is_anonymous")
        return False

    def get_id(self):
        print("user.get_id")
