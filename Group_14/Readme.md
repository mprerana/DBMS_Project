# Online-Literature-Management-System
HOOT

## packages required:
Npm 6.4.1,
Django 2.2.1,
Djangorestframework 3.9.3,
Django-rest-knox 3.9.0,
MySQL connector 8.0.12,
Pillow 6.0.0.

the node packages required are present in package.json.

The root folder is where package.json is present.

The project folder is the one where manage.py is present.


## Steps to be followed

1. create a mysql user with username "admin" and password "dbmsproject".

2. create a database "Project".

3. execute "npm install" in root folder to install all the node packages(the pip packages mentioned above have to be installed separately)  required to run the app.

4. execute "npm run dev" in root folder in one terminal and "python manage.py runserver" in project folder in another terminal.
