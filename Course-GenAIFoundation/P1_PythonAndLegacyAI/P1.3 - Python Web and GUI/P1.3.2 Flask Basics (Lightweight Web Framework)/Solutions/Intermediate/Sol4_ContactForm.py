from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    error = None
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        message = request.form.get('message', '').strip()
        if not name or not message:
            error = "Both name and message are required."
            return render_template('contact.html', error=error, name=name, message=message)
        return f"<h2>Thank you, {name}! Your message has been received.</h2>"
    return render_template('contact.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)
