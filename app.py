#pip installed
from flask import Flask, redirect, request, render_template
from flask_login import LoginManager, login_required, current_user

#db
from mongoengine import *

#auth
from passlib.hash import sha256_crypt

#i defined these
from user import User
from form import LoginForm, RegistrationForm
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
    return redirect("/register")
    

@app.route('/')
def main():
    #assume that if user has hackru account, he is already in db

    #case1: user does not have food account 
    #case2: user has food account, but his flask_login not initialized yet
    #case3: user has food account and his flask_login already initialized

    return redirect("/register")

@login_required
@app.route('/dashboard')
def dashboard():
    print("this is dashboard")
    
        

@app.route('/login', methods=["GET", "POST"])
def login(): 

    form = LoginForm()

    #same as .is_submitted() and .validate()
    #is_submitted() returns true if form is an active request
    #and the method is POST, PUT, PATCH, DELETE

    #validation deals with whether the form has all fields filled, are long enough, etc
    if form.validate and request.method == "POST":
        user = User(request.form['username'], request.form['password'])        

        if user.is_authenticated():
            login_user(user, remember = True) #this works by calling load_user 
            return redirect("/dashboard")       
        else: 
            return redirect("/err")
    #call LCS endpoint, probably

    return render_template('login.html', form=form)


@app.route('/register', methods=["GET","POST"])
def register():
    form = RegistrationForm()

    #supposedly this can be solved withh form.validate_on_submit
    #but it was not working. I'll figure out why #LATER
    if form.validate and request.method == "POST":

        #hash password
        hash_pw = sha256_crypt.hash(request.form['password'])

        #store data in db
        new_user = User_db(username = request.form['username'], password = hash_pw).save()

        return redirect("/err") #CHANGE
                            
        
    return render_template("register.html", form = form)


@app.route('/err')
def errorr():
    print("ya fucked")
    return render_template('ya_fucked.html')

def add_user():
    #add to mongodb
    #does not actually create instance of User

    #.save() saves user to mongodb database
    new_user = User_db(username='andrea', completed=0, 
                    counter = 5,
                    is_doing_challenge = False).save()


#for checking if the code compiles
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4096)





