import socketio
from flask import Flask
import os
import subprocess
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
import sys
from pathlib import Path
import requests
import json

#app = Flask(__name__)
sio = socketio.Client()

save_path = os.path.dirname(os.path.abspath(__file__))
url = 'ws://localhost:7000/'
api_url = 'http://localhost:5000/'
script_name = ''
UID = sys.argv[1]
password = ''
token = sys.argv[2]
auth_data = {"username" : UID}

def download_script(url, path):
    print("downloads", file=sys.stderr);
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        with open(path, 'w') as f:
            f.write(json.loads(response.text)[2])
        return True
    else:
        return False

@sio.on('execute')
def handle_message(message):
    print("executes", file=sys.stderr);
    script_id = message['script_id']
    script_url = api_url + 'scripts/' + str(script_id)
    if (download_script(script_url, save_path + '/Script.py')):
        os.chdir(save_path)
        cmd = subprocess.Popen(('cmd /k python Script.py'), creationflags=subprocess.CREATE_NEW_CONSOLE)
        print("Ran?")
        return 200
    else:
        return {'error': 'Script not found'}, 400

if __name__ == '__main__':
    sio.connect(url, auth=auth_data)
    while (True):
        continue
