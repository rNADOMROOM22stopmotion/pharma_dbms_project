import os
from functools import wraps
import dotenv
from pydantic import ValidationError
from models import db, rating
from models.models import User
from flask import Flask, render_template, request, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
dotenv.load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_KEY")
#app.permanent_session_lifetime = timedelta(days=5)
cursor, conn = db.cursor()


def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if 'email' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return wrapper

# sample
# USER = {'email': 'admin', 'password': '1234'}

@app.route('/')
@login_required
def home():
    logged_in = True if 'email' in session else False
    cursor.execute("""SELECT json_agg(row_to_json(p)) FROM (SELECT * FROM medicines) AS p;""")
    posts = cursor.fetchall()[0]['json_agg']

    cursor.execute("""SELECT cart FROM users WHERE email = %s""", (session['email'],))
    cart_num = cursor.fetchone()["cart"] or "0"

    return render_template("index.html", logged_in = logged_in, posts=posts, rating=rating.rating, cart_num=cart_num)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = request.args.get('error') or ""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        cursor.execute("""SELECT * FROM users WHERE email = %s""", (email,))
        USER = cursor.fetchone()
        if USER == None:
            return redirect(url_for('login', error= 'User does not exists.'))
        elif check_password_hash(USER['password_hash'], password):
            session['email'] = email
            session['logged_in'] = True
            return redirect(url_for('home'))
        else:
            session['logged_in'] = False
            return render_template('login.html', error='Invalid credentials')
    return render_template("login.html", error=error)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = request.args.get('error') or ""
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        try:
            u = User(email=email, password=password)
        except ValidationError as e:
            errors = []
            for err in e.errors():
                errors.append(err['loc'][0])
            if len(errors) == 2:
                field = "Email address and 6 character password."
            elif "email" in errors:
                field = "Email address."
            else:
                field = "6 character password"
            return redirect(url_for('signup', error=f"Please enter a valid {field}"))
        password_hash = generate_password_hash(password)
        cursor.execute("""INSERT INTO users (email, password_hash) VALUES (%s, %s)""", (u.email, password_hash))
        conn.commit()
        return redirect(url_for('login'))
    return render_template("signup.html", error=error)

@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('home'))

@app.route("/cart", methods=['GET', 'POST'])
@login_required
def cart():
    logged_in = True if 'email' in session else False
    source = request.args.get('source') or None
    if source == "addcart":
        product_name = request.args.get('product')
        cursor.execute("""UPDATE users SET cart = cart + 1 WHERE email = %s;""", (session['email'],))

        cursor.execute("""
            UPDATE cart
            SET quantity = quantity + 1
            WHERE "user" = (SELECT id FROM users WHERE email = %s)
            AND medicine = %s
        """, (session['email'], product_name))

        if cursor.rowcount == 0: # rowcount is 0 if no row was updated/ row does not exists
            cursor.execute("""
                INSERT INTO cart ("user", medicine, quantity)
                SELECT id, %s, 1
                FROM users
                WHERE email = %s
            """, (product_name, session['email']))
        conn.commit()

        return redirect(url_for('home'))
    if source == "cart":
        act = request.args.get('act')
        if act == "inc":
            pass
        elif act == "dec":
            pass

    cursor.execute("""
            SELECT * FROM cart
            WHERE "user" = (SELECT id FROM users WHERE email = %s)
        """, (session['email'],))
    products = cursor.fetchall()
    total = 0
    for med in products:
        med_name = med['medicine']
        cursor.execute("""SELECT * FROM medicines WHERE name = %s""", (med_name,))
        med_data = cursor.fetchone()
        med["price"] = med_data["price"]
        total += med_data["price"]
        med["sale"] = med_data["sale"]
        med["image"] = med_data["image"]
        med["stock"] = med_data["stock"]
    return render_template("cart.html", logged_in = logged_in, products=products, total=total)

if __name__ == "__main__":
    app.run(debug=True, port=5000)