import 'package:flutter/material.dart';

import 'package:songs_app/models/users.dart';
import 'package:songs_app/utils/database_files/usersCRUD.dart';

class ShowUsers extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    return _ShowUsersState();
  }
}

class _ShowUsersState extends State<ShowUsers> {
  List<User> userList = List<User>();

  @override
  void initState() {
    debugPrint('hello');
    getUsers();
    super.initState();
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
        body: Center(
          child: Column(
            children: <Widget>[
              RaisedButton(
                child: Text('get users'),
                onPressed: getUsers,
              ),
            ],
          ),
        ));
  }

  void getUsers() async {
    debugPrint('getting all users');
    userList = await UsersCRUD().getUserList();
    debugPrint('Got users of ${userList.length} ${userList[0].email}');
    setState(() {
      userList = userList;
    });
  }
}
