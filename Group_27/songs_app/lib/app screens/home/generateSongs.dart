import 'package:songs_app/models/songs.dart';
import 'package:songs_app/app screens/playlists_class.dart';

// External Functions...
List<List> createSongs() {
  List<List> playlistSongs = List<List>();
  
  playlistSongs.add(Song.withID('1','You Belong With Me', 3.4,'assets/songs/song-bg-1.jpg' ,'dummy loc' , '01', 'Dua Lipa').fromSongtoList());
  playlistSongs.add(Song.withID('2','We don\'t talk anymore', 4.4, 'assets/songs/song-bg-1.jpg','dummy loc' , '01', 'Dua Lipa').fromSongtoList());
  playlistSongs.add(Song.withID('3','You Belong With Me', 5.4, 'assets/songs/song-bg-1.jpg','dummy loc' , '01', 'Dua Lipa').fromSongtoList());
  playlistSongs.add(Song.withID('4','You Belong With Me', 3.4, 'assets/songs/song-bg-1.jpg','dummy loc' , '01', 'Dua Lipa').fromSongtoList());
  playlistSongs.add(Song.withID('5','You Belong With Me', 3.4, 'assets/songs/song-bg-1.jpg','dummy loc' , '01', 'Dua Lipa').fromSongtoList());
  
  return playlistSongs;
}

// Populate Playlists...
List<List> populatePlaylists() {
  List<List> playlists = List<List>();
  
  playlists.add(PlaylistClass('playlist01', 01, createSongs()).fromPlaylisttoList());
  playlists.add(PlaylistClass('playlist02', 02, createSongs()).fromPlaylisttoList());
  playlists.add(PlaylistClass('playlist03', 03, createSongs()).fromPlaylisttoList());
  playlists.add(PlaylistClass('playlist03', 03, createSongs()).fromPlaylisttoList());

  return playlists;
}