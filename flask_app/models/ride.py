from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user, queries
from flask import flash
db="rideshares"
table="rides"
class Ride:
    def __init__(self, data):
        self.id = data["id"]
        self.destination = data["destination"]
        self.pickup_location = data["pickup_location"]
        self.pickup_date = data["pickup_date"]
        self.details = data["details"]
        self.driver = None
        self.rider = None
        self.messages = []

    @classmethod
    def save(cls, data):
        query = queries.create_query(table, data)
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def get_all_without_driver(cls):
        query = "SELECT * FROM rides LEFT JOIN users ON users.id = rides.users_id WHERE drivers_id IS NULL;"
        results = connectToMySQL(db).query_db(query)
        all_rides = []
        for row in results:
            ride = cls(row)

            rider_data = {
                "id": row["users.id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "email": row["email"],
                "password": row["password"]
            }
            ride.rider = user.User(rider_data)
            all_rides.append(ride)
        return all_rides

    @classmethod
    def get_all_with_driver(cls):
        query = "SELECT * FROM rides LEFT JOIN users ON users.id = rides.users_id JOIN users AS drivers ON rides.drivers_id = drivers.id WHERE rides.drivers_id IS NOT NULL;"

        results = connectToMySQL(db).query_db(query)
        print(results)
        all_rides = []
        for row in results:
            ride = cls(row)

            rider_data = {
                "id": row["users.id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "email": row["email"],
                "password": row["password"]
            }
            driver_data = {
                "id": row["drivers.id"],
                "first_name": row["drivers.first_name"],
                "last_name": row["drivers.last_name"],
                "email": row["drivers.email"],
                "password": row["drivers.password"]
            }

            ride.driver = user.User(driver_data)
            ride.rider = user.User(rider_data)

            
            all_rides.append(ride)
        return all_rides

    @classmethod
    def get(cls, id):
        data = {"id": id}
        query = "SELECT * FROM rides LEFT JOIN users ON users.id = rides.users_id JOIN users AS drivers ON drivers.id = rides.drivers_id WHERE rides.id = %(id)s;"

        result = connectToMySQL(db).query_db(query, data)

        ride = result[0]

        rider_data = {
            "id": ride["users.id"],
            "first_name": ride["first_name"],
            "last_name": ride["last_name"],
            "email": ride["email"],
            "password": ride["password"]
        }
        driver_data = {
            "id": ride["drivers.id"],
            "first_name": ride["drivers.first_name"],
            "last_name": ride["drivers.last_name"],
            "email": ride["drivers.email"],
            "password": ride["drivers.password"]
        }

        ride = cls(ride)
        ride.rider=user.User(rider_data)
        ride.driver = user.User(driver_data)
        return ride

            


    @classmethod
    def update(cls, data):
        query = queries.update_query(table, data)
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def destroy(cls, id):
        data ={"id": id}
        query = queries.delete_query(table)
        return connectToMySQL(db).query_db(query, data)

    @staticmethod 
    def validate_ride(ride):
        is_valid = True
        if len(ride["destination"]) < 3:
            flash("Destination is required and must be at least 3 characters long")
            is_valid = False
        if len(ride["pickup_location"]) < 3:
            flash("Location is required and must be at least 3 characters long")
            is_valid = False
        if not ride["pickup_date"]:
            flash("Date is required")
            is_valid = False
        if len(ride["details"]) < 10:
            flash("Details are required and must have at least 10 characters")
            is_valid = False
        return is_valid

    @staticmethod
    def validate_update(ride):
        is_valid=True
        if len(ride["pickup_location"]) < 3:
            flash("Location is required and must be at least 3 characters long")
            is_valid = False
        if len(ride["details"]) < 10:
            flash("Details are required and must have at least 10 characters")
            is_valid = False
        return is_valid
        












