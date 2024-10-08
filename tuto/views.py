from .app import *
from flask import render_template
from .models import get_sample, get_author, AuthorForm

from flask import url_for ,redirect, request
from .app import db
from .models import Author, Book



@app.route("/")
def home():
    return render_template("home.html", title="My Books !", books=get_sample(), bootstrap=bootstrap)


@app.route("/detail/<id>")
def detail(id):
    try:
        books = get_sample()  # ou `Book.query.all()` si tu utilises une base de données
        book = books[int(id) - 1]
        return render_template("detail.html", book=book)
    except IndexError:
        return render_template("404.html"), 404


@app.route("/edit/author/<int:id>")
def edit_author(id):
    a = get_author(id)
    f = AuthorForm(id=a.id, name=a.name)
    return render_template("edit-author.html", author=a, form=f)


@app.route("/save/author/", methods =("POST" ,))
def save_author():
    a = None
    f = AuthorForm()
    if f.validate_on_submit():
        id = int(f.id.data)
        a = get_author(id)
        a.name = f.name.data
        db.session.commit()
        return redirect(url_for('edit_author', id=a.id))
    a = get_author(int(f.id.data))
    return render_template("edit-author.html", author=a, form=f)


@app.route("/authors")
def authors():
    return render_template("authors.html", authors=Author.query.all())

@app.route("/add/author", methods =("GET" , "POST"))
def add_author():
    a = None
    f = AuthorForm()
    if f.validate_on_submit():
        id = int(f.id.data)
        a = get_author(id)
        a.name = f.name.data
        db.session.commit()
        return redirect(url_for('edit_author', id=a.id))
    a = get_author(int(f.id.data))
    return render_template("edit-author.html", author=a, form=f)

@app.route("/search", methods=["GET"])
def search():
    query = request.args.get('query')
    authors = Author.query.filter(Author.name.like(f'%{query}%')).all()  # Cherche les auteurs par nom
    books = []
    
    for author in authors:
        author_books = Book.query.filter(Book.author_id == author.id).all()  # Récupère tous les livres de cet auteur
        books.extend(author_books)  # Ajoute les livres à la liste
    
    return render_template("search_results.html", books=books, query=query)
