QaProject

<h1 align="center">  The Library Of Babel </h1>


```diff
+ version 3.0.0
```
<h4 align="center">Design, Jenkins, Risk assessment </h4>

![image](https://user-images.githubusercontent.com/104978129/174300216-246d5557-703e-44ef-9116-566a19191f45.png)
(Full description of application interface and functionality is described in version 1)
<br>
<br>
<h4>The CI CD Pipeline</h4>
describes the general flow of the project from the development stages to deployment. 
<br>

![image](https://user-images.githubusercontent.com/104978129/174324827-659845f7-47d5-40bb-8093-6067fa911789.png)


<br>
<br>
<h4>Risk assessment</h4>
risk assessment carried out at the start of the project and expanded as project devloped. 

![image](https://user-images.githubusercontent.com/104978129/174333456-e0471718-e949-4770-b26d-2d7fef936b63.png)

<br>
<br>
<br>

<h4>analysis </h4>

In terms of the application it currently operates as the staff side of a book store. From my trello boards below you can see the full scope of the project would have been to also build the customer side. I would have expanded on some design aspects and developed a Login feature that would have only granted access to the staff functionality for valid users. The biggest obstacle in developing the full scope was the time constraints rather than technical. Nonetheless the project in terms of functionality meets the requirements. 

Otherwise the other area which had room for improvement would have been testing. I would have liked to carried out more thorough testing and achieved a higher test coverage. This was more a technical downfall but the time constraints also played a role as some parts of the program I found difficult to test for.

<br>
<br>
<br>

```diff
! version 2.0.0
```

<h4 align="center">Implementation of bootstrap & unit testing</h4>


<br>
<br>
<h5> New Design sample - functionality is the same as version 1</h5>

![image](https://user-images.githubusercontent.com/104978129/174298361-06c47299-3427-4c92-a4f4-20851a2c0815.png)
<br>
<br>
<br>
![image](https://user-images.githubusercontent.com/104978129/174298531-c3021791-e6f3-4e58-9315-9933df8f01fa.png)
<br>
<br>
<br>
<br>

<h4 align="center"> Unit Testing and Coverage </h4>
<br>


![image](https://user-images.githubusercontent.com/104978129/174298678-ef67b9e4-1493-4877-9dc5-93ffa28faece.png)
<br>
<br>
<br>
<br>
<br>
<br>
















```diff
-- version 1.0.0 -- 
```


<b>Introduction </b>

first version - basic CRUD application with two tables sharing a one-to-many relationship. Application is a book store which currently allows users to,

* add new books or authors
* view all books in alphabetically order with their author 
* view each authors page which displays only their books 
* update books 
* delete books by title
* delete books by ID 

current version is only intended as a basic framework to be built upon. Currently has almost no design aspects or navigation bar. Does include some intensive form validators although a few will later be changed to flasks WTForms built-in validators. 


<b>Architecture</b> 

Project was built on google cloud platform. Using SQL database instance to store and retrieve data linked to a VM instance to develop the application with flask using git as the version control. 

<b>Planning</b> 
 
Based on the project requirements I first created user stories, use cases and tasks needed to complete the project. I then used that to model my table relationships and break down the project into different stages using their complexity and MoSCoW prioritisation to create manageable sprints which form the basis of every version. 

  * database relationship model

Two tables sharing a one to many relationship. One author can have many books
![image](https://user-images.githubusercontent.com/104978129/174067343-d110cf91-b57f-45f8-8a4c-2f579aa5991d.png)
<BR>
<BR>

  * user stories

(![image](https://user-images.githubusercontent.com/104978129/174062669-a5aa999a-10de-47b8-b317-4a8f9974a900.png))


<BR>
<BR>
  
  
  * Trello board

 
the colour on the labels represent manageable sprints grouped together by their relevance and complexity. Each task is also judged under the MoSCoW framework. 

![image](https://user-images.githubusercontent.com/104978129/174062846-dc4d4b57-6329-4669-8412-afbbe2755daf.png)

  
<b>Database</b> 

SQL database was created and hosted on GCP and linked to the project. The database was also linked to workbench which i occocially used as another tool just to check the CRUD functionality was working as intended. 

<img src="https://github.com/ramtin-K1996/QaProject-flask-The-Library-of-Babel-/blob/main/photos%20&%20diagrams/Screenshot%20(181).png" width="400"/> <img src="https://github.com/ramtin-K1996/QaProject-flask-The-Library-of-Babel-/blob/main/photos%20&%20diagrams/Screenshot%20(184).png" width="350"/> 

<BR>
<BR>
<BR>
  
<h3 align="center">  Application </h3>
currently the application has minimal design and doesn't have a navigation bar, users have to navigate to desired page via the address bar
  
<BR>
<BR>  
<h5 align="center">  CRUD functionality in use </h5>

 
<b> CREATE </b>

users can add books and authors 

* Add author 
<br>
users need to enter first name, last name and the author’s nationality. All fields need to be filled otherwise it won’t be added. 
  
![image](https://user-images.githubusercontent.com/104978129/174093933-41bec4c5-2132-4a1a-9643-6255b3658d4f.png)
  
Once entered the user will be given a message that the author has been added to the system.
![image](https://user-images.githubusercontent.com/104978129/174094094-7d89677b-ab48-46ff-bb3f-c18288477fe0.png)

To avoid duplicates in the database if the author is already added then the user will get a message.
![image](https://user-images.githubusercontent.com/104978129/174094219-22a79bc8-6ab7-4abc-b11e-82abd3b38bd7.png)
  

* Add books 
<br>
Users need to enter a title, genre and author ID to link it with the right author. once done they will get a message notifying them that the book has been added.
  
![image](https://user-images.githubusercontent.com/104978129/174094575-5b738128-dbe9-4019-872f-09d5acb9ed18.png)
  
  
<b> READ </b>
  
<br>There are two ways to view books.
* view all
<br>
navigating to the view all page will display all the books in the system alongside their author sorted A-Z
  
![image](https://user-images.githubusercontent.com/104978129/174094952-cb0832ca-c8b0-4e1e-b70a-d8558b5263af.png)

 * view authors' books
<br>
can view a specific authors catology by entering their last name in the address bar.

![image](https://user-images.githubusercontent.com/104978129/174095067-65322d94-0da6-44be-b528-541518b7a572.png)


<b> UPDATE </b>
<br>
to update a book the user needs the book ID then they can change the title and genre to whatever they want. 
![image](https://user-images.githubusercontent.com/104978129/174095412-45a1b614-3950-459c-9727-261a888545ef.png)
  
  

<b> DELETE </b>
<br>
books can be deleted two ways both stored on the same page either by the book id or by the title. Once deleted the user will get a message notifying them the book title has been removed. 
  
![image](https://user-images.githubusercontent.com/104978129/174095839-5916f260-874e-4d1c-82ce-774eb2a82679.png)
 
  
If deleting by the book title the application will check if the title is in the database notifying if no book with that title exists in the database. 

![image](https://user-images.githubusercontent.com/104978129/174095919-0a8c113c-6720-41c1-893c-0ab6f5393d81.png)

  
  
  
  



