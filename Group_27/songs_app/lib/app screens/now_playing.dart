import 'dart:async';

import 'package:flutter/material.dart';

import 'package:songs_app/app screens/home/home.dart';
import 'package:songs_app/services/loader.dart';

import 'package:songs_app/app screens/now_playing_widgets/play-controller-icons.dart';

import 'package:audioplayers/audioplayers.dart';

import 'package:songs_app/services/storage.dart';
import 'package:songs_app/models/songDetails.dart';
import 'package:songs_app/services/songServieces.dart';


enum PlayMode {
  /// Play songs in [REPEAT] mode ...
  REPEAT, 
  /// Play songs in [ONE REPEAT] mode ...
  REPEAT_ONE, 
  /// Play songs in [NO REPEAT] mode ...
  NO_REPEAT
}

AudioPlayer audioPlayer = new AudioPlayer();

// Now Playing Widget
class NowPlayingWidget extends StatefulWidget {

  NowPlayingWidget({this.fullScreenOn: true, this.args, this.allSongs});

  final bool fullScreenOn;
  final Map<String, dynamic> args;
  final List<SongDetails> allSongs;

  @override
  State<StatefulWidget> createState() => NowPlayingWidgetState();

}

// Now Playing Widget State
class NowPlayingWidgetState extends State<NowPlayingWidget> {

  bool _isLoading = true;

  double seekValue = 0.0;

  PlayMode playMode;

  Duration position;
  Duration duration;
  String imgLocation;

  List<SongDetails> albumSongs;


  get isPlaying => playerState == PlayerState.PLAYING;
  get isPaused => playerState == PlayerState.PAUSED;

  get durationText =>
      duration != null ? duration.toString().split('.').first : '';
  get positionText =>
      position != null ? position.toString().split('.').first : '';

  @override
  initState() {
    super.initState();
    initPlayer();
    initAlbums();
    updateImgLoc();
    audioPlayer.onAudioPositionChanged.listen((p) {
      setState(() {
        seekValue = p.inMinutes.toDouble();
      });
    });
    // initAudioPlayer();
  }

  @override
  void dispose() {
    super.dispose();
  }

  // Function runs on call of it's parent class...
  void initPlayer() async {
    await audioPlayer.setReleaseMode(ReleaseMode.STOP);
    if ( widget.fullScreenOn ) {
      if (playerState == PlayerState.PLAYING || playerState == PlayerState.PAUSED) {
        setState(() {
          playerState = PlayerState.STOPPED;
          audioPlayer.stop();
        });
      }
      play();
    }
  }

  void initAlbums() async {
    albumSongs = await SongServies().getAlbumSongs(currSong.album.albumId);
    setState(() {_isLoading = false;});
  }

  void initAudioPlayer() {
    audioPlayer.onAudioPositionChanged.listen((p) {
      setState(() {
        seekValue = p.inMinutes.toDouble();
      });
    });
    audioPlayer.onPlayerStateChanged.listen((s) {
      if (s == AudioPlayerState.STOPPED) {
        setState(() {
          playerState = PlayerState.STOPPED;
        });
        if (currentIndex < widget.allSongs.length-1) {
          currentIndex += 1;
          currSong = widget.allSongs[currentIndex];
          changeSong();
        }
      }
    }, 
    onError: (msg) {
      setState(() {
        playerState = PlayerState.STOPPED;
        duration = new Duration(seconds: 0);
        position = new Duration(seconds: 0);
      });
    });
  }

  Future<void> updateImgLoc() async {
    imgLocation = await StorageIO().getImageLink(currSong.image.imgLocation);
    setState(() {});
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

  void onComplete() {
    setState(() => playerState = PlayerState.STOPPED);
  }


/// Controlling Song...
  /// [PLAY] ...
  Future<void> play() async {
    await audioPlayer.play(await StorageIO().getLink(currSong.song.location));
    setState(() => playerState = PlayerState.PLAYING);
  }

  /// [PAUSE] ...
  Future<void> pause() async {
    await audioPlayer.pause();
    setState(() => playerState = PlayerState.PAUSED);
  }

  /// [STOP] ...
  Future<void> resume() async {
    await audioPlayer.resume();
    setState(() => playerState = PlayerState.PLAYING);
  }

  /// [STOP] ...
  Future<void> stop() async {
    await audioPlayer.stop();
    setState(() {
      playerState = PlayerState.STOPPED;
      position = new Duration();
    });
  }

  /// [CHANGE] ...
  Future<void> changeSong() async {
    await audioPlayer.stop();
    setState(() {
      playerState = PlayerState.STOPPED;
      position = new Duration();
    });
    updateImgLoc();
    play();
  }
/// End of functions------------------------------------------------------------------------------
  

  // Building Widget... 
  @override
  Widget build(BuildContext context) {

    // Return Statement...
    return _isLoading ? Loader() : 
    Scaffold(
      body: Container(

        child: ListView(
          children: <Widget>[

            widget.fullScreenOn ? exitFullScreen(context) : SizedBox(height: 0),

            currentSongDisplay(audioPlayer),

            SizedBox(height: 65,),

            widget.fullScreenOn
            ?
            displayPlaylistHeader()
            :
            SizedBox(height: 0,),

            displayAlbumName(),
            displayAlbumSongs(),
          
          ],

        ),
        decoration: widget.fullScreenOn 
        ?
        null
        :
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
/// End of Return Statement----------------------------------------------------------------------------


// Widgets...
  // Go Back Button...
  Widget exitFullScreen(BuildContext context,) {
    return Container(
      margin: EdgeInsets.only(top: 20),
      child: Center(
          child: RaisedButton(
          elevation: 6.0,
          child: Text('Exit Full Screen', style: TextStyle(color: Colors.white),),
          onPressed: () {
            setState(() {
              tabController.index = 1;
            });
            Navigator.pushNamed(context, '/homePage');
          },
          shape: BeveledRectangleBorder(borderRadius: BorderRadius.all(Radius.circular(10))),
          color: Colors.red[400],
        ),
      )
    );
  }


  // Song Card...
  Widget songDisplayCard() {
    return imgLocation == null 
    ?
    SizedBox(
      height: 300,
      width: 300,
      child: Center(
        child: SizedBox(
          height: 50,
          width: 50,
          child: CircularProgressIndicator(),
        ),
      ),
    )
    :
    Card(
      clipBehavior: Clip.antiAliasWithSaveLayer,
      margin: EdgeInsets.only(top: 50),
      child: Container(
        height: 300,
        width: 300,
        child: Image.network(imgLocation, fit: BoxFit.cover,),
      ),
      elevation: 32,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(16),
      ),
    );
  }


  // Song Name...
  Widget songName() {
    return Padding(
      padding: const EdgeInsets.only(top: 42),
      child: Text(
        currSong.song.title,
        style: TextStyle(fontSize: 32,
        fontWeight: FontWeight.bold),
      ),
    );
  }


  // Album Name...
  Widget albumArtistName() {
    return Column(
      children: <Widget>[
        Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text('Album:  ', style: TextStyle(color: Colors.black54),),
            Text(
              currSong.album.albumName,
              style: TextStyle(color: Colors.indigo),
            ),
          ],
        ),
        Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text('Artist:  ', style: TextStyle(color: Colors.black54),),
            Text(
              currSong.artist.name,
              style: TextStyle(color: Colors.indigo),
            ),
          ],
        )
      ],
    );
  }


  // Song Length indicator...
  Widget songLengthIndicator() {
    return Container(
      height: 4,
      margin: EdgeInsets.only(top: 40, left: 10, right: 10, bottom: 10),
      child: Row(
        children: <Widget>[
          Expanded(
            child: Text('0.0', style: TextStyle(), textAlign: TextAlign.start,),
          ),
          Expanded(
            child: Text(secToMin(currSong.song.length).toStringAsFixed(2), style: TextStyle(), textAlign: TextAlign.end,),
          )
        ],
      ),
    );
  }


  // Slider...
  Widget songSlider() {
    return Slider(
      value: seekValue,
      min: 0.0,
      activeColor: Colors.red[500],
      inactiveColor: Colors.red[100],
      max: 4.47,
      onChangeStart: (value) {},
      onChanged: (double value) { setState(() {seekValue = value;}); },
      onChangeEnd: (value) async {},
    );
  }


  /// Play/Pause Song..
  Widget playerStateButton() {
    return playerState == PlayerState.PLAYING || playerState == PlayerState.PAUSED 
    ?
    Expanded(child: IconButton(
      icon: playerState == PlayerState.PLAYING
      ?
      PlayControllerIcons().getPauseIcon() : PlayControllerIcons().getPlayIcon(),
      onPressed: () {
        switch (playerState) {
          case PlayerState.PLAYING:
            pause();
            break;
          case PlayerState.PAUSED:
            resume();
            break;
          default:
        }
      },
    ))
    :
    CircularProgressIndicator();
  }

  /// Change Song...
  Widget changeSongButton(Icon icon, String changeDirection) {
    return Expanded(child: IconButton(
      icon: icon,
      onPressed: () {
        switch (changeDirection.toLowerCase()) {
          case 'left':
            if (currentIndex != 0) {
              currentIndex -= 1;
              currSong = widget.allSongs[currentIndex];
              changeSong();
            }
            break;
          case 'right':
            if (currentIndex != widget.allSongs.length-1) {
              currentIndex += 1;
              currSong = widget.allSongs[currentIndex];
              changeSong();
            }
            break;
          default:
        }
      },
    ));
  }

  /// Change PlayerState...
  Widget playerModeButton(Icon icon,) {
    return Expanded(child: IconButton(
      icon: icon,
      onPressed: () {},
    ));
  }


  // Display Playlist Header...
  Widget displayPlaylistHeader() {
    
    return Container(
      
      height: 70,
      
      margin: EdgeInsets.only(left: 0,),
      
      child: Center(
        child: Text(

          'album'.toUpperCase(),
          style: TextStyle(
            fontSize: 30,
            fontFamily: 'Magnificent',
          ),
          textAlign: TextAlign.center,
          overflow: TextOverflow.fade,
        
        ),
      ),

      decoration: BoxDecoration(
        border: Border(top: BorderSide(color: Colors.black))
      ),
    
    );
  
  }


  // Display Playlist Name...
  Widget displayAlbumName() {

    return Container(
      
      height: 70,
      
      margin: EdgeInsets.only(left: 0,),
      
      child: Container(
        padding: EdgeInsets.only(top: 17, left: 20),
        child: Text(

          albumSongs.first.album.albumName,
          style: TextStyle(
            fontSize: 30,
            fontFamily: 'Magnificent',
          ),
          textAlign: TextAlign.start,
          overflow: TextOverflow.fade,

        ),
      ),

      color: Colors.indigo[200],
    
    );
  }


/// Main Widget...
  /// Currently Playing Part ...
  Widget currentSongDisplay(AudioPlayer audioPlayer) {

    return Center(
      // heightFactor: 0.8,
      child: Column(
        children: <Widget>[
          songDisplayCard(),
          songName(),

          albumArtistName(),

          songLengthIndicator(),
          songSlider(),
          
          Padding(
            padding: const EdgeInsets.only(top: 35),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                
                playerModeButton(PlayModeIcons().getShuffleIcon()),

                changeSongButton(PlayControllerIcons().getPrevIcon(), 'left'),
                
                /// switching between [play] and [pause] ...
                playerState == PlayerState.PAUSED
                ? 
                playerStateButton()
                :
                (
                  playerState == PlayerState.PLAYING
                  ? 
                  playerStateButton()
                  :
                  playerStateButton()
                ),

                changeSongButton(PlayControllerIcons().getNextIcon(), 'right'),
                playerModeButton(PlayModeIcons().getNoRepeat()),

              ],
            ),
          ),

        ],
      ),
    );

  }


  // Displaying Playlists Songs...
  Widget displayAlbumSongs() {

    return Container(
      color: Color.fromRGBO(190, 190, 190, 0.5),
      height: 300.0,
      child: ListView.builder(
          scrollDirection: Axis.vertical,
          itemCount: albumSongs.length,
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
                      albumSongs[index].song.title,
                      style: TextStyle(
                          color: Colors.redAccent,
                          fontFamily: 'Gothic',
                          fontStyle: FontStyle.italic,
                          fontWeight: FontWeight.w800),
                    ),
                    subtitle: Row(
                      children: <Widget>[
                        Text(
                          'Album: ' + currSong.album.albumName,
                          style: TextStyle(fontSize: 12.5),
                        ),
                        Text(
                          '      Duraton: ' + secToMin(albumSongs[index].song.length).toStringAsFixed(2) + ' mins',
                          style: TextStyle(
                            fontSize: 12.5,
                          ),
                        ),
                      ],
                    ),
                    // // PopUpMenu...
                    // trailing: new PopupMenuButton<String>(
                    //   child: Icon(Icons.playlist_add),
                    //   itemBuilder: (BuildContext context) {
                    //     return playlistNames.map((String playlistName) {
                    //       return new PopupMenuItem<String>(
                    //         child: Text(playlistName),
                    //         value: playlistName,
                    //       );
                    //     }).toList();
                    //   },
                    // ),
                    // onLongPress: () {
                    //   showDialog(
                    //       context: context,
                    //       barrierDismissible: false,
                    //       builder: (BuildContext context) {
                    //         return AlertDialog(
                    //           title: Text('Not Interested?'),
                    //           content: SingleChildScrollView(
                    //             child: ListBody(
                    //               children: <Widget>[
                    //                 Text('You don\'t want to see this song on your home screen?'),
                    //               ],
                    //             ),
                    //           ),
                    //           actions: <Widget>[
                    //             FlatButton(
                    //               child: Text('Remove'),
                    //               onPressed: () {
                    //                 debugPrint('Cancelled Operation!');
                    //                 Navigator.of(context).pop();
                    //               },
                    //             ),
                    //             FlatButton(
                    //               child: Text('Cancel'),
                    //               onPressed: () {
                    //                 debugPrint('Cancelled Operation!');
                    //                 Navigator.of(context).pop();
                    //               },
                    //             ),
                    //           ],
                    //         );
                    //       });

                    //   debugPrint('Pressed too long');
                    // },
                    onTap: () {
                      playerState = PlayerState.PLAYING;
                      currSong = albumSongs[index];
                      navigateToNowPlaying(context,);
                    },
                  ),
                ));
          }),
    );
  }

  double secToMin(double secs) => secs/60 ;

// Navigators------------------------------------------------------------------------------------------------------------------
  /// Navigation to [Now Playing] ...
  void navigateToNowPlaying(BuildContext context,) {
    Navigator.push(context, MaterialPageRoute(builder: (BuildContext context) => NowPlayingWidget(args: widget.args,)));
  }

}
