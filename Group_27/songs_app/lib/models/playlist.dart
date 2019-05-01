class Playlist {
  //playlist attributes
  String _playlistId;
  String _userId;
  String _name;

  //constructor functions
  Playlist(this._userId, this._name);
  Playlist.withID(this._playlistId, this._userId, this._name);

  // get functions
  String get playlistId {
    return _playlistId;
  }

  String get name {
    return this._name;
  }

  String get userId {
    return this._userId;
  }

  //set functions
  set name(String name) {
    this._name = name;
  }

  set userId(String id) {
    this._userId = id;
  }

  // function to convert object to map
  Map<String, dynamic> toMap() {
    Map<String, dynamic> playlistMap = Map<String, dynamic>();
    if (this._playlistId != null) {
      playlistMap['playlistId'] = this._playlistId;
    }
    playlistMap['userId'] = this._userId;
    playlistMap['name'] = this._name;

    return playlistMap;
  }

  //function to convert map to playlist
  Playlist.fromMaptoPlaylist(Map<String, dynamic> map) {
    this._playlistId = map['playlistId'];
    this._userId = map['userId'];
    this._name = map['name'];
  }

  //function to convert firestore database map to playlist
  Playlist.fromFirestoreMaptoPlaylist(Map<String, dynamic> map,String fid) {
    this._playlistId = fid;
    this._userId = map['userId'];
    this._name = map['name'];
  }
}
