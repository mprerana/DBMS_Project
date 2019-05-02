import 'dart:async';

import 'package:cloud_firestore/cloud_firestore.dart';

import 'package:songs_app/models/songBy.dart';
import 'package:songs_app/utils/database_files/tables.dart';

class SongByForestoreCRUD {

  static SongByForestoreCRUD _songByForestoreCRUD = SongByForestoreCRUD._createInstance();

  SongByForestoreCRUD._createInstance();

  factory SongByForestoreCRUD() => _songByForestoreCRUD;

  /// inserts songby into the songby collection of firestore database
  Future<DocumentReference> insertSongBy(SongBy songby) async {
    DocumentReference songByDoc = await Firestore.instance
        .collection(SongByTable.tableName)
        .add(songby.toMap());
    return songByDoc;
  }

  /// returns songby object of songby id
  Future<SongBy> getSongByWithId(String id) async {
    QuerySnapshot songByQuerySnaps = await Firestore.instance
        .collection(SongByTable.tableName)
        .where(SongByTable.colSongId, isEqualTo: id)
        .getDocuments();
    if (songByQuerySnaps.documents.isEmpty) {
      print('songBy with id: $id doesn\'t exist');
      return null;
    }
    DocumentSnapshot songBySnap = songByQuerySnaps.documents[0];
    SongBy songBy = SongBy.fromMaptoSongBy(songBySnap.data);
    return songBy;
  }

  /// gets all the songby in al list
  Future<List<SongBy>> getAllSongBy() async {
    QuerySnapshot songBySnaps = await Firestore.instance
        .collection(SongByTable.tableName)
        .getDocuments();
    List<SongBy> songByList = List<SongBy>();
    for (DocumentSnapshot doc in songBySnaps.documents) {
      songByList.add(SongBy.fromMaptoSongBy(doc.data));
    }

    return songByList;
  }
}
