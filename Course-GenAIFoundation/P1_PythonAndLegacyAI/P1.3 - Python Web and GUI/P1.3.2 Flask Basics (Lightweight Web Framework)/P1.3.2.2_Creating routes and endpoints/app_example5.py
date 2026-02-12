from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Home Page"

# Handle 404 - Page Not Found
@app.errorhandler(404)
def page_not_found(error):
    return """
    <h1>Page not found! (404)</h1>
    <p>The page you are looking for does not exist.</p>
    """, 404

# Handle 500 - Server Error
@app.errorhandler(500)
def server_error(error):
    return """
    <h1>Server error! (500)</h1>
    <p>Something went wrong on our end.</p>
    """, 500

if __name__ == '__main__':
    print("Starting Flask app with error handlers...")
    print("Open http://localhost:5000 in your browser")
    print("Try visiting a non-existent URL like: http://localhost:5000/invalid")
    app.run(debug=True)
