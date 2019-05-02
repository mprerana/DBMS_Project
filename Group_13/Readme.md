# Installation modules:<br>
&nbsp;	`pip install reportlab`<br>
&nbsp;	`pip install rlextra -i https://EMAIL:PASSWORD@www.reportlab.com/pypi`<br>
&nbsp;&nbsp;		(insert email and password created in reportlab website above.)<br>
&nbsp;	`pip install django-ckeditor`<br>
&nbsp;	`pip install pyodbc`<br>
&nbsp;	`pip install pyschedule`<br>
&nbsp;	`pip install pyftdblib`<br>
# Execution
Install all the dependencies as mentioned above.<br />
## For hosting the server <br />
&nbsp;Go to folder server_apps<br />
&nbsp;&nbsp;run `python server.py`<br>
&nbsp;&nbsp;&nbsp;This runs the database server.

## For hosting webserver<br />
&nbsp;&nbsp;Go to folder <br />
&nbsp;&nbsp; run `python manage.py runserver 0.0.0.0:00` <br />
&nbsp;&nbsp; for hosting on a particular ip address and port number.

# For desktop application to enroll for aadhar<br />
&nbsp;Go to enroll <br />
&nbsp;&nbsp; run `python a.py` <br /><br />
**Note:** This requires the server to be hosted, or else the above step doesn't work. 

## Working
As soon as the user is enrolled at a data center the user can access all the features available online which was earlier hosted on web server.<br />
User is required to bring necessary proofs at the time of enrollment.<br />
If the user wants to update his details online, he needs to submit the respective proofs.<br />
Once proofs are verified, the details are updated.<br /> 
`backup` folder is basically for backing up the database.<br />
`data` folder is for saving the data.
