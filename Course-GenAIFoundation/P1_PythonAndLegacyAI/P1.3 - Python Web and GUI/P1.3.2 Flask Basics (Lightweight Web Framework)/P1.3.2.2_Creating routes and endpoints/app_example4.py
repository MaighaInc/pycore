from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def home():
    # Generate URLs dynamically
    about_url = url_for('about_page')
    user_url = url_for('user_profile', username='alice')
    return f"""
    <html>
    <body>
    <h1>Home Page</h1>
    <a href="{about_url}">About</a><br>
    <a href="{user_url}">Alice's Profile</a>
    </body>
    </html>
    """

@app.route('/about')
def about_page():
    home_url = url_for('home')
    return f"""
    <html>
    <body>
    <h1>About Page</h1>
    <a href="{home_url}">Back Home</a>
    </body>
    </html>
    """

@app.route('/user/<username>')
def user_profile(username):
    home_url = url_for('home')
    return f"""
    <html>
    <body>
    <h1>Profile: {username}</h1>
    <a href="{home_url}">Back Home</a>
    </body>
    </html>
    """

if __name__ == '__main__':
    print("Starting Flask app with url_for()...")
    print("Open http://localhost:5000 in your browser")
    print("Click on the links to navigate")
    app.run(debug=True)
