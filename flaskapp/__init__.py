from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# Instantiate Flask.
app = Flask(__name__)
# Secret hash key , used bcrypt.
app.config['SECRET_KEY'] = '58536585b6d207ca4c42ef1c7012c881'

# Set SQLALCHEMY Instance Location to our site project location.
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
# Instantiate different tools that are needed for the app.
# SQL Alchemy
db = SQLAlchemy(app)
# Bcrypt
bcrypt = Bcrypt(app)
# LoginManager from flask_login
login_manager = LoginManager(app)

# Routes are imported here to avoid circular imports.
# app needs to be created first so it can create routes, therefore,
# routes are imported after app is instantiated.
from flaskapp import routes
