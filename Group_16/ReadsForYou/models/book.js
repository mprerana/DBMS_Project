const db = require('../util/database');

exports.Category = class Category{
    constructor(CategoryId, CategoryName){
        this.CategoryId = CategoryId;
        this.CategoryName = CategoryName;
    }
    static create_table(){
        db.execute(`create table IF NOT EXISTS Category(
                    CategoryId int UNIQUE, 
                    CategoryName varchar(100), 
                    PRIMARY KEY (CategoryId));`);
    }
}

exports.Users = class Users{
    constructor(UserId, Password){
        this.UserId = UserId;
        this.Password = Password;
    }
    static create_table(){
        db.execute(`create table IF NOT EXISTS Users(
                    UserId varchar(50),
                    Password varchar(50),
                    PRIMARY KEY (UserId));`);
    }
}

exports.Books = class Books{
    constructor(ASIN, FileName, ImageURL, Title, Author, CategoryId, Temporary){
        this.ASIN = ASIN;
        this.FileName = FileName;
        this.ImageURL = ImageURL;
        this.Title = Title;
        this.Author = Author;
        this.CategoryId = CategoryId;
        this.Temporary = Temporary;
       // this.fetchData = (data) => this.fetchBookDetails(data);
    }
    static create_table(){
        return db.execute(`create table IF NOT EXISTS Books(ASIN varchar(13), 
                    FileName varchar(20), ImageURL varchar(100), 
                    Title varchar(255), Author varchar(100), 
                    CategoryId int, Temporary varchar(255), 
                    PRIMARY KEY (ASIN));`);

        // return db.execute(`call create_booksTable();`);
    }

    static fetchBookDetails(ASIN){
        return db.execute(`select ASIN, Filename, ImageURL, Title, Author, B.CategoryId, C.CategoryName
                         from Books as B, Category as C where ASIN = '${ASIN}' and B.CategoryId=C.CategoryId;`);
        //return db.execute(`select * from Books`);
    }

    static fetchAll(){
        return db.execute('select * from Books ORDER BY RAND() LIMIT 8');
    }

    static fetchByParam(param){
        return db.execute(`call getBook('${param}')`);
    }

    adminAddBook(){
        return db.execute(`insert into Books values(?,?,?,?,?,?,?)`,
        [this.ASIN, this.FileName, this.ImageURL, this.Title, this.Author, this.CategoryId, this.Temporary]);
    }

    adminEditBook(){
        return db.execute(`update Books set 
                          ASIN = ?, FileName = ?, ImageURL = ?, Title = ?, Author = ?,
                          CategoryId = ?, Temporary = ?`,
                          [this.ASIN, this.FileName, this.ImageURL, this.Title, this.Author, this.CategoryId, this.Temporary]);
    }

}

exports.Favourites = class Favourites{
    constructor(ASIN, UserId){
        this.ASIN = ASIN;
        this.UserId = UserId;
    }
    static create_table(){
        db.execute(`create table IF NOT EXISTS Favourites(ASIN varchar(13), 
                   UserId varchar(50), 
                   FOREIGN KEY (ASIN) REFERENCES Books(ASIN),   
                   FOREIGN KEY (UserId) REFERENCES Users(UserId)
                   ON DELETE CASCADE);`);
    }
    static fetchAllFromFavorites(id){
        return db.execute(`select F.ASIN, B.Title, B.ImageURL, B.CategoryId from Books as B, Favourites as F where B.ASIN=F.ASIN and F.UserId='${id}';`);
    }

    addBookToFavs(){
        return db.execute(`insert into Favourites values(?,?)`,
        [this.ASIN, this.UserId]);
    }

    deleteFromFavs(){
        return db.execute(`delete from Favourites where UserId='?' and ASIN='?'`,
        [this.UserId, this.ASIN]);
    }
    
}

exports.Ratings = class Ratings{
    constructor(ASIN, UserId, RateValue, Review){
        this.ASIN = ASIN;
        this.UserId = UserId;
        this.RateValue = RateValue;
        this.Review = Review;
    }

    AddtoRatedBooks(){
        db.execute(`insert into Ratings values(?,?,?,?)`,
         [this.ASIN, this.UserId, this.RateValue, '']);
    }
};
    
    


    



    




