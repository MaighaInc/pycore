from flask import Flask, render_template

app = Flask(__name__)

@app.route('/books')
def books():
    book_list = [
        {"title": "The Martian", "author": "Andy Weir"},
        {"title": "Atomic Habits", "author": "James Clear"},
        {"title": "To Kill a Mockingbird", "author": "Harper Lee"}
    ]
    return render_template('books.html', books=book_list)

if __name__ == '__main__':
    app.run(debug=True)
