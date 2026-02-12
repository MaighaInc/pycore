from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database
users = [
    {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'},
    {'id': 2, 'name': 'Bob', 'email': 'bob@example.com'}
]
next_id = 3

# GET all users
@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# GET specific user
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user), 200

# Create new user (POST)
@app.route('/api/users', methods=['POST'])
def create_user():
    global next_id
    data = request.get_json()
    new_user = {'id': next_id, 'name': data.get('name'), 'email': data.get('email')}
    users.append(new_user)
    next_id += 1
    return jsonify(new_user), 201

if __name__ == '__main__':
    app.run(debug=True)
