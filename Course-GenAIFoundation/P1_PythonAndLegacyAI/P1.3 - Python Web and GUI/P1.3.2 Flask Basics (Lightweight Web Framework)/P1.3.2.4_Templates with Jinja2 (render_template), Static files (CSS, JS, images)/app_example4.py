from flask import Flask, render_template

app = Flask(__name__)

# Home page using template inheritance
@app.route('/')
def home():
    return render_template('page_home.html', title='Home')

# About page using template inheritance
@app.route('/about')
def about():
    return render_template('page_about.html', title='About Us')

# Contact page using template inheritance
@app.route('/contact')
def contact():
    return render_template('page_contact.html', title='Contact')

if __name__ == '__main__':
    app.run(debug=True)
