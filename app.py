
from flask import Flask, jsonify
import json

app = Flask(__name__)

# Path to the backend file
DATA_FILE = 'data.json'

# Load data from the backend file
def load_data():
    try:
        with open(DATA_FILE, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []  # Return an empty list if the file does not exist

@app.route('/api', methods=['GET'])
def api_route():
    data = load_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)