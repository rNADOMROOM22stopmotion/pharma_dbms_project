import os
import random

import dotenv
from models import db
from flask import Flask, render_template, request, session, redirect, url_for

dotenv.load_dotenv()
app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_KEY")
#app.permanent_session_lifetime = timedelta(days=5)
cursor = db.cursor()

# sample
USER = {'email': 'admin', 'password': '1234'}

@app.route('/')
def home():
    logged_in = True if 'email' in session else False
    rating = random.randint(3, 5)
    cursor.execute("""SELECT json_agg(row_to_json(p)) FROM (
    SELECT * FROM medicines
    ) AS p;
    """)
    posts = cursor.fetchall()[0][0]
    return render_template("index.html", logged_in = logged_in, posts=posts, rating=rating)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email == USER['email'] and password == USER['password']:
            session['email'] = email
            session['logged_in'] = True
            return redirect(url_for('home'))
        else:
            session['logged_in'] = False
            return render_template('login.html', error='Invalid credentials')
    return render_template("login.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template("signup.html")

@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True, port=5000)