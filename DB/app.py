from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:Nwankwo1@host/database_name"

db = SQLAlchemy(app)


class Customers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)

class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_name = db.Column(db.String(50), nullable=False)
    date = db.Column(db.DateTime), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)


if __name__ == "__main__":
    app.run(debug=True)