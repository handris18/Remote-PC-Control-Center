from flask import Flask
import os
import subprocess
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
import sys
from pathlib import Path

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 1080
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'remote_pc_controller'
app.config['JWT_SECRET_KEY'] = 'Client'  
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access']
jwt = JWTManager(app)

save_path = os.path.dirname(os.path.abspath(__file__)) + 'Script.py'
url = 'http://example.com/'
successful = False
script_name = ''
UID = ''
password = ''

#websocket client
#jwt authentication
#generate unique UIDs

@app.route('/')
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
            return {'error': 'Script not found'}, 400

def download_script(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'w') as f:
            f.write(response.content)
        successful = True
    else:
        successful = False

if __name__ == '__main__':
    main_path = os.path.dirname(__file__)
    path = os.path.join(main_path, '..\\Persistence\\UID.txt')
    with open(path, 'r') as f:
        UID = f.read()
    password = sys.argv[1]
    login = {UID:password}
    '''res = requests.post(url + '/login', json=login)
    if res.status_code == 200:
        app.run(debug=True)'''
    if password != '':
        app.run(debug=True)
