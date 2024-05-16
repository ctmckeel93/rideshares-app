from flask_app import app
from flask import redirect, request
from flask_app.models import message

@app.route("/messages", methods=["POST"])
def create_message():
    message.Message.save(request.form)
    return redirect("/rides/" + str(request.form["rides_id"]))
