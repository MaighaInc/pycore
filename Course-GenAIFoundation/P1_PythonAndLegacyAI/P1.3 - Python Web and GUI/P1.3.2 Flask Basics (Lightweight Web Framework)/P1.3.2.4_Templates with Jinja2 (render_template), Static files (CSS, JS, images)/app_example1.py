from flask import Flask, render_template

app = Flask(__name__)

# Basic template with variables
@app.route('/')
def home():
    username = 'Alice'
    title = 'Welcome to My App'
    return render_template('home.html', username=username, title=title)

# Template with user profile
@app.route('/profile/<name>')
def profile(name):
    user = {
        'name': name,
        'age': 25,
        'email': f'{name}@example.com'
    }
    return render_template('user.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)
