import 'package:flutter/material.dart';
import 'package:audioplayers/audioplayers.dart';

// Audio Player...
class AudioPlayerWidget extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    return AudioPlayerState();
  }
}

// Audio Player State...
class AudioPlayerState extends State<AudioPlayerWidget> {

  AudioPlayer audioPlayer = AudioPlayer();

  @override
  Widget build(BuildContext context) {
    return Container(
      child: RaisedButton(
        child: Icon(Icons.play_arrow),
        onPressed: () {
          play();
        },
      ),
    );
  }

  // Play Audio...
  play() async {
    await audioPlayer.play('./songs/Hymn_For_The_Weekend.mp3', isLocal: true);
  }
}
