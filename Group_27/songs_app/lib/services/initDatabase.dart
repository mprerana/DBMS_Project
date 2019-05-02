// imports of models
import 'package:songs_app/models/users.dart';
import 'package:songs_app/models/genre.dart';
import 'package:songs_app/models/playlist.dart';
import 'package:songs_app/models/image.dart';
import 'package:songs_app/models/albums.dart';
import 'package:songs_app/models/artists.dart';
import 'package:songs_app/models/songs.dart';
import 'package:songs_app/models/songBy.dart';
import 'package:songs_app/models/frequentlyHeard.dart';
import 'package:songs_app/models/includes.dart';

// imports of sqlite crud files
import 'package:songs_app/utils/database_files/usersCRUD.dart';
import 'package:songs_app/utils/database_files/genreCRUD.dart';
import 'package:songs_app/utils/database_files/playlistCRUD.dart';
import 'package:songs_app/utils/database_files/imagesCRUD.dart';
import 'package:songs_app/utils/database_files/albumsCRUD.dart';
import 'package:songs_app/utils/database_files/artist.CRUD.dart';
import 'package:songs_app/utils/database_files/songsCRUD.dart';
import 'package:songs_app/utils/database_files/songbyCRUD.dart';
import 'package:songs_app/utils/database_files/frequentlyheardCRUD.dart';
import 'package:songs_app/utils/database_files/includesCRUD.dart';

// imports of firestore crud files
import 'package:songs_app/utils/cloudStore_files/usersFirestoreCRUD.dart';
import 'package:songs_app/utils/cloudStore_files/genreFirestoreCRUD.dart';
import 'package:songs_app/utils/cloudStore_files/playlistFirestoreCRUD.dart';
import 'package:songs_app/utils/cloudStore_files/imagesFirestoreCRUD.dart';
import 'package:songs_app/utils/cloudStore_files/albumFirestoreCRUD.dart';
import 'package:songs_app/utils/cloudStore_files/artistFirestoreCRUD.dart';
import 'package:songs_app/utils/cloudStore_files/songFirestoreCRUD.dart';
import 'package:songs_app/utils/cloudStore_files/songByFirestoreCRUD.dart';
import 'package:songs_app/utils/cloudStore_files/frequentlyHeardFirestoreCRUD.dart';
import 'package:songs_app/utils/cloudStore_files/includesFirestoreCRUD.dart';

class InitData {
  static InitData _initData;

  InitData._createInstance();

  factory InitData() {
    if (_initData == null) {
      _initData = InitData._createInstance();
      print('Updating the database w.r.t firestore database');
      populateDatatoDatabase();
    }
    return _initData;
  }

  static Future<void> populateDatatoDatabase() async {

    // users table
    print('Adding users collection to user table');
    List<User> userList = await UserFirestoreCRUD().getAllUsers();
    for (User user in userList) {
      await UsersCRUD().insertUser(user);
    }

    // genre table
    print('Adding genres collection to genre table');
    List<Genre> genreList = await GenreFirestoreCRUD().getAllGenre();
    for (Genre genre in genreList) {
      await GenreCRUD().insertGenre(genre);
    }

    // playlist table
    print('Adding playlists collection to genre table');
    List<Playlist> playListList = await PlaylistFirestoreCRUD().getAllPlayLists();
    for (Playlist playlist in playListList) {
      await PlaylistCRUD().insertPlaylist(playlist);
    }

    // images table
    print('Adding images collection to image table');
    List<Images> imagesList = await ImagesFirestoreCRUD().getAllImageList();
    for (Images image in imagesList) {
      await ImagesCRUD().insertImage(image);
    }

    // album table
    print('Adding albums collection to album table');
    List<Album> albumList = await AlbumFirestoreCRUD().getAllAlbums();
    for (Album album in albumList) {
      await AlbumCRUD().insertAlbum(album);
    }

    // artist table
    print('Adding artists collection to artist table');
    List<Artist> artistList = await ArtistFirestoreCRUD().getAllArtists();
    for (Artist artist in artistList) {
      await ArtistsCRUD().insertArtist(artist);
    }

    // songs table
    print('Adding songs collection to songs table');
    List<Song> songsList = await SongFirestoreCRUD().getAllSongs();
    for (Song song in songsList) {
      await SongsCRUD().insertSong(song);
    }

    // songBy table
    print('adding songby collection to songby table');
    List<SongBy> songByList = await SongByForestoreCRUD().getAllSongBy();
    for (SongBy songBy in songByList) {
      await SongByCRUD().insertSongBy(songBy);
    }

    // frequentlyheard table
    print('Adding frequently heard collection to frequentlyheard table');
    List<FrequentlyHeard> frequentlyHeardList = await FrequentlyHeardFirestoreCRUD().getAllFrequentlyHeard();
    for (FrequentlyHeard frequentlyHeard in frequentlyHeardList) {
      await FrequentlyHeardCRUD().insertFrequentlyHeard(frequentlyHeard);
    }

    // includes table
    print('Adding includes collection to includes table');
    List<Includes> includesList = await IncludesFirestoreCRUD().getAllIncludes();
    for (Includes includes in includesList) {
      await IncludesCRUD().insertIncludes(includes);
    }
  }
}