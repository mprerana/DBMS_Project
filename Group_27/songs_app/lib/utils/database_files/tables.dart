class UsersTable {

  static String tableName = 'Users';
  
  // column names
  static String colUserId = 'userId';
  static String colFirstName = 'firstName';
  static String colLastName = 'lastName';
  static String colEmail = 'email';
  static String colGender = 'gender';
  static String colDOB = 'dateOfBirth';
  static String colLastLogin = 'lastLogin';
  static String colActiveStatus = 'activeStatus';
  
  // create table command
  static String createTable = 'CREATE TABLE $tableName($colUserId TEXT PRIMARY KEY,' +
                      ' $colFirstName TEXT NOT NULL, $colLastName TEXT NOT NULL, ' + 
                      ' $colEmail TEXT NOT NULL UNIQUE, $colGender TEXT NOT NULL, $colDOB TEXT NOT NULL, ' + 
                      '$colLastLogin TEXT NULL, $colActiveStatus TEXT NULL)';

  // indexing for this table
  static String indexSQL = 'CREATE UNIQUE INDEX ${colEmail}_$tableName ON $tableName ($colEmail)';

}

class GenreTable {

  static String tableName = 'Genre';

  // column names
  static String colGenreId = 'genreId';
  static String colName = 'name';

  // create table command
  static String createTable = 'CREATE TABLE $tableName($colGenreId TEXT PRIMARY KEY, ' + 
                              '$colName TEXT NOT NULL UNIQUE)';

  // indexing for this table
  static String indexSQL = 'CREATE INDEX ${colName}_$tableName ON $tableName ($colName)';

}

class PlaylistTable {

  static String tableName = 'Playlists';

  // column names
  static String colPlaylistId = 'playlistId';
  static String colUserId = 'userId';
  static String colName = 'name';

  // create table command
  static String createTable = 'CREATE TABLE $tableName($colPlaylistId TEXT PRIMARY KEY, ' + 
                              '$colUserId TEXT NOT NULL, $colName VARCHAR(30), ' +  
                              'CONSTRAINT FK_${UsersTable.tableName} FOREIGN KEY ($colUserId) '+
                              'REFERENCES ${UsersTable.tableName}(${UsersTable.colUserId}))';

  // indexing for this table
  static String indexSQL = 'CREATE INDEX ${colName}_$tableName ON $tableName ($colName)';

}

class Imagestable {

  static String tableName = 'Images';

  // column names
  static String colImageId = 'imageId';
  static String colImgLocation = 'imgLocation';
  static String colName = 'name';

  // create table command
  static String createTable = 'CREATE TABLE $tableName($colImageId TEXT PRIMARY KEY, '+
                              '$colImgLocation VARCHAR(300) NOT NULL UNIQUE, $colName VARCHAR(150) NOT NULL UNIQUE'+
                              ')';

  // indexing for this table
  // static String indexSQL = 'CREATE INDEX ${}_${} ON $tableName ($)';

}

class AlbumsTable {

  static String tableName = 'Albums';

  // column names
  static String colAlbumId = 'albumId';
  static String colAlbumName = 'albumName';
  static String colReleaseDate = 'releaseDate';
  static String colAlbumLength = 'albumLength';
  static String colTotalTracks = 'totalTracks';
  static String colGenreId = 'genreId';
  static String colImageId = 'imageId';

  // create table command
  static String createTable = 'CREATE TABLE $tableName($colAlbumId TEXT PRIMARY KEY, '+
                              '$colAlbumName VARCHAR(200) NOT NULL, '+
                              '$colReleaseDate TEXT NOT NULL,'+
                              '$colAlbumLength REAL DEFAULT 0 NOT NULL,'+
                              '$colTotalTracks INT DEFAULT 0 NOT NULL, '+
                              '$colGenreId TEXT NOT NULL,'+
                              '$colImageId TEXT NOT NULL,'+
                              'CONSTRAINT FK_${GenreTable.tableName} FOREIGN KEY ($colGenreId) '+
                              'REFERENCES ${GenreTable.tableName}(${GenreTable.colGenreId}))'; 

  // indexing for this table
  static String indexSQL = 'CREATE INDEX ${colAlbumName}_$tableName ON $tableName ($colAlbumName)';

}

class ArtistTable {

  static String tableName = 'Artists';

  // column names
  static String colArtistId = 'artistId';
  static String colName = 'name';
  static String colTotalSongs = 'totalSongs';
  static String colTotalAlbums = 'totalAlbums';
  static String colImageId = 'imageId';

  //create table command
  static String createTable = 'CREATE TABLE $tableName($colArtistId TEXT PRIMARY KEY, '+
                              '$colName VARCHAR(100) NOT NULL, '+
                              '$colTotalSongs INT DEFAULT 0 NOT NULL, '+
                              '$colTotalAlbums INT DEFAULT 0 NOT NULL, '+
                              '$colImageId TEXT NOT NULL, '+
                              'CONSTRAINT FK_${Imagestable.tableName} FOREIGN KEY ($colImageId) '+
                              'REFERENCES ${Imagestable.tableName}(${Imagestable.colImageId}))';

  // indexing for this table
  static String indexSQL = 'CREATE INDEX ${colName}_$tableName ON $tableName ($colName)';

}

class SongsTable {

  static String tableName = 'Songs';

  // column names
  static String colSongId = 'songId';
  static String colTitle = 'title';
  static String colLength = 'length';
  static String colLocation = 'location';
  static String colAlbumId = 'albumId';
  static String colGenreId = 'genreId';
  static String colImageId = 'imageId';

  // create table command
  static String createTable = 'CREATE TABLE $tableName($colSongId TEXT PRIMARY KEY, '+
                              '$colTitle VARCHAR(300) NOT NULL, '+
                              '$colLength REAL DEFAULT 0 NOT NULL, '+
                              '$colLocation TEXT NOT NULL, '+
                              '$colAlbumId TEXT NOT NULL, '+
                              '$colGenreId TEXT NOT NULL, '+
                              '$colImageId TEXT NOT NULL, '+
                              'CONSTRAINT FK_${AlbumsTable.tableName} FOREIGN KEY ($colAlbumId) '+
                              'REFERENCES ${AlbumsTable.tableName}(${AlbumsTable.colAlbumId}), '+
                              'CONSTRAINT FK_${GenreTable.tableName} FOREIGN KEY ($colGenreId) '+
                              'REFERENCES ${GenreTable.tableName}(${GenreTable.colGenreId}), '+
                              'CONSTRAINT FK_${Imagestable.tableName} FOREIGN KEY ($colImageId) '+
                              'REFERENCES ${Imagestable.tableName}(${Imagestable.colImageId}))';

  // indexing for this table
  static String indexSQL = 'CREATE INDEX ${colTitle}_$tableName ON $tableName ($colTitle)';

}

class SongByTable {
  
  static String tableName = 'SongBy';

  // column names
  static String colSongId = 'songId';
  static String colAlbumId = 'albumId';
  static String colArtistId = 'artistId';

  // create table command secondary indexed the artistid
  static String createTable = 'CREATE TABLE $tableName($colSongId TEXT PRIMARY KEY NOT NULL, '+
                              '$colAlbumId TEXT NOT NULL, '+
                              '$colArtistId TEXT NOT NULL, '+
                              'CONSTRAINT FK_${SongsTable.tableName} FOREIGN KEY ($colSongId) '+
                              'REFERENCES ${SongsTable.tableName}(${SongsTable.colSongId}), '+
                              'CONSTRAINT FK_${AlbumsTable.tableName} FOREIGN KEY ($colAlbumId) '+
                              'REFERENCES ${AlbumsTable.tableName}(${AlbumsTable.colAlbumId}), '+
                              'CONSTRAINT FK_${ArtistTable.tableName} FOREIGN KEY ($colArtistId) '+
                              'REFERENCES ${ArtistTable.tableName}(${ArtistTable.colArtistId}))';

  // indexing for this table
  static String indexSQL = 'CREATE INDEX all_$tableName ON $tableName ($colAlbumId,$colArtistId)';

}

class FrequentlyHeardTable {
  
  static String tableName = 'FrequentlyHeard';

  // column names
  static String colUserId = 'userId';
  static String colSongId = 'songId';
  static String colAlbumId = 'albumId';
  static String colCount = 'count';
  static String colWeekNo = 'weekNo';
  
  // create table command clusterind indexed userid
  static String createTable = 'CREATE TABLE $tableName($colUserId TEXT NOT NULL, '+
                              '$colSongId TEXT NOT NULL, '+
                              '$colAlbumId TEXT NOT NULL, '+
                              '$colCount INT NULL, '+
                              '$colWeekNo INT NULL, '+
                              'CONSTRAINT PK_$tableName PRIMARY KEY ($colUserId,$colSongId), '+
                              'CONSTRAINT FK_${UsersTable.tableName} FOREIGN KEY ($colUserId) '+
                              'REFERENCES ${UsersTable.tableName}(${UsersTable.colUserId}), '+
                              'CONSTRAINT FK_${SongsTable.tableName} FOREIGN KEY ($colSongId) '+
                              'REFERENCES ${SongsTable.tableName}(${SongsTable.colSongId}), '+
                              'CONSTRAINT FK_${AlbumsTable.tableName} FOREIGN KEY ($colAlbumId) '+
                              'REFERENCES ${AlbumsTable.tableName}(${AlbumsTable.colAlbumId})) WITHOUT ROWID';

  // indexing for this table
  static String indexSQL = 'CREATE INDEX user_$tableName ON $tableName ($colUserId)';

}

class IncludesTable {

  static String tableName = 'Includes';

  // column names
  static String colIncludesId = 'includesId';
  static String colSongId = 'songId';
  static String colAlbumId = 'albumId';

  // create table command cluster indexed
  static String createTable = 'CREATE TABLE $tableName($colIncludesId TEXT, '+
                              '$colSongId TEXT NOT NULL, '+
                              '$colAlbumId TEXT NOT NULL, '+
                              'CONSTRAINT PK_${IncludesTable.tableName} PRIMARY KEY '+
                              '(${IncludesTable.colSongId},${IncludesTable.colIncludesId}) '+
                              'CONSTRAINT FK_${PlaylistTable.tableName} FOREIGN KEY ($colIncludesId) '+
                              'REFERENCES ${PlaylistTable.tableName}(${PlaylistTable.colPlaylistId}), '+
                              'CONSTRAINT FK_${SongsTable.tableName} FOREIGN KEY ($colSongId) '+
                              'REFERENCES ${SongsTable.tableName}(${SongsTable.colSongId}), '+
                              'CONSTRAINT FK_${AlbumsTable.tableName} FOREIGN KEY ($colAlbumId) '+
                              'REFERENCES ${AlbumsTable.tableName}(${AlbumsTable.colAlbumId})) WITHOUT ROWID';

  // indexing for this table
  static String indexSQL = 'CREATE INDEX ${colIncludesId}_$tableName ON $tableName ($colIncludesId)';

}


