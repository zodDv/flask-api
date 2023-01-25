from flask import Flask
import os 
from flask_jwt_extended import JWTManager
from models import db, ma 


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["JWT_SECRET_KEY"] = "super-secret"  
jwt = JWTManager(app)

db.init_app(app)
ma.init_app(app)