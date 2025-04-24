from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['todoDatabase']
collection = db['todoItems']

@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    itemName = request.json.get('itemName')
    itemDescription = request.json.get('itemDescription')

    if itemName and itemDescription:
        collection.insert_one({'itemName': itemName, 'itemDescription': itemDescription})
        return jsonify({'message': 'To-Do item saved successfully'}), 200
    else:
        return jsonify({'error': 'Invalid input'}), 400

if __name__ == '__main__':
    app.run(debug=True)