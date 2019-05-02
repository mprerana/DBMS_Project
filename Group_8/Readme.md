# Group-08

 ## *Movie Review System*


Our Website is an online database of information related to films, television programs, vidoes, TV shows and internet streams including cast, production crew and personnel biographies, plot summaries, fan reviews and movie ratings.
The movie pages and other review information is accessible to all the Internet Users, but a registration process is necessary to contribute information to the site and make movie ticket bookings.



### Softwares Used:

1. NoSQL database (mongodb)
2. Node js framework
3. Firebase  (authentication)
4. Keras and Tensorflow (Sentiment Analysis)



### Modules to Install:

npm modules:

1. body-parser: "^1.18.3",
2. express: "^4.16.4",
3. express-handlebars: "^3.0.2",
4. firebase: "^5.9.2",
5. handlebars-helpers: "^0.10.0",
6. hbs: "^4.0.3",
7. in_array: "^1.1.0",
8. mongo-oplog: "^2.1.4",
9. mongodb-stitch-browser-sdk: "^4.3.2",
10. mongoose: "^5.4.20",
11. multer: "^1.4.1",
12. nodemailer": "^6.1.1"


### Running the code:

1. To install all the required modules, run the command npm install.

2. For the data in the mongodb database to be accessed by the website, the mongodb server also must be run.
   cd/mongo/bin -> ./mongod --dbpath ~/mongo-data

3. All the routes for the website are configured in index_1.js file. This file is to be run to start the website server.

4. The main page of the website is displayed where the user needs to login or register using his information.

5. Upon navigating into the homepage, the user can perform various activities like commenting and rating a movie, browsing his/her favourite movies and cast, making ticket bookings and many more.