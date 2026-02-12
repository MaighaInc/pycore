from flask import Flask

# Create a Flask app instance
app = Flask(__name__)

# Define a route - homepage
@app.route('/')
def home():
    return "Welcome to Flask! This is the home page."

# Define another route - about page
@app.route('/about')
def about():
    return "This is the about page."

# Define a route with dynamic content
@app.route('/user/<name>')
def greet(name):
    return f"Hello, {name}! Welcome to Flask."

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
