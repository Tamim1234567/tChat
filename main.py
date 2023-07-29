from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'  # Replace with your own secret key
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print('Client connected!')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected!')

@socketio.on('message_from_client')
def handle_message(data):
    message = data['message']
    print(f'Received message: {message}')
    # Broadcast the message to all connected clients
    emit('message_from_server', {'message': message}, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, debug=True)
