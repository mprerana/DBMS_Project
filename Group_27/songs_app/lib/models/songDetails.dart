import 'package:songs_app/models/songs.dart';
import 'package:songs_app/models/albums.dart';
import 'package:songs_app/models/artists.dart';
import 'package:songs_app/models/image.dart';

class SongDetails {
  // song details attributes
  Song _song;
  Album _album;
  Artist _artist;
  Images _image;

  SongDetails(this._song,this._album,this._artist, this._image);

  Song get song => _song;
  Album get album => _album;
  Artist get artist => _artist;
  Images get image => _image;

  set song(Song song) {
    this._song = song;
  }
  set album(Album album) {
    this._album = album;
  }
  set artist(Artist artist) {
    this._artist = artist;
  }
  set image(Images image) {
    this._image = image;
  }
}