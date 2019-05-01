import 'package:flutter/material.dart';
import 'package:cloud_firestore/cloud_firestore.dart';

import 'package:songs_app/services/authentication.dart';
import 'package:songs_app/services/loader.dart';
import 'package:songs_app/utils/database_files/usersCRUD.dart';
import 'package:songs_app/utils/cloudStore_files/usersFirestoreCRUD.dart';
import 'package:songs_app/models/users.dart';

class Register extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    return RegisterState();
  }
}

class RegisterState extends State<Register> {
  final GlobalKey<FormState> _formKey = GlobalKey<FormState>();

  final BaseAuth auth = BaseAuth();
  bool _isLoading = false;

  String _firstName;
  String _lastName;
  String _email;
  DateTime _dob = DateTime.now();
  String _password;
  String _gender = 'Male';

  TextEditingController passWordController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return WillPopScope(
      child: Scaffold(
        appBar: AppBar(
          leading: IconButton(
            icon: Icon(Icons.arrow_back),
            onPressed: () {
              Navigator.pop(context, true);
            },
          ),
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
        debugPrint('Exiting register page');
        Navigator.of(context).pop();
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
                    margin: EdgeInsets.only(top: 30),
                    child: Text(
                      'Register',
                      style: TextStyle(
                          fontSize: 40,
                          fontFamily: 'TooneyNoodle',
                          color: Colors.deepPurple),
                      textAlign: TextAlign.center,
                    ),
                  ),

                  // First name...
                  Container(
                    width: 350,
                    height: 50,
                    margin: EdgeInsets.only(top: 28, bottom: 30),
                    child: TextFormField(
                      keyboardType: TextInputType.text,
                      textAlign: TextAlign.justify,
                      cursorRadius: Radius.circular(5),
                      cursorColor: Colors.grey,
                      autocorrect: true,
                      keyboardAppearance: Brightness.dark,
                      decoration: InputDecoration(
                        border: OutlineInputBorder(
                            borderSide: BorderSide(color: Colors.deepPurple)),
                        labelText: 'First Name',
                        hintText: 'First Name',
                      ),
                      validator: (value) {
                        if (value.isEmpty) {
                          return 'Can not be Empty';
                        }
                        return null;
                      },
                      onSaved: (value) {
                        _firstName = value;
                      },
                    ),
                  ),

                  // Last Name...
                  Container(
                    width: 350,
                    height: 50,
                    child: TextFormField(
                      keyboardType: TextInputType.text,
                      textAlign: TextAlign.justify,
                      cursorRadius: Radius.circular(5),
                      cursorColor: Colors.grey,
                      autocorrect: true,
                      keyboardAppearance: Brightness.dark,
                      decoration: InputDecoration(
                        border: OutlineInputBorder(
                            borderSide: BorderSide(color: Colors.deepPurple)),
                        labelText: 'Last Name',
                        hintText: 'Last Name',
                      ),
                      validator: (value) {
                        if (value.isEmpty) {
                          return 'Can not be Empty';
                        }
                        return null;
                      },
                      onSaved: (value) {
                        _lastName = value;
                      },
                    ),
                  ),

                  // Email Id...
                  Container(
                    width: 350,
                    height: 50,
                    margin: EdgeInsets.fromLTRB(0, 30, 0, 30),
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
                        if (!(value.contains('@'))) {
                          return 'Email is invalid';
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
                      child: Row(
                        children: <Widget>[
                          // Gender Selection...
                          Expanded(
                            child: Container(
                              height: 100,
                              margin: EdgeInsets.only(top: 35),
                              child: DropdownButton<String>(
                                value: _gender,
                                onChanged: (String newValue) {
                                  setState(() {
                                    _gender = newValue;
                                  });
                                },
                                items: <String>[
                                  'Male',
                                  'Female',
                                  'Others'
                                ].map<DropdownMenuItem<String>>((String value) {
                                  return DropdownMenuItem<String>(
                                    value: value,
                                    child: Text(value),
                                  );
                                }).toList(),
                                isDense: true,
                              ),
                            ),
                          ),
                          // Date of Birth...
                          Expanded(
                            child: RaisedButton(
                              onPressed: () => _selectDate(context),
                              child: Text(
                                "Date of birth: ${_dob.year}/${_dob.month}/${_dob.day}",
                                textAlign: TextAlign.center,
                              ),
                            ),
                          )
                        ],
                      )),

                  // Password...
                  Container(
                    width: 350,
                    height: 50,
                    margin: EdgeInsets.only(top: 30),
                    child: TextFormField(
                      controller: passWordController,
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
                          return 'Password can\'t be null';
                        }
                        if (value.length <= 6) {
                          return 'Password must be atleast 7 letter';
                        }
                        return null;
                      },
                      onSaved: (value) {
                        _password = value;
                      },
                    ),
                  ),

                  // ReEnter password
                  Container(
                    width: 350,
                    height: 50,
                    margin: EdgeInsets.only(top: 30),
                    child: TextFormField(
                      textAlign: TextAlign.justify,
                      cursorRadius: Radius.circular(5),
                      cursorColor: Colors.grey,
                      keyboardAppearance: Brightness.dark,
                      decoration: InputDecoration(
                        border: OutlineInputBorder(
                            borderSide: BorderSide(color: Colors.deepPurple)),
                        labelText: 'Confirm Password',
                        hintText: '*************',
                      ),
                      obscureText: true,
                      validator: (value) {
                        if (value != passWordController.text) {
                          return 'Password didn\'t match';
                        }
                        return null;
                      },
                      onSaved: (value) {
                        _password = value;
                      },
                    ),
                  ),

                  // Register Button...
                  Container(
                      width: 350,
                      margin: EdgeInsets.only(top: 30, bottom: 40),
                      child: RaisedButton(
                        child: Text(
                          'Register',
                          style: TextStyle(color: Colors.white),
                        ),
                        onPressed: () {
                          debugPrint('pressed Register button!');
                          _validateAndSubmit();
                        },
                        color: Colors.indigo,
                      )),

                  Container(
                      child: Column(
                    children: <Widget>[
                      Text(
                        'Already Registered? tap the LogIn button',
                      ),
                      FlatButton(
                        child: Text(
                          'LOG IN',
                          style: TextStyle(fontSize: 15),
                        ),
                        onPressed: () {
                          Navigator.of(context).pop();
                        },
                        textColor: Colors.blue,
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
      // print('firstname: $_firstName, lastname: $_lastName, gender: $_gender, email: $_email,dob: $_dob,password: $_password');
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
        String userid = await auth.signUp(_email, _password);
        await auth.sendEmailVerification();
        print(userid);
        _showAlertDialog('Status', 'Check your mail to verify');
        await auth.signOut();
        _saveUserToDatabases();
        setState(() {
          _isLoading = false;
        });
      } catch (error) {
        print('error: $error');
        _showAlertDialog('Error', error.toString());
        setState(() {
          _isLoading = false;
        });
      }
    }
  }

  Future<Null> _selectDate(BuildContext context) async {
    final DateTime picked = await showDatePicker(
        context: context,
        initialDate: _dob,
        firstDate: DateTime(1900, 8),
        lastDate: DateTime(2101));
    if (picked != null && picked != _dob)
      setState(() {
        _dob = picked;
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

  void _saveUserToDatabases() async {
    User user = User(
        _firstName, _lastName, _email, _gender, _dob, DateTime.now(), true);

    debugPrint('inserting user to firestore');
    DocumentReference userRef = await UserFirestoreCRUD().insertUser(user);
    debugPrint('created user to firestore');
    DocumentSnapshot userDoc = await userRef.get();
    await UsersCRUD().insertUser(
        User.fromFirestoreMaptoUser(userDoc.data, userRef.documentID));

    Navigator.of(context)
        .pushNamedAndRemoveUntil('/loginPage', (Route<dynamic> route) => false);
  }
}
