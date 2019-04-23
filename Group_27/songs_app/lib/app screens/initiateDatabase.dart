// import 'package:flutter/material.dart';
// import 'package:songs_app/utils/database_files/albumsCRUD.dart';
// import 'package:songs_app/utils/database_files/artist.CRUD.dart';
// import 'package:songs_app/utils/database_files/genreCRUD.dart';
// import 'package:songs_app/utils/database_files/imagesCRUD.dart';

// import 'package:songs_app/utils/database_helper.dart';
// import 'package:songs_app/utils/database_files/usersCRUD.dart';
// import 'package:songs_app/utils/database_files/playlistCRUD.dart';
// import 'package:songs_app/models/playlist.dart';
// import 'package:songs_app/models/users.dart';
// import 'package:songs_app/models/albums.dart';
// import 'package:songs_app/models/artists.dart';
// import 'package:songs_app/models/frequentlyHeard.dart';
// import 'package:songs_app/models/genre.dart';
// import 'package:songs_app/models/image.dart';
// import 'package:songs_app/models/includes.dart';

// import 'package:sqflite/sqflite.dart';
// import 'package:cloud_firestore/cloud_firestore.dart';

// import 'package:songs_app/utils/database_files/songbyCRUD.dart';
// import 'package:songs_app/utils/database_files/songsCRUD.dart';
// import 'package:songs_app/utils/database_files/frequentlyheardCRUD.dart';
// import 'package:songs_app/utils/database_files/includesCRUD.dart';

// import 'package:songs_app/models/songs.dart';
// import 'package:songs_app/models/songBy.dart';

// class CreateDatabasePage extends StatefulWidget {
//   @override
//   State<StatefulWidget> createState() {
//     return _CreateDatabasePageState();
//   }
// }

// class _CreateDatabasePageState extends State<CreateDatabasePage> {
//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       appBar: AppBar(
//         centerTitle: true,
//         title: Text('Creating Database'),
//       ),
//       body: Center(
//         child: ListView(
//           children: <Widget>[
//             Text('Hello World'),
//             RaisedButton(
//               child: Text('Add Data to firebase'),
//               onPressed: _addToFirestore,
//             ),
//             RaisedButton(
//               child: Text('Add Database'),
//               onPressed: _initializeDatabase,
//             ),
//             RaisedButton(
//               child: Text('Insert Users'),
//               onPressed: _doQuery1,
//             ),
//             RaisedButton(
//               child: Text('Update Users'),
//               onPressed: _doQuery2,
//             ),
//             RaisedButton(
//               child: Text('insert genre'),
//               onPressed: _doQuery9,
//             ),
//             RaisedButton(
//               child: Text('update genre'),
//               onPressed: _doQuery10,
//             ),
//             RaisedButton(
//               child: Text('delete genre'),
//               onPressed: _doQuery11,
//             ),
//             RaisedButton(
//               child: Text('insert playlist'),
//               onPressed: _doQuery12,
//             ),
//             RaisedButton(
//               child: Text('update playlist'),
//               onPressed: _doQuery13,
//             ),
//             RaisedButton(
//               child: Text('delete playlist'),
//               onPressed: _doQuery14,
//             ),
//             RaisedButton(
//               child: Text('insert image'),
//               onPressed: _doQuery15,
//             ),
//             RaisedButton(
//               child: Text('update image'),
//               onPressed: _doQuery16,
//             ),
//             RaisedButton(
//               child: Text('delete image'),
//               onPressed: _doQuery17,
//             ),
//             RaisedButton(
//               child: Text('insert albums'),
//               onPressed: _doQuery3,
//             ),
//             RaisedButton(
//               child: Text('update albums'),
//               onPressed: _doQuery4,
//             ),
//             RaisedButton(
//               child: Text('delete albums'),
//               onPressed: _doQuery5,
//             ),
//             RaisedButton(
//               child: Text('insert artist'),
//               onPressed: _doQuery6,
//             ),
//             RaisedButton(
//               child: Text('update artist'),
//               onPressed: _doQuery7,
//             ),
//             RaisedButton(
//               child: Text('delete artist'),
//               onPressed: _doQuery8,
//             ),
//             RaisedButton(
//               child: Text('insert songs'),
//               onPressed: _doQuery50,
//             ),
//             RaisedButton(
//               child: Text('Update song'),
//               onPressed: _doQuery51,
//             ),
//             RaisedButton(
//               child: Text('delete songs'),
//               onPressed: _doQuery52,
//             ),
//             RaisedButton(
//               child: Text('insert songby'),
//               onPressed: _doQuery53,
//             ),
//             RaisedButton(
//               child: Text('update songby'),
//               onPressed: _doQuery54,
//             ),
//             RaisedButton(
//               child: Text('delete songby'),
//               onPressed: _doQuery55,
//             ),
//             RaisedButton(
//               child: Text('insert freq'),
//               onPressed: _doQuery56,
//             ),
//             RaisedButton(
//               child: Text('update freq'),
//               onPressed: _doQuery57,
//             ),
//             RaisedButton(
//               child: Text('delete freq'),
//               onPressed: _doQuery58,
//             ),
//             RaisedButton(
//               child: Text('insert includes'),
//               onPressed: _doQuery59,
//             ),
//             RaisedButton(
//               child: Text('update includes'),
//               onPressed: _doQuery60,
//             ),
//             RaisedButton(
//               child: Text('delete includes'),
//               onPressed: _doQuery61,
//             ),
//           ],
//         ),
//       ),
//     );
//   }

//   // void _deleteDB() {
//   //   DatabaseHelper databaseHelper = DatabaseHelper();
//   //   print("\n\n\nDeleted database\n\n\n\n\n");
//   // }

//   void _addToFirestore() async {
//     final Firestore _db = Firestore.instance;
//     DocumentReference ref = await _db.collection('CRUD').add({'data': {'hello':15}});
//     print(ref.updateData({'data':'hey'}));
//     // await _db.collection('helloall').where(field);
//   }

//   void _initializeDatabase() async {
//     // UsersCRUD();
//     // int result = await UsersCRUD().insertUser(user1);
//     // print(result);
//     var data = DatabaseHelper();
//     Database db = await data.database;
//     print(db);
//   }

//   void _doQuery1() async {
//     var data = DatabaseHelper();
//     // data.createTandI();
//     Database db = await data.database;
//     User user1 = User.withId(1, 'Hemanth', 'vanam', 'hemanthtemp07@gmail.com',
//         'male', DateTime(1999, 5, 7), DateTime(2014, 5, 12), true);
//     User user2 = User.withId(2, 'Ravi', 'vanam', 'ravitemp07@gmail.com', 'male',
//         DateTime(1999, 5, 7), DateTime(2014, 5, 12), true);
//     User user3 = User.withId(
//         3,
//         'Chinna',
//         'sheripally',
//         'chinnatemp07@gmail.com',
//         'male',
//         DateTime(1999, 5, 7),
//         DateTime(2014, 5, 12),
//         true);
//     User user4 = User.withId(
//         4,
//         'parvathi',
//         'kenche',
//         'parvathitemp07@gmail.com',
//         'female',
//         DateTime(1999, 5, 7),
//         DateTime(2014, 5, 12),
//         true);
//     User user5 = User.withId(
//         5,
//         'chandana',
//         'sheripally',
//         'chandanatemp07@gmail.com',
//         'female',
//         DateTime(1999, 5, 7),
//         DateTime(2014, 5, 12),
//         true);
//     Playlist playlist = Playlist(55, 'newPlaylist');
//     await UsersCRUD().insertUser(user1);
//     await UsersCRUD().insertUser(user2);
//     await UsersCRUD().insertUser(user3);
//     await UsersCRUD().insertUser(user4);
//     await UsersCRUD().insertUser(user5);
//     print(await PlaylistCRUD().insertPlaylist(playlist));
//     var result1 = await PlaylistCRUD().getPlaylistMapList();
//     print(result1);
//     dynamic result = await db.rawQuery('SELECT * FROM Users');
//     printMap(result);
//   }

//   void _doQuery2() async {
//     User user1 = User.withId(1, 'Hemanasdf', 'vanam', 'hemanthtemp07@gmail.com',
//         'male', DateTime(1999, 5, 7), DateTime(2014, 5, 12), true);
//     await UsersCRUD().deleteUser(user1.email);
//     dynamic result = await UsersCRUD().getUserMapList();
//     print(result);
//   }

//   void _doQuery3() async {
//     var data = DatabaseHelper();
//     // data.createTandI();
//     Database db = await data.database;
//     Album album1 = Album.withId(1, 'album1', DateTime(2109, 4, 6), 4, 1, 1, 1);
//     Album album2 = Album.withId(2, 'album2', DateTime(2109, 4, 7), 5, 2, 2, 2);
//     Album album3 = Album.withId(3, 'album3', DateTime(2109, 4, 8), 6, 3, 3, 3);

//     await AlbumCRUD().insertAlbum(album1);
//     await AlbumCRUD().insertAlbum(album2);
//     await AlbumCRUD().insertAlbum(album3);
//     dynamic result = await db.rawQuery('SELECT * FROM Albums');
//     printMap(result);
//   }

//   void _doQuery4() async {
//     Album album1 =
//         Album.withId(1, 'updated album1', DateTime(2109, 4, 6), 4, 1, 1, 1);
//     await AlbumCRUD().updateAlbum(album1);
//     dynamic result = await AlbumCRUD().getAlbumMapList();
//     printMap(result);
//   }

//   void _doQuery5() async {
//     Album album1 =
//         Album.withId(1, 'updated album1', DateTime(2109, 4, 6), 4, 1, 1, 1);
//     await AlbumCRUD().deleteAlbum(album1.albumName);
//     dynamic result = await AlbumCRUD().getAlbumMapList();
//     printMap(result);
//   }

//   void _doQuery6() async {
//     var data = DatabaseHelper();
//     // data.createTandI();
//     Database db = await data.database;
//     Artist artist1 = Artist.withId(1, "artist1", 1, 1, 1);
//     Artist artist2 = Artist.withId(2, "artist1", 2, 2, 2);
//     Artist artist3 = Artist.withId(3, "artist1", 3, 3, 3);

//     await ArtistsCRUD().insertArtist(artist1);
//     await ArtistsCRUD().insertArtist(artist2);
//     await ArtistsCRUD().insertArtist(artist3);
//     dynamic result = await db.rawQuery('SELECT * FROM Artists');
//     printMap(result);
//   }

//   void _doQuery7() async {
//     Artist artist1 = Artist.withId(1, "updated artist1", 1, 1, 1);
//     await ArtistsCRUD().updateArtist(artist1);
//     dynamic result = await ArtistsCRUD().getArtistMapList();
//     printMap(result);
//   }

//   void _doQuery8() async {
//     await ArtistsCRUD().deleteArtist("updated artist1");
//     dynamic result = await ArtistsCRUD().getArtistMapList();
//     printMap(result);
//   }

//   void _doQuery9() async {
//     var data = DatabaseHelper();
//     // data.createTandI();
//     Database db = await data.database;
//     Genre genre1 = Genre.withId(1, "genre1");
//     Genre genre2 = Genre.withId(2, "genre2");
//     Genre genre3 = Genre.withId(3, "genre3");

//     await GenreCRUD().insertGenre(genre1);
//     await GenreCRUD().insertGenre(genre2);
//     await GenreCRUD().insertGenre(genre3);
//     dynamic result = await db.rawQuery('SELECT * FROM Genre');
//     printMap(result);
//   }

//   void _doQuery10() async {
//     Genre genre1 = Genre.withId(1, " updated genre1");
//     await GenreCRUD().updateGenre(genre1);
//     dynamic result = await GenreCRUD().getGenreMapList();
//     print(result);
//   }

//   void _doQuery11() async {
//     Genre genre1 = Genre.withId(1, " updated genre1");
//     await GenreCRUD().deleteGenre(genre1.name);
//     dynamic result = await GenreCRUD().getGenreMapList();
//     print(result);
//   }

//   void _doQuery12() async {
//     var data = DatabaseHelper();
//     // data.createTandI();
//     Database db = await data.database;
//     Playlist playlist1 = Playlist.wihtID(1, 1, "playlist1");
//     Playlist playlist2 = Playlist.wihtID(2, 2, "playlist2");
//     Playlist playlist3 = Playlist.wihtID(3, 3, "playlist3");

//     await PlaylistCRUD().insertPlaylist(playlist1);
//     await PlaylistCRUD().insertPlaylist(playlist2);
//     await PlaylistCRUD().insertPlaylist(playlist3);
//     dynamic result = await db.rawQuery('SELECT * FROM Playlists');
//     printMap(result);
//   }

//   void _doQuery13() async {
//     Playlist playlist1 = Playlist.wihtID(1, 1, "updated playlist1");
//     await PlaylistCRUD().updatePlaylist(playlist1);
//     dynamic result = await PlaylistCRUD().getPlaylistMapList();
//     print(result);
//   }

//   void _doQuery14() async {
//     Playlist playlist1 = Playlist.wihtID(1, 1, "updated playlist1");
//     await PlaylistCRUD().deletePlaylist(playlist1.name);
//     dynamic result = await PlaylistCRUD().getPlaylistMapList();
//     print(result);
//   }

//   void _doQuery15() async {
//     var data = DatabaseHelper();
//     // data.createTandI();
//     Database db = await data.database;
//     Images image1 = Images.withId(1, "image location1", "image name1");
//     Images image2 = Images.withId(2, "image location2", "image name2");
//     Images image3 = Images.withId(3, "image location3", "image name3");

//     await ImagesCRUD().insertImage(image1);
//     await ImagesCRUD().insertImage(image2);
//     await ImagesCRUD().insertImage(image3);
//     dynamic result = await db.rawQuery('SELECT * FROM Images');
//     printMap(result);
//   }

//   void _doQuery16() async {
//     Images image1 = Images.withId(1, "image location", "omage name1");
//     await ImagesCRUD().updateImage(image1);
//     dynamic result = await ImagesCRUD().getImageMapList();
//     print(result);
//   }

//   void _doQuery17() async {
//     Images image1 = Images.withId(1, "image location", "omage name1");
//     await ImagesCRUD().deleteImage(image1.name);
//     dynamic result = await ImagesCRUD().getImageMapList();
//     print(result);
//   }

//   void printMap(List<Map<String, dynamic>> map) {
//     for (int i = 0; i < map.length; i++) {
//       map[i].forEach((k, v) {
//         return print('key $k, value:$v');
//       });
//       print('\n\n');
//     }
//   }

//   void _doQuery50() async {
//     var data = DatabaseHelper();
//     // data.createTandI();
//     Database db = await data.database;
//     Song song1 = Song.withId(1, 'IntheEnd', 150, 4, 5, 6);
//     Song song2 = Song.withId(2, 'new', 150, 8, 2, 6);
//     Song song3 = Song.withId(3, 'kiss', 150, 6, 5, 6);
//     Song song4 = Song.withId(4, 'anything', 150, 4, 7, 6);

//     await SongsCRUD().insertSong(song1);
//     await SongsCRUD().insertSong(song2);
//     await SongsCRUD().insertSong(song3);
//     await SongsCRUD().insertSong(song4);

//     dynamic result = await db.rawQuery('SELECT * FROM Songs');
//     printMap(result);

//     dynamic result1 = await db.rawQuery('SELECT * FROM Artists');
//     print('\n\n idhuiwudi');
//     printMap(result1);
//   }

//   void _doQuery51() async {
//     Song song1 = Song.withId(1, 'In the End', 150, 4, 5, 6);
//     await SongsCRUD().updateSong(song1);
//     dynamic result = await SongsCRUD().getSongMapList();
//     print(result);
//   }

//   void _doQuery52() async {
//     Song song1 = Song.withId(1, 'In the End', 150, 4, 5, 6);
//     await SongsCRUD().deleteSong(song1.title);
//     dynamic result = await SongsCRUD().getSongMapList();
//     print(result);
//   }

//   void _doQuery53() async {
//     var data = DatabaseHelper();
//     // data.createTandI();
//     Database db = await data.database;

//     SongBy songby1 = SongBy.withId(1, 4, 5);
//     SongBy songby2 = SongBy.withId(2, 5, 6);
//     SongBy songby3 = SongBy.withId(3, 6, 7);

//     await SongByCRUD().insertSongBy(songby1);
//     await SongByCRUD().insertSongBy(songby2);
//     await SongByCRUD().insertSongBy(songby3);

//     dynamic result = await db.rawQuery('SELECT * FROM SongBy');
//     printMap(result);
//   }

//   void _doQuery54() async {
//     SongBy songby1 = SongBy.withId(1, 4, 5);
//     await SongByCRUD().updateSongBy(songby1);
//     dynamic result = await SongByCRUD().getSongByMapList();
//     print(result);
//   }

//   void _doQuery55() async {
//     SongBy songby1 = SongBy.withId(1, 4, 5);
//     await SongByCRUD().deleteSongBy(songby1.artistId);
//     dynamic result = await SongByCRUD().getSongByMapList();
//     print(result);
//   }

//   void _doQuery56() async {
//     var data = DatabaseHelper();
//     // data.createTandI();
//     Database db = await data.database;

//     FrequentlyHeard frequentlyheard = FrequentlyHeard.withId(1, 2, 2, 1, 2);
//     FrequentlyHeard freq2 = FrequentlyHeard.withId(2, 3, 1, 1, 2);
//     FrequentlyHeard freq3 = FrequentlyHeard.withId(3, 4, 2, 1, 2);

//     await FrequentlyHeardCRUD().insertFrequentlyHeard(frequentlyheard);
//     await FrequentlyHeardCRUD().insertFrequentlyHeard(freq2);
//     await FrequentlyHeardCRUD().insertFrequentlyHeard(freq3);

//     dynamic result = await db.rawQuery('SELECT * FROM FrequentlyHeard');
//     printMap(result);
//   }

//   void _doQuery57() async {
//     FrequentlyHeard freq1 = FrequentlyHeard.withId(2, 5, 2, 1, 2);
//     await FrequentlyHeardCRUD().updateFrequentlyHeard(freq1);
//     dynamic result = await FrequentlyHeardCRUD().getFrequentlyHeardMapList();
//     print(result);
//   }

//   void _doQuery58() async {
//     FrequentlyHeard freq1 = FrequentlyHeard.withId(1, 2, 2, 1, 2);
//     await FrequentlyHeardCRUD().deleteFrequentlyHeard(freq1.songId);
//     dynamic result = await FrequentlyHeardCRUD().getFrequentlyHeardMapList();
//     print(result);
//   }

//   void _doQuery59() async {
//     var data = DatabaseHelper();
//     // data.createTandI();
//     Database db = await data.database;

//     Includes incl1 = Includes.withId(1, 1, 2);
//     Includes incl2 = Includes.withId(2, 2, 3);
//     Includes incl3 = Includes.withId(3, 3, 4);

//     await IncludesCRUD().insertIncludes(incl1);
//     await IncludesCRUD().insertIncludes(incl3);
//     await IncludesCRUD().insertIncludes(incl2);

//     dynamic result = await db.rawQuery('SELECT * FROM Includes');
//     printMap(result);
//   }

//   void _doQuery60() async {
//     Includes incl2 = Includes.withId(4, 4, 3);
//     await IncludesCRUD().updateIncludes(incl2);
//     dynamic result = await IncludesCRUD().getIncludesMapList();
//     print(result);
//   }

//   void _doQuery61() async {
//     Includes incl2 = Includes.withId(2, 2, 3);

//     await IncludesCRUD().deleteIncludes(incl2.songId);
//     dynamic result = await IncludesCRUD().getIncludesMapList();
//     print(result);
//   }
// }
