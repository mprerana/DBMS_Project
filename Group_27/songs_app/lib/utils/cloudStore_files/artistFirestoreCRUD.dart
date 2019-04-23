import 'dart:async';

import 'package:cloud_firestore/cloud_firestore.dart';

import 'package:songs_app/models/artists.dart';
import 'package:songs_app/utils/database_files/tables.dart';

class ArtistFirestoreCRUD {
  /// inserts artist to artist collection database
  Future<DocumentReference> insertArtist(Artist artist) async {
    DocumentReference artistDoc = await Firestore.instance
        .collection(ArtistTable.tableName)
        .add(artist.toMap());
    return artistDoc;
  }

  /// gets the artist record from the database with paramaters as document id
  Future<Artist> getArtistWithId(String id) async {
    DocumentSnapshot artistSnap = await Firestore.instance
        .collection(ArtistTable.tableName)
        .document(id)
        .get();
    Artist artist =
        Artist.fromFirestoreMaptoArtist(artistSnap.data, artistSnap.documentID);
    return artist;
  }

  /// gets all the artist from the database in list
  Future<List<Artist>> getAllArtists() async {
    QuerySnapshot artistDocs = await Firestore.instance
        .collection(ArtistTable.tableName)
        .getDocuments();
    List<Artist> artistList = List<Artist>();
    for (DocumentSnapshot doc in artistDocs.documents) {
      artistList.add(Artist.fromFirestoreMaptoArtist(doc.data, doc.documentID));
    }

    return artistList;
  }
}
