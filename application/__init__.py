from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:Nwankwo1@35.189.108.251:3306/flaskdb"

db = SQLAlchemy(app)

from application import routes