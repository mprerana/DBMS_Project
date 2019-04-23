import 'package:flutter/material.dart';

import 'package:songs_app/app screens/home.dart';

// Playlists Widget...
class PlaylistWidget extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    return PlaylistWidgetState();
  }
}

// Playlists Widget State...
class PlaylistWidgetState extends State<PlaylistWidget> {
  @override
  Widget build(BuildContext context) {
    return Container(
      child: ListView(
        scrollDirection: Axis.vertical,
        children: <Widget>[
          // Recently Played...
          Container(
            margin: EdgeInsets.only(top: 30, bottom: 5),
            child: Text(
              'Recently Played',
              style: TextStyle(
                fontSize: 40,
                fontFamily: 'LUMOS',
                fontWeight: FontWeight.bold,
                color: Colors.white,
              ),
            ),
          ),
          RecentlyPlayed(),

          // Playlists...
          Container(
            margin: EdgeInsets.only(top: 30, bottom: 5),
            child: Text(
              'Your Playlists',
              style: TextStyle(
                fontSize: 40,
                fontFamily: 'LUMOS',
                fontWeight: FontWeight.bold,
                color: Colors.white,
              ),
            ),
          ),
          Playlist(),
        ],
      ),
      decoration: BoxDecoration(
          border: Border(
              top: BorderSide(
                  color: Colors.blue, width: 3.0, style: BorderStyle.solid))),
    );
  }
}

// Display Playlist Songs...
Widget displayPlaylistSongs(List<List> playlists, List playlist) {

  List<String> playlistNames = List<String>();
  for (var i = 0; i < playlists.length; i++) {
    playlistNames.add(playlists[i][0]);
  }

  List songs =playlist[2];

  return Container(
    color: Color.fromRGBO(190, 190, 190, 0.5),
    height: 300.0,
    child: ListView.builder(
        scrollDirection: Axis.vertical,
        itemCount: songs.length,
        itemBuilder: (BuildContext context, int index) {
          return Container(
              width: 160.0,
              child: SizedBox(
                child: ListTile(
                  leading: Icon(
                    Icons.album,
                    size: 40,
                    color: Colors.amber,
                  ),
                  title: Text(
                    songs[index][0],
                    style: TextStyle(
                        color: Colors.redAccent,
                        fontFamily: 'Gothic',
                        fontStyle: FontStyle.italic,
                        fontWeight: FontWeight.w800),
                  ),
                  subtitle: Row(
                    children: <Widget>[
                      Text(
                        'Album: ' + songs[index][2].toString(),
                        style: TextStyle(fontSize: 12.5),
                      ),
                      Text(
                        '      Duraton: ' + songs[index][1].toString() + ' mins',
                        style: TextStyle(
                          fontSize: 12.5,
                        ),
                      ),
                    ],
                  ),
                  // PopUpMenu...
                  trailing: new PopupMenuButton<String>(
                    child: Icon(Icons.playlist_add),
                    itemBuilder: (BuildContext context) {
                      return playlistNames.map((String playlist) {
                        return new PopupMenuItem<String>(
                          child: Text(playlist),
                          value: playlist,
                        );
                      }).toList();
                    },
                  ),
                  onLongPress: () {
                    showDialog(
                        context: context,
                        barrierDismissible: false,
                        builder: (BuildContext context) {
                          return AlertDialog(
                            title: Text('Not Interested?'),
                            content: SingleChildScrollView(
                              child: ListBody(
                                children: <Widget>[
                                  Text(
                                      'You don\'t want to see this song on your home screen?'),
                                ],
                              ),
                            ),
                            actions: <Widget>[
                              FlatButton(
                                child: Text('Remove'),
                                onPressed: () {
                                  debugPrint('Cancelled Operation!');
                                  Navigator.of(context).pop();
                                },
                              ),
                              FlatButton(
                                child: Text('Cancel'),
                                onPressed: () {
                                  debugPrint('Cancelled Operation!');
                                  Navigator.of(context).pop();
                                },
                              ),
                            ],
                          );
                        });

                    debugPrint('Pressed too long');
                  },
                  onTap: () {
                    debugPrint('Canot play this song!');
                    currSong.clear();
                    currSong = songs[index].toList();
                    navigateToNowPlaying(context, currSong, playlist);
                  },
                ),
              ));
        }),
  );
}
