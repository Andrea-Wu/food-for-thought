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
from form import LoginForm, RegistrationForm, ChallengeForm
from models import User_db, Challenge_db
from challenge import Challenge

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


#counts current num of challenges in database
#might break
totalChallenges = Challenge_db.objects.count()


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

    ##to set a user as admin. 

#    user = User_db.objects.get(id="YonYonsen")
#    user.is_admin = True
#    user.save()
    

    return redirect("/login")

@app.route('/dashboard')
@login_required
def dashboard():
    print("this is dashboard")
    return render_template("dashboard.html", user=current_user)


#add is_admin to user.py & models.py
@app.route('/admin', methods=["GET", "POST"])
@login_required
def admin():
    if not current_user.is_admin:
        return redirect("/err")

    print("this is the admin page")

    form = ChallengeForm()
    print("form created")
    if form.validate_on_submit():

        print("validated form")
        title = request.form['title']
        body = request.form['body']


        global totalChallenges 
        totalChallenges += 1
        newChallenge = Challenge_db(id = totalChallenges, title = title, body=body).save()
        print("created challenge")
        return redirect("/admin")        
        
        

    return render_template("admin.html", form=form, count=totalChallenges)
    

def add_challenge():
    if not current_user.is_admin:
        return redirect("/err")


@app.route("/request")
@login_required
def request_challenge():
    print("this is the request challenge page")


@app.route("/actives")
@login_required
def active_challenges():
    #a list of the user's active challenges...stored in db & displayed
    print("list of active challenges")

    #get a list of integers corresponding to user's active challenges
    activeInts = User_db.objects.get(id=current_user.id).actives
    print("got actives")

    #associate each integer with a corresponding challenge
    activeChals = []
    for a in activeInts:
        chal = Challenge_db.objects.get(id = a)
        print(chal.title)
        activeChals.append(chal)

    return render_template("actives.html", activeChals = activeChals)



@app.route("/display")    
@login_required
def display_challenge():

    challengeID = request.args.get("challengeID", default=-1)

    print("challenge is:" + str(challengeID))


    #this means user tried to manually access URL
    if challengeID == -1:
        return redirect("/err")

    #make sure user actually has access to that challenge
    activeChals = User_db.objects.get(id = current_user.id).actives

    if not int(challengeID) in activeChals:
        return redirect("/err")

    #query db for challenge with that id
    c = Challenge_db.objects.get(id = challengeID)

    return render_template("display.html", challenge=c)



@app.route('/login', methods=["GET", "POST"])
def login(): 

    if current_user.is_authenticated:
        return redirect("/dashboard")

    form = LoginForm()

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





