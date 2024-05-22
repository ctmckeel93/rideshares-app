from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_socketio import SocketIO
app = Flask(__name__)
app.secret_key = "flubbernuggets"
socketio = SocketIO(app)
Bootstrap5(app)
