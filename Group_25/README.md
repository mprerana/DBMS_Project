# CMS
DBMS PROJECT GROUP NUMBER 25

Install virtual environment:
  sudo pip3 install virtualenv

Create a virtualenv by using the command:
  python3 -m virtualenv

Activate venv by using the command:
  source <path_to_environment>/bin/activate

To run the project do the following:

    Configure your MySQL database NAME, USER, PASSWORD inside eventManagement > settings.py

         DATABASES = {   
             'default': {
                 'ENGINE': 'django.db.backends.mysql',
                 'NAME': '---',
                 'USER': '---',
                 'PASSWORD': '----',
                 'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
                 'PORT': '3306',
                 }
             }

    Activate the virtualenv(if not already activated) and open the project directory in the terminal and write the following commands

     python manage.py makemigrations
     python manage.py migrate

    Run the project by the command

     python manage.py runserver

