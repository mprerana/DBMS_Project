class Pesticides{

String _crop;
String _pesticides;





 
  Pesticides(this._crop,this._pesticides);

  // get fuctions for variables
  String get crop {
    return _crop;
  }

  String get pesticides{
    return _pesticides;
  }

  

  // setter functions for the variables
  set id(String value) {
    this._crop = value;
  }
set pesticides(String value) {
    this._pesticides = value;
  }

 Map<String, dynamic> toMap() {
    Map<String, dynamic> map = Map<String, dynamic>();

    
  
    map['pesticides'] = _pesticides;
    map['crop']=_crop;
  
    
    return map;
  }

  // function to convert map to user object
  Pesticides.fromMapObject(Map<String,dynamic> map) {
    this._crop = map['crop'];
    this._pesticides= map['pesticides'];
    
     
  
  }
}

