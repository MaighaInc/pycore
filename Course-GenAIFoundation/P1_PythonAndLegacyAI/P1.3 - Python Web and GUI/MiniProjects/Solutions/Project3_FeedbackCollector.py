"""
Mini Project 3: Feedback Collector Web App (Solution)
"""

from flask import Flask, render_template, request, redirect, url_for
import os


app = Flask(__name__)
feedbacks = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        feedback = request.form['feedback']
        category = request.form['category']
        rating = request.form.get('rating', '')
        feedbacks.append({
            'name': name,
            'email': email,
            'feedback': feedback,
            'category': category,
            'rating': rating
        })
        return redirect(url_for('index'))
    # Filtering by category
    category_filter = request.args.get('category')
    if category_filter:
        filtered = [f for f in feedbacks if f['category'] == category_filter]
    else:
        filtered = feedbacks
    categories = sorted(set(f['category'] for f in feedbacks))
    return render_template('feedback.html', feedbacks=filtered, categories=categories, selected_category=category_filter)

if __name__ == '__main__':
    app.run(debug=True)
