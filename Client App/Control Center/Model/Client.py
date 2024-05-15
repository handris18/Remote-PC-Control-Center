from flask import Flask
import os
import subprocess
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
import sys
from pathlib import Path
import socketio

#app = Flask(__name__)
sio = socketio.Client()
'''app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 1080
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'remote_pc_controller'
app.config['JWT_SECRET_KEY'] = 'Client'  
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access']
jwt = JWTManager(app)'''

save_path = os.path.dirname(os.path.abspath(__file__)) + 'Script.py'
url = 'ws://localhost:7000'
api_url = 'http://localhost:5000'
successful = False
script_name = ''
UID = sys.argv[1]
password = ''
auth_data = {"username" : UID}

'''@app.route('/')
def Is_Online():
    return 'Online!'

@app.route('/run_script')
def process_message():
    data = request.json
    if 'run script' == data['action']:
        script_name = data['script_id']
        script_url = url + 'scripts/' + script_id
        download_script(script_url, save_path)
        if (successful):
            subprocess.run(['python', save_path])
            return 200
        else:
            return {'error': 'Script not found'}, 400'''

def download_script(url, save_path):
    print("runs", file=sys.stderr);
    response = requests.get(url)  #need jwt token header      Authorization: Bearer {jwt_token}
    if response.status_code == 200:
        with open(save_path, 'w') as f:
            f.write(response.content)
        successful = True
    else:
        successful = False

@sio.on('execute')
def handle_message(message):
    print("executes", file=sys.stderr);
    script_id = message['script_id']
    script_url = api_url + 'scripts/' + script_id
    download_script(script_url, save_path)
    if (successful):
        subprocess.run(['python', save_path])
        return 200
    else:
        return {'error': 'Script not found'}, 400

if __name__ == '__main__':
    sio.connect(url, auth=auth_data)
