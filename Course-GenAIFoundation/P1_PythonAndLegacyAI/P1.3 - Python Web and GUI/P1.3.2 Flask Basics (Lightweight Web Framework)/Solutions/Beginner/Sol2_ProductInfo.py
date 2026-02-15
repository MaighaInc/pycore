from flask import Flask

app = Flask(__name__)

@app.route('/product')
def product():
    return '''
    <h2>Wireless Headphones</h2>
    <p><strong>Price:</strong> $59.99</p>
    <p><strong>Description:</strong> High-quality wireless headphones with noise cancellation and 20-hour battery life.</p>
    '''

if __name__ == '__main__':
    app.run(debug=True)
