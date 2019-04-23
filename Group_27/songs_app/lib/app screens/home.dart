import 'package:flutter/material.dart';
import 'package:animator/animator.dart';

import 'package:songs_app/app screens/playlists_class.dart';
import 'package:songs_app/models/songs.dart';
import 'package:songs_app/services/authentication.dart';

import 'package:songs_app/app screens/now_playing.dart';
import 'package:songs_app/app screens/profile.dart';
import 'package:songs_app/app screens/popular_songs.dart';
import 'package:songs_app/app screens/playlists.dart';

// Home Widget...
class Home extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    return HomeState();
  }
}

class HomeState extends State<Home> with SingleTickerProviderStateMixin<Home>{

  TabController tabController;
  MaterialColor color = Colors.teal;
  bool firstIndex = true, secondIndex, thirdIndex;
  @override
  void initState() {
    super.initState();
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

  @override
  void dispose() {
    super.dispose();
    tabController.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: 3,
      child: Stack(
        children: <Widget>[
          Container(
            child: Image.asset('assets/msc-bg-3.jpg', fit: BoxFit.cover, width: double.infinity, height: 250,),
          ),
          Scaffold(
            drawer: SideDrawer(),
            backgroundColor: Colors.transparent,
            
            appBar: PreferredSize(
              preferredSize: Size.fromHeight(150),
              child: AppBar(
                backgroundColor: Colors.transparent,
                elevation: 0,
                centerTitle: true,
                title: Text("BLYNK",
                  style: TextStyle(
                      fontFamily: 'Halfomania-Regular',
                      color: Colors.white,
                      fontSize: 85,
                  ),
                ),

                actions: <Widget>[

                  Container(
                    margin: EdgeInsets.only(right: 10, top: 3),
                    child: IconButton(
                      iconSize: 40,
                      icon: Icon(Icons.account_circle),
                      onPressed: () {
                        Navigator.push(context, MaterialPageRoute(builder: (BuildContext context) => Profile()));
                      },
                    ),
                  ),

                ],

                bottom: TabBar(tabs: <Widget>[
                  Tab(icon: Icon(Icons.library_music, color: Colors.white,), child: Animator(
                    tween: Tween<Offset>(begin: Offset(0, 0), end: Offset(0, -5)),
                    duration: Duration(milliseconds: 1000),
                    statusListener: (status, setup) {
                      if(status == AnimationStatus.completed) {
                        setup.controller.stop();
                      }
                    },
                    builder: (anim) => Transform.translate(
                      offset: anim.value,
                      child: Text('Popular Songs', style: TextStyle(fontWeight: FontWeight.bold),),
                    ),
                  )),
                  Tab(icon: Icon(Icons.music_note, color: Colors.white,), child: Animator(
                    tween: Tween<Offset>(begin: Offset(0, 0), end: Offset(0, -5)),
                    duration: Duration(milliseconds: 1000),
                    statusListener: (status, setup) {
                      if(status == AnimationStatus.completed) {
                        setup.controller.stop();
                      }
                    },
                    builder: (anim) => Transform.translate(
                      offset: anim.value,
                      child: Text('Now PLaying', style: TextStyle(fontWeight: FontWeight.bold),),
                    ),
                  )),
                  Tab(icon: Icon(Icons.queue_music, color: Colors.white,), child: Animator(
                    tween: Tween<Offset>(begin: Offset(0, 0), end: Offset(0, -5)),
                    duration: Duration(milliseconds: 1000),
                    statusListener: (status, setup) {
                      if(status == AnimationStatus.completed) {
                        setup.controller.stop();
                      }
                    },
                    builder: (anim) => Transform.translate(
                      offset: anim.value,
                      child: Text('Playlists', style: TextStyle(fontWeight: FontWeight.bold),),
                    ),
                  )),
                  //Tab(icon: Icon(Icons.repeat, color: Colors.white,), text: 'Adopt',),
                ],
                  indicator: UnderlineTabIndicator(
                      borderSide: BorderSide(color: color, width: 4.0),
                      insets: EdgeInsets.fromLTRB(80, 20, 80, 0)
                  ),
                  unselectedLabelColor: Colors.grey,
                  labelStyle: TextStyle(color: Colors.white, fontSize: 16),
                  labelColor: Colors.white,
                  unselectedLabelStyle: TextStyle(fontSize: 0),
                  controller: tabController,
                ),
              ),
            ),
            body: TabBarView(children: <Widget>[
              PopularSongsWidget(),
              currSong.length == 0
              ?
                Center(
                  child: Text('Play any song.', style: TextStyle(color: Colors.white, fontSize: 30, fontFamily: 'Magnificent'),),
                )
              :
                NowPlayingWidget(
                  appBarOn: false,
                  topPadding: 50,
                  songName: currSong[0],
                  artistName: currSong[3].toString(),
                  albumName: currSong[2].toString(),
                  artistImage: 'assets/artists/duaLipa.jpg',
                  songLength: currSong[1],
                  playlists: playlists,
                  playlist: playlist,
                ),
              PlaylistWidget(),
            ],
              controller: tabController,
            ),
          ),
        ],
      ),
    );
  }
}

// ---------------------------------------------------------------------------------------------------------------
// ---------------------------------------------------------------------------------------------------------------
// Widgets...

// Side Drawer...
class SideDrawer extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return new Drawer(
      child: new Column(
        children: <Widget>[
          new UserAccountsDrawerHeader(
              accountName: new Text("Music player"), accountEmail: null),
          new Column(
            children: <Widget>[
              new ListTile(
                  leading: new Icon(Icons.settings,
                      color: Theme.of(context).accentColor),
                  title: new Text("Settings"),
                  onTap: () {
                    debugPrint('No Settings available!!');
                  }),
              new ListTile(
                  leading: new Icon(Icons.account_circle,
                      color: Theme.of(context).accentColor),
                  title: new Text("LogOut"),
                  onTap: () async {
                    await BaseAuth().signOut();
                    Navigator.of(context).pushNamedAndRemoveUntil(
                        '/loginPage', (Route<dynamic> route) => false);
                    // Navigator.popUntil(context, ModalRoute.withName('/loginPage'));
                    debugPrint('Navigated to login page');
                  }),
              new ListTile(
                  leading: new Icon(Icons.account_box,
                      color: Theme.of(context).accentColor),
                  title: new Text("Profile"),
                  onTap: () {
                    Navigator.of(context).pushNamed('/profilePage');
                    debugPrint('Navigated to login page');
                  }),
              new ListTile(
                  leading: new Icon(Icons.play_circle_filled,
                      color: Theme.of(context).accentColor),
                  title: new Text("Play a song"),
                  onTap: () {
                    Navigator.of(context).pushNamed('/playAsong');
                    debugPrint('Navigated to Plaing page');
                  }),
            ],
          )
        ],
      ),
    );
  }
}

// int _currentIndex = 1;

// Bottom Navigation Bar...
// class BottomNavigator extends StatelessWidget {
//   @override
//   Widget build(BuildContext context) {
//     return new BottomNavigationBar(
//       currentIndex: _currentIndex,
//       items: [
//         BottomNavigationBarItem(
//           icon: IconButton(
//             icon: Icon(Icons.home),
//             onPressed: () {
//               _currentIndex = 0;
//               Navigator.popUntil(context, ModalRoute.withName('/homePage'));
//             },
//           ),
//           title: Text('Home'),
//         ),
//         BottomNavigationBarItem(
//           icon: FlatButton(
//             child: Row(
//               children: <Widget>[
//                 Text('    '),
//                 Icon(
//                   Icons.play_arrow,
//                   size: 35,
//                 ),
//                 Icon(
//                   Icons.pause,
//                   size: 35,
//                 ),
//                 Text('    '),
//               ],
//             ),
//             onPressed: () {
//               debugPrint('Cannot play this song');
//             },
//           ),
//           title: Text(
//             '',
//             style: TextStyle(fontSize: 0),
//           ),
//         ),
//         BottomNavigationBarItem(
//             icon: IconButton(
//               icon: Icon(Icons.account_circle),
//               onPressed: () {
//                 _currentIndex = 2;
//                 Navigator.of(context).pushNamed('/profilePage');
//                 debugPrint('No Profile');
//               },
//             ),
//             title: Text('Profile'))
//       ],
//     );
//   }
// }

// Songs List Header...
class Headers extends StatelessWidget {
  Headers(this._header);

  final String _header;

  @override
  Widget build(BuildContext context) {
    return Card(
      margin: EdgeInsets.only(left: 0, right: 0, top: 0, bottom: 0),
      child: ListTile(
        leading: Text(
          _header,
          style: TextStyle(
              fontSize: 20, fontFamily: 'LUMOS', fontWeight: FontWeight.w800),
        ),
      ),
    );
  }
}

// Current Playing Song...
List currSong = List();

// Recently Played Songs...
class RecentlyPlayed extends StatelessWidget {
  final List<List> songs = createPlaylist();

  @override
  Widget build(BuildContext context) {
    return Container(
      height: 140,
      child: ListView.builder(
        scrollDirection: Axis.horizontal,
        itemCount: songs.length,
        itemBuilder: (BuildContext context, int index) {
          String songName = '';
          for (var i = 0; i < 16; i++) {
            songName += songs[index][0][i];
          }
          songName += '...';
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
                            debugPrint('Cannot Play this playlist!');
                            currSong.clear();
                            currSong = songs[index].toList();
                            playlist = PlaylistClass('Random', playlists.length, createPlaylist()).fromPlaylisttoList();
                            navigateToNowPlaying(context, currSong, playlist);
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
}

// Playlists...
class Playlist extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    List<List> playlists = List<List>();
    playlists.add(
        PlaylistClass('playlist01', 01, createPlaylist()).fromPlaylisttoList());
    playlists.add(
        PlaylistClass('playlist02', 02, createPlaylist()).fromPlaylisttoList());
    playlists.add(
        PlaylistClass('playlist03', 03, createPlaylist()).fromPlaylisttoList());
    playlists.add(
        PlaylistClass('playlist03', 03, createPlaylist()).fromPlaylisttoList());

    return Container(
      height: 140,
      child: ListView.builder(
        scrollDirection: Axis.horizontal,
        itemCount: playlists.length,
        itemBuilder: (BuildContext context, int index) {
          List song = playlists[index][2][0];
          String songName = '';
          for (var i = 0; i < 16; i++) {
            songName += playlists[index][2][0][0][i];
          }
          songName += '...';
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
                            currSong.clear();
                            currSong = song.toList();
                            navigateToNowPlaying(context, currSong, playlists[index]);
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
}

// Create Playlist Widget...
class CreatePlaylist extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Container(
      height: 50,
      width: 100,
      child: Card(
        child: IconButton(
          icon: Icon(Icons.playlist_add),
          onPressed: () {
            debugPrint('Cannot create playlist');
          },
          tooltip: 'Create Playlist',
        ),
      ),
    );
  }
}

List<List> playlists = List<List>();
List playlist =List();

// Top Release Widget...
class TopRelease extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final List<List> songs = createPlaylist();

    List<List> playlists = List<List>();
    playlists.add(PlaylistClass('playlist01', playlists.length, createPlaylist())
        .fromPlaylisttoList());
    playlists.add(PlaylistClass('playlist02', playlists.length, createPlaylist())
        .fromPlaylisttoList());
    playlists.add(PlaylistClass('playlist03', playlists.length, createPlaylist())
        .fromPlaylisttoList());
      
    List<String> playlistNames = List<String>();
      for (var i = 0; i < playlists.length; i++) {
        playlistNames.add(playlists[i][0]);
    }

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
                          '      Duraton: ' +
                              songs[index][1].toString() +
                              ' mins',
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
                      playlist = PlaylistClass('Random', playlists.length, createPlaylist()).fromPlaylisttoList();
                      navigateToNowPlaying(context, currSong, playlist);
                    },
                  ),
                ));
          }),
    );
  }
}

// Navigation to Now Playing...
void navigateToNowPlaying(BuildContext context, List song, List playlist) {
  Navigator.push(context, MaterialPageRoute(builder: (BuildContext context) => NowPlayingWidget(
                                                                                songName: song[0],
                                                                                artistName: song[3].toString(),
                                                                                albumName: song[2].toString(),
                                                                                songLength: song[1],
                                                                                playlists: playlists,
                                                                                playlist: playlist,
                                                                                // artistImage: 'assets/msc-bg-2.jpg',
                                                                              )
  ));
}

// External Functions...
List createPlaylist() {
  List<List> playlistSongs = List<List>();
  playlistSongs
      .add(Song.withID('1','You Belong With Me', 3.4,'dummy loc' , '01', '01', '01').fromSongtoList());
  playlistSongs
      .add(Song.withID('2','We don\'t talk anymore', 4.4,'dummy loc' , '01', '01', '01').fromSongtoList());
  playlistSongs
      .add(Song.withID('3','You Belong With Me', 5.4,'dummy loc' , '01', '01', '01').fromSongtoList());
  playlistSongs
      .add(Song.withID('4','You Belong With Me', 3.4,'dummy loc' , '01', '01', '01').fromSongtoList());
  playlistSongs
      .add(Song.withID('5','You Belong With Me', 3.4,'dummy loc' , '01', '01', '01').fromSongtoList());
  return playlistSongs;
}
