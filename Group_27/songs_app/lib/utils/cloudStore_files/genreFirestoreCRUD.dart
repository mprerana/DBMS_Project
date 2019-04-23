import 'dart:async';

import 'package:cloud_firestore/cloud_firestore.dart';

import 'package:songs_app/models/genre.dart';
import 'package:songs_app/utils/database_files/tables.dart';

class GenreFirestoreCRUD {
  /// inserts genre map to the firestore collection
  // function to insert into genre table
  Future<DocumentReference> insertGenre(Genre genre) async {
    DocumentReference genreDoc = await Firestore.instance
        .collection(GenreTable.tableName)
        .add(genre.toMap());
    return genreDoc;
  }

  /// gets genre snapshot with genre id as parameter and returns genre object
  Future<Genre> getGenreWithID(String genreId) async {
    DocumentSnapshot userSnap = await Firestore.instance
        .collection(GenreTable.tableName)
        .document(genreId)
        .get();
    Genre genre =
        Genre.fromFirestoreMaptoGenre(userSnap.data, userSnap.documentID);
    return genre;
  }

  /// gets all genre snapshots in list form
  Future<List<Genre>> getAllGenre() async {
    QuerySnapshot genreDocs = await Firestore.instance
        .collection(GenreTable.tableName)
        .getDocuments();
    List<Genre> genreList = List<Genre>();
    for (DocumentSnapshot doc in genreDocs.documents) {
      genreList.add(Genre.fromFirestoreMaptoGenre(doc.data, doc.documentID));
    }
    return genreList;
  }
}
