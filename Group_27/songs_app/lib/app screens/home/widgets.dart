import 'dart:io';
import 'package:flutter/material.dart';

import 'package:songs_app/app screens/home/home_screen_sub_widgets.dart';

// Home Screen Widgets...
class HomeScreenWidgets {

  // Side Drawer Widget...
  Widget sideDrawer(BuildContext context) {
    String userName = 'Vishwanth';
    return new Drawer(
      child: new Column(
        children: <Widget>[
          new UserAccountsDrawerHeader(
              accountName: new Text(userName), accountEmail: null),
          SideDrawerTiles().sideDrawerTiles(context),
        ],
      ),
    );
  }

  // App Bar Widget...
  Widget appBar(BuildContext context, TabController tabController, Color color) {
    return PreferredSize(
      preferredSize: Size.fromHeight(150),
      child: AppBarWidgets().appBar(context, tabController, color),
    );
  }

  // Avatar...
  Widget avatar(File f, String title, MaterialColor color) {
    return new Material(
      borderRadius: new BorderRadius.circular(20.0),
      elevation: 3.0,
      child: f != null
          ? new Image.file(
              f,
              fit: BoxFit.cover,
            )
          : new CircleAvatar(
              child: new Icon(
                Icons.play_arrow,
                color: Colors.white,
              ),
              backgroundColor: color,
            ),
    );
  }

}
