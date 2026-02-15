from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name', '')
        return f"<h2>Thank you, {name}! Your message has been received.</h2>"
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
