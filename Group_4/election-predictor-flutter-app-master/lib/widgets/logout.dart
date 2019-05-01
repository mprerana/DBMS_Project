import 'package:flutter/material.dart';
import 'package:scoped_model/scoped_model.dart';

import '../scoped_models/main.dart';

class LogoutListTile extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    // TODO: implement build
    return ScopedModelDescendant<MainModel>(
        builder: (BuildContext context, Widget child, MainModel model) {
          return ListTile(
            leading:  Icon(Icons.exit_to_app),
            title: Text('logout'),
            onTap: (){
              model.logout();
              Navigator.pushReplacementNamed(context, '/');
            },
          );
        });
  }
}
