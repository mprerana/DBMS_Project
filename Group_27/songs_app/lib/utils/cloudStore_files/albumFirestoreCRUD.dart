import 'dart:async';

import 'package:cloud_firestore/cloud_firestore.dart';

import 'package:songs_app/models/albums.dart';
import 'package:songs_app/utils/database_files/tables.dart';

class AlbumFirestoreCRUD {

  static AlbumFirestoreCRUD _albumFirestoreCRUD = AlbumFirestoreCRUD._createInstance();

  AlbumFirestoreCRUD._createInstance();

  factory AlbumFirestoreCRUD() {
    return _albumFirestoreCRUD;
  }

  /// inserts the album map into album collection of firestore database
  Future<DocumentReference> insertAlbum(Album album) async {
    DocumentReference albumDoc = await Firestore.instance
        .collection(AlbumsTable.tableName)
        .add(album.toMap());
    return albumDoc;
  }

  /// gets a album from with album id
  Future<Album> getAlbumWithId(String albumId) async {
    DocumentSnapshot albumSnap = await Firestore.instance
        .collection(AlbumsTable.tableName)
        .document(albumId)
        .get();
    Album album =
        Album.fromFirestoreMaptoAlbum(albumSnap.data, albumSnap.documentID);
    return album;
  }

  /// gets all album as a list from the firestore database
  Future<List<Album>> getAllAlbums() async {
    QuerySnapshot albumDocs = await Firestore.instance
        .collection(AlbumsTable.tableName)
        .getDocuments();
    List<Album> albumList = List<Album>();
    for (DocumentSnapshot doc in albumDocs.documents) {
      albumList.add(Album.fromFirestoreMaptoAlbum(doc.data, doc.documentID));
    }

    return albumList;
  }
}
