from flask import Flask, jsonify, request

app = Flask(__name__)

products = [
    {'id': 1, 'name': 'Laptop', 'price': 999.99},
    {'id': 2, 'name': 'Phone', 'price': 499.99}
]
next_id = 3

# Create product with validation
@app.route('/api/products', methods=['POST'])
def create_product():
    global next_id
    data = request.get_json()
    
    # Validation
    if not data:
        return jsonify({'error': 'No JSON data provided'}), 400
    
    if 'name' not in data or not data['name']:
        return jsonify({'error': 'Name is required'}), 400
    
    if 'price' not in data:
        return jsonify({'error': 'Price is required'}), 400
    
    try:
        price = float(data['price'])
        if price < 0:
            return jsonify({'error': 'Price must be positive'}), 400
    except (ValueError, TypeError):
        return jsonify({'error': 'Price must be a number'}), 400
    
    new_product = {'id': next_id, 'name': data['name'], 'price': price}
    products.append(new_product)
    next_id += 1
    return jsonify(new_product), 201

@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(products), 200

if __name__ == '__main__':
    app.run(debug=True)
