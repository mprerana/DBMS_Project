import 'dart:async';

import 'package:cloud_firestore/cloud_firestore.dart';

import 'package:songs_app/models/image.dart';
import 'package:songs_app/utils/database_files/tables.dart';

class ImagesFirestoreCRUD {

  static ImagesFirestoreCRUD _imagesFirestoreCRUD = ImagesFirestoreCRUD._createInstance();

  ImagesFirestoreCRUD._createInstance();

  factory ImagesFirestoreCRUD() => _imagesFirestoreCRUD;

  /// inserts images map to the firestore collection
  Future<DocumentReference> insertImages(Images image) async {
    DocumentReference genreDoc = await Firestore.instance
        .collection(Imagestable.tableName)
        .add(image.toMap());
    return genreDoc;
  }

  /// gets a snapshot of the image and converts it into image class
  Future<Images> getImageWithID(String genreId) async {
    DocumentSnapshot userSnap = await Firestore.instance
        .collection(Imagestable.tableName)
        .document(genreId)
        .get();
    Images image =
        Images.fromFirestoreMaptoImage(userSnap.data, userSnap.documentID);
    return image;
  }

  /// gets all images list form the firestore database
  Future<List<Images>> getAllImageList() async {
    QuerySnapshot imagesDocs = await Firestore.instance
        .collection(Imagestable.tableName)
        .getDocuments();
    List<Images> imagesList = List<Images>();
    for (DocumentSnapshot doc in imagesDocs.documents) {
      imagesList.add(Images.fromFirestoreMaptoImage(doc.data, doc.documentID));
    }

    return imagesList;
  }
}
