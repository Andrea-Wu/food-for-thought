from flask_login import UserMixin
from models import Hacker

class User(UserMixin):

    def __init__(self, username):
        self.username = username
    
    def is_authenticated():
        print("user.is_authenticated")

    def is_active():
        print("user.is_active")

    def is_anonymous():
        print("user.is_anonymous")

    def get_id():
        print("user.get_id")
