from flask import Flask, make_response, jsonify

app = Flask(__name__)

# Response with custom headers
@app.route('/custom-header')
def custom_header():
    response = make_response("Custom header response")
    response.headers['X-Custom-Header'] = 'MyValue'
    return response

# JSON response with custom headers
@app.route('/api/data')
def api_data():
    data = {"message": "Hello API"}
    response = make_response(jsonify(data))
    response.headers['Content-Type'] = 'application/json'
    return response

# Response with cookies
@app.route('/set-cookie')
def set_cookie():
    response = make_response("Cookie set!")
    response.set_cookie('session_id', 'abc123', max_age=3600)
    return response

if __name__ == '__main__':
    print("Starting Flask app for custom responses...")
    print("Try: http://localhost:5000/custom-header, /api/data, /set-cookie")
    app.run(debug=True)
