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
    return f"Method: {request.method}, You searched for: {query}"

# Access headers
@app.route('/headers')
def show_headers():
    user_agent = request.headers.get('User-Agent')
    return f"Method: {request.method}, Your browser: {user_agent}"

if __name__ == '__main__':
    print("Starting Flask app for request handling...")
    print("Open http://localhost:5000/info to see request method and path")
    print("Try: http://localhost:5000/search?q=python")
    print("Try: http://localhost:5000/headers to see your browser info")
    app.run(debug=True)
