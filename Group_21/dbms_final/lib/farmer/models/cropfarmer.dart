class Cropfarmer {
 int _fid;
 String _price;
 String _crop;

 

  // creating the constructor
  //farmer(this._latitude,this._longitude);
  Cropfarmer(this._fid,this._price,this._crop);

  // get fuctions for variables
  int get fid {
    return _fid; 
  }

  String get price {
    return _price;
  }

  String get crop {
    return _crop;
  }
  

  // setter functions for the variables
  set fid(int value) {
    this._fid = value;
  }

  set price(String value) {
    this._price = value;
  }

  set crop(String value) {
    this._crop = value;
  }


  // functions to convert the user to map
  Map<String, dynamic> toMap() {
    Map<String, dynamic> map = Map<String, dynamic>();

    if(fid != null) {
      map['fid'] = _fid;
    }
  
    map['price'] = _price;
    map['crop']=_crop;
  
    
    return map;
  }

  // function to convert map to user object
  Cropfarmer.fromMapObject(Map<String,dynamic> map) {
    this._fid = map['fid'];
    this._crop= map['crop'];
    this._price = map['price'];
    
  
  }
}