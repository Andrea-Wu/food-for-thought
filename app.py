#pip installed
from flask import Flask, redirect
from flask_login import LoginManager, login_required

#i defined these
from user import User
from form import LoginForm

#initialize app
app = Flask(__name__)

#initialize login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/login'

#callback function for login_user
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)




@app.route('/')
def main():
    #i'm assuming...use LCS to check if user is logged in
    #login_user()
    return redirect("/dashboard")


@app.route('/dashboard')
def welcome():
    print("this is dashboard")
    
    login = False
    #pseudocode, don't know how to authenticate yet
    if login == False:
        return redirect("/login")
        

@app.route('/login')
def login(): 

    form = LoginForm()
    if form.validate_on_submit():
        user = User(request.form['username'])
        #maybe check authentication again?
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

#for checking if the code compiles
if __name__ == "__main__":
    main()





