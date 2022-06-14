from application import db
from application.models import db,books,author
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField

db.drop_all()
db.create_all()

Kafka=author(first_name="Franz",last_name="Kafka",nationality="Czech Republic")
Fitzgerald=author(first_name="F. Scott",last_name="Fitzgerald",nationality="American")
salinger=author(first_name="j.d ",last_name="salinger",nationality="American")
Borges=author(first_name="Jorge Luis",last_name="Borges",nationality="argentina")
márquez=author(first_name=" gabriel",last_name="garcía márquez",nationality="Colombia ")
db.session.add(Kafka)
db.session.add(Fitzgerald)
db.session.add(salinger)
db.session.add(Borges)
db.session.add(márquez)
db.session.commit()


book1= books(title="One Hundred Years of Solitude",genre="magical realism",booksbr=márquez)
book2=books(title="The great gatsby", genre="tragedy",booksbr=Fitzgerald)
book3=books(title="Fictions", genre="Anthology",booksbr=Borges)
book4=books(title="The Metamorphosis", genre="magical realism",booksbr=Kafka)
book5=books(title="The catcher in the rye",genre="coming of age",booksbr=salinger)
book6=books(title="The trial",genre="magical realism",booksbr=Kafka)
db.session.add(book1)
db.session.add(book2)
db.session.add(book3)
db.session.add(book4)
db.session.add(book5)
db.session.add(book6)
db.session.commit()


