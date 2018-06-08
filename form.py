from wtforms import BooleanField, StringField, PasswordField, SubmitField, validators

#this is for the large input in admin page
from wtforms.widgets import TextArea
from wtforms.validators import Length, DataRequired, InputRequired, EqualTo
from flask_wtf import FlaskForm
#yike
class LoginForm(FlaskForm):
    username = StringField("Username", [Length(min=4, max=25), 
                                        InputRequired()])
    password = PasswordField("Password", [InputRequired()])
    submit = SubmitField("submit")

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[Length(min=4, max=25), 
                                    InputRequired()])

    password = PasswordField("Password", validators=[InputRequired(), 
                                    EqualTo("confirm", message="passwords must match")])
    
    confirm = PasswordField("Confirm Password")
    submit = SubmitField("submit")

class ChallengeForm(FlaskForm):
    title = StringField("Title", validators=[InputRequired()])
    body = StringField("Body", validators=[InputRequired()], widget=TextArea())
    submit = SubmitField("submit")
