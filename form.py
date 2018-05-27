from wtforms import Form, BooleanField, StringField, PasswordField, validators

class LoginForm(Form):
    username = StringField("Username", [validators.Length(min=4, max=25), 
                                        validators.DataRequired()])
    password = PasswordField("Password", [validators.DataRequired()])
