class User {
  
  // User attributes
  String _userId;
  String _firstName;
  String _lastName;
  String _email;
  String _gender;
  DateTime _dateOfBirth;
  DateTime _lastLogin;
  bool _activeStatus;

  // Constructor functions
  User(this._firstName,this._lastName,this._email,this._gender,this._dateOfBirth,this._lastLogin,this._activeStatus);
  User.withId(this._userId,this._firstName,this._lastName,this._email,this._gender,this._dateOfBirth,this._lastLogin,this._activeStatus);

  // get functions for variables
  String get userId {
    return _userId;
  }
  String get firstName {
    return _firstName;
  }
  String get lastName {
    return _lastName;
  }
  String get email {
    return _email;
  }
  String get gender {
    return _gender;
  }
  DateTime get dateOfBirth {
    return _dateOfBirth;
  }
  DateTime get lastLogin {
    return _lastLogin;
  }
  bool get activeStatuc {
    return _activeStatus;
  }

  // setter functions for variables
  set firstName(String fname) {
    this._firstName = fname;
  }
  set lastName(String lname) {
    this._lastName = lname;
  }
  set email(String newEmail) {
    this._email = newEmail;
  }
  set gender(String newGender) {
    this._gender = newGender;
  }
  set dateOfBirth(DateTime newdatetime) {
    this._dateOfBirth = newdatetime;
  }
  set lastLogin(DateTime newlastlogin) {
    this._lastLogin = newlastlogin;
  }
  set activeStatus(bool status) {
    this._activeStatus = status;
  }

  // function to convert user to map object
  Map<String, dynamic> toMap() {
    Map<String, dynamic> userMap = Map<String, dynamic>();

    if(this._userId != null)
      userMap['userId'] = this._userId;
    userMap['firstName'] = this._firstName;
    userMap['lastName'] = this._lastName;
    userMap['email'] = this._email;
    userMap['gender'] = this._gender;
    userMap['dateOfBirth'] = this._dateOfBirth.toIso8601String();
    userMap['lastLogin'] = this._lastLogin.toIso8601String();
    userMap['activeStatus'] = this._activeStatus.toString();

    return userMap;
  }

  // function to convert map object to user object
  User.fromMaptoUser(Map<String,dynamic> map) {
    this._userId = map['userId'];
    this._firstName = map['firstName'];
    this._lastName = map['lastName'];
    this._email = map['email'];
    this._gender = map['gender'];
    this._dateOfBirth = DateTime.parse(map['dateOfBirth']);
    this._lastLogin = DateTime.parse(map['lastLogin']);
    // this._activeStatus = map['activeStatus'];
    if (map['activeStatus'] == 'true') {
      this._activeStatus = true;
    }
    else {
      this._activeStatus = false;
    }
  }

  // function to convert firestore database map object to user object
  User.fromFirestoreMaptoUser(Map<String,dynamic> map, String fid) {
    this._userId = fid;
    this._firstName = map['firstName'];
    this._lastName = map['lastName'];
    this._email = map['email'];
    this._gender = map['gender'];
    this._dateOfBirth = DateTime.parse(map['dateOfBirth']);
    this._lastLogin = DateTime.parse(map['lastLogin']);
    // this._activeStatus = map['activeStatus'];
    if (map['activeStatus'] == 'true') {
      this._activeStatus = true;
    }
    else {
      this._activeStatus = false;
    }
  }
}