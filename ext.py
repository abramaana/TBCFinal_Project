from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__, template_folder='templates')
app.config["SECRET_KEY"] = "111"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config['UPLOAD_FOLDER'] = 'static/uploads'

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'home'

@login_manager.user_loader
def load_user(user_id):
    from models import User
    return User.query.get(int(user_id))