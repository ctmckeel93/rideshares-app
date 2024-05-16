from flask_app import app
from flask_app.controllers import user_controller, ride_controller, message_controller
from dotenv import load_dotenv
load_dotenv()

if __name__ == "__main__":
    app.run(debug=True)