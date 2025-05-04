from app import app, db
from app.models.books import Books
from flask import render_template, redirect, request

@app.route('/books')
def index():
    books = Books.query.all()
    return render_template('index.html', books = books) 

@app.route('/books/register', methods=['POST'])
def register_book():
    form_name = request.form['title']
    form_author = request.form['author']

    new_book = Books(
        book_name = form_name,
        author = form_author
    )
    db.session.add(new_book)
    db.session.commit()
    return redirect('/books')

@app.route('/books/delete/<int:id>', methods=['POST'])
def delete_book(id):
    book_to_delete = Books.query.get(id)
    if book_to_delete:
        db.session.delete(book_to_delete)  
        db.session.commit()  
    return redirect('/books')