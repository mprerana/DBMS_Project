class SongBy {
  // attributes 
  String _songId;
  String _albumId;
  String _artistId;

  //Constructor functions
  SongBy(this._songId, this._albumId, this._artistId);

  // get functions for variables
  String get songId => this._songId;
  String get albumId => this._albumId;
  String get artistId => this._artistId;

  // setter functions for variables
  set songId(String id) {
    this._songId = id;
  }
  set albumId(String id) {
    this._albumId = id;
  }
  set artistId(String id) {
    this._artistId = id;
  }

  // function to convert class object to map object
  Map<String,dynamic> toMap() {
    Map<String,dynamic> map = Map<String,dynamic>();

    map['songId'] = this._songId;
    map['albumId'] = this._albumId;
    map['artistId'] = this._artistId;

    return map;
  }

  // function to convert map object to class object
  SongBy.fromMaptoSongBy(Map<String,dynamic> map) {
    this._songId = map['songId'];
    this._albumId = map['albumId'];
    this._artistId = map['artistId'];
  }

  // // function to convert firestore database map object to class object
  // SongBy.fromFirestoreMaptoSongBy(Map<String,dynamic> map, String fid) {
  //   this._songId = fid;
  //   this._albumId = map['albumId'];
  //   this._artistId = map['artistId'];
  // }
}