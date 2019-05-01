class FrequentlyHeard {

  // FrequentlyHeard attributes 
  String _userId;
  int _songId;
  int _albumId;
  int _count;
  int _weekNo;

  // constructor functions
  FrequentlyHeard(this._userId,this._songId,this._albumId,this._count,this._weekNo);

  // get functions for variables
  String get userId => _userId;
  int get songId => _songId;
  int get albumId => _albumId;
  int get count => _count;
  int get weekNo => _weekNo;

  // setter functions for variables
  set userId(String id) {
    this._userId = id;
  }
  set songId(int newsongid) {
    this._songId = newsongid;
  }
  set albumId(int id) {
    this._albumId = id;
  }
  set count(int newcount) {
    this._count = newcount;
  }
  set weekNo(int newweekNo) {
    this._weekNo = newweekNo;
  }

  // function to convert frequentlyHeard object to map object
  Map<String, dynamic> toMap() {
    Map<String, dynamic> map = Map<String, dynamic>();

    map['userId'] = this._userId;
    map['songId'] = this._songId;
    map['albumId'] = this._albumId;
    map['count'] = this._count;
    map['weekNo'] = this._weekNo;

    return map;
  }

  // function to convert map object to frequntlyHeard object
  FrequentlyHeard.fromMaptoFrequentlyHeard(Map<String, dynamic> map) {
    this._userId = map['userId'];
    this._songId = map['songId'];
    this._albumId = map['albumId'];
    this._count = map['count'];
    this._weekNo = map['weekNo'];
  }

  // function to convert map object to frequntlyHeard object
  // FrequentlyHeard.fromFirestoreMaptoFrequentlyHeard(Map<String, dynamic> map, String fid) {
  //   this._userId = fid;
  //   this._songId = map['songId'];
  //   this._albumId = map['albumId'];
  //   this._count = map['count'];
  //   this._weekNo = map['weekNo'];
  // }
}