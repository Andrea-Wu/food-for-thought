#pip installed
from flask import Flask, redirect
from flask_login import LoginManager, login_required, current_user
from mongoengine import *

#i defined these
from user import User
from form import LoginForm
from models import User_db

#initialize app
app = Flask(__name__)

#initialize login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/login'

#connect to database
connect('fooddb')

#callback function for login_user
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id) 

#connect to database

def test_main():
    print("this is the test main")
    print("testing how to query if key exists in db")
    
   # add_user()
    
    try:
        comp = User_db.objects.get(username = 'sidney').counter
        print(comp)
    except:
        #not found in db, redirect to login    

    #add_user()

    

@app.route('/')
def main():
    #case1: user does not have hackru account
    #case2: user has hackRU account, but his flask_login not initialized yet
    #case3: user has hackRU account and his flask_login already initialized

    return redirect("/dashboard")

@login_required
@app.route('/dashboard')
def dashboard():
    print("this is dashboard")
    
        

@app.route('/login')
def login(): 

    form = LoginForm()
    if form.validate_on_submit():

        #user = User(request.form['username'])
        user = User('andrea')        

        if user.is_authenticated():
            login_user(user) #this works by calling load_user 
            return redirect("/dashboard")       
        else: 
            return redirect("/err")
    #call LCS endpoint, probably
    print("this is user login")

@app.route('/err')
def errorr():
    print("ya fucked")

def add_user():
    #add to mongodb
    #does not actually create instance of User

    #.save() saves user to mongodb database
    new_user = User_db(username='andrea', completed=0, 
                    counter = 5,
                    is_doing_challenge = False).save()


#for checking if the code compiles
if __name__ == "__main__":
    test_main()





