from flask import Flask, request

app = Flask(__name__)

# Access URL path
@app.route('/info')
def info():
    return f"Method: {request.method}, Path: {request.path}"

# Access query parameters (?name=value)
@app.route('/search')
def search():
    query = request.args.get('q', 'default')
    return f"You searched for: {query}"

# Access form data (POST)
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    return f"Login: {username}"

# Access headers
@app.route('/headers')
def show_headers():
    user_agent = request.headers.get('User-Agent')
    return f"Your browser: {user_agent}"

if __name__ == '__main__':
    print("Starting Flask app for request handling...")
    print("Try: http://localhost:5000/search?q=python")
    app.run(debug=True)
