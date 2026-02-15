from flask import Flask, render_template, request

app = Flask(__name__)

books = [
    {"title": "The Martian", "author": "Andy Weir"},
    {"title": "Atomic Habits", "author": "James Clear"},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee"}
]

@app.route('/books', methods=['GET', 'POST'])
def book_catalog():
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        author = request.form.get('author', '').strip()
        if title and author:
            books.append({"title": title, "author": author})
    return render_template('books.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)
