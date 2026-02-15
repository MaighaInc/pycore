from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        name = request.form.get('name', '')
        message = request.form.get('message', '')
        return render_template('greeting_card.html', name=name, message=message)
    return render_template('greet_form.html')

if __name__ == '__main__':
    app.run(debug=True)
