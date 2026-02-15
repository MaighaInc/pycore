from flask import Flask, render_template, request

app = Flask(__name__)

messages = []

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        message = request.form.get('message', '').strip()
        if name and message:
            messages.append({'name': name, 'message': message})
            return f"<h2>Thank you, {name}! Your message has been received.</h2>"
    return render_template('contact.html')

@app.route('/messages')
def show_messages():
    return render_template('messages.html', messages=messages)

if __name__ == '__main__':
    app.run(debug=True)
