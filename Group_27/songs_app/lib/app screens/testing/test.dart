// import 'dart:io';

// import 'package:flutter/material.dart';
// import 'package:cloud_firestore/cloud_firestore.dart';
// // import 'package:firebase_auth/firebase_auth.dart';

// // import 'package:songs_app/services/authentication.dart';
// // import 'package:songs_app/models/users.dart';
// // import 'package:songs_app/utils/database_files/usersCRUD.dart';

// import 'package:songs_app/models/artists.dart';
// import 'package:songs_app/models/albums.dart';
// import 'package:songs_app/models/songs.dart';
// import 'package:songs_app/models/image.dart';
// import 'package:songs_app/models/genre.dart';
// import 'package:songs_app/models/songBy.dart';

// import 'package:songs_app/utils/database_files/artist.CRUD.dart';
// import 'package:songs_app/utils/database_files/albumsCRUD.dart';
// import 'package:songs_app/utils/database_files/songsCRUD.dart';
// import 'package:songs_app/utils/database_files/imagesCRUD.dart';
// import 'package:songs_app/utils/database_files/songbyCRUD.dart';

// import 'package:songs_app/utils/cloudStore_files/artistFirestoreCRUD.dart';
// import 'package:songs_app/utils/cloudStore_files/albumFirestoreCRUD.dart';
// import 'package:songs_app/utils/cloudStore_files/songFirestoreCRUD.dart';
// import 'package:songs_app/utils/cloudStore_files/imagesFirestoreCRUD.dart';
// import 'package:songs_app/utils/cloudStore_files/genreFirestoreCRUD.dart';
// import 'package:songs_app/utils/cloudStore_files/songByFirestoreCRUD.dart';

// import 'package:songs_app/services/storage.dart';

// class TestPage extends StatefulWidget {

//   @override
//   State<StatefulWidget> createState() {
//     return TestPageState();
//   }
// }

// class TestPageState extends State<TestPage> {

//   File _chachedFile;
//   String _paths;

//   @override
//   Widget build(BuildContext context) {
//     return WillPopScope(
//       child: Scaffold(
//         appBar: AppBar(
//           leading: null,
//           title: Text(
//             'BLINK',
//             style: TextStyle(
//               fontSize: 25,
//               fontFamily: 'Velhos Tempos',
//             ),
//             textAlign: TextAlign.center,
//           ),
//           centerTitle: true,
//           backgroundColor: Colors.deepPurple,
//         ),
//         body: _getBody(),
//         floatingActionButton: FloatingActionButton(
//           child: Icon(Icons.cloud_download),
//           onPressed: () async {
//             _chachedFile = await StorageIO().downloadImage(_paths);
//             setState(() {
//              _chachedFile = _chachedFile; 
//             });
//           },
//         ),
//       ),
//       onWillPop: () {
//         Navigator.of(context).pop();
//       },
//     );
//   }

//   Widget _getBody() {
//     return Center(
//       child: Column(
//         crossAxisAlignment: CrossAxisAlignment.center,
//         children: <Widget>[
//           RaisedButton(
//             child: Text('Add Images'),
//             onPressed: addImages,
//           ),
//           RaisedButton(
//             child: Text('Add Artists'),
//             onPressed: addArtist,
//           ),
//           RaisedButton(
//             child: Text('Add Albums'),
//             onPressed: addAlbum,
//           ),
//           RaisedButton(
//             child: Text('Add Songs'),
//             onPressed: addSong,
//           ),
//           RaisedButton(
//             child: Text('Add SongBy'),
//             onPressed: addSongBy,
//           ),
//           // Row(
//           //   children: dogPaths
//           //       .map((name) => GestureDetector(
//           //             child: Image.asset(
//           //               'assets/artists/'+name,
//           //               width: 100,
//           //             ),
//           //             onTap: () async {
//           //               // await StorageIO().uploadImage(name,'assets/$name');
//           //               await StorageIO().uploadSong('newSong', 'assets/Alan_Walker_-_Alone.mp3');
//           //               setState(() {
//           //                 _paths = name; 
//           //               });
//           //             },
//           //           ))
//           //       .toList(),
//           // ),
//           Container(
//             color: Colors.black,
//             width: 150,
//             height: 150,
//             child: _chachedFile != null ? Image.asset(_chachedFile.path) : Container(),
//           ),
//         ],
//       ),
//     );
//   }

//   final List<String> dogPaths = <String>[
//     '24KMagic.jpg',
//     'allYourFault.jpg',
//     'badlands.jpg',
//     'divide.jpg',
//     'don\'tSmileAtMe.jpg',
//     'duaLipa.jpg',
//     'expectations.jpg',
//     'forYou.jpg',
//     'home.jpg',
//     'hopelessFountianKingdom.jpg',
//     'laundryService.jpg',
//     'lonely.jpg',
//     'OralFixation.jpg',
//     'pitchPerfect2.jpg',
//     'prism.jpg',
//     'recovery.jpg',
//     'reputation.jpg',
//     'revival.jpg',
//     'scorpion.jpg',
//     'sing.jpg',
//     'smackThat.jpg',
//     'taylorSwift.jpg',
//     'theGrenadeSession.jpg',
//     'whenWeAllFallAsleep.jpg',
//     'witness.jpg',
//   ];

//   void addImages() async {

//     // List<Images> imageList = List<Images>();

//     // for (String imageName in dogPaths) {
//     // await StorageIO().uploadImage(imageName, 'assets/albums/$imageName', 'Albums');
//     //   imageList.add(Images('Albums/'+imageName, 'Album'+imageName));
//     // }
    
//     // for (Images image in imageList) {
//     //   DocumentReference ref = await ImagesFirestoreCRUD().insertImages(image);
//     //   DocumentSnapshot snap = await ref.get();
//     //   Images newImage = Images.fromFirestoreMaptoImage(snap.data, snap.documentID);
//     //   await ImagesCRUD().insertImage(newImage);
//     // }
//   }

//   void addArtist() async {
//     // List<Artist> artistList = List<Artist>();

//     // List<Images> imagesList = await ImagesCRUD().getImageList();

//     // artistList.add(Artist('Akon', 0, 0, imagesList[0].imageId));
//     // artistList.add(Artist('Ariana Grande', 0, 0, imagesList[1].imageId));
//     // artistList.add(Artist('Bebe Rexha', 0, 0, imagesList[2].imageId));
//     // artistList.add(Artist('Billie Eilish', 0, 0, imagesList[3].imageId));
//     // artistList.add(Artist('Bruno Mars', 0, 0, imagesList[4].imageId));
//     // artistList.add(Artist('Drake', 0, 0, imagesList[5].imageId));
//     // artistList.add(Artist('Dua Lipa', 0, 0, imagesList[6].imageId));
//     // artistList.add(Artist('Ed Sheeran', 0, 0, imagesList[7].imageId));
//     // artistList.add(Artist('Eminem', 0, 0, imagesList[8].imageId));
//     // artistList.add(Artist('Hasley', 0, 0, imagesList[9].imageId));
//     // artistList.add(Artist('Katy Perry', 0, 0, imagesList[10].imageId));
//     // artistList.add(Artist('Rihanna', 0, 0, imagesList[11].imageId));
//     // artistList.add(Artist('Selena Gomez', 0, 0, imagesList[12].imageId));
//     // artistList.add(Artist('Shakira', 0, 0, imagesList[13].imageId));
//     // artistList.add(Artist('Taylor Swift', 0, 0, imagesList[14].imageId));

//     // for (Artist artist in artistList) {
//     //   DocumentReference ref = await ArtistFirestoreCRUD().insertArtist(artist);
//     //   DocumentSnapshot snap = await ref.get();
//     //   Artist newArtist =
//     //       Artist.fromFirestoreMaptoArtist(snap.data, snap.documentID);
//     //   await ArtistsCRUD().insertArtist(newArtist);
//     // }
//     // print('Success');
//   }

//   void addAlbum() async {
//     // List<Album> albumList = List<Album>();

//     // List<Images> imageList = await ImagesFirestoreCRUD().getAllImageList();
//     // List<Genre> genreList = await GenreFirestoreCRUD().getAllGenre();
//     // print(imageList.length);

//     // albumList.add(Album('24K Magic', DateTime(2016), 0, 0, genreList[11].genreId, imageList[15].imageId));
//     // albumList.add(Album('All Your Fault', DateTime(2015), 0, 0, genreList[7].genreId, imageList[16].imageId));
//     // albumList.add(Album('Badlands', DateTime(2015), 0, 0, genreList[7].genreId, imageList[17].imageId));
//     // albumList.add(Album('Divide', DateTime(2017), 0, 0, genreList[8].genreId, imageList[18].imageId));
//     // albumList.add(Album('Don\'t Smile At Me', DateTime(2015), 0, 0, genreList[7].genreId, imageList[19].imageId));
//     // albumList.add(Album('Dua Lipa', DateTime(2015), 0, 0, genreList[8].genreId, imageList[20].imageId));
//     // albumList.add(Album('Expecations', DateTime(2015), 0, 0, genreList[7].genreId, imageList[21].imageId));
//     // albumList.add(Album('For You', DateTime(2015), 0, 0, genreList[7].genreId, imageList[22].imageId));
//     // albumList.add(Album('Home', DateTime(2015), 0, 0, genreList[7].genreId, imageList[23].imageId));
//     // albumList.add(Album('Hopeless Fountain Kingdom', DateTime(2015), 0, 0, genreList[7].genreId, imageList[24].imageId));
//     // albumList.add(Album('Laundry Service', DateTime(2014), 0, 0, genreList[11].genreId, imageList[25].imageId));
//     // albumList.add(Album('Lonely', DateTime(2012), 0, 0, genreList[7].genreId, imageList[26].imageId));
//     // albumList.add(Album('Loud', DateTime(2012), 0, 0, genreList[8].genreId, imageList[27].imageId));
//     // albumList.add(Album('Oral Fixation', DateTime(2010), 0, 0, genreList[7].genreId, imageList[28].imageId));
//     // albumList.add(Album('Pitch Perfect 2', DateTime(2010), 0, 0, genreList[7].genreId, imageList[29].imageId));
//     // albumList.add(Album('Prism', DateTime(2009), 0, 0, genreList[7].genreId, imageList[30].imageId));
//     // albumList.add(Album('Recovery', DateTime(2010), 0, 0, genreList[7].genreId, imageList[31].imageId));
//     // albumList.add(Album('Revival', DateTime(2010), 0, 0, genreList[7].genreId, imageList[32].imageId));
//     // albumList.add(Album('Scorpion', DateTime(2010), 0, 0, genreList[7].genreId, imageList[33].imageId));
//     // albumList.add(Album('Sing', DateTime(2010), 0, 0, genreList[7].genreId, imageList[34].imageId));
//     // albumList.add(Album('Smack That', DateTime(2010), 0, 0, genreList[7].genreId, imageList[35].imageId));
//     // albumList.add(Album('Taylor Swift', DateTime(2010), 0, 0, genreList[7].genreId, imageList[36].imageId));
//     // albumList.add(Album('The Grenade Session', DateTime(2010), 0, 0, genreList[7].genreId, imageList[37].imageId));
//     // albumList.add(Album('When We All Fall Asleep', DateTime(2010), 0, 0, genreList[7].genreId, imageList[38].imageId));
//     // albumList.add(Album('Witness', DateTime(2010), 0, 0, genreList[7].genreId, imageList[39].imageId));

//     // for (Album album in albumList) {
//     //   DocumentReference ref = await AlbumFirestoreCRUD().insertAlbum(album);
//     //   DocumentSnapshot snap = await ref.get();
//     //   Album newAlbum =
//     //       Album.fromFirestoreMaptoAlbum(snap.data, snap.documentID);
//     //   await AlbumCRUD().insertAlbum(newAlbum);
//     // }
//   }

//   void addSong() async {
//     // List<Song> songList = List<Song>();

//     // songList.add(Song('24K Magic', 226, '24K Magic.mp3', '-LdXuRnl22yNpbYkbh2C','-Ld8QQpQ6AB_cTnjIqNT','-LdXi93FoV--3eDqbtds'));
//     // songList.add(Song('Bad At Love', 181, 'bad at love.mp3', '-LdXuU3TP9Ad62GmNGxS','-Ld8PU3ME9PEDY_DF96g',''));
//     // songList.add(Song('Colors',246, 'colors.mp3', '-LdXuSRnJCjFmSkeWXRE','-Ld8PU3ME9PEDY_DF96g','-LdXiAwOhUwfqBXAQZYd'));
//     // songList.add(Song('Shape of You',240, 'Shape of you.mp3', '-LdXuShCCbKs8X9yA2BY','-Ld8OssS_BNVkHTDSfvp','-LdXi9gFdEhu7l33nrai'));
//     // songList.add(Song('Ocean Eyes', 200, 'Ocean Eyes.mp3', '-LdXuSw7YP1TiEvqghTR','-Ld8PU3ME9PEDY_DF96g','-LdXi9sCc-GQrEuivgh4'));
//     // songList.add(Song('New Rules',212, 'New Rules.mp3', '-LdXuTB9kborODE5XAKL','-Ld8QQpQ6AB_cTnjIqNT','-LdXiA3mzq4-ZQxenlMd'));
//     // songList.add(Song('I\'m a Mess', 184, 'I\'m a Mess.mp3', '-LdXuTP4F3RaxxZuMgZf','-Ld8PU3ME9PEDY_DF96g','-LdXi9UAz4IUZoJzj7aU'));
//     // songList.add(Song('The Heart Wants What It Wants', 180, 'The Heart Want.mp3', '-LdXuTcC4Sua6RaV2hZM','SoJGDlBDTBweawATirP1','-LdXiAHdzL6cPqbaBlR6'));
//     // songList.add(Song('Towards The Sun', 273, 'Towards The Sun.mp3', '-LdXuTqdwbwQS88gN9s4','-Ld8PT2S0ON6zBufpzIW','-LdXiAjXgPtks7YiWJaD'));

//     // for (Song song in songList) {
//     //   DocumentReference ref = await SongFirestoreCRUD().insertSong(song);
//     //   DocumentSnapshot snap = await ref.get();
//     //   Song newSong = Song.fromFirestoreMaptoSong(snap.data, snap.documentID);
//     //   await SongsCRUD().insertSong(newSong);
//     // }
//   }

//   Future<void> addSongBy() async {
    
//     List<SongBy> songbyList = List<SongBy>();

//     songbyList.add(SongBy('-Ldj2wa-q3juIIr-KqOA', '-LdXuRnl22yNpbYkbh2C', '-LdV7QS_qRHEzHC_Am_N'));
//     songbyList.add(SongBy('-Ldj2x0x3n76pMWpWA1s', '-LdXuU3TP9Ad62GmNGxS', '-LdV7RXhB3uDYe7HmiDk'));
//     songbyList.add(SongBy('-Ldj2xITnyICMgdezSYO', '-LdXuSRnJCjFmSkeWXRE', '-LdV7RXhB3uDYe7HmiDk'));
//     songbyList.add(SongBy('-Ldj2xY2OUjhLvWBCAoH', '-LdXuShCCbKs8X9yA2BY', '-LdV7R7wX82ENwvITZXI'));
//     songbyList.add(SongBy('-Ldj2xnBZd1mUK2-u46v', '-LdXuSw7YP1TiEvqghTR', '-LdV7QFL5tbXZH4YUsW1'));
//     songbyList.add(SongBy('-Ldj2y1v-WvOlwoLZgI1', '-LdXuTB9kborODE5XAKL', '-LdV7QupAWT-R9hSE6Hh'));
//     songbyList.add(SongBy('-Ldj2yGheZUzNUeh--pc', '-LdXuTP4F3RaxxZuMgZf', '-LdV7Q1fKWwcYpOZ1KAM'));
//     songbyList.add(SongBy('-Ldj2yXPpkxui5ZRY8OB', '-LdXuTcC4Sua6RaV2hZM', '-LdV7SAOXbLAvMq_dHh9'));
//     songbyList.add(SongBy('Ldj2ypT7DWrvVpoje2O', '-LdXuTqdwbwQS88gN9s4', '-LdV7RxiJ_lUl15nT45e'));

//     for (SongBy songby in songbyList) {
//       DocumentReference ref = await SongByForestoreCRUD().insertSongBy(songby);
//       DocumentSnapshot snap = await ref.get();
//       SongBy newSongBy = SongBy.fromMaptoSongBy(snap.data);
//       await SongByCRUD().insertSongBy(newSongBy);
//     }
//   }
// }