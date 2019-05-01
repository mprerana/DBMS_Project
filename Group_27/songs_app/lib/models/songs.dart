class Song {
  // Song attributes
  String _songId;
  String _title;
  double _length;
  String _location;
  String _albumId;
  String _genreId;
  String _imageId;

  //Constructor functions
  Song(this._title, this._length,this._location, this._albumId,
      this._genreId, this._imageId);
  Song.withID(this._songId, this._title, this._length,this._location, this._albumId,
      this._genreId, this._imageId);

  // get functions for variables
  String get songId {
    return _songId;
  }

  String get title {
    return _title;
  }

  double get length {
    return _length;
  }

  String get location {
    return _location;
  }

  String get albumId {
    return _albumId;
  }

  String get genreId {
    return _genreId;
  }

  String get imageId {
    return _imageId;
  }

//setter functions for variables
  set title(String title) {
    this._title = title;
  }

  set length(double length) {
    this._length = length;
  }

  set location(String location) {
    this._location = location;
  }

  set albumId(String albumId) {
    this._albumId = albumId;
  }

  set genreId(String genreId) {
    this._genreId = genreId;
  }

  set imageId(String imageId) {
    this._imageId = imageId;
  }

// function to convert song to map object

  Map<String, dynamic> toMap() {
    Map<String, dynamic> songMap = Map<String, dynamic>();

    if (this._songId != null) 
      songMap["songId"] = this._songId;
    songMap["title"] = this._title;
    songMap["length"] = this._length;
    songMap['location'] = this._location;
    songMap["albumId"] = this._albumId;
    songMap["genreId"] = this._genreId;
    songMap['imageId'] = this._imageId;

    return songMap;
  }

  //function to convert map object to song object
  Song.fromMaptoSong(Map<String, dynamic> map) {
    this._songId = map["songId"];
    this._title = map["title"];
    this._length = map["length"].toDouble();
    this._location = map["location"];
    this._albumId = map["albumId"];
    this._genreId = map["genreId"];
    this._imageId = map['imageId'];
  }

  //function to convert map object to song object
  Song.fromFirestoreMaptoSong(Map<String, dynamic> map, String fid) {
    this._songId = fid;
    this._title = map["title"];
    this._length = map["length"];
    this._location = map["location"];
    this._albumId = map["albumId"];
    this._genreId = map["genreId"];
    this._imageId = map['imageId'];
  }

  // Function to convert a song object to list
  List fromSongtoList(){
    return [this._songId, this._title, this._length,this._location, this._albumId, this._genreId, this._imageId];
  }
}
