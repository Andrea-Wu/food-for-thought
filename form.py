from wtforms import BooleanField, StringField, PasswordField, SubmitField, validators
from flask_wtf import FlaskForm
#yike
class LoginForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=4, max=25), 
                                        validators.DataRequired()])
    password = PasswordField("Password", [validators.DataRequired()])
    submit = SubmitField("submit")

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[validators.Length(min=4, max=25), 
                        validators.InputRequired()])

    password = PasswordField("Password", validators=[validators.InputRequired(), 
                                         validators.EqualTo("confirm", message="passwords must match")])
    
    confirm = PasswordField("Confirm Password")
    submit = SubmitField("submit")
