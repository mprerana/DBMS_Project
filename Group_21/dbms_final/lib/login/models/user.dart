class User {
  int _id;
  String _email;
  String _password;
  
  String _firstname;
  String _lastname;
  String _streetname;
  String _pincode;
  String _state;
  String _city;
  String _usertype;
  String _mobileno;
 // String _dob1; 
 

  // creating the constructor
  User(this._email,this._password,this._firstname,this._lastname,this._streetname,this._city,this._state,this._pincode,this._usertype,this._mobileno);
  User.withId(this._id,this._email,this._password,this._firstname,this._lastname,this._streetname,this._city,this._state,this._pincode,this._usertype,this._mobileno);

  // get fuctions for variables
  int get id {
    return _id;
  }

  String get email {
    return _email;
  }

  String get password {
    return _password;
  }
  String get firstname {
    return _firstname;
  }
String get lastname {
    return _lastname;
  }
String get streetname {
    return _streetname;
  }
String get state {
    return _state;
  }
String get pincode {
    return _pincode;
  }
String get city{
    return _city;
  }
String get usertype {
    return _usertype;
  }
  String get mobileno {
    return _mobileno;
  }


  // setter functions for the variables
  set id(int value) {
    this._id = value;
  }

  set email(String value) {
    this._email = value;
  }

  set password(String value) {
    this._password = value;
  }
set firstname(String value) {
    this._firstname = value;
  }
  set lastname(String value) {
    this._lastname = value;
  }
set streetname(String value) {
    this._streetname = value;
  }
set state(String value) {
    this._state = value;
  }
set city(String value) {
    this._city = value;
  }
set usertype(String value) {
    this._usertype = value;
  }
set pincode(String value) {
    this._pincode = value;
  }
set mobileno(String value) {
    this._mobileno = value;
  }


  // functions to convert the user to map
  Map<String, dynamic> toMap() {
    Map<String, dynamic> map = Map<String, dynamic>();

    if(id != null) {
      map['id'] = _id;
    }
    map['email'] = _email;
    map['password'] = _password;
    map['usertype']=_usertype;
    map['Firstname']=_firstname;
    map['Lastname']=_lastname;
    map['Streetname']=_streetname;
    
    map['City']=_city;
    map['State']=_state;
    
    map['Pincode']=_pincode;
    map['mobileno']=_mobileno;
    
    return map;
  }

  // function to convert map to user object
  User.fromMapObject(Map<String,dynamic> map) {
    this._id = map['id'];
    this._email = map['email'];
    this._password = map['password'];
     this.usertype=map['usertype'];
    this.firstname=map['Firstname'];
    this.lastname=map['Lastname'];
    this.streetname=map['Streetname'];
    this._mobileno=map['mobileno'];
    
    this.city=map['City'];
    this.state=map['State'];
    this.pincode=map['Pincode'];
   
  
  }
}