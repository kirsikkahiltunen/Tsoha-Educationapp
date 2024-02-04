from flask import Flask
from flask import render_template, request
import re

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/courses", methods=["POST"])
def courses():
    username = request.form["username"]
    password = request.form["password"]

    if username == "demo_oppilas" and password == "demo_oppilas":
        return render_template("courses_student.html")
    if username == "demo_opettaja" and password == "demo_opettaja":
        return render_template("courses_teacher.html")
    
    else:
        return render_template("invaliduser.html")
    
@app.route("/signup_done", methods=["POST"])
def signup_done():
    firstname = request.form["firstname"]
    lastname = request.form["lastname"]
    username = request.form["username"]
    password = request.form["password1"]

    def is_valid(password):
        #this function check if the password is valid
        special_characters="!@#$%&*/()[]-_=+}?';,:.<>\``~^{"
        numbers=list(range (10))
        #first it checks if the password is long enough
        if len(password)<8:
            return False
        #then it checks if it have at least one of the special characters
        if not re.search(special_characters, password):
            return False
        if not re.search(numbers, password):
            return False
        else:
            return True

    if is_valid(password):
        return render_template("login.html")
    
    else:
        return render_template("invalidpassword.html")
    
    