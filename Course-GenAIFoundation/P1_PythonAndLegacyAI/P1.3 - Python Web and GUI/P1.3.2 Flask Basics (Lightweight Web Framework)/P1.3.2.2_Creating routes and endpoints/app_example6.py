from flask import Flask

app = Flask(__name__)

# Integer parameter
@app.route('/age/<int:age>')
def check_age(age):
    if age < 18:
        return f"You are {age}, you are a minor"
    else:
        return f"You are {age}, you are an adult"

# Float parameter
@app.route('/temp/<float:celsius>')
def convert_temp(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return f"{celsius}°C = {fahrenheit}°F"

# Path parameter (captures everything)
@app.route('/files/<path:filepath>')
def view_file(filepath):
    return f"File path: {filepath}"

if __name__ == '__main__':
    print("Starting Flask app with parameter types...")
    print("Open http://localhost:5000 in your browser")
    print("Try:")
    print("  http://localhost:5000/age/25")
    print("  http://localhost:5000/temp/100")
    print("  http://localhost:5000/files/documents/report.pdf")
    app.run(debug=True)
