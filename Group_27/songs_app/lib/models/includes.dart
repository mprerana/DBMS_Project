class Includes {
  // includes attributes
  String _includesId;
  String _songId;
  String _albumId;

  //constructor functions
  Includes(this._includesId, this._songId, this._albumId);

  //getter functions
  String get includesId {
    return _includesId;
  }

  String get songId {
    return _songId;
  }

  String get albumId {
    return _albumId;
  }

  //setter functions
  set songId(String id) {
    this._songId = id;
  }

  set albumId(String id) {
    this._albumId = id;
  }

  Map<String, dynamic> toMap() {
    Map<String, dynamic> includesMap = Map<String, dynamic>();
    includesMap['includesId'] = this._includesId;
    includesMap['songId'] = this._songId;
    includesMap['albumId'] = this._albumId;

    return includesMap;
  }

  //functions to convert map object to includes object
  Includes.fromMaptoIncludes(Map<String, dynamic> map) {
    this._includesId = map['includesId'];
    this._songId = map['songId'];
    this._albumId = map['albumId'];
  }

  //functions to convert map object to includes object
  // Includes.fromFirestoreMaptoIncludes(Map<String, dynamic> map, String fid) {
  //   this._includesId = fid;
  //   this._songId = map['songId'];
  //   this._albumId = map['albumId'];
  // }
}
