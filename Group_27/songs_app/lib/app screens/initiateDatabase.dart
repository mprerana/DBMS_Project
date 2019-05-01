import 'package:flutter/material.dart';
import 'package:sqflite/sqflite.dart';

import 'package:songs_app/services/loader.dart';
import 'package:songs_app/utils/database_helper.dart';
import 'package:songs_app/services/initDatabase.dart';

class InitDatabasePage extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    return _InitDatabasePageState();
  }
}

class _InitDatabasePageState extends State<InitDatabasePage> {
  Database db;

  @override
  void initState() {
    getDatabase();
    super.initState();
  }

  void getDatabase() async {
    db = await DatabaseHelper().database;
    print('Got the database');
    await InitData.populateDatatoDatabase();
    Navigator.of(context).pushReplacementNamed('/loginPage');
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        leading: null,
        title: Text(
          'BLINK',
          style: TextStyle(
            fontSize: 25,
            fontFamily: 'Velhos Tempos',
          ),
          textAlign: TextAlign.center,
        ),
        centerTitle: true,
        backgroundColor: Colors.deepPurple,
      ),
      body: _getBody(),
    );
  }

  Widget _getBody() {
      return Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text('Syncing local database with firebase'),
            Loader(),
          ],
        ),
      );
    }
}
