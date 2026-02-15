from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

books = [
    {"id": 1, "title": "The Martian", "author": "Andy Weir"},
    {"id": 2, "title": "Atomic Habits", "author": "James Clear"},
    {"id": 3, "title": "To Kill a Mockingbird", "author": "Harper Lee"}
]

def get_book(book_id):
    return next((b for b in books if b["id"] == book_id), None)

@app.route('/books', methods=['GET', 'POST'])
def book_catalog():
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        author = request.form.get('author', '').strip()
        if title and author:
            new_id = max([b['id'] for b in books], default=0) + 1
            books.append({"id": new_id, "title": title, "author": author})
    return render_template('books.html', books=books)

@app.route('/books/<int:book_id>')
def book_detail(book_id):
    book = get_book(book_id)
    return render_template('book_detail.html', book=book)

@app.route('/books/delete/<int:book_id>', methods=['POST'])
def delete_book(book_id):
    book = get_book(book_id)
    if book:
        books.remove(book)
    return redirect(url_for('book_catalog'))

if __name__ == '__main__':
    app.run(debug=True)
