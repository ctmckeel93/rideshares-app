from dotenv import load_dotenv
load_dotenv()
from flask_app import app
from flask_app.controllers import user_controller, ride_controller, message_controller, socket_controller
from flask_app import socketio


if __name__ == "__main__":
    socketio.run(app,debug=True)