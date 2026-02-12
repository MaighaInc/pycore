from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Feedback form with redirect
@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form.get('name')
        rating = request.form.get('rating')
        comment = request.form.get('comment')
        
        # Process feedback (save to database, send email, etc.)
        # ...
        
        return redirect(url_for('thank_you', name=name))
    
    return render_template('feedback_form.html')

# Thank you page
@app.route('/thank-you')
def thank_you():
    name = request.args.get('name', 'Guest')
    return render_template('thank_you.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
