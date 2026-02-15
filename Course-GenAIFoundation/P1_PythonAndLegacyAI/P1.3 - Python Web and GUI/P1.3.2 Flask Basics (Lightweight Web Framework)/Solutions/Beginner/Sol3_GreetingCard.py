from flask import Flask

app = Flask(__name__)

@app.route('/greet/<name>')
def greet(name):
    return f'''
    <div style="border:2px solid #4CAF50; padding:20px; width:300px; margin:30px auto; text-align:center;">
        <h1>Greetings, {name}!</h1>
        <p>Wishing you a wonderful day!</p>
    </div>
    '''

if __name__ == '__main__':
    app.run(debug=True)
