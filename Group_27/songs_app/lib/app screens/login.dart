import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:firebase_auth/firebase_auth.dart';

import 'package:songs_app/services/loader.dart';
import 'package:songs_app/services/authentication.dart';

import 'package:songs_app/models/users.dart';
import 'package:songs_app/utils/cloudStore_files/usersFirestoreCRUD.dart';
import 'package:songs_app/utils/database_files/usersCRUD.dart';

class Login extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    return _LoginPageState();
  }
}

class _LoginPageState extends State<Login> {
  final GlobalKey<FormState> _formKey = GlobalKey<FormState>();

  final BaseAuth auth = BaseAuth();
  bool _isLoading = false;

  String _email;
  String _password;

  @override
  Widget build(BuildContext context) {
    return WillPopScope(
      child: Scaffold(
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
      ),
      onWillPop: () {
        AlertDialog alertDialog = AlertDialog(
          title: Center(
            child: Text('Are you sure'),
          ),
          content: Text('  want to close the app?'),
          actions: <Widget>[
            FlatButton(
              child: Text('Not Yet'),
              onPressed: () {
                Navigator.of(context, rootNavigator: true).pop('dialog');
              },
            ),
            FlatButton(
              child: Text('Yes'),
              onPressed: () {
                // return exit(0);
                SystemChannels.platform.invokeMethod('SystemNavigator.pop');
              },
            ),
          ],
        );
        showDialog(
            context: context,
            builder: (_) {
              return alertDialog;
            });
      },
    );
  }

  Widget _getBody() {
    if (_isLoading) {
      return Loader();
    } else {
      return Form(
        key: _formKey,
        child: ListView(
          children: <Widget>[
            Container(
              child: Column(
                children: <Widget>[
                  Container(
                    margin: EdgeInsets.only(top: 70),
                    child: Icon(
                      Icons.account_circle,
                      size: 120,
                    ),
                  ),
                  Container(
                    margin: EdgeInsets.only(top: 10, bottom: 20),
                    child: Text(
                      'LOG IN',
                      style: TextStyle(
                          fontSize: 40,
                          fontFamily: 'TooneyNoodle',
                          color: Colors.deepPurple),
                      textAlign: TextAlign.center,
                    ),
                  ),
                  Container(
                    width: 350,
                    height: 50,
                    margin: EdgeInsets.only(bottom: 30),
                    child: TextFormField(
                      keyboardType: TextInputType.emailAddress,
                      textAlign: TextAlign.justify,
                      cursorRadius: Radius.circular(5),
                      cursorColor: Colors.grey,
                      autocorrect: true,
                      keyboardAppearance: Brightness.dark,
                      decoration: InputDecoration(
                        border: OutlineInputBorder(
                            borderSide: BorderSide(color: Colors.deepPurple)),
                        labelText: 'Email',
                        hintText: 'example@example.com',
                      ),
                      validator: (value) {
                        if (value.isEmpty) {
                          return 'Email can\'t be empty';
                        }
                        if (!value.contains('@')) {
                          return 'Please provide correct emailid';
                        }
                        return null;
                      },
                      onSaved: (value) {
                        _email = value;
                      },
                    ),
                  ),
                  Container(
                    width: 350,
                    height: 50,
                    margin: EdgeInsets.all(5),
                    child: TextFormField(
                      textAlign: TextAlign.justify,
                      cursorRadius: Radius.circular(5),
                      cursorColor: Colors.grey,
                      keyboardAppearance: Brightness.dark,
                      decoration: InputDecoration(
                        border: OutlineInputBorder(
                            borderSide: BorderSide(color: Colors.deepPurple)),
                        labelText: 'Password',
                        hintText: '*************',
                      ),
                      obscureText: true,
                      validator: (value) {
                        if (value.isEmpty) {
                          return 'Password can\'t be emply';
                        }
                        if (value.length < 6) {
                          return 'Password must be atleast 6 characters';
                        }
                        return null;
                      },
                      onSaved: (value) {
                        _password = value;
                      },
                    ),
                  ),
                  Container(
                      width: 200,
                      margin: EdgeInsets.only(top: 20, bottom: 0.0),
                      child: RaisedButton(
                        child: Text(
                          'LOG IN',
                          style: TextStyle(color: Colors.white),
                        ),
                        onPressed: () {
                          _validateAndSubmit();
                        },
                        color: Colors.indigo,
                      )),
                  Container(
                    margin: EdgeInsets.fromLTRB(75.0,0.0,0.0,0.0),
                    child: Row(
                      children: <Widget>[
                        Text('Forgot Password?'),
                        Container(
                          width: 200.0,
                          child: FlatButton(
                            child: Text(
                              'Reset Password',
                              style: TextStyle(fontSize: 15),
                            ),
                            onPressed: () {
                              Navigator.of(context).pushNamed('/resetPasswordPage');
                            },
                            textColor: Colors.blue,
                          ),
                        )
                      ],
                    ),
                  ),
                  Row(
                    children: <Widget>[
                      Expanded(
                        child: Container(),
                      ),
                      Container(
                        width: 150,
                        child: Divider(
                          color: Colors.black,
                        ),
                      ),
                      Expanded(
                        child: Container(),
                      ),
                      Container(
                        width: 25.0,
                        child: Text('OR'),
                      ),
                      Expanded(
                        child: Container(),
                      ),
                      Container(
                        width: 150,
                        child: Divider(
                          color: Colors.black,
                        ),
                      ),
                      Expanded(
                        child: Container(),
                      ),
                    ],
                  ),
                  Container(
                    margin: EdgeInsets.fromLTRB(0.0, 15.0, 0.0, 0.0),
                    child: Column(
                      children: <Widget>[
                      Text(
                        'Not yet registered? tap the register button',
                      ),
                      Container(
                        width: 120,
                        child: FlatButton(
                          child: Text(
                            'Register',
                            style: TextStyle(fontSize: 15),
                          ),
                          onPressed: () {
                            Navigator.of(context).pushNamed('/registerPage');
                          },
                          textColor: Colors.blue,
                        ),
                      )
                    ],
                  )),
                ],
              ),
            ),
          ],
        ),
      );
    }
  }

  bool _validateAndSave() {
    final FormState form = _formKey.currentState;
    if (form.validate()) {
      form.save();
      return true;
    }
    return false;
  }

  void _validateAndSubmit() async {
    if (_validateAndSave()) {
      debugPrint('Validated the form');
      setState(() {
        _isLoading = true;
      });
      try {
        String userid = await auth.login(_email, _password);
        print(userid);
        bool userStatus = await auth.isEmailVerified();
        setState(() {
          _isLoading = false;
        });
        print('user Status:$userStatus');
        if (userStatus == false) {
          showDialog(
              context: context,
              builder: (_) {
                return AlertDialog(
                  title: Center(
                    child: Text(
                      'Please verify your email before login',
                      style: TextStyle(
                          color: Colors.red, fontFamily: 'Magnificent'),
                    ),
                  ),
                  content: Text('click on resend mail verfication'),
                  actions: <Widget>[
                    FlatButton(
                      child: Text('Resend mail'),
                      onPressed: _resendEmailVerification,
                    ),
                    FlatButton(
                      child: Text('OK'),
                      onPressed: () {
                        auth.signOut();
                        Navigator.of(context, rootNavigator: true)
                            .pop('dialog');
                      },
                    )
                  ],
                );
              });
        } else {
          _updateLastLogin();
          Navigator.of(context).pushReplacementNamed('/homePage');
        }
        // _getUserFromDB();
      } catch (error) {
        print('error: $error');
        _showAlertDialog('Error', error.toString());
        setState(() {
          _isLoading = false;
        });
      }
    }
  }

  void _updateLastLogin() async {
    FirebaseUser firebaseUser = await auth.getCurrentUser();
    User loggedUser = await UsersCRUD().getUserByID(firebaseUser.email);
    loggedUser.lastLogin = DateTime.now();
    print(loggedUser.lastLogin);
    await UsersCRUD().updateUser(loggedUser);
    await UserFirestoreCRUD().updateUserWithID(loggedUser);
  }

  void _resendEmailVerification() async {
    setState(() {
      _isLoading = true;
    });
    await auth.sendEmailVerification();
    await auth.signOut();
    Navigator.of(context, rootNavigator: true).pop('dialog');
    setState(() {
      _isLoading = false;
    });
  }

  void _showAlertDialog(String title, String message) {
    AlertDialog alertDialog = AlertDialog(
      title: Text(title),
      content: Text(message),
    );
    showDialog(
        context: context,
        builder: (_) {
          return alertDialog;
        });
  }
}
