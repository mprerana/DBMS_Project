# Election-Predictor
Keep up with the news of upcoming general elections and predict the winner based on data and statistical analysis.   

The required packages are present in the requirements.txt file.<br>  
To run the project, please do the following:<br>

1. Create a virtualenv by using the command<br> 
  `python3 -m virtualenv <environment name>`<br>
  
If virtualenv is not present, install it by using the command<br> 
  `sudo pip3 install virtualenv`<br><br> 
2. Activate it by the command,<br>
  `source <path_to_environment>/bin/activate`<br><br>
3. Use this command for installing all the necessary packages for running the project<br>
  `pip install -r requirements.txt`<br><br>
4. We are using MYSQL in our settings backend. The name and the password of the database should be replaced appropriately<br><br>

    DATABASES = { 
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'election_predictordb',
            'USER': '<USER_NAME>',
            'PASSWORD': '<PASSWORD>',
            'HOST': 'localhost',
            'PORT': '',
        }
    }
<br>
5. Change directory into the project directory<br><br>

6. Finally, run the project using:<br>
  `python manage.py runserver`
