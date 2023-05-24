from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField,  validators
from wtforms.validators import DataRequired

class LoginForm(Form):
    username = StringField("username", validators=[ validators.DataRequired()])
    password = PasswordField("password", validators=[ validators.DataRequired()])
    rememberMe= BooleanField("rememberMe")
