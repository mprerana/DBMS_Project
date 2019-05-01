class Clockset{
  int _id;
  String _date;
  String _time;
  String _reason;
  int _idf;
  
  Clockset(this._id,this._idf,this._date,this._time,[this._reason]);
  int get id=>_id;
  int get idf=>_idf;
  String get date=>_date;
  String get time=>_time;
  String get reason=>_reason;
  set id(int value) {
    this._id = value;
  }
  set idf(int value) {
    this._idf = value;
  }
  set date(String newdate){
    this._date=newdate;
  }
  set time(String newtime){
    this._time=newtime;
  }
  set reason(String newreason){
    this._reason=newreason;
  }
  Map<String,dynamic> toMap(){
    var map=Map<String,dynamic>();
    map['id']=_id;
    if(id!=null && idf!=null){
    map['idf']=_idf;
    }
    map['date']=_date;
    map['time']=_time;
    map['reason']=_reason;


    return map;
  }
Clockset.fromMapObject(Map<String,dynamic> map){
  this._id=map['id'];
  this._idf=map['idf'];
  this._date=map['date'];
  this._time=map['time'];
  this._reason=map['reason'];
  // print('asdzfghjkljgfdfghjklkljhg');
}



}