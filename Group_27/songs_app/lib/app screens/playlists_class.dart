class PlaylistClass {

  String playlistName;
  int songId;
  List song;

  PlaylistClass(this.playlistName, this.songId, this.song);

  List fromPlaylisttoList(){
    return [playlistName, songId, song];
  }

}
