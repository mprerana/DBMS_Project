import 'dart:async';

import 'package:cloud_firestore/cloud_firestore.dart';

import 'package:songs_app/models/includes.dart';
import 'package:songs_app/utils/database_files/tables.dart';

class IncludesFirestoreCRUD {

  static IncludesFirestoreCRUD _includesFirestoreCRUD = IncludesFirestoreCRUD._createInstance();

  IncludesFirestoreCRUD._createInstance();

  factory IncludesFirestoreCRUD() => _includesFirestoreCRUD;

  /// inserts include map to firestore collection include
  Future<DocumentReference> insertInclude(Includes include) async {
    DocumentReference docRef = await Firestore.instance
        .collection(IncludesTable.tableName)
        .add(include.toMap());
    return docRef;
  }

  /// gets include with include id and song id
  Future<Includes> getIncludesWithIds(String includeId, String songId) async {
    QuerySnapshot snaps = await Firestore.instance
        .collection(IncludesTable.tableName)
        .where(IncludesTable.colIncludesId, isEqualTo: includeId)
        .where(IncludesTable.colSongId, isEqualTo: songId)
        .getDocuments();
    if (snaps.documents.isEmpty) {
      print(
          'Includes with includeid: $includeId, songId: $songId doesn\'t exist');
      return null;
    }
    DocumentSnapshot includeSnap = snaps.documents.first;
    return Includes.fromMaptoIncludes(includeSnap.data);
  }

  /// returns all includes documents as list of includes object
  Future<List<Includes>> getAllIncludes() async {
    QuerySnapshot includeSnaps = await Firestore.instance
        .collection(IncludesTable.tableName)
        .getDocuments();
    List<Includes> includesList = List<Includes>();
    for (DocumentSnapshot doc in includeSnaps.documents) {
      includesList.add(Includes.fromMaptoIncludes(doc.data));
    }

    return includesList;
  }
}
