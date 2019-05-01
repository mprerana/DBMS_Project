# SocialCircleEvents
All required packages are in the requirements.txt file

To install the packages,do the following:
(Steps valid for ubuntu systems)

Install virtual environment(if not present already):
    
    sudo pip3 install virtualenv
     
Create a virtualenv by using the command:
    
    python3 -m virtualenv
    
Activate venv by using the command:

    source <path_to_environment>/bin/activate
    
Install requirements for the project by running the command:
    
    pip install -r requirements.txt

For Windows, equivalent commands to set up virtual environment and install requirements can be used.

To run the project do the following:

1. Configure your MySQL database NAME, USER, PASSWORD inside eventManagement > settings.py

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

2. Activate the virtualenv(if not already activated) and open the project directory in the terminal and write the following commands

        python manage.py makemigrations
        python manage.py migrate

3. Run the project by the command

        python manage.py runserver
