from flask import Flask

app = Flask(__name__)

# Route 1: Home page
@app.route('/')
def home():
    return "Welcome Home!"

# Route 2: About page
@app.route('/about')
def about():
    return "About Us"

# Route 3: Contact page
@app.route('/contact')
def contact():
    return "Contact Us"

if __name__ == '__main__':
    print("Starting Flask app...")
    print("Open http://localhost:5000 in your browser")
    print("Try: / , /about , /contact")
    app.run(debug=True)
