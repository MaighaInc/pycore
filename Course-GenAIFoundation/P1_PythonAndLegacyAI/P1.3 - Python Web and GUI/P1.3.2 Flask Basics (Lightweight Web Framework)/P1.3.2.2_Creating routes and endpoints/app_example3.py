from flask import Flask, request

app = Flask(__name__)

# GET request (default)
@app.route('/data', methods=['GET'])
def get_data():
    return "Getting data..."

# POST request
@app.route('/submit', methods=['POST'])
def submit_form():
    return "Form submitted!"

# Handle both GET and POST
@app.route('/form', methods=['GET', 'POST'])
def handle_form():
    if request.method == 'POST':
        return "Processing form data..."
    else:
        return "Display form"

if __name__ == '__main__':
    print("Starting Flask app with HTTP methods...")
    print("Open http://localhost:5000 in your browser")
    print("Try:")
    print("  http://localhost:5000/data (GET)")
    print("  http://localhost:5000/form (GET)")
    app.run(debug=True)
