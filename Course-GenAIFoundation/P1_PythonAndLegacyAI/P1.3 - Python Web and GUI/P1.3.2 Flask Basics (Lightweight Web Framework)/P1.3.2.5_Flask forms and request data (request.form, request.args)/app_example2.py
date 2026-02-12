from flask import Flask, render_template, request

app = Flask(__name__)

# Registration form with validation
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username', '')
        email = request.form.get('email', '')
        age = request.form.get('age', '')
        
        # Validation
        if len(username) < 3:
            return "Username must be at least 3 characters"
        if '@' not in email:
            return "Invalid email"
        try:
            age_int = int(age)
            if age_int < 13:
                return "Must be 13 or older"
        except ValueError:
            return "Age must be a number"
        
        return f"Registration successful! Welcome {username}"
    return render_template('register_form.html')

if __name__ == '__main__':
    app.run(debug=True)
