from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_wtf.file import FileField, FileSize, FileAllowed, FileRequired

class RegisterForm(FlaskForm):
    image = FileField()
    email = StringField(validators=[DataRequired(), Email()])
    username = StringField(validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField(validators=[DataRequired(), Length(min=6, max=20)])
    usernameL = StringField(validators=[DataRequired(), Length(min=2, max=20)])
    passwordL = PasswordField(validators=[DataRequired(), Length(min=6, max=20)])
    submit = SubmitField()

class ItemForm(FlaskForm):
    name = StringField(validators=[DataRequired())
    image = FileField()
    submit = SubmitField()