from flask import Flask, render_template, abort, request, redirect
import mysql.connector
import os

app = Flask(__name__)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="iconic"
)
cur = mydb.cursor()

app.secret_key = os.urandom(24)

@app.route('/index', methods = ['POST', 'GET'])
@app.route('/home', methods = ['POST', 'GET'])
@app.route('/', methods = ['POST', 'GET'])
def home():
    if request.method == "POST":
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        try:
            cur.execute("INSERT INTO `enrollments`(name, phone, email) VALUES (%s,%s,%s)",(name,phone,email))
            mydb.commit()
            return redirect("https://rzp.io/l/7PuRzjYrh")
        except:
            return render_template('error.html', code="500", title="Something went wrong", desc="Oops. Something went wrong.<br /> Please try again later.")
    return render_template('home.html')

@app.route('/<template>')
def render(template):
    return render_template(template + '.html')
