from application import db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField


class author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    nationality = db.Column(db.String(30), nullable=False)
    book = db.relationship('books', backref='booksbr')


class books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(30), nullable=False)
    author_id=db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    

class author_form(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    nationality =StringField('nationality')
    submit = SubmitField('Add to database')

class book_form(FlaskForm):
    title = StringField("titles")
    genre = StringField("genre")
    author = IntegerField("author ID")
    submit = SubmitField("Submit")

class book_update(FlaskForm):
    book = IntegerField("BOOK ID")
    title = StringField("update title")
    genre = StringField("update genre")  
    submit = SubmitField("Submit")


class book_deleteby(FlaskForm):
    bookdft=StringField ("TITLE")
    submit = SubmitField("DELETE")
    bookdf = IntegerField ("BOOK ID")
    submit2 = SubmitField("DELETE")



