class Genre {
  // attributes for genre
  String _genreId;
  String _name;

  //constructors
  Genre(this._name);
  Genre.withId(this._genreId,this._name);

  // get functions for variables
  String get genreId => this._genreId;
  String get name => this._name;

  // set functions for varaibles
  set name(String genreName) {
    this._name = genreName;
  }

  // function to convert class object to map object
  Map<String,dynamic> toMap() {
    Map<String,dynamic> map = Map<String,dynamic>();

    if (this._genreId != null) {
      map['genreId'] = this._genreId;
    }
    map['name'] = this._name;

    return map;
  }

  // function to convert map object to class object
  Genre.fromMaptoGenre(Map<String,dynamic> map) {
    this._genreId = map['genreId'];
    this._name = map['name'];
  }

  // function to convert firestore database map object to class object
  Genre.fromFirestoreMaptoGenre(Map<String,dynamic> map, String fid) {
    this._genreId = fid;
    this._name = map['name'];
  }
}