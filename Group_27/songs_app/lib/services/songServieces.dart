import 'package:songs_app/models/songs.dart';
import 'package:songs_app/models/albums.dart';
import 'package:songs_app/models/artists.dart';
import 'package:songs_app/models/songDetails.dart';
import 'package:songs_app/models/songBy.dart';
import 'package:songs_app/models/image.dart';

import 'package:songs_app/utils/database_files/songsCRUD.dart';
import 'package:songs_app/utils/database_files/albumsCRUD.dart';
import 'package:songs_app/utils/database_files/artist.CRUD.dart';
import 'package:songs_app/utils/database_files/songbyCRUD.dart';
import 'package:songs_app/utils/database_files/imagesCRUD.dart';

class SongServies {
  static SongServies _songServies = SongServies._createInstance();

  SongServies._createInstance();

  factory SongServies() {
    return _songServies;
  }

  Future<List<SongDetails>> getAllSongDetails() async {
    List<Song> songList = await SongsCRUD().getSongList();
    List<Album> albumList = await AlbumCRUD().getAlbumList();
    List<Artist> artistList = await ArtistsCRUD().getArtistList();
    List<SongBy> songByList = await SongByCRUD().getSongByList();
    List<Images> imageList = await ImagesCRUD().getImageList();
    List<SongDetails> songDetailList = List<SongDetails>();
    for (SongBy songBy in songByList) {
      Song song;
      Album album;
      Artist artist;
      Images image;
      for (Song songs in songList) {
        if (songBy.songId == songs.songId) {
          song = songs;
          break;
        }
      }
      for (Images image1 in imageList) {
        if(image1.imageId == song.imageId) {
          image = image1;
          break;
        }
      }
      for (Album albums in albumList) {
        if (songBy.albumId == albums.albumId) {
          album = albums;
          break;
        }
      }
      for (Artist artists in artistList) {
        if (songBy.artistId == artists.artistId) {
          artist = artists;
          break;
        }
      }
      songDetailList.add(SongDetails(song, album, artist, image));
    }

    return songDetailList;
  }

  Future<List<SongDetails>> getAlbumSongs(String albumid) async {
    List<Song> songList = await SongsCRUD().getSongList();
    Album album = await AlbumCRUD().getAlbumById(albumid);
    List<Artist> artistList = await ArtistsCRUD().getArtistList();
    List<SongBy> songByList = await SongByCRUD().getSongByList();
    List<Images> imageList = await ImagesCRUD().getImageList();
    List<SongDetails> songDetailList = List<SongDetails>();
    for (SongBy songBy in songByList) {
      Song song;
      Artist artist;
      Images image;
      if (songBy.albumId == albumid) {
        for (Song songs in songList) {
          if (songBy.songId == songs.songId) {
            song = songs;
            break;
          }
        }
        for (Images image1 in imageList) {
        if(image1.imageId == song.imageId) {
          image = image1;
          break;
        }
      }
        for (Artist artists in artistList) {
          if (songBy.artistId == artists.artistId) {
            artist = artists;
            break;
          }
        }
        songDetailList.add(SongDetails(song, album, artist,image));
      }
    }

    return songDetailList;
  }

}