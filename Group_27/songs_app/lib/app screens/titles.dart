import 'package:flutter/material.dart';

// Titles...

// main app Title...
Text appTitle() {
  
  return Text(
    "BLYNK",
    style: TextStyle(
      fontFamily: 'Halfomania',
      color: Colors.white,
      fontSize: 85,
    ),
  );

}

// srted Songs Titles...
Container sortedSongsTitles(String title) {

  return Container(
    margin: EdgeInsets.only(top: 30, bottom: 5),
    child: Text(
      title,
      style: TextStyle(
        fontSize: 40,
        fontFamily: 'LUMOS',
        fontWeight: FontWeight.bold,
        color: Colors.white,
      ),
    ),
  );

}
