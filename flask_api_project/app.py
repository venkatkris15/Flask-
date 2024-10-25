from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
data = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"}
]

# Route to get all data
@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data)

# Route to get data by ID
@app.route('/data/<int:data_id>', methods=['GET'])
def get_data_by_id(data_id):
    item = next((item for item in data if item["id"] == data_id), None)
    return jsonify(item) if item else ('', 404)

# Route to add new data
@app.route('/data', methods=['POST'])
def add_data():
    new_item = request.get_json()
    data.append(new_item)
    return jsonify(new_item), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
