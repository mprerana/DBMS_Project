import 'dart:async';

import 'package:cloud_firestore/cloud_firestore.dart';

import 'package:songs_app/models/songs.dart';
import 'package:songs_app/utils/database_files/tables.dart';

class SongFirestoreCRUD {
  /// inserts song map to firestore collection songs
  Future<DocumentReference> insertSong(Song song) async {
    DocumentReference songDoc = await Firestore.instance
        .collection(SongsTable.tableName)
        .add(song.toMap());
    return songDoc;
  }

  /// returns song object with id
  Future<Song> getSongWithId(String id) async {
    DocumentSnapshot songSnap = await Firestore.instance
        .collection(SongsTable.tableName)
        .document(id)
        .get();
    Song song = Song.fromFirestoreMaptoSong(songSnap.data, songSnap.documentID);
    return song;
  }

  /// returns all songs in list form
  Future<List<Song>> getAllSongs() async {
    QuerySnapshot songSnaps = await Firestore.instance
        .collection(SongsTable.tableName)
        .getDocuments();
    List<Song> songList = List<Song>();
    for (DocumentSnapshot snap in songSnaps.documents) {
      songList.add(Song.fromFirestoreMaptoSong(snap.data, snap.documentID));
    }

    return songList;
  }
}
