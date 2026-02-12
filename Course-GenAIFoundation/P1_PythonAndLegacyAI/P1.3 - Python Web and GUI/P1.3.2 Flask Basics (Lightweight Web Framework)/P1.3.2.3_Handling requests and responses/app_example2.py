from flask import Flask, jsonify

app = Flask(__name__)

# Plain text response
@app.route('/text')
def text_response():
    return "This is plain text"

# HTML response
@app.route('/html')
def html_response():
    return """
    <html>
    <body>
    <h1>Hello from HTML</h1>
    <p>This is HTML content</p>
    </body>
    </html>
    """

# JSON response
@app.route('/api/user')
def json_response():
    user_data = {
        "id": 1,
        "name": "Alice",
        "email": "alice@example.com"
    }
    return jsonify(user_data)

if __name__ == '__main__':
    print("Starting Flask app for response types...")
    print("Try: http://localhost:5000/text, /html, /api/user")
    app.run(debug=True)
