import 'package:flutter/material.dart';
import 'package:scoped_model/scoped_model.dart';
import 'package:flutter_staggered_grid_view/flutter_staggered_grid_view.dart';

import '../scoped_models/main.dart';
import '../models/news.dart';

import '../widgets/logout.dart';
import '../widgets/newscard.dart';
import '../widgets/myitems.dart';

class HomePage extends StatefulWidget {
  final MainModel model;

  HomePage(this.model);

  @override
  State<StatefulWidget> createState() {
    return _HomePageState();
  }
}

Widget drawer() {
  return Drawer(
    child: Column(
      children: <Widget>[
        AppBar(
          automaticallyImplyLeading: false,
          title: Text('choose'),
        ),
        Divider(),
        LogoutListTile(),
      ],
    ),
  );
}



class _HomePageState extends State<HomePage> {

  @override
  void initState() {
    widget.model.getAddress();
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      drawer: drawer(),
      appBar: AppBar(
        title: Text(
          'Home',
          style: TextStyle(
            color: Colors.white,
          ),
        ),
      ),
      body: StaggeredGridView.count(
              //home page
              crossAxisCount: 2,
              crossAxisSpacing: 12.0,
              mainAxisSpacing: 12.0,
              padding: EdgeInsets.symmetric(horizontal: 16.0, vertical: 8.0),
              children: <Widget>[
                myItems(Icons.weekend, 'Welcome ${widget.model.authenticatedUser.username}!!', 0xffed622b),
                myItems(Icons.new_releases, 'news', 0xff26cb3c, '/news'),
                myItems(Icons.pie_chart_outlined, 'analysis', 0xffff3266, '/analysis'),
                myItems(Icons.lightbulb_outline, 'Events', 0xff3399fe, '/events'),
              ],
              staggeredTiles: [
                StaggeredTile.extent(2, 130.0),
                StaggeredTile.extent(1, 150.0),
                StaggeredTile.extent(1, 150.0),
                StaggeredTile.extent(2, 230.0),
              ],
            ),
    );
  }
}

