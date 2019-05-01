const { Client } = require('pg');
const users = require('./users');
const userProfile = require('./userProfile');
const restaurants = require('./restaurants');
const verification = require('./verification');
const tracking = require('./tracking');
const deliveryAgent = require('./deliveryAgent');
const client = new Client({
    user: 'dbms',
    host: 'localhost',
    database: 'db',
    password: 'password',
    port: 5432,
})

client.setup = function() {
    const query = {
        text: `create table if not exists users(
            id serial,
            isActive boolean default false,
            username varchar(255) primary key,
            email varchar(255) NOT NULL UNIQUE,
            password varchar(10000) not null,
            role varchar(2) default '1',
            created timestamp,
            modified timestamp
            );
            drop trigger if exists add_created_timestamp on users;
            drop trigger if exists add_modified_timestamp on users;

            CREATE OR REPLACE FUNCTION created_timestamp() 
            RETURNS TRIGGER AS $$
            BEGIN
                NEW.created = now();
                NEW.modified = now();
                RETURN NEW; 
            END;
            $$ language 'plpgsql';
            CREATE OR REPLACE FUNCTION modified_timestamp() 
            RETURNS TRIGGER AS $$
            BEGIN
                NEW.created = OLD.created;
                NEW.modified = now();
                RETURN NEW; 
            END;
            $$ language 'plpgsql';
            
            create trigger add_created_timestamp
            before insert on users
            for each row
            execute procedure created_timestamp();
            
            create trigger add_modified_timestamp
            before update on users
            for each row
            execute procedure modified_timestamp();
            

            CREATE TABLE if not exists userProfile (
                username varchar(255),
                firstname varchar(255) NOT NULL,
                lastname varchar(255) NOT NULL,
                phone varchar(255) NOT NULL,
                address varchar(1000) NOT NULL,
                pictureurl varchar(500),
                PRIMARY KEY (username),
                FOREIGN KEY (username) REFERENCES users (username)
               );
            CREATE TABLE if not exists verification (
                username varchar(255),
                token varchar(1000),
                type varchar(1) NOT NULL,
                PRIMARY KEY (token),
                FOREIGN KEY (username) REFERENCES users (username)
            );

            CREATE TABLE if not exists restaurantApplications (
                id serial,
                name varchar(500) NOT NULL,
                email varchar(255),
                lon varchar(100) NOT NULL,
                lat varchar(100) NOT NULL,
                zipcode varchar(6) NOT NULL,
                phone varchar(10) NOT NULL,
                address varchar(1000) NOT NULL,
                logourl varchar(500),
                openingHrs time NOT NULL,
                closingHrs time NOT NULL,
                status varchar(1) default 'P',
                PRIMARY KEY (id)
            );
            CREATE TABLE if not exists restaurantProfile (
                username varchar(255),
                name varchar(500) NOT NULL,
                email varchar(255),
                lon varchar(100) NOT NULL,
                lat varchar(100) NOT NULL,
                zipcode varchar(6) NOT NULL,
                phone varchar(10) NOT NULL,
                address varchar(1000) NOT NULL,
                logourl varchar(500),
                openingHrs time(4),
                closingHrs time(4),
                ordersCompleted integer default 0,
                PRIMARY KEY (username)
            );
            CREATE TABLE if not exists deliveryAgent (
                username varchar(225) NOT NULL,
                firstname varchar(225)NOT NULL,
                lastname varchar(225),
                phone varchar(255) NOT NULL,
                status varchar(1) NOT NULL,
                lon varchar(100) NOT NULL,
                lat varchar(100) NOT NULL,
                ordersCompleted integer default 0,
                PRIMARY KEY (username),
                FOREIGN KEY (username) REFERENCES users (username)
            );
            
            CREATE TABLE if not exists category (
                id serial,
                categoryName varchar(255),
                rest_username varchar(255),
                PRIMARY KEY (id),
                FOREIGN KEY (rest_username) REFERENCES restaurantProfile (username)
            );
            
            CREATE TABLE if not exists item (
                id serial,
                itemName varchar(255) NOT NULL,
                price real NOT NULL,
                description varchar(1000),
                photoUrl varchar(500),
                categoryId INTEGER,
                restId varchar(255),
                PRIMARY KEY (id),
                FOREIGN KEY (restId) REFERENCES restaurantProfile (username),
                FOREIGN KEY (categoryId) REFERENCES category (id)
            );
            
            CREATE TABLE if not exists orders (
                id serial,
                username varchar(255) NOT NULL,
                rest_name varchar(255) NOT NULL,
                lat varchar(100) NOT NULL,
                lon varchar(100) NOT NULL,
                del_username varchar(255) NOT NULL,
                PRIMARY KEY (id),
                FOREIGN KEY (username) REFERENCES users(username),
                FOREIGN KEY (rest_name) REFERENCES restaurantProfile(username),
                FOREIGN KEY (del_username) REFERENCES deliveryAgent(username)
                
            );
            
            
            CREATE TABLE if not exists orderItem (
                orderId INTEGER,
                itemId INTEGER,
                quantity integer NOT NULL,
                PRIMARY KEY (orderId,itemId),
                FOREIGN KEY (orderId) REFERENCES orders(id),
                FOREIGN KEY (itemId) REFERENCES item(id)
                
            );
            
            
            CREATE TABLE if not exists tracking (
                orderId INTEGER,
                lat varchar(100) NOT NULL,
                lon varchar(100) NOT NULL,
                PRIMARY KEY (orderId),
                FOREIGN KEY (orderId) REFERENCES orders(id)
                
            );
            
            CREATE OR REPLACE FUNCTION clear_restAppl() 
            RETURNS TRIGGER AS $$
            BEGIN
                IF NEW.status = 'A' THEN
                INSERT INTO restaurantProfile
                VALUES (CONCAT('restaurant',NEW.id), NEW.name, NEW.email, NEW.lon, NEW.lat, NEW.zipcode, NEW.phone, NEW.address, NEW.logourl, NEW.openingHrs, NEW.closingHrs);
                INSERT INTO users(username,email,password,role)
                VALUES (CONCAT('restaurant',NEW.id),NEW.email,MD5(random()::text),'3');
                END IF;
                DELETE FROM restaurantApplications WHERE email=NEW.email;
                RETURN NEW; 
            END;
            $$ language 'plpgsql';
            
            drop trigger if exists update_restAppl on restaurantApplications;

            create trigger update_restAppl
            after update on restaurantApplications
            for each row
            execute procedure clear_restAppl();
            `,
    }
    this.query(query)
    .then(res => {
        console.log(res.command)
    })
    .catch(e => console.log(e.stack))
};

client.connect();
client.insertUser = users.insertUser;
client.getVerifiedUser = users.getVerifiedUser;
client.getUser = users.getUser;
client.getUserByEmail = users.getUserByEmail;
client.updateUser = users.updateUser;
client.deleteUser = users.deleteUser;
client.comparePassword = users.comparePassword;
client.changePassword = users.changePassword;

client.insertUserProfile = userProfile.insertUserProfile;
client.getUserProfile = userProfile.getUserProfile;
client.updateUserProfile = userProfile.updateUserProfile;
client.deleteUserProfile = userProfile.deleteUserProfile;
client.getUsers = users.getUsers;
client.setActive = users.setActive;

client.insertNewToken = verification.insertNewToken;
client.verifyToken = verification.verifyToken;
client.deleteToken = verification.deleteToken;

client.restaurantApply = restaurants.restaurantApply;
client.getRestaurantApplications = restaurants.getRestaurantApplications;
client.getRestaurantApplicationByEmail = restaurants.getRestaurantApplicationByEmail;
client.getRestaurantApplicationByID = restaurants.getRestaurantApplicationByID;
client.updateRestaurantApplication = restaurants.updateRestaurantApplication;
client.getRestaurantProfiles = restaurants.getRestaurantProfiles;
client.getRestaurantItems = restaurants.getRestaurantItems;
client.getRestaurantCategory = restaurants.getRestaurantCategory;
client.addRestaurantCategory = restaurants.addRestaurantCategory;
client.getRestaurantCategories = restaurants.getRestaurantCategories;
client.getRestaurantItem = restaurants.getRestaurantItem;
client.addRestaurantItem = restaurants.addRestaurantItem;
client.createOrder = restaurants.createOrder;
client.addOrderItem = restaurants.addOrderItem;
client.getLastOrder = restaurants.getLastOrder;

client.trackOrder = tracking.trackOrder;
client.updateLocation = deliveryAgent.updateLocation;
module.exports = client;
