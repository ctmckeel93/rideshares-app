from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models import user, ride, message

@app.route("/rides/<int:id>")
def ride_details(id):
    logged_in = user.User.get_by_id(session["logged_in"])
    ride_details = ride.Ride.get(id)
    ride_messages = message.Message.get_messages_by_ride({"ride_id": id})
    return render_template("rides/details.html", ride=ride_details, ride_messages=ride_messages, logged_in=logged_in)

@app.route("/rides", methods=["GET","POST"])
def create_ride_request():
    if not "logged_in" in session:
        return redirect("/")
    
    if request.method == "GET":
        return render_template("rides/create.html", logged_in=user.User.get_by_id(session["logged_in"]) )
    else:
        if not ride.Ride.validate_ride(request.form):
            return redirect("/rides")
        ride.Ride.save(request.form)
        return redirect("/dashboard")

@app.route("/rides/edit/<int:id>", methods=["GET", "POST"])
def update_ride(id):
    if request.method == "GET":
        ride_to_edit = ride.Ride.get(id)
        return render_template("rides/edit.html", ride=ride_to_edit)
    else:
        if not ride.Ride.validate_update(request.form):
            return redirect("/rides/edit/" + str(id))
        ride.Ride.update(request.form)
        return redirect("/rides/" + str(id))

@app.route("/rides/driver/<int:ride_id>")
@app.route("/rides/driver/<int:drivers_id>/<int:ride_id>")
def update_driver(ride_id,drivers_id=None):
    data = {
        "id": ride_id ,
        "drivers_id": drivers_id 
    }
    user.User.drive_for(data)
    return redirect("/dashboard")

@app.route("/rides/delete/<int:ride_id>")
def destroy_ride(ride_id):
    ride.Ride.destroy(ride_id)
    return redirect("/dashboard")