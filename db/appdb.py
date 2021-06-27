from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:Nwankwo1@35.189.108.251:3306/flaskdb"

db = SQLAlchemy(app)


class customers(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    name = db.Column(db.String(50), nullable=False)
    customer_orders = db.relationship('orders', backref='order_entry')

class orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_name = db.Column(db.String(100), nullable=False)
    order_date = db.Column(db.DateTime, default=datetime.now)
    customer_order_id = db.Column(db.Integer, db.ForeignKey('customers.id'))


if __name__ == "__main__":
    app.run(debug=True)