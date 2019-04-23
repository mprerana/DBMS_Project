import 'package:flutter/material.dart';

// Variables...
bool shuffleOn = false;

// Currently Playing Part...
Widget firstWidget(Map<String, dynamic> args) {
  
  return Center(
    child: Column(
      children: <Widget>[
        Card(
          clipBehavior: Clip.antiAliasWithSaveLayer,
          margin: EdgeInsets.only(top: args['topPadding']),
          child: Container(
            height: 300,
            width: 300,
            decoration: BoxDecoration(
                image: DecorationImage(
                    image: AssetImage(args['artistImage']),
                    fit: BoxFit.cover)),
          ),
          elevation: 32,
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(16),
          ),
        ),
        Padding(
          padding: const EdgeInsets.only(top: 42),
          child: Text(
            args['songName'],
            style: TextStyle(fontSize: 32,
            fontWeight: FontWeight.bold),
          ),
        ),
        Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text('Album: ', style: TextStyle(color: Colors.black54),),
            Text(
              args['albumName'],
              style: TextStyle(color: Colors.indigo),
            ),
          ],
        ),
        Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text('Artist: ', style: TextStyle(color: Colors.black54),),
            Text(
              args['artistName'],
              style: TextStyle(color: Colors.indigo),
            ),
          ],
        ),
        Container(
          height: 4,
          margin: EdgeInsets.only(top: 40, left: 10, right: 10),
          child: Row(
            children: <Widget>[
              Expanded(
                child: Text('0.0', style: TextStyle(), textAlign: TextAlign.start,),
              ),
              Expanded(
                child: Text(args['songLength'], style: TextStyle(), textAlign: TextAlign.end,),
              )
            ],
          ),
        ),
        Container(
          margin: EdgeInsets.only(top: 20),
          width: 400,
          height: 2,
          decoration: BoxDecoration(
            color: Colors.blueGrey
          ),
          child: Container(
            margin: EdgeInsets.only(right: double.infinity, left: 0),
            child: IconButton(
              padding: EdgeInsets.only(top: 0),
              icon: Icon(Icons.album, color: Colors.blueGrey, size: 15,),
              onPressed: () {debugPrint('pressed');},
            ),
          ),
        ),
        Padding(
          padding: const EdgeInsets.only(top: 50),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              Expanded(child: IconButton(
                icon: Icon(Icons.shuffle, color: shuffleOn ? Colors.black : Colors.grey,),
                onPressed: () {
                  switch (shuffleOn) {
                    case true:
                      shuffleOn = false;
                      break;
                    case false:
                      shuffleOn = true;
                      break;
                    default:
                  }
                },
              )),
              Expanded(child: IconButton(
                icon: Icon(Icons.skip_previous),
                onPressed: () {},
              )),
              Expanded(
                child: Center(
                  child: IconButton(
                    padding: EdgeInsets.only(left: 0, bottom: 30),
                    icon: Icon(
                      Icons.play_circle_outline,
                      color: Colors.black,
                      size: 54,
                    ),
                    onPressed: () {},
                  ),
                ),
              ),
              Expanded(child: IconButton(
                icon: Icon(Icons.skip_next),
                onPressed: () {},
              )),
              Expanded(child: IconButton(
                icon: Icon(Icons.repeat, color: Colors.grey,),
                onPressed: () {},
              )),
            ],
          ),
        ),

      ],
    ),
  );
}
