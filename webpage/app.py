from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return 'This is the about page, please bear with us as we are still building!'

if __name__ == "__main__":
    app.run(debug=True)