from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
#from flask_user import UserManager
#from classwebapp.models import User

app = Flask(__name__)
app.config['SECRET_KEY'] = '85e3cbdb42f209e26b179176e90b4506'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
#db_adapter = SQLAlchemyAdapter(db, User)
bcrypt = Bcrypt(app)
#user_manager = UserManager(app, db, User)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from classwebapp import routes
