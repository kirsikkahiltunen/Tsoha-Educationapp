from flask import Flask
from flask import redirect, render_template, request
import re
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///Tsoha2"
db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]


    sql = text("SELECT* FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})

    user = result.fetchone()
    

    if not user:
        return render_template("invaliduser.html", message="Käyttäjätunnus tai salasana väärin")
    else:
        hash_value = user.password
        if check_password_hash(hash_value, password):
            if user.user_type == "1":
                firstname=user.firstname
                lastname=user.lastname
                sql_courses = text("""SELECT courses.course_name FROM courses JOIN course_enrollments ON courses.id = course_enrollments.course_id WHERE course_enrollments.user_id = :user_id""")
                result_courses = db.session.execute(sql_courses, {"user_id": user.id})
                courses = result_courses.fetchall()
                return render_template("courses_student.html", firstname = firstname, lastname = lastname, username = username, courses = courses)
            elif user.user_type == "2":
                firstname=user.firstname
                lastname=user.lastname
                sql_teacher_courses = text("""SELECT courses.course_name FROM courses WHERE courses.teacher_id =:teacher_id""")
                result_teacher_courses = db.session.execute(sql_teacher_courses, {"teacher_id": user.id})
                courses = result_teacher_courses.fetchall()
                return render_template("courses_teacher.html", firstname = firstname, lastname = lastname, username = username, courses = courses)
        else:
            return render_template("invaliduser.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/courses", methods=["POST"])
def courses():
    username = request.form["username"]
    password = request.form["password"]


    sql = text("SELECT* FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})

    user = result.fetchone()
    

    if not user:
        return render_template("invaliduser.html", message="Käyttäjätunnus tai salasana väärin")
    else:
        hash_value = user.password
        if check_password_hash(hash_value, password):
            if user.user_type == "1":
                firstname=user.firstname
                lastname=user.lastname
                sql_courses = text("""SELECT courses.course_name FROM courses JOIN course_enrollments ON courses.id = course_enrollments.course_id WHERE course_enrollments.user_id = :user_id""")
                result_courses = db.session.execute(sql_courses, {"user_id": user.id})
                courses = result_courses.fetchall()
                return render_template("courses_student.html", firstname = firstname, lastname = lastname, username = username, courses = courses)
            elif user.user_type == "2":
                firstname=user.firstname
                lastname=user.lastname
                sql_teacher_courses = text("""SELECT courses.course_name FROM courses WHERE courses.teacher_id =:teacher_id""")
                result_teacher_courses = db.session.execute(sql_teacher_courses, {"teacher_id": user.id})
                courses = result_teacher_courses.fetchall()
                return render_template("courses_teacher.html", firstname = firstname, lastname = lastname, username = username, courses = courses)
        else:
            return render_template("invaliduser.html")
    
@app.route("/signup_done", methods=["POST"])
def signup_done():
    firstname = request.form["firstname"]
    lastname = request.form["lastname"]
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    user_type = request.form["user_type"]

    #def is_valid(password1, password2):
        #this function check if the password is valid
        #special_characters= r"!@#$%&*/()[]-_=+}?';,:.<>\``~^{"
        #numbers=list(range (10))
        #if password1 == password2:
            #first it checks if the password is long enough
            #if len(password1)<8:
            #    return False
            #then it checks if it have at least one of the special characters
            #if not re.search(special_characters, password1):
            #    return False
            #if not re.search(numbers, password1):
            #    return False
            #else:
            #    return True

    if password1 == password2:
        hash_value = generate_password_hash(password1)
        sql = text("INSERT INTO users (username, password, firstname, lastname, user_type) VALUES (:username, :password, :firstname, :lastname, :user_type)")
        db.session.execute(sql, {"username":username, "password":hash_value, "firstname":firstname, "lastname":lastname, "user_type":user_type})
        db.session.commit()
        return render_template("login.html")
    
    else:
        return render_template("invalidpassword.html")
    
