from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    name = "Jane Doe"
    bio = "Flask enthusiast and lifelong learner. Loves building web apps and teaching others."
    quote = "The best way to learn is to build."
    return render_template('home.html', name=name, bio=bio, quote=quote)

if __name__ == '__main__':
    app.run(debug=True)
