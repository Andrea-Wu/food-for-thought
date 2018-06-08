#pip installed
from flask import Flask, redirect, request, render_template, flash
from flask_login import LoginManager, login_required, current_user
from flask_login import login_user, logout_user
#making sure it fits my screen srry

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
app.config['TESTING'] = False

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
        user = User_db.objects.get(id = user_id) #this might break
        print("user loaded")
    except:
        print("user not found")
        return None

    return User(user.id)

#connect to database
    

@app.route('/')
def main():
    #assume that if user has hackru account, he is already in db

    #case1: user does not have food account 
    #case2: user has food account, but his flask_login not initialized yet
    #case3: user has food account and his flask_login already initialized

    return redirect("/login")

@app.route('/dashboard')
@login_required
def dashboard():
    print("this is dashboard")
    return render_template("dashboard.html")



@app.route("/request")
@login_required
def request_challenge():
    print("this is the request challenge page")


@app.route("/actives")
@login_required
def active_challenges():
    #a list of the user's active challenges...stored in db & displayed
    print("list of active challenges")
    return render_template("actives.html")



@app.route("/display")    
@login_required
def display_challenge(challenge =-1):
    print("challenge is:" + str(challenge))

    if challenge == -1:
        return redirect("/err")
    return render_template("display.html")


        



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
            user = User(uname)
            login_user(user, remember = True) #this works by calling load_user 
            return redirect("/dashboard")       
        else: 
            print("yer password was wrong")
            flash("bad login")
            return redirect("/login")
    elif request.method == "POST":
        #post, but not validated
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
        new_user = User_db(id = request.form['username'], password = hash_pw).save()

        return redirect("/login") #CHANGE
    elif request.method == "POST":
        flash("bad registration")
        return redirect("/register")                    
        
    print(form.errors)
    return render_template("register.html", form = form)


@app.route('/err')
@login_required
def errorr():
    print("ya fucked")
    return render_template('ya_fucked.html')


def verify_password(username, password):
    #If they are equal, return true
   
    print("verifying password")
    
    #err check for if username exists in db
    try:
        stored_pw = User_db.objects.get(id =username).password
    except: 
        return False        

    return sha256_crypt.verify(password, stored_pw)

@app.route("/logout")
@login_required    
def logout():
    logout_user()
    return render_template("logout.html")
    


#for checking if the code compiles
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4096)





