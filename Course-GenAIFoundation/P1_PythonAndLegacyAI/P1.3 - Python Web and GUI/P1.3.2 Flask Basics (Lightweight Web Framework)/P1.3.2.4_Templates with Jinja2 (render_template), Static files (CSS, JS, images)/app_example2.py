from flask import Flask, render_template

app = Flask(__name__)

# Display list of items
@app.route('/items')
def items():
    products = ['Laptop', 'Phone', 'Tablet', 'Monitor']
    return render_template('items.html', products=products)

# Display users with conditionals
@app.route('/users')
def users():
    users_list = [
        {'name': 'Alice', 'age': 25, 'status': 'active'},
        {'name': 'Bob', 'age': 17, 'status': 'active'},
        {'name': 'Charlie', 'age': 30, 'status': 'inactive'}
    ]
    return render_template('users.html', users=users_list)

if __name__ == '__main__':
    app.run(debug=True)
