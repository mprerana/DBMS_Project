
class triggerdeleteclockset{
  int _id;
  int _alrmid;
  
  triggerdeleteclockset(this._id,this._alrmid);
  int get id=>_id;
  int get alrmid=>_alrmid;
   set id(int value) {
    this._id = value;
  }
  set alrmid(int value) {
    this._alrmid = value;
  }
  
  Map<String,dynamic> toMap(){
    var map=Map<String,dynamic>();
    map['id']=_id;
    if(id!=null && alrmid!=null){
    map['alrmid']=_alrmid;
    }
   

    return map;
  }
triggerdeleteclockset.fromMapObject(Map<String,dynamic> map){
  this._id=map['id'];
  this._alrmid=map['alrmid'];
  // print('asdzfghjkljgfdfghjklkljhg');
}



}