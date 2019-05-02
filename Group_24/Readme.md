
Car services Management System


To install the packages,do the following: 

To run the project do the following:

Configure your MySQL database NAME, USER, PASSWORD inside dbmsproject > settings.py

     DATABASES = {   
         'default': {
             'ENGINE': 'django.db.backends.mysql',
             'NAME': '',
             'USER': '',
             'PASSWORD': '',
             'HOST': 'localhost',  
             'PORT': '3306',
             }
         }

To add triggers and procedures:
run the SQL commmands in triggers_procedures.txt file in the mysql command promt 

Installed apps:

for crispy forms
run command :

pip install --upgrade django-crispy-forms

for geopy
run command :

pip install geopy


python manage.py makemigrations

python manage.py migrate

Run code command:
python manage.py runserver
