class Agro {
  int _id;
  String _qualifications;
  
  
 

  // creating the constructor
  
  Agro(this._id,this._qualifications);

  // get fuctions for variables
  int get id {
    return _id;
  }

  String get qualifications{
    return _qualifications;
  }

  

  // setter functions for the variables
  set id(int value) {
    this._id = value;
  }

  set qualifications(String value) {
    this._qualifications = value;
  }

  

  // functions to convert the user to map
  Map<String, dynamic> toMap() {
    Map<String, dynamic> map = Map<String, dynamic>();

    if(id != null) {
      map['id'] = _id;
    }
  
    map['qualifications'] = _qualifications;
  
  
    
    return map;
  }

  // function to convert map to user object
  Agro.fromMapObject(Map<String,dynamic> map) {
    this._id = map['id'];
    this._qualifications= map['qualifications'];
    
     
  
  }
}