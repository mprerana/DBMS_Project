import 'dart:async';

import 'package:cloud_firestore/cloud_firestore.dart';

import 'package:songs_app/models/playlist.dart';
import 'package:songs_app/utils/database_files/tables.dart';

class PlaylistFirestoreCRUD {
  /// inserts playlist map to the firestore collection
  // function to insert into playlist collection
  Future<DocumentReference> insertPlaylist(Playlist playList) async {
    DocumentReference userDoc = await Firestore.instance
        .collection(PlaylistTable.tableName)
        .add(playList.toMap());
    return userDoc;
  }

  /// gets playlist snapshot with playlistid as parameter and returns playlist object
  Future<Playlist> getPlaylistWithID(String playListId) async {
    DocumentSnapshot playlistSnap = await Firestore.instance
        .collection(PlaylistTable.tableName)
        .document(playListId)
        .get();
    Playlist playlist = Playlist.fromFirestoreMaptoPlaylist(
        playlistSnap.data, playlistSnap.documentID);
    return playlist;
  }

  /// gets all playlists snapshots in list form
  Future<List<Playlist>> getAllPlayLists() async {
    QuerySnapshot playListDocs = await Firestore.instance
        .collection(PlaylistTable.tableName)
        .getDocuments();
    List<Playlist> playListList = List<Playlist>();
    for (DocumentSnapshot doc in playListDocs.documents) {
      playListList
          .add(Playlist.fromFirestoreMaptoPlaylist(doc.data, doc.documentID));
    }
    return playListList;
  }
}
