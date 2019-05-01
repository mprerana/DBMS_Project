import 'dart:async';
import 'dart:io';

import 'package:sqflite/sqflite.dart';
import 'package:path_provider/path_provider.dart';

import 'package:songs_app/utils/database_files/tables.dart';
import 'package:songs_app/utils/database_files/triggers.dart';
import 'package:songs_app/utils/database_files/viewsDB.dart';

class DatabaseHelper {
  // Making the instances of the class singleton
  static DatabaseHelper _databaseHelper;
  static Database _database;

  // some constant variables

  // named constructor to get new instance of databasehelper class
  DatabaseHelper._createInstance();

  // constructor for the databasehelper class
  factory DatabaseHelper() {
    if(_databaseHelper == null) {
      _databaseHelper = DatabaseHelper._createInstance();
    }
    return _databaseHelper;
  }

  // get function for the database instance
  Future<Database> get database async {
    if(_database == null) {
      _database = await _initializeDatabase();
    }
    return _database;
  }

  Future<Database> _initializeDatabase() async {
    Directory directory = await getApplicationDocumentsDirectory();
    String path = directory.path + 'songs_app.db';

    await deleteDatabase(path);
    Future<Database> userDatabase = openDatabase(path,version: 1,onCreate: _createDB);
    return userDatabase;
  }

  void _createDB(Database db, int version) async {

    await db.execute('PRAGMA foreign_keys = ON');

    // Create tables
    await db.execute(UsersTable.createTable);
    await db.execute(GenreTable.createTable);
    await db.execute(PlaylistTable.createTable);
    await db.execute(Imagestable.createTable);
    await db.execute(AlbumsTable.createTable);
    await db.execute(ArtistTable.createTable);
    await db.execute(SongsTable.createTable);
    await db.execute(SongByTable.createTable);
    await db.execute(FrequentlyHeardTable.createTable);
    await db.execute(IncludesTable.createTable);
    print('Tables created successfully');

    // Create indexes for tables
    await db.execute(UsersTable.indexSQL);
    await db.execute(GenreTable.indexSQL);
    await db.execute(PlaylistTable.indexSQL);
    await db.execute(AlbumsTable.indexSQL);
    await db.execute(ArtistTable.indexSQL);
    await db.execute(SongsTable.indexSQL);
    await db.execute(SongByTable.indexSQL);
    await db.execute(FrequentlyHeardTable.indexSQL);
    await db.execute(IncludesTable.indexSQL);
    print('Indexes created successfully');

    // Create triggers for tables
    await db.execute(Triggers.triggerinsertSongOnArtist);
    await db.execute(Triggers.triggerinsertSongOnAlbum);
    await db.execute(Triggers.triggerinsertAlbumOnArtist);
    print('Triggers created successfully');

    // Create views for tables
    await db.execute(Views.getRecentReleases);
    await db.execute(Views.getTopArtist);
    await db.execute(Views.getRomantic);
    await db.execute(Views.getEDM);
    await db.execute(Views.getKPOP);
    await db.execute(Views.getMelody);
    await db.execute(Views.getReligious);
    await db.execute(Views.getRock);
    await db.execute(Views.getOldIsGold);
    print('Views created successfully');
  }
}