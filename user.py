from flask_login import UserMixin
from models import User_db

class User(UserMixin):

    def __init__(self, username):
        self.id = username
        #self.password = password
        #time since last challenge accepted
        #the right hand side queries 'fooddb' database
        try:
            self.counter = User_db.objects.get(id= username).counter
        except:
            self.counter = 0

        #number of challenges completed
        try:
            self.completed = User_db.objects.get(id = username).completed
        except:
            self.completed = 0

