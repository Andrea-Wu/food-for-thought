#pip installed
from flask import Flask, redirect, request, render_template, flash
from flask_login import LoginManager, login_required, current_user, login_user

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

app.config['SECRET_KEY'] = "shhhhh"

#initialize login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/login'

#connect to database
connect('fooddb')

#callback function for login_user
@login_manager.user_loader
def load_user(user_id):
    try:
        user = User_db.objects.get(user_id) #this might break
    except:
        user = None

    return user

#connect to database
    

@app.route('/')
def main():
    #assume that if user has hackru account, he is already in db

    #case1: user does not have food account 
    #case2: user has food account, but his flask_login not initialized yet
    #case3: user has food account and his flask_login already initialized

    return redirect("/login")

@login_required
@app.route('/dashboard')
def dashboard():
    print("this is dashboard")
    return render_template("dashboard.html")
    
        



@app.route('/login', methods=["GET", "POST"])
def login(): 

    form = LoginForm()

    #same as .is_submitted() and .validate()
    #is_submitted() returns true if form is an active request
    #and the method is POST, PUT, PATCH, DELETE

    #validation deals with whether the form has all fields filled, are long enough, etc
    if form.validate_on_submit():
        print(form.errors)
        uname = request.form['username']

        passwd =  request.form['password']        


    
        if verify_password(uname, passwd):
            print("password correct!")
            user = User(uname, passwd)
            login_user(user, remember = True) #this works by calling load_user 
            return redirect("/dashboard")       
        else: 
            print("yer password was wrong")
            flash("bad login")
            return redirect("/login")
    #call LCS endpoint, probably

    print(form.errors)
    return render_template('login.html', form=form)



@app.route('/register', methods=["GET","POST"])
def register():
    form = RegistrationForm()

    
    if form.validate_on_submit():
        
        print(request.form['password'])
        print(request.form['confirm'])

        #hash password
        hash_pw = sha256_crypt.hash(request.form['password'])

        #store data in db
        new_user = User_db(username = request.form['username'], password = hash_pw).save()

        return redirect("/login") #CHANGE
                            
        
    print(form.errors)
    return render_template("register.html", form = form)


@app.route('/err')
def errorr():
    print("ya fucked")
    return render_template('ya_fucked.html')


def verify_password(username, password):
    #If they are equal, return true
   
    print("verifying password")
    
    #err check for if username exists in db
    try:
        stored_pw = User_db.objects.get(username=username).password
    except: 
        return False        

    return sha256_crypt.verify(password, stored_pw)
    
    


#for checking if the code compiles
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4096)





