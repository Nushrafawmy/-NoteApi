# -NoteApi
**NoteApi Sample Application**

Setup

1.clone the repository
$ git clone https://github.com/Nushrafawmy/-NoteApi.git

$ cd noteApi

2.Create a virtual environment to install dependencies in and activate it:
$ pipenv shell

3.Install requirements
$ pip install -r requirements.txt

4.Postgres used in the project
change note_project/settings.py file according to db credintials

5.To Execute the project
$ python manage.py runserver

6.To Execute Test cases
$ python manage.py test

URLs,
1. GET http://localhost:8000/note
2. GET http://localhost:8000/note/1
3. POST http://localhost:8000/note
4. PUT http://localhost:8000/note/4
5. PATCH http://localhost:8000/note/4
6. DELETE http://localhost:8000/note/4
