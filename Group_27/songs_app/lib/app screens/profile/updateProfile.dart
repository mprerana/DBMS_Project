import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';

import 'package:songs_app/utils/database_files/usersCRUD.dart';
import 'package:songs_app/models/users.dart';
import 'package:songs_app/utils/database_helper.dart';
import 'package:songs_app/utils/cloudStore_files/usersFirestoreCRUD.dart';

// Profile Widget...

class UserProfile extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    return _UserProfilePage();
  }
}

class _UserProfilePage extends State<UserProfile> {
  DatabaseHelper databaseHelper = DatabaseHelper();
  final GlobalKey<FormState> formkey = GlobalKey<FormState>();

  _UserProfilePage() {
    g2();
  }

  User _user;
  // String _userId;
  String _firstName;
  String _lastName;
  String _email;
  String _gender;

  String _userEmail;

  Future<String> _getUserAuthEmail() async {
    FirebaseUser user = await FirebaseAuth.instance.currentUser();
    setState(() {
      _userEmail = user.email;

      print(_userEmail);
    });
    return this._userEmail;
  }

  Future<User> getUserFromEmail() async {
    String emailid = await _getUserAuthEmail();
    Map<String, dynamic> userMap = await UsersCRUD().getUserMapByEmail(emailid);
    User user = User.fromMaptoUser(userMap);
    return user;
  }

  Future<User> getUser() async {
    return getUserFromEmail();
  }

  void g2() async {
    String emailid = await _getUserAuthEmail();
    Map<String, dynamic> userMap = await UsersCRUD().getUserMapByEmail(emailid);
    _user = User.fromMaptoUser(userMap);

    setState(() {
      _email = _user.email;
      _firstName = _user.firstName;
      _lastName = _user.lastName;
      _gender = _user.gender;
      print(_user);
    });
    print(_email);
  }

  void update() async {
    String emailid = await _getUserAuthEmail();
    Map<String, dynamic> userMap = await UsersCRUD().getUserMapByEmail(emailid);
    User user = User.fromMaptoUser(userMap);
    await UsersCRUD().updateUser(user);
  }

  List<String> maptoList(Map<String, dynamic> map) {
    var _list = map.values.toList();
    return _list;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        resizeToAvoidBottomPadding: false,
        appBar: AppBar(
          title: Text('Register Page'),
        ),
        body: Padding(
            padding: EdgeInsets.all(30.0),
            child: SingleChildScrollView(
                child: Form(
                    key: formkey,
                    child: Column(children: <Widget>[
                      // TextFormField(
                      //   decoration: InputDecoration(
                      //       labelText: _email,
                      //       icon: new Icon(
                      //         Icons.email,
                      //         color: Colors.grey,
                      //       )),
                      //       onSaved: (value) => _email = value),

                      TextFormField(
                        decoration: InputDecoration(
                            labelText: _firstName,
                            icon: new Icon(
                              Icons.email,
                              color: Colors.grey,
                            )),
                        validator: (value) => value.isEmpty ? null : null,
                        onSaved: (value) => value.isEmpty
                            ? value = _firstName
                            : _firstName = value,
                      ),

                      TextFormField(
                          decoration: InputDecoration(
                              labelText: _lastName,
                              icon: new Icon(
                                Icons.email,
                                color: Colors.grey,
                              )),
                          validator: (value) => value.isEmpty ? null : null,
                          onSaved: (value) => value.isEmpty
                              ? value = _lastName
                              : _lastName = value),

                      //NOTE : I AM NOT ABLE TO UPDATE THE LAST NAME //

                      TextFormField(
                        decoration: InputDecoration(
                            labelText: _gender,
                            icon: new Icon(
                              Icons.email,
                              color: Colors.grey,
                            )),
                        validator: (value) => value.isEmpty ? null : null,
                        onSaved: (value) =>
                            value.isEmpty ? value = _gender : _gender = value,
                      ),

                      RaisedButton(
                        child: Text('Update Profile'),
                        onPressed: () async {
                          bool validator = validateForm();
                          if (validator == true) {
                            //databaseHelper.updateEmailll(_email,_user);
                            _user.firstName = _firstName;
                            _user.lastName = _lastName;
                            _user.gender = _gender;
                            print('Email updated : $_email');
                            print('FirstName Updated : $_firstName ');
                            print('LastName Updated : $_lastName ');
                            print('StreetName Updated $_gender');
                            print('User : $_user');
                            await UsersCRUD().updateUser(_user);
                            await UserFirestoreCRUD().updateUserWithID(_user);
                            setState(() {});
                          } else {
                            print('Not Validated');
                          }
                        },
                        color: Colors.green[300],
                        padding: const EdgeInsets.all(8.0),
                        textColor: Colors.white,
                      ),
                    ])))));
  }

  void button() {}
  bool validateForm() {
    final FormState form = formkey.currentState;
    if (form.validate()) {
      form.save();
      return true;
    } else
      return false;
  }
}
