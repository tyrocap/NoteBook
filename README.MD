### SUM-NOTES PROJECT
A notebook-like website created with Django, jQuery and PostgreSQL  
(Inspired by brevity of Twitter and convenience of Goodreads)

## Table of Contents
- Introduction
- Technologies
- Tentative Schedule

#### Introduction
As the title suggests, this is a single-page website intended to bring
brevity of Twitter (character limit) and convenience of Goodreads (ease of
 CRUD) into one place and address 'The-Curse-of-Reading-and-Forgetting
 ' phenomenon. To add more clarity, the kind of forgetting we are talking
about here is a special type where the spine of the book is familiar, the
title rings some bells and the table of contents reminds an idea or two.     
This type of forgetting raises a number of practical questions and
this application is my partial answer to one of them: Am I really reading?  
 Background aside, the website has following features and functionalities:
 - Authentication - although all user are welcome to visit the site, in order
  to fully participate they need to sign up to the site. This is handled by
   django-allauth.
 - Home Page - all books are displated here and the page supports
  filter by category or search by category and title functionalities. 
 - Individual Book Page - once user finds the book under interest, one click
takes the user to book's unique page where the user has the ability to post
multiple chain-like notes (each post is limited to 255 characters to
reinforce the idea of synthesizing the most important idea). Under each post
or chain of posts, other users have the ability to comment, which supports
'the clash of worldviews'. 
- Book Search Page - in a case where a user is unable to locate a particular
title, the site gives the user several options: 1) search the book from
Google and Goodreads databases through their respective APIs and add the
book under interest or 2) add the book manually by entering the necessary
information about a given work, including title, author, image, and description
.   

#### Technologies
- Django 3.0.6
- Python 3.7.4
- HTML/CSS
- jQuery
- PostgreSQL

#### Tentative Schedule
###### ISSUES TO WORK:
- [x] Home page front
- [x] Home page back

###### ISSUES TO WORK:
- [x] Authentication
- [x] Category filter and search features  
- [x] Necessary data 

###### ISSUES TO WORK:
- [x] Notes page front 
- [x] Notes page basic backend

###### ISSUES TO WORK:
- [x] Add-book page front
- [x] Add-book page basic backend
- [x] Home page pagination 

##### ISSUES TO WORK:
- [x] Category filter optimization
- [x] Add-book - manual part
- [x] Add-book buttons
- [x] Add-book page final style
- [ ] Notes functionality
- [ ] Comments functionality
- [ ] Notes page style
