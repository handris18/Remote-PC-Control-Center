from flask import Flask,request, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

connected_clients = {}  # Dictionary to track connected clients

@socketio.on('connect')
def handle_connect():
    client_id = request.sid  # Get the unique ID of the client
    connected_clients[client_id] = None  # Add the client to the dictionary
    print(f'Client {client_id} connected')

@socketio.on('disconnect')
def handle_disconnect():
    client_id = request.sid  # Get the unique ID of the client
    connected_clients.pop(client_id, None)  # Remove the client from the dictionary
    print(f'Client {client_id} disconnected')

@socketio.on('send_message')
def send_message(data):
    sender_id = request.sid
    recipient_id = data['recipient_id']
    message = data['message']
    
    # Send message to the specified recipient
    socketio.emit('receive_message', {'sender_id': sender_id, 'message': message}, room=recipient_id)

if __name__ == '__main__':
    print('Starting server...')
    socketio.run(app, host='0.0.0.0', port=5000)
