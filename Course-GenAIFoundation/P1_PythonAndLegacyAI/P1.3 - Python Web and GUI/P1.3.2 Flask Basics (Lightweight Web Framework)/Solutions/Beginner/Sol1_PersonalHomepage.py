from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Jane Doe</h1>
    <p>Flask enthusiast and lifelong learner. Loves building web apps and teaching others.</p>
    <blockquote>"The best way to learn is to build."</blockquote>
    '''

if __name__ == '__main__':
    app.run(debug=True)
