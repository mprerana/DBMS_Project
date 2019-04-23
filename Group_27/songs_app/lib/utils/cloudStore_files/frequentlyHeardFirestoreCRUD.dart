import 'dart:async';

import 'package:cloud_firestore/cloud_firestore.dart';

import 'package:songs_app/models/frequentlyHeard.dart';
import 'package:songs_app/utils/database_files/tables.dart';

class FrequentlyHeardFirestoreCRUD {
  /// inserts frequentlyHeard to firstore database collection FrequentlyHeard
  Future<DocumentReference> insertFrequentlyHeard(FrequentlyHeard frequenltyHeard) async {
    DocumentReference docRef = await Firestore.instance
        .collection(FrequentlyHeardTable.tableName)
        .add(frequenltyHeard.toMap());
    return docRef;
  }

  /// return frequentlyHeard object with userid and songid
  Future<FrequentlyHeard> getFrequentlyHeardWithIds(String userId, String songId) async {
    QuerySnapshot snaps = await Firestore.instance
        .collection(FrequentlyHeardTable.tableName)
        .where(FrequentlyHeardTable.colUserId, isEqualTo: userId)
        .where(FrequentlyHeardTable.colSongId, isEqualTo: songId)
        .getDocuments();
    if (snaps.documents.isEmpty) {
      print(
          'frequently Heard with userid: $userId, songid: $songId doesn\'t exist');
      return null;
    }
    DocumentSnapshot frequntlyHeardSnap = snaps.documents.first;
    return FrequentlyHeard.fromMaptoFrequentlyHeard(frequntlyHeardSnap.data);
  }

  /// returns all frequentlyHeard as list
  Future<List<FrequentlyHeard>> getAllFrequentlyHeard() async {
    QuerySnapshot frequentlyHeardSnaps = await Firestore.instance
        .collection(FrequentlyHeardTable.tableName)
        .getDocuments();
    List<FrequentlyHeard> frequentlyHeardList = List<FrequentlyHeard>();
    for (DocumentSnapshot doc in frequentlyHeardSnaps.documents) {
      frequentlyHeardList.add(FrequentlyHeard.fromMaptoFrequentlyHeard(doc.data));
    }

    return frequentlyHeardList;
  }
}
