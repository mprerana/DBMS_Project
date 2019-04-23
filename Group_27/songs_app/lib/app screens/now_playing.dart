import 'package:flutter/material.dart';
// import 'package:audioplayers/audioplayers.dart';

import 'package:songs_app/app screens/now_playing_widgets/widgets.dart';
// import 'package:songs_app/app screens/home.dart';
import 'package:songs_app/app screens/playlists.dart';

// Now Playing Widget
class NowPlayingWidget extends StatelessWidget {

  NowPlayingWidget({
    Key key,
    this.appBarOn: true,
    this.topPadding: 100.0, 
    this.songName, 
    this.artistName: 'Unknown', 
    this.albumName: 'Unknown', 
    this.artistImage: 'assets/songs/song-bg-1.jpg',
    this.songLength: 0.00,
    this.playlists,
    this.playlist,
  }) : super(key: key);

  final bool appBarOn;
  final double topPadding;
  final String songName;
  final String artistName;
  final String albumName;
  final String artistImage;
  final double songLength;
  final List<List> playlists;
  final List playlist;

  @override
  Widget build(BuildContext context) {

    final Map<String, dynamic> args = {
      'topPadding': topPadding, 
      'songName': songName,
      'albumName': albumName,
      'artistName': artistName,
      'artistImage': artistImage,
      'songLength':songLength.toString(),
    };

    return Scaffold(
      appBar: appBarOn ? 
        AppBar(
          backgroundColor: Colors.blueGrey, 
          brightness: Brightness.dark, 
          centerTitle: true, 
          title: Title(
            child: Text(
              'BLYNK',
              style: TextStyle(
                fontFamily: 'Halfomania-Regular',
                fontSize: 60,
              ),
            ), 
            color: Colors.white,
          ),
          
        )
      : null,
      body: Container(
        child: ListView(
          children: <Widget>[

            firstWidget(args),
            SizedBox(height: 85,),
            Text(
              playlist[0],
              style: TextStyle(
                fontSize: 30,
                fontFamily: 'Magnificent',
              ),
            ),
            displayPlaylistSongs(playlists, playlist),
          
          ],
        ),
        decoration: appBarOn ?
        null :
        BoxDecoration(
          border: Border(
            top: BorderSide(
              color: Colors.pink,
              width: 3.0,
              style: BorderStyle.solid
            )
          )
        ),
      ),
    );
  }

}
