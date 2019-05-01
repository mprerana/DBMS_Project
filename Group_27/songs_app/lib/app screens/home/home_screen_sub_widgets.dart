import 'package:flutter/material.dart';
import 'package:animator/animator.dart';

import 'package:songs_app/services/authentication.dart';

import 'package:songs_app/app screens/titles.dart';


// Side Drawer Tiles...
class SideDrawerTiles {
  

  // Settings tile...
  ListTile settingsTile(BuildContext context) {

    return new ListTile(
      leading: new Icon(Icons.settings,
          color: Theme.of(context).accentColor),
      title: new Text("Settings"),
      onTap: () {
        debugPrint('No Settings available!!');
      }
    );

  }


  // Logout Tile...
  ListTile logoutTile(BuildContext context) {

    return new ListTile(
      leading: new Icon(Icons.account_circle,
          color: Theme.of(context).accentColor),
      title: new Text("LogOut"),
      onTap: () async {
        await BaseAuth().signOut();
        Navigator.of(context).pushNamedAndRemoveUntil(
            '/loginPage', (Route<dynamic> route) => false);
        // Navigator.popUntil(context, ModalRoute.withName('/loginPage'));
        debugPrint('Navigated to login page');
      }
    );

  }


  // Profile Tile...
  ListTile profileTile(BuildContext context) {
  
    return new ListTile(
      leading: new Icon(Icons.account_box,
          color: Theme.of(context).accentColor),
      title: new Text("Profile"),
      onTap: () {
        Navigator.of(context).pushNamed('/profilePage');
        debugPrint('Navigated to login page');
      }
    );
  
  }


  // PlaySong Tile...
  ListTile playSongTile(BuildContext context) {

    return new ListTile(
      leading: new Icon(Icons.play_circle_filled,
          color: Theme.of(context).accentColor),
      title: new Text("Play a song"),
      onTap: () {
        Navigator.of(context).pushNamed('/playAsong');
        debugPrint('Navigated to Plaing page');
      }
    );

  }

  // All Tiles of Side Drawer...
  Column sideDrawerTiles(BuildContext context) {
    return new Column(
      children: <Widget>[

        SideDrawerTiles().settingsTile(context),
        SideDrawerTiles().logoutTile(context),
        SideDrawerTiles().profileTile(context),
        SideDrawerTiles().playSongTile(context),

      ],
    );
  }

}


// App Bar Sub Widgets...
class AppBarWidgets {


  // Profile Widget...
  Container profile(BuildContext context) {

    return Container(
      margin: EdgeInsets.only(right: 10, top: 3),
      child: IconButton(
        iconSize: 40,
        icon: Icon(Icons.account_circle),
        onPressed: () {Navigator.pushNamed(context, '/profilePage');},
      ),
    );
  
  }


  // Tab Bar...
  TabBar tabBar(TabController tabController, Color color) {

    return TabBar(
      tabs: <Widget>[TabBarWidgets().tab1(), TabBarWidgets().tab2(), TabBarWidgets().tab3()],
      indicator: UnderlineTabIndicator(
        borderSide: BorderSide(color: color, width: 4.0),
        insets: EdgeInsets.fromLTRB(80, 20, 80, 0)
      ),
      unselectedLabelColor: Colors.grey,
      labelStyle: TextStyle(color: Colors.white, fontSize: 16),
      labelColor: Colors.white,
      unselectedLabelStyle: TextStyle(fontSize: 0),
      controller: tabController,
    );

  }

  
  // PreferredSize child...
  AppBar appBar(BuildContext context, TabController tabController, Color color) {
    return AppBar(
      backgroundColor: Colors.transparent,
      elevation: 0,
      centerTitle: true,
      title: appTitle(),
      actions: <Widget>[profile(context)],
      bottom: tabBar(tabController, color),
    );
  }

}


// Tab Bar Widgets...
class TabBarWidgets {

  // Tab1...
  Tab tab1() {
    return Tab(
      icon: Icon(
        Icons.library_music,
        color: Colors.white,
      ),
      child: Animator(
        tween: Tween<Offset>(begin: Offset(0, 0), end: Offset(0, -5)),
        duration: Duration(milliseconds: 1000),
        statusListener: (status, setup) {
          if (status == AnimationStatus.completed) {
            setup.controller.stop();
          }
        },
        builder: (anim) => Transform.translate(
              offset: anim.value,
              child: Text(
                'Popular Songs',
                style: TextStyle(fontWeight: FontWeight.bold),
              ),
            ),
      )
    );
  }


  // Tab2...
  Tab tab2() {
    return Tab(
      icon: Icon(
        Icons.music_note,
        color: Colors.white,
      ),
      child: Animator(
        tween: Tween<Offset>(begin: Offset(0, 0), end: Offset(0, -5)),
        duration: Duration(milliseconds: 1000),
        statusListener: (status, setup) {
          if (status == AnimationStatus.completed) {
            setup.controller.stop();
          }
        },
        builder: (anim) => Transform.translate(
              offset: anim.value,
              child: Text(
                'Now PLaying',
                style: TextStyle(fontWeight: FontWeight.bold),
              ),
            ),
      )
    );
  }


  // Tab3...
  Tab tab3() {
    return Tab(
      icon: Icon(
        Icons.queue_music,
        color: Colors.white,
      ),
      child: Animator(
        tween: Tween<Offset>(begin: Offset(0, 0), end: Offset(0, -5)),
        duration: Duration(milliseconds: 1000),
        statusListener: (status, setup) {
          if (status == AnimationStatus.completed) {
            setup.controller.stop();
          }
        },
        builder: (anim) => Transform.translate(
              offset: anim.value,
              child: Text(
                'Playlists',
                style: TextStyle(fontWeight: FontWeight.bold),
              ),
            ),
      )
    );
  }

}
