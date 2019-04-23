import 'package:songs_app/utils/database_files/tables.dart';

class Views {

  // view to get recent ablbums
  static String getRecentReleases = 'CREATE VIEW getRecentSongs AS '+
                                    'SELECT (${AlbumsTable.colAlbumId}, '+
                                    '${AlbumsTable.colAlbumName}, ${AlbumsTable.colImageId}) '+
                                    'FROM ${AlbumsTable.tableName} ORDER BY ${AlbumsTable.colReleaseDate} DESC LIMIT 10';

  static String getTopArtist =  'CREATE VIEW getTopArtist AS '+
                                'SELECT (${ArtistTable.colArtistId}, '+
                                '${ArtistTable.colName},${ArtistTable.colImageId}) '+
                                'FROM ${ArtistTable.tableName} ORDER BY ${ArtistTable.colTotalSongs} DESC LIMIT 10';

  static String getRomantic =   'CREATE VIEW getRomantic AS '+
                                'SELECT (${SongsTable.colSongId}, ${SongsTable.colTitle}, ${SongsTable.colImageId}) '+
                                'FROM ${SongsTable.tableName} WHERE ${SongsTable.colGenreId} ='+
                                ' (SELECT (${GenreTable.colGenreId}) '+
                                ' FROM ${GenreTable.tableName} WHERE ${GenreTable.colName} = \'Romantic\' ) LIMIT 10';

  static String getMelody = 'CREATE VIEW getMelody AS '+
                                'SELECT (${SongsTable.colSongId}, ${SongsTable.colTitle}, ${SongsTable.colImageId}) '+
                                'FROM ${SongsTable.tableName} WHERE ${SongsTable.colGenreId} ='+
                                ' (SELECT (${GenreTable.colGenreId}) '+
                                ' FROM ${GenreTable.tableName} WHERE ${GenreTable.colName} = \'Melody\' ) '+
                                ' ORDER BY ${SongsTable.colSongId} DESC LIMIT 10';

  static String getReligious = 'CREATE VIEW getReligious AS '+
                                'SELECT (${SongsTable.colSongId}, ${SongsTable.colTitle}, ${SongsTable.colImageId}) '+
                                'FROM ${SongsTable.tableName} WHERE ${SongsTable.colGenreId} ='+
                                ' (SELECT (${GenreTable.colGenreId}) '+
                                ' FROM ${GenreTable.tableName} WHERE ${GenreTable.colName} = \'Religios\' ) '+
                                'ORDER BY ${SongsTable.colSongId} DESC LIMIT 10';

  static String getEDM = 'CREATE VIEW getEDM AS '+
                                'SELECT (${SongsTable.colSongId}, ${SongsTable.colTitle}, ${SongsTable.colImageId}) '+
                                'FROM ${SongsTable.tableName} WHERE ${SongsTable.colGenreId} ='+
                                ' (SELECT (${GenreTable.colGenreId}) '+
                                ' FROM ${GenreTable.tableName} WHERE ${GenreTable.colName} = \'EDM\' )'+
                                ' ORDER BY ${SongsTable.colSongId} DESC LIMIT 10';

  static String getKPOP = 'CREATE VIEW getKPOP AS '+
                                'SELECT (${SongsTable.colSongId}, ${SongsTable.colTitle}, ${SongsTable.colImageId}) '+
                                'FROM ${SongsTable.tableName} WHERE ${SongsTable.colGenreId} ='+
                                ' (SELECT (${GenreTable.colGenreId}) '+
                                ' FROM ${GenreTable.tableName} WHERE ${GenreTable.colName} = \'KPOP\' )'+
                                ' ORDER BY ${SongsTable.colSongId} DESC LIMIT 10';

  static String getRock = 'CREATE VIEW getRock AS '+
                                'SELECT (${SongsTable.colSongId}, ${SongsTable.colTitle}, ${SongsTable.colImageId}) '+
                                'FROM ${SongsTable.tableName} WHERE ${SongsTable.colGenreId} ='+
                                ' (SELECT (${GenreTable.colGenreId}) '+
                                ' FROM ${GenreTable.tableName} WHERE ${GenreTable.colName} = \'Rock\' )'+
                                ' ORDER BY ${SongsTable.colSongId} DESC LIMIT 10';

  static String getOldIsGold = 'CREATE VIEW getOldIsGold AS '+
                                'SELECT (${SongsTable.colSongId}, ${SongsTable.colTitle}, ${SongsTable.colImageId}) '+
                                'FROM ${SongsTable.tableName} WHERE ${SongsTable.colGenreId} ='+
                                ' (SELECT (${GenreTable.colGenreId}) '+
                                ' FROM ${GenreTable.tableName} WHERE ${GenreTable.colName} = \'Old is Gold\' )'+
                                ' ORDER BY ${SongsTable.colSongId} DESC LIMIT 10';

}