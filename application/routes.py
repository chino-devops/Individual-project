from application import app, db
from application.models import customers


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return 'This is the about page, please bear with us as we are still building!'


@app.route('/add')
def add():
    new_customers = customers(name="james doe")
    db.session.add(new_customers)
    db.session.commit()
    return "Added new entry to database"

@app.route('/read')
def read():
    all_customers = customers.query.all()
    games_string = ""
    for customer in all_customers:
        customers_string += "<br>"+ customer.name
    return customers_string

@app.route('/update/<name>')
def update(name):
    first_customer = customers.query.first()
    first_customer.name = name
    db.session.commit()
    return first_customer.name