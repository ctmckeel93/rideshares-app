from flask_app import app
from flask import redirect, request, session
from flask_app.models import message

@app.route("/messages", methods=["POST"])
def create_message():
    if not "logged_in" in session:
        return redirect("/")
    
    is_valid = message.Message.validate_message(request.form)

    if is_valid:
        message.Message.save(request.form)

    return redirect("/rides/" + str(request.form["rides_id"]))
