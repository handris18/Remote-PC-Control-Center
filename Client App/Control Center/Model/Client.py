from flask import Flask
import os
import subprocess

app = Flask(__name__)

save_path = os.path.dirname(os.path.abspath(__file__)) + 'Script.py'
url = 'http://example.com/'
successful = False
script_name = ''

@app.route('/')
def Is_Online():
    return 'Online!'

@app.route('/run_script')
def process_message():
    data = request.json
    if 'run script' == data['action']:
        script_name = data['script_name']
        script_url = url + script_name
        download_script(script_url, save_path)
        if (successful):
            with open(save_path, 'r') as f:
                script = f.read()
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
    app.run(debug=True)