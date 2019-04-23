import 'dart:async';

import 'package:cloud_firestore/cloud_firestore.dart';

import 'package:songs_app/models/users.dart';
import 'package:songs_app/utils/database_files/tables.dart';

class UserFirestoreCRUD {
  /// inserts user map to the firestore collection
  // function to insert into user collection
  Future<DocumentReference> insertUser(User user) async {
    DocumentReference userDoc = await Firestore.instance
        .collection(UsersTable.tableName)
        .add(user.toMap());
    return userDoc;
  }

  /// gets user snapshot with userid as parameter and returns user object
  Future<User> getUserWithID(String userId) async {
    DocumentSnapshot userSnap = await Firestore.instance
        .collection(UsersTable.tableName)
        .document(userId)
        .get();
    User user = User.fromFirestoreMaptoUser(userSnap.data, userSnap.documentID);
    return user;
  }

  Future<void> updateUserWithID(User user) async {
    await Firestore.instance
        .collection(UsersTable.tableName)
        .document(user.userId)
        .updateData(user.toMap());
    return;
  }

  /// gets all users snapshots in list form
  Future<List<User>> getAllUsers() async {
    QuerySnapshot userDocs = await Firestore.instance
        .collection(UsersTable.tableName)
        .getDocuments();
    List<User> userList = List<User>();
    for (DocumentSnapshot doc in userDocs.documents) {
      userList.add(User.fromFirestoreMaptoUser(doc.data, doc.documentID));
    }
    return userList;
  }
}
