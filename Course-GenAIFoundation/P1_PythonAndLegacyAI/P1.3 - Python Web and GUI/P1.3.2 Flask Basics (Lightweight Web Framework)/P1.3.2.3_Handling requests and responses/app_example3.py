from flask import Flask, jsonify

app = Flask(__name__)

# 200 OK (default)
@app.route('/success')
def success():
    return "Success!", 200

# 201 Created (after creating resource)
@app.route('/create', methods=['POST'])
def create():
    new_item = {"id": 1, "name": "Item"}
    return jsonify(new_item), 201

# 400 Bad Request (client error)
@app.route('/bad')
def bad_request():
    return "Bad request!", 400

# 404 Not Found
@app.route('/notfound')
def not_found():
    return "Not found!", 404

# 500 Server Error
@app.route('/error')
def server_error():
    return "Server error!", 500

if __name__ == '__main__':
    print("Starting Flask app for status codes...")
    print("Try: http://localhost:5000/success, /bad, /notfound")
    app.run(debug=True)
