import 'package:flutter/material.dart';

// Play Controller Icons...
class PlayControllerIcons {

  // Icons Size...
  double size = 30;

  Icon getPrevIcon() {
    return Icon(Icons.skip_previous, size: size,);
  }

  Icon getPlayIcon() {
    return Icon(Icons.play_circle_outline, size: size,);
  }

  Icon getPauseIcon() {
    return Icon(Icons.pause_circle_outline, size: size,);
  }

  Icon getNextIcon() {
    return Icon(Icons.skip_next, size: size,);
  }

  Icon getAddPlaylistIcon() {
    return Icon(Icons.playlist_add, color: Colors.brown[500], size: size,);
  }

  Icon getLoadingIcon() {
    return Icon(Icons.play_circle_filled);
  } 

}

// Play Mode Icons...
class PlayModeIcons {

  // Icons Size...
  double size = 30;

  Icon getShuffleIcon() {
    return Icon(Icons.shuffle, size: size, color: Colors.brown[500]);
  }

  Icon getRepeatIcon() {
    return Icon(Icons.repeat, size: size, color: Colors.brown[500]);
  }

  Icon getRepeatOneIcon() {
    return Icon(Icons.repeat_one, size: size, color: Colors.brown[500]);
  }

  Icon getNoRepeat() {
    return Icon(Icons.not_interested, size: size, color: Colors.brown[500]);
  }

}
