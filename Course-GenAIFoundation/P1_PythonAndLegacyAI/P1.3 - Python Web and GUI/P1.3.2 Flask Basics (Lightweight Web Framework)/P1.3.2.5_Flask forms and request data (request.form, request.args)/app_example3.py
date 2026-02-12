from flask import Flask, render_template, request
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# File upload handler
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file selected"
        
        file = request.files['file']
        if file.filename == '':
            return "No file selected"
        
        # Check file type
        allowed_ext = {'txt', 'pdf', 'png', 'jpg'}
        ext = file.filename.split('.')[-1].lower()
        if ext not in allowed_ext:
            return f"File type .{ext} not allowed"
        
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return f"File {filename} uploaded successfully!"
    
    return render_template('upload_form.html')

if __name__ == '__main__':
    app.run(debug=True)
