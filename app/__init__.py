from flask import Flask
#from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(12)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://lrjbyvmjvfbgiv:060d61f325fce981a143f955e01b4a38ef64368f3b31be135a163a38500d17e4@ec2-75-101-133-29.compute-1.amazonaws.com:5432/d3psed55guvtgj'
HEROKU_POSTGRESQL_GOLD_URL='postgres://ulthhzglvnufge:90ef21c0f496551b55e57f35e44b7f04c59a2b49de44d89fb154ac7a24a56fa4@ec2-54-221-236-144.compute-1.amazonaws.com:5432/ddushe7t02abnd'"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views\