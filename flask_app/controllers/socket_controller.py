from app import socketio

@socketio.on("connect")
def connect():
    print("Connecting...")
    print("Welcome to flask sockets!")

@socketio.on("disconnect")
def disconnect():
    print("Goodbye then!")

@socketio.on("test")
def test(data):
    print(data["message"])
    print("Testing")

