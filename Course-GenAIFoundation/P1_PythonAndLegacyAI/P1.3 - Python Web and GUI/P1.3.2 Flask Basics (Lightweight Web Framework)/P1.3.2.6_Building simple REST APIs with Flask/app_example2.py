from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'},
    {'id': 2, 'name': 'Bob', 'email': 'bob@example.com'}
]

# UPDATE user (PUT)
@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    data = request.get_json()
    user['name'] = data.get('name', user['name'])
    user['email'] = data.get('email', user['email'])
    return jsonify(user), 200

# DELETE user
@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    original_len = len(users)
    users = [u for u in users if u['id'] != user_id]
    if len(users) == original_len:
        return jsonify({'error': 'User not found'}), 404
    return '', 204

@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

if __name__ == '__main__':
    app.run(debug=True)
