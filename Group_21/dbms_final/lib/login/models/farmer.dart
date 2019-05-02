class Farmer {
  int _id;
  String _latitude;
  String _longitude;
  
 

  // creating the constructor
  //farmer(this._latitude,this._longitude);
  Farmer(this._id,this._latitude,this._longitude);

  // get fuctions for variables
  int get id {
    return _id; 
  }

  String get latitude {
    return _latitude;
  }

  String get longitude {
    return _longitude;
  }
  

  // setter functions for the variables
  set id(int value) {
    this._id = value;
  }

  set latitude(String value) {
    this._latitude = value;
  }

  set longitude(String value) {
    this._longitude = value;
  }


  // functions to convert the user to map
  Map<String, dynamic> toMap() {
    Map<String, dynamic> map = Map<String, dynamic>();

    if(id != null) {
      map['id'] = _id;
    }
  
    map['latitude'] = _latitude;
    map['longitude']=_longitude;
  
    
    return map;
  }

  // function to convert map to user object
  Farmer.fromMapObject(Map<String,dynamic> map) {
    this._id = map['id'];
    this._latitude= map['latitude'];
    this._longitude = map['longitude'];
    
  
  }
}