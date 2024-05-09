from flask import Flask, request, jsonify
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_mysqldb import MySQL
from datetime import datetime
import json
import sys
from io import StringIO


app = Flask(__name__)
CORS(app)
app.config['MYSQL_HOST'] = 'mysql'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'easy_access'
app.config['JWT_SECRET_KEY'] = 'Aminebk2001'  
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access']
jwt = JWTManager(app)
mysql = MySQL(app)

class User:
    def __init__(self, user_id, email, password):
        self.user_id = user_id
        self.email = email
        self.password = password
        self.jwt_token = None

# Token blacklist (this could be a database table)
blacklisted_tokens = set()

# Route to get all the users data from the database
@app.route('/data', methods=['GET'])
def get_data():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM users''')
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

@app.route('/register', methods=['POST'])
def register():
    device_number = request.json.get('device_number')
    password = request.json.get('password')
    
    # Check if device number already exists
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE device_number = %s", (device_number,))
    device = cur.fetchone()
    
    if device:
        return jsonify({"message": "Device number already registered"}), 400
    
    # Insert new device into the database
    cur.execute("INSERT INTO users (device_number, password) VALUES (%s, %s)", (device_number, password))
    mysql.connection.commit()
    cur.close()
    
    return jsonify({"message": "Registration successful"}), 200


# Endpoint for user login and JWT token generation
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    device_number = data.get('device_number')
    password = data.get('password')

    # Fetch user from database based on email
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE device_number = %s", (device_number,))
    user = cur.fetchone()
    cur.close()

    if user:
        user_id, stored_password = user[0], user[2]

        # Check if the password matches
        if password == stored_password:
            # Generate JWT token
            access_token = create_access_token(identity=user_id)
            return jsonify({'message': 'Login successful', 'access_token': access_token}), 200

    # Return error message for invalid credentials
    return jsonify({'error': 'Invalid email or password'}), 401

# Endpoint to create a new coding script
@app.route('/scripts/create', methods=['POST'])
@jwt_required()
def create_script():
    data = request.json
    script_name = data.get('script_name')
    content = data.get('content')
    user_id = get_jwt_identity()

    if not script_name or content == None:
        return jsonify({'error': 'Script name and content are required'}), 400

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO scripts (user_id, script_name, content,date_created) VALUES (%s, %s, %s, NOW())", (user_id, script_name, content))

    # Get the last inserted script_id
    cur.execute("SELECT LAST_INSERT_ID()")
    script_id = cur.fetchone()[0]

    mysql.connection.commit()
    cur.close()
    
    return jsonify({'message': f'Script {script_id} created successfully', 'script_id': script_id}), 201

# Endpoint to edit a specific coding script by ID
@app.route('/scripts/<int:script_id>/update', methods=['PUT'])
@jwt_required()
def edit_script(script_id):
    current_user = get_jwt_identity()
    data = request.json
    new_script_name = data.get('script_name')
    new_content = data.get('content')

    if not new_script_name and not new_content:
        return jsonify({'error': 'Script name or content is required for editing'}), 400

    cur = mysql.connection.cursor()
    # Check if the script exists and belongs to the current user
    cur.execute("SELECT user_id FROM scripts WHERE script_id = %s", (script_id,))
    result = cur.fetchone()
    if not result:
        return jsonify({'error': 'Script not found'}), 404
    if result[0] != current_user:
        return jsonify({'error': 'You are not authorized to edit this script'}), 403

    # Update script_name and/or content in the database
    if new_script_name:
        cur.execute("UPDATE scripts SET script_name = %s WHERE script_id = %s", (new_script_name, script_id))
    if new_content:
        cur.execute("UPDATE scripts SET content = %s WHERE script_id = %s", (new_content, script_id))
    mysql.connection.commit()
    cur.close()

    return jsonify({'message': 'Script updated successfully'}), 200




# fetch the scripts
@app.route('/scripts/fetch', methods=['GET'])
@jwt_required()
def fetch_scripts():
    current_user = get_jwt_identity()

    cur = mysql.connection.cursor()
    cur.execute("SELECT script_id , script_name , content FROM scripts WHERE user_id = %s", (current_user,))
    scripts = cur.fetchall()
    cur.close()

    if scripts:
        return jsonify(scripts), 200
    else:
        return jsonify({'message': 'No scripts found for the current user'}), 404


# Endpoint to fetch a specific coding script by ID
@app.route('/scripts/<int:script_id>', methods=['GET'])
@jwt_required()
def fetch_script(script_id):
    current_user = get_jwt_identity()

    cur = mysql.connection.cursor()
    cur.execute("SELECT script_id , script_name , content  FROM scripts WHERE script_id = %s AND user_id = %s", (script_id, current_user))
    script = cur.fetchone()
    cur.close()

    if script:
        return jsonify(script), 200
    else:
        return jsonify({'error': 'Script not found'}), 404

# Endpoint to execute a specific coding script by ID
@app.route('/scripts/<int:script_id>/execute', methods=['POST'])
@jwt_required()
def execute_script(script_id):
    current_user = get_jwt_identity()

    cur = mysql.connection.cursor()
    cur.execute("SELECT content FROM scripts WHERE script_id = %s AND user_id = %s", (script_id, current_user))
    script_content_tuple = cur.fetchone()
    cur.close()

    if script_content_tuple:
        script_content = script_content_tuple[0]  # Accessing the first element of the tuple
        # Execute the script
        try:
            # Capture standard output and error
            sys.stdout = StringIO()
            sys.stderr = StringIO()
            exec(script_content)
            output = sys.stdout.getvalue()
            error = sys.stderr.getvalue()
            # Restore sys.stdout and sys.stderr
            sys.stdout = sys.__stdout__
            sys.stderr = sys.__stderr__
            # Check if there was any error during execution
            if error:
                return jsonify({'error': error}), 500
            else:
                return jsonify({'output': output}), 200
        except Exception as e:
            return jsonify({'error': f'Error executing script: {str(e)}'}), 500
    else:
        return jsonify({'error': 'Script not found'}), 404



if __name__ == '__main__':
    app.run(debug=True)
