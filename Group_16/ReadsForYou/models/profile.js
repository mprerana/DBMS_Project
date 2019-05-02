
const db  = require('../util/database');



module.exports = class Profile {
  constructor(UserId, FirstName, LastName, Age, Sex, Email, Image) {
    this.UserId = UserId;
    this.FirstName = FirstName;
    this.LastName = LastName;
    this.Age = Age;
    this.Sex = Sex;
    this.Email = Email;
    this.Image = Image;
  }

  static create_table(){
    db.execute(`create table IF NOT EXISTS Profile(
              UserId varchar(50),
              FirstName varchar(50),
              LastName varchar(50),
              Age int,
              Sex varchar(1),
              Email varchar(50),
              Image blob,
              FOREIGN KEY (UserId) 
              REFERENCES Users(UserId) ON DELETE CASCADE
  );
  `);
}

  save() {
    db.execute('INSERT INTO Profile (UserId, FirstName, LastName, Age, Sex, Email, Image) VALUES (?, ?, ?, ?, ?, ?, ?)',
  [  this.UserId, this.FirstName, this.LastName, this.Age, this.Sex, this.Email, this.Image]
)}

  update(profileUserId, updatedFirstName, updatedLastName, updatedAge, updatedSex, updatedEmail, updatedImage) {
      return db.execute('UPDATE Profile SET FirstName = ?, LastName = ?, Age = ?, Sex = ?, Email = ?, Image = ?  WHERE Profile.UserId = ?',
      [updatedFirstName, updatedLastName, updatedAge, updatedSex, updatedEmail, updatedImage, profileUserId]);
  };



  static fetchAll() {
    return db.execute('SELECT * FROM Profile');
  }

  static findByUserId(UserId) {
    return db.execute('SELECT * FROM Profile WHERE Profile.UserId = ?', [UserId]);
  }
};
