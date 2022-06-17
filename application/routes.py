from application import app, db
from application.models import *
from flask import Flask, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
import itertools


@app.route('/home')
def home():
    return render_template('home.html')

@app.route("/")
def re():
    
    return redirect(url_for("home"))

#user can go to a authors page directly to view all their books
@app.route('/<name>')
def kaf(name):
    authorspage=author.query.filter_by(last_name=name).first()
    authorspage_str= authorspage.first_name +" "+ name + " books"      
    return render_template('search.html',authorspage_str=authorspage_str,authorspage=authorspage)


@app.route('/view_all')
def viewing_all():
    #this page is going to list every book in the database in alphabetical order
    idrange=[books.id for books in books.query.all()] #first get every book's id. 
    plist=[]

    #next run a loop which is going to get every book and match it with it's author based on the book id.
    for i in idrange:       
        listitle=books.query.filter_by(id=i).first()
        plist+={listitle.title}
        listauthor=author.query.filter_by(id=listitle.author_id).first()
        plist.append(listauthor.first_name +" "+ listauthor.last_name + "  ")

    #now there is a list with every book followed by the authors name. however this information is still unconnected in a list

    #turning the list into a dictionary linking every two items together. i.e   1:2/3:4/5:6 become keys and value pairs
    plist=dict(itertools.zip_longest(*[iter(plist)] * 2, fillvalue="")) 
   
    sortedbooks=sorted(plist)#sorted on a dictionary will only sort for the keys removing the values

    #there is now a dictionary with the books:authors and a list with the books sorted in order. 
    #going to use both to get a string with books sorted in order followed by author split with\n
    bookssorted_a_z=" \n"
    for i in sortedbooks:
        values=plist[i]
        bookssorted_a_z += f'{i}:{values}\n'
    
    bookssorted_a_z=bookssorted_a_z.split("\n") #use the \n to split the list so it can be split up in the html file.

    return render_template('view_all.html',bookssorted_a_z=bookssorted_a_z)

    
@app.route('/add_books',methods=['GET', 'POST'])
def registerbooks():
    message = ""
    form=book_form()
    if request.method == "POST":
        addtitle=form.title.data
        addgenre=form.genre.data
        addauthorid=form.author.data
        newbook=books(title=addtitle, genre=addgenre,author_id=addauthorid)
        db.session.add(newbook)
        db.session.commit()
        message= f'Added {addtitle} to database'
        
    return render_template('addingb.html',form=form, message=message)


@app.route('/add_authors',methods=['GET', 'POST'])
def register():
    message = ""
    form = author_form()

    if request.method == 'POST':
        ADDfirst_name= form.first_name.data
        ADDlast_name= form.last_name.data
        ADDnationality=form.nationality.data
        if ADDfirst_name== None:
            ADDfirst_name=" "
        if ADDlast_name== None:
            ADDlast_name=" "
        if ADDnationality== None:
            ADDnationality=" "
        ADDfirst_name=ADDfirst_name.strip() #had to add strip method otherwie same name with spaces was added.
        ADDlast_name=ADDlast_name.strip()

        a1 = [author.first_name for author in author.query.all()]
        a2 = [author.last_name for author in author.query.all()]
        a1=[element.lower() for element in a1] ; a1
        a2=[element.lower() for element in a2] ; a2

        #making sure all fields are added.
        if len(ADDfirst_name) == 0 or len(ADDlast_name) == 0 or len(ADDnationality)==0:
            message = "all fields need to be filled"

        #making sure that no duplicate entrys are made for authors.i.e. user enters same name but capitalized
        #first name and surname split up in case of authors having same first or surname 
        elif ADDfirst_name.lower() in a1 and ADDlast_name.lower() in a2:
            message = "already in database"
        
        else:
            newauthor=author(first_name=ADDfirst_name,last_name=ADDlast_name,nationality=ADDnationality)
            db.session.add(newauthor)
            db.session.commit()
            message = f'Thank you, {ADDfirst_name} {ADDlast_name} has been added to the database'
    return render_template('addinga.html', form=form, message=message)



@app.route('/update',methods=['GET', 'POST'])
def update():
    form = book_update()
    message=""
    if request.method == 'POST':
        updatetitle=form.book.data
        book2update=books.query.filter_by(id=updatetitle).first()
        book2update.title = form.title.data
        book2update.genre = form.genre.data
        db.session.commit()
        message = "book has been updated"

    return render_template('update.html',form=form,message=message)


@app.route('/delete',methods=['GET','POST'])
def delete():
    message=''
    message2=''
    form = book_deleteby()
    b1 = [books.title for books in books.query.all()]
    
    if request.method == 'POST':
        deletetitle=form.bookdft.data

        
        if deletetitle in b1:
            message2=f'{deletetitle} has been removed from database'
            deletetitle=books.query.filter_by(title=deletetitle).first()
            db.session.delete(deletetitle)
            db.session.commit()

        elif deletetitle== "" : 
            message2=""

        else:
            message2="Title not in database"



        deleteid=form.bookdf.data
        if deleteid is None:
            message=""
        else:
            book_to_delete=books.query.filter_by(id=deleteid).first()
            message = f'{book_to_delete.title} has been removed from database'
            db.session.delete(book_to_delete)
            db.session.commit()
        
    return render_template('delete.html',form=form,message2=message2,message=message)
