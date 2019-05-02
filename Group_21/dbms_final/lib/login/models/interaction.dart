class Interaction {
 int _fid;
 int _aid;
 String _status;

 

  // creating the constructor
  //farmer(this._latitude,this._longitude);
  Interaction(this._fid,this._aid,this._status);

  // get fuctions for variables
  int get fid {
    return _fid; 
  }

  int get aid {
    return _aid;
  }

  String get status {
    return _status;
  }
  

  // setter functions for the variables
  set fid(int value) {
    this._fid = value;
  }

  set aid(int value) {
    this._aid = value;
  }

  set status(String value) {
    this._status = value;
  }


  // functions to convert the user to map
  Map<String, dynamic> toMap() {
    Map<String, dynamic> map = Map<String, dynamic>();

    if(fid != null) {
      map['fid'] = _fid;
    }
  
    map['aid'] = _aid;
    map['status']=_status;
  
    
    return map;
  }

  // function to convert map to user object
  Interaction.fromMapObject(Map<String,dynamic> map) {
    this._fid = map['fid'];
    this._aid= map['aid'];
    this._status = map['status'];
    
  
  }
}