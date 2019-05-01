import 'package:songs_app/utils/database_files/tables.dart';

class Triggers {

  // trigger to update artist songs count on insert of a song in songs table
  static String triggerinsertSongOnArtist = 'CREATE TRIGGER ${SongsTable.tableName}_OnInsert_${ArtistTable.tableName} '+
                                            'AFTER INSERT ON ${SongsTable.tableName} '+
                                            'BEGIN '+
                                            'UPDATE ${ArtistTable.tableName} SET ${ArtistTable.colTotalSongs} = ${ArtistTable.colTotalSongs}+1 '+
                                            'WHERE ${ArtistTable.colArtistId} = (SELECT (${SongByTable.colArtistId}) FROM ${SongByTable.tableName} '+
                                            'WHERE ${SongByTable.colSongId} = new.${SongsTable.colSongId} ) ; '+
                                            'END';

  // trigger to update album songs count on insert of a song in songs table
  static String triggerinsertSongOnAlbum =  'CREATE TRIGGER ${SongsTable.tableName}_OnInsert_${AlbumsTable.tableName} '+
                                            'AFTER INSERT ON ${SongsTable.tableName} '+
                                            'BEGIN '+
                                            'UPDATE ${AlbumsTable.tableName} SET ${AlbumsTable.colTotalTracks} = ${AlbumsTable.colTotalTracks}+1 '+
                                            'WHERE ${AlbumsTable.colAlbumId} = (SELECT (${SongByTable.colAlbumId}) FROM ${SongByTable.tableName} '+
                                            'WHERE ${SongByTable.colSongId} = new.${SongsTable.colSongId} ) ; '+
                                            'END';

  // trigger to update album count in artist table on insert of a album in album table
  static String triggerinsertAlbumOnArtist =  'CREATE TRIGGER ${AlbumsTable.tableName}_OnInsert_${ArtistTable.tableName} '+
                                              'AFTER INSERT ON ${AlbumsTable.tableName} '+
                                              'BEGIN '+
                                              'UPDATE ${ArtistTable.tableName} SET ${ArtistTable.colTotalAlbums} = '+
                                              '${ArtistTable.colTotalAlbums} + 1 '+
                                              'WHERE ${ArtistTable.colArtistId} = (SELECT (${SongByTable.colArtistId}) '+
                                              'FROM ${SongByTable.tableName} '+
                                              'WHERE ${SongByTable.colAlbumId} = new.${AlbumsTable.colAlbumId}); '+
                                              'END';

}