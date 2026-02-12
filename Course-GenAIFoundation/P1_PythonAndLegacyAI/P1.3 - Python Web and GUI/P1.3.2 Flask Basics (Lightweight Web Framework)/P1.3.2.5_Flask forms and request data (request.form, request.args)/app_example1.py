from flask import Flask, render_template, request

app = Flask(__name__)

# Display form (GET) and process form (POST)
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        return f"Thank you {name}! We received your message: {message}"
    return render_template('contact_form.html')

# Simple GET form with query parameters
@app.route('/search')
def search():
    query = request.args.get('q', 'No search term')
    return f"You searched for: {query}"

if __name__ == '__main__':
    app.run(debug=True)
