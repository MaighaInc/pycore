from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

greeting_cards = []

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        name = request.form.get('name', '')
        message = request.form.get('message', '')
        greeting_cards.append({'name': name, 'message': message})
        return render_template('greeting_card.html', name=name, message=message)
    return render_template('greet_form.html')

@app.route('/greet/history')
def greet_history():
    return render_template('greet_history.html', cards=greeting_cards)

if __name__ == '__main__':
    app.run(debug=True)
