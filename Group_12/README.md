# BlogIn

## Introduction

Many people love to read and write articles. We
can easily get an article from the internet to read
but if we want to create a blog or publish a new
article, we need to create a website which turns
out to be costly and difficult to manage
especially for people with non-technical
background. So, we created a platform where
people can share ideas at click of a button


## Scope 

This web-app allow users of all age and
background to share their ideas and thoughts
with the world. It also facilitates them to read
articles of her/his interest and appreciate their
blog by liking them. Along with it also let
her/him to follow various interests and their
favourite bloggers. If they want to read some
article after some time, it allows them to
bookmark those articles and access them from
profile. If they are very much inspired from any
article, they can share such blogs with on social
networking websites like Facebook, LinkedIn
and Twitter.

## Functional Requirements

BlogIn’ has two primary actors – Author and
Reader. Fig 2.1 shows Actor-Use case
interaction, illustrating all major use cases.

### Author - Use Case
The author composes a new article using CKEditor, a rich text editor. It allows her/him to set
a cover photo for his blog. It is necessary for
her/him to provide title for his blog. Using CKEditor, media – images and videos – can be
inserted.

### Reader - Use Case

The Reader can read articles of his interest. He
can view bookmarked articles in his profile. 


## How to Run This Project

### Server
In current directory run command ```pip install -r requirements.txt``` and then run the server using ```python manage.py runserver```

### Client
Run ```cd templates```, followed by ```npm i``` to all dependencies related to vue. To run client server run ```npm run serve```
