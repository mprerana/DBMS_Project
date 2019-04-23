import 'package:flutter/material.dart';

import './home.dart';

// PopularSongs Widget...
class PopularSongsWidget extends StatefulWidget {
  
  @override
  State<StatefulWidget> createState() {
    return PopularSongsWidgetState();
  }

}

// PopularSongs Widget State...
class PopularSongsWidgetState extends State<PopularSongsWidget> {

  @override
  Widget build(BuildContext context) {

    return Container(
      child: ListView(
        scrollDirection: Axis.vertical,
        children: <Widget>[

          Container(
            margin: EdgeInsets.only(top: 30, bottom: 5),
            child: Text(
              'Top Releases',
              style: TextStyle(
                fontSize: 40,
                fontFamily: 'LUMOS',
                fontWeight: FontWeight.bold,
                color: Colors.white,
              ),
            ),
          ),
          TopRelease(),

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

}
