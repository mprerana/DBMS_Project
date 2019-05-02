class Farmer {
  int _id;
  String _oldemail;
  String _newemail;
  
 

  // creating the constructor
  //farmer(this._oldemail,this._newemail);
  Farmer(this._id,this._oldemail,this._newemail);

  // get fuctions for variables
  int get id {
    return _id; 
  }

  String get oldemail {
    return _oldemail;
  }

  String get newemail {
    return _newemail;
  }
  

  // setter functions for the variables
  set id(int value) {
    this._id = value;
  }

  set oldemail(String value) {
    this._oldemail = value;
  }

  set newemail(String value) {
    this._newemail = value;
  }


  // functions to convert the user to map
  Map<String, dynamic> toMap() {
    Map<String, dynamic> map = Map<String, dynamic>();

    if(id != null) {
      map['id'] = _id;
    }
  
    map['oldemail'] = _oldemail;
    map['newemail']=_newemail;
  
    
    return map;
  }

  // function to convert map to user object
  Farmer.fromMapObject(Map<String,dynamic> map) {
    this._id = map['id'];
    this._oldemail= map['oldemail'];
    this._newemail = map['newemail'];
    
  
  }
}