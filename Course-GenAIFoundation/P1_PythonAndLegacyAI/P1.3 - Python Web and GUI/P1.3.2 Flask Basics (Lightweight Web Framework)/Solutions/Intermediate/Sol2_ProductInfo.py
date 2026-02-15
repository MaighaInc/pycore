from flask import Flask, render_template, url_for

app = Flask(__name__)

products = [
    {"id": 1, "name": "Wireless Headphones", "price": 59.99, "desc": "High-quality wireless headphones with noise cancellation."},
    {"id": 2, "name": "Smart Watch", "price": 99.99, "desc": "Track your fitness and notifications on the go."},
    {"id": 3, "name": "Bluetooth Speaker", "price": 29.99, "desc": "Portable speaker with deep bass and long battery life."}
]

@app.route('/products')
def product_list():
    return render_template('products.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    return render_template('product_detail.html', product=product)

if __name__ == '__main__':
    app.run(debug=True)
