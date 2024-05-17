import logging
from flask import Flask, request, render_template
from flask_socketio import SocketIO, emit
from flask_socketio import ConnectionRefusedError

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')

connected_clients = {}  # Dictionary to track connected clients

@socketio.on('connect')
def handle_connect(auth):
    if (auth is None):
        raise ConnectionRefusedError('unathorized!')
    else:
        username = auth['username']
        connected_clients[username] = request.sid
        app.logger.info(f'Client {username} connected')

@socketio.on('disconnect')
def handle_disconnect():
    client_id = request.sid  # Get the unique ID of the client
    for username in [key for key, value in connected_clients.items() if value == client_id]:
        connected_clients.pop(username, None)
    app.logger.info(f'Client {client_id} disconnected')

@socketio.on('execute')
def send_message(data):
    sender_id = request.sid
    recipient_id = data['recipient_id']
    script_id = data['script_id']
    
    # Send message to the specified recipient
    session_id = connected_clients.get(recipient_id, None)
    if (session_id is None):
        emit('execute fail', {'message': 'User is not connected'})
    else:
        socketio.emit('execute', {'script_id': script_id}, to=session_id)
        emit('execute success', {'message': 'The execute message was sent'})

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True, allow_unsafe_werkzeug=True)