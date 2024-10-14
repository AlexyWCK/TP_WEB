from .app import db

from flask_wtf import FlaskForm
from wtforms import StringField , HiddenField
from wtforms. validators import DataRequired


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __repr__(self):#c'est un to string
        return "<Author (%d) %s>" % (self.id, self.name)



class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float)
    title = db.Column(db.String(100))
    url = db.Column(db.String(100))
    img = db.Column(db.String(100))
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    author = db.relationship('Author',
    backref=db.backref('books', lazy='dynamic'))
    def __repr__(self ):
        return "<Book (%d) %s>" % (self.id, self.title)


class AuthorForm(FlaskForm):
    id = HiddenField('id')
    name = StringField('Nom', validators=[DataRequired()])



def get_sample():
    return Book.query.all()

def get_author(id):
    return Author.query.get(id)
