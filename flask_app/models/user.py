from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_bcrypt import Bcrypt
from flask_app.models import queries
from flask import flash
import re

bcrypt = Bcrypt(app)
db = "rideshares"
table = "users"
REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")
PASSWORD_REGEX = re.compile(r"^(?=.{8,}$)(?=.*?[A-Z])(?=.*?[0-9])")


class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.rides = []

    @classmethod
    def save(cls, data):
        # query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        query = queries.create_query(table, data)
        print(query)
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def get_by_id(cls, id):
        data = {"id": id}
        query = queries.get_by(table, "id")
        return cls(connectToMySQL(db).query_db(query, data)[0])

    @classmethod
    def get_by_email(cls, email):
        data = {"email": email}
        query = queries.get_by(table, "email")
        results = connectToMySQL(db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def drive_for(cls, data):
        query = "UPDATE rides SET drivers_id=%(drivers_id)s WHERE id=%(id)s;"
        return connectToMySQL(db).query_db(query, data)

    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user["first_name"]) < 2:
            flash("First name must have at least 2 characters", "register")
            is_valid = False
        if len(user["last_name"]) < 2:
            flash("Last name must have at least 2 characters", "register")
            is_valid = False
        if len(user["email"]) < 2:
            flash("Email must have at least 2 characters", "register")
            is_valid = False
        if not REGEX.match(user["email"]):
            flash("Invalid email format", "register")
            is_valid = False
        if User.get_by_email(user["email"]) != False:
            flash("Email is already taken", "register")
            is_valid = False
        if len(user["password"]) < 8:
            flash("Password must have at least 8 characters", "register")
            is_valid = False
        # if not PASSWORD_REGEX.match(user["password"]):
        #     flash("Password must contain 1 capital letter and one number", "register")
        #     is_valid = False
        if user["password"] != user["confirm"]:
            flash("Passwords must match", "register")
            is_valid = False
        return is_valid

    @staticmethod
    def validate_login(user):
        user_in_db = User.get_by_email(user["email"])
        if user_in_db == False:
            flash("Invalid login attempt", "login")
            return False
        if not bcrypt.check_password_hash(user_in_db.password, user["password"]):
            flash("Invalid login attempt", "login")
            return False
        return True
