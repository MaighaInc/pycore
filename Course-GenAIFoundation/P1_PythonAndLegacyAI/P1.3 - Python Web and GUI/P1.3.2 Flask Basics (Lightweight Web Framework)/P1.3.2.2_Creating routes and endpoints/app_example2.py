from flask import Flask

app = Flask(__name__)

@app.route('/')
def default():
    return f"Welcome to the Flask Server!"

# Route with one parameter
@app.route('/user/<name>')
def greet_user(name):
    return f"Hello, {name}!"

# Route with multiple parameters
@app.route('/post/<int:post_id>')
def get_post(post_id):
    return f"Post ID: {post_id}"

# Route with string and integer parameters
@app.route('/profile/<username>/<int:user_id>')
def profile(username, user_id):
    return f"Profile: {username} (ID: {user_id})"

if __name__ == '__main__':
    print("Starting Flask app with route parameters...")
    print("Open http://localhost:5000 in your browser")
    print("Try:")
    print("  http://localhost:5000/user/maya")
    print("  http://localhost:5000/post/42")
    print("  http://localhost:5000/profile/john/123")
    app.run(debug=True)
