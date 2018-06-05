from wtforms import Form, BooleanField, StringField, PasswordField, validators
#yike
class LoginForm(Form):
    username = StringField("Username", [validators.Length(min=4, max=25), 
                                        validators.DataRequired()])
    password = PasswordField("Password", [validators.DataRequired()])


class RegistrationForm(Form):
    username = StringField("Username", [validators.Length(min=4, max=25), 
                        validators.DataRequired(), 
                        validators.EqualTo("confirm", message="passwords must match")])

    password = PasswordField("Password", [validators.DataRequired()])
    confirm = PasswordField("Confirm Password", [validators.DataRequired()])
