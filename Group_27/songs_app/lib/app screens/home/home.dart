import 'package:flutter/material.dart';

import 'package:songs_app/app screens/playlists_class.dart';
// import 'package:songs_app/services/authentication.dart';

import 'package:songs_app/app screens/now_playing.dart';
import 'package:songs_app/app screens/titles.dart';

import 'package:songs_app/app screens/home/widgets.dart';
import 'package:songs_app/app screens/home/generateSongs.dart';
import 'package:songs_app/services/loader.dart';

import 'package:songs_app/services/songServieces.dart';
import 'package:songs_app/models/songDetails.dart';


/// Communicates the current state of the audio player.
enum PlayerState {
  /// Player is stopped. No file is loaded to the player. Calling [resume] or [pause] will result in exception.
  STOPPED,
  /// Currently playing a file. The user can [pause], [resume] or [stop] the playback.
  PLAYING,
  /// Paused. The user can [resume] the playback without providing the URL.
  PAUSED,
  /// The playback has been completed. This state is the same as [STOPPED]
  COMPLETED,
}

/// [Global Variables] ...
PlayerState playerState;
TabController tabController;

// Current Playing Song...
SongDetails currSong;

// Populating PlayLists...
List<List> playlists = populatePlaylists();
List playlist = List();

int currentIndex = 0;


// -------------------------------------------------------- //
// Home Widget...
class Home extends StatefulWidget {
  @override
  State<StatefulWidget> createState() => HomeState();
}

class HomeState extends State<Home> with SingleTickerProviderStateMixin<Home>{

  bool _isLoading = true;

  List<SongDetails> songDetailsList;
  Map<String, dynamic> args = Map<String, dynamic>();

  // Colors and theme...
  MaterialColor color = Colors.teal;
  bool firstIndex = true, secondIndex, thirdIndex;

  @override
  void initState() {

    super.initState();
    initSongs();
    tabController = TabController(vsync: this, length: 3)
    ..addListener(() {
      setState(() {
        switch (tabController.index) {
          case 0:
            color = Colors.teal;
            firstIndex = true;
            secondIndex = false;
            thirdIndex = false;
            break;
          case 1:
            color = Colors.pink;
            firstIndex = false;
            secondIndex = true;
            thirdIndex = false;
            break;
          case 2:
            color = Colors.blue;
            firstIndex = false;
            secondIndex = false;
            thirdIndex = true;
            break;
        }
      });
    });

  }

  void initSongs() async {
    songDetailsList = await SongServies().getAllSongDetails();
    setState(() {_isLoading = false;});
  }

  @override
  void dispose() {
    super.dispose();
    tabController.dispose();
    if (playerState == PlayerState.PLAYING || playerState == PlayerState.PAUSED) {
      audioPlayer.stop();
    }
  }

/// Controlling State of Song...
  /// [PlayerState] = [PLAYING] ...
  void setPlayingState() {
    setState(() {
      playerState = PlayerState.PLAYING;
    });
  }

  /// [PlayerState] = [PAUSED] ...
  void setPauseState() {
    setState(() {
      playerState = PlayerState.PAUSED;
    });
  }

  /// [PlayerState] = [COMPLETED] ...
  void setCompletedState() {
    setState(() {
      playerState = PlayerState.COMPLETED;
    });
  }

  /// Updating [args] and [currSong] ...
  void updateArgs() {
    args.clear();
    args = {
      'songName': currSong.song.title,
      'albumName': currSong.album.albumName,
      'artistName': currSong.artist.name,
      // 'artistImage': currSong.song.imageId,
      'artistImage': 'assets/songs/song-bg-1.jpg',
      'songLength': currSong.song.length,
    };
  }


  /// Build Widget...
  @override
  Widget build(BuildContext context) {

    // Return Statement...
    return DefaultTabController(

      length: 3,
      
      child: Stack(
        children: <Widget>[
          
          Container(
            child: Image.asset('assets/msc-bg-3.jpg', fit: BoxFit.cover, width: double.infinity, height: 250,),
          ),
          
          Scaffold(

            backgroundColor: Colors.transparent,

            drawer: HomeScreenWidgets().sideDrawer(context),
            
            appBar: HomeScreenWidgets().appBar(context, tabController, color),
            
            body: TabBarView(

              controller: tabController,
              children: <Widget>[

                _isLoading ? Loader() : popularSongsWidget(),
                _isLoading ? Loader() :
                currSong == null
                ?
                Center(
                  child: Text('Play any song.', style: TextStyle(color: Colors.white, fontSize: 30, fontFamily: 'Magnificent'),),
                )
                :
                NowPlayingWidget(fullScreenOn: false, args: args, allSongs: songDetailsList,),
                _isLoading ? Loader() : playlistWidget(),

              ],
            
            ),

          ),

        ],
      ),

    );
  }


// Widgets-------------------------------------------------------------------------------------------------------------------
  /// [Popular Songs Widget] ...
  Widget popularSongsWidget() {
    return Container(
      child: ListView(
        scrollDirection: Axis.vertical,
        
        children: <Widget>[

          sortedSongsTitles('Top Releases'),
          topRelease(),

        ],
      ),

      decoration: BoxDecoration(
        border: Border(
          top: BorderSide(
            color: Colors.teal[400],
            width: 3.0,
            style: BorderStyle.solid
          )
        )
      ),
    );
  }


  /// [Playlist Widget] ...
  Widget playlistWidget() {
    return Container(
      child: ListView(

        scrollDirection: Axis.vertical,
        children: <Widget>[

          // Recently Played...
          sortedSongsTitles('Recently Played'),
          recentlyPlayed(),

          // Playlists...
          sortedSongsTitles('Your Playlists'),
          playlistsWidget(),

        ],

      ),
      decoration: BoxDecoration(border: Border(top: BorderSide(color: Colors.blue, width: 3.0, style: BorderStyle.solid))),
    );
  }


// Sub Widgets-----------------------------------------------------------------------------------------------------------------------------

  // Recently Played...
  Widget recentlyPlayed() {
    return Container(
      height: 140,
      child: ListView.builder(
        scrollDirection: Axis.horizontal,
        itemCount: songDetailsList.length,
        itemBuilder: (BuildContext context, int index) {
          String songName;
          if ( songDetailsList[index].song.title.toString().length >= 16 ) {
            songName = limitText(songDetailsList[index].song.title.toString(), 16);
          } else {
            songName = songDetailsList[index].song.title.toString();
          }
          return Container(
            child: SizedBox(
              width: 140,
              child: Card(
                child: Column(
                  children: <Widget>[
                    Container(
                        margin: EdgeInsets.only(top: 30, right: 3),
                        child: IconButton(
                          padding: EdgeInsets.only(left: 0),
                          icon: Icon(
                            Icons.play_arrow,
                            size: 50,
                            color: Colors.orangeAccent,
                          ),
                          onPressed: () {
                            currSong = songDetailsList[index];
                            currentIndex = index;
                            playlist = PlaylistClass('Random', playlists.length, createSongs()).fromPlaylisttoList();
                            navigateToNowPlaying(context);
                          },
                        )),
                    Container(
                      margin: EdgeInsets.only(top: 20, left: 12),
                      child: Row(
                        children: <Widget>[
                          Icon(
                            Icons.music_note,
                            size: 12.5,
                            color: Colors.blueAccent,
                          ),
                          Text(
                            songName,
                            style: TextStyle(
                                fontSize: 11,
                                fontFamily: 'Gothic',
                                fontWeight: FontWeight.bold),
                          ),
                        ],
                      ),
                    ),
                  ],
                ),
              ),
            ),
          );
        },
      ),
    );
  }

  // Playlists...
  Widget playlistsWidget() {
    return Container(
      height: 140,
      child: ListView.builder(
        scrollDirection: Axis.horizontal,
        itemCount: playlists.length,
        itemBuilder: (BuildContext context, int index) {
          String songName;
          if ( songDetailsList[index].song.title.toString().length >= 16 ) {
            songName = limitText(songDetailsList[index].song.title.toString(), 16);
          } else {
            songName = songDetailsList[index].song.title;
          }
          return Container(
            child: SizedBox(
              width: 140,
              child: Card(
                child: Column(
                  children: <Widget>[
                    ListTile(
                      dense: true,
                      title: Text(
                        playlists[index][0],
                        style: TextStyle(
                            fontSize: 15,
                            fontFamily: 'Magnificent',
                            fontWeight: FontWeight.bold),
                      ),
                    ),
                    Row(
                      children: <Widget>[
                        Text('  '),
                        Icon(
                          Icons.music_note,
                          size: 12,
                          color: Colors.blueAccent,
                        ),
                        Text(
                          ' ' + songName,
                          style: TextStyle(
                            fontSize: 10,
                            fontFamily: 'Serif',
                          ),
                          textAlign: TextAlign.right,
                        ),
                      ],
                    ),
                    Container(
                        margin: EdgeInsets.only(top: 15),
                        child: IconButton(
                          icon: Icon(
                            Icons.playlist_play,
                            size: 35,
                            color: Colors.orangeAccent,
                          ),
                          onPressed: () {
                            debugPrint('Cannot Play this playlist!');
                            playlist = playlists[index];
                            navigateToNowPlaying(context);
                          },
                        ))
                  ],
                ),
              ),
            ),
          );
        },
      ),
    );
  }

  Widget topRelease() {

    List<String> playlistNames = List<String>();
    for (var i = 0; i < playlists.length; i++) {
      playlistNames.add(playlists[i][0]);
    }

    return Container(
      color: Color.fromRGBO(190, 190, 190, 0.5),
      height: 300.0,
      child: ListView.builder(
          scrollDirection: Axis.vertical,
          itemCount: songDetailsList.length,
          itemBuilder: (BuildContext context, int index) {
            String songName, albumName;
            if ( songDetailsList[index].song.title.toString().length >= 16 ) {
              songName = limitText(songDetailsList[index].song.title.toString(), 16);
            } else {
              songName = songDetailsList[index].song.title;
            }
            if ( songDetailsList[index].album.albumName.length >= 10 ) {
              albumName = limitText(songDetailsList[index].album.albumName, 10);
            } else {
              albumName = songDetailsList[index].album.albumName;
            }
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
                      songName,
                      style: TextStyle(
                          color: Colors.redAccent,
                          fontFamily: 'Gothic',
                          fontStyle: FontStyle.italic,
                          fontWeight: FontWeight.w800),
                    ),
                    subtitle: Row(
                      children: <Widget>[
                        Text(
                          'Album: ' + albumName,
                          style: TextStyle(fontSize: 12.5),
                        ),
                        Text(
                          '      Duraton: ' + secToMin(songDetailsList[index].song.length).toStringAsFixed(2) + ' mins',
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
                        return playlistNames.map((String playlistName) {
                          return new PopupMenuItem<String>(
                            child: Text(playlistName),
                            value: playlistName,
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
                      currSong = songDetailsList[index];
                      currentIndex = index;
                      playlist = PlaylistClass('Random', playlists.length, createSongs()).fromPlaylisttoList();
                      navigateToNowPlaying(context);
                    },
                  ),
                ));
          }),
    );
  }


  String limitText(String text, int limitValue) {
    String name = '';
    for (var i = 0; i < limitValue; i++) {
      name += text[i];
    }
    name += '...';
    return name;
  }


  double secToMin(double secs) => secs/60 ;


// Navigators------------------------------------------------------------------------------------------------------------------
  /// Navigation to [Now Playing] ...
  void navigateToNowPlaying(BuildContext context) {
    updateArgs();
    Navigator.push(context, MaterialPageRoute(builder: (BuildContext context) => NowPlayingWidget(args: args, allSongs: songDetailsList,)
    ));
  }

}
