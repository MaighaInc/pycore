from flask import Flask, render_template

app = Flask(__name__)

# Page with CSS styling
@app.route('/')
def home():
    return render_template('styled.html')

# API endpoint for dynamic content
@app.route('/api/data')
def get_data():
    return {'message': 'Hello from API'}

if __name__ == '__main__':
    app.run(debug=True)
