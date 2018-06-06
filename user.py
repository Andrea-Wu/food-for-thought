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
        return User_db.objects.get(username = self.username).authenticated 

    def is_active(self):
        return self.is_authenticated()

    def is_anonymous(self):
        return not self.is_authenticated()

    def get_id(self):
        return self.username
