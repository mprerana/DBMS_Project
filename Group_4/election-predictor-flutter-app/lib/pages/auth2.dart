import 'package:flutter/material.dart';
import 'package:scoped_model/scoped_model.dart';
import 'dart:async';

import '../scoped_models/main.dart';
import '../models/auth.dart';

class AuthPage2 extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    // TODO: implement createState
    return _AuthPageState();
  }
}

class _AuthPageState extends State<AuthPage2> {
  String _email = 'saurabh@gmail.com';
  String _password = 'kuch bhi';
  final GlobalKey<FormState> _formkey = GlobalKey<FormState>();
  final TextEditingController _passwordTextController = TextEditingController();
  AuthMode _authMode = AuthMode.login;

  Map<String, dynamic> user = {
    'email': 'email',
    'password': 'password',
    'fname': 'no',
    'lname': 'no',
    'phnumber': '9999',
    'location': 'mumbai',
    'gender': 'male',
    'party': 'no',
    'party_admin': false,
    'description': 'no',
    'returnSecureToken': true,
  };

  @override
  Widget build(BuildContext context) {
    final double deviceWidth = MediaQuery.of(context).size.width;
    final double targetwidth =
        deviceWidth > 550.0 ? deviceWidth * 0.90 : deviceWidth * 0.98;
    final double targetPadding = deviceWidth - targetwidth;

    final logo = Hero(
      tag: 'logo',
      child: CircleAvatar(
        backgroundColor: Colors.transparent,
        radius: 48.0,
        child: Image.asset('assets/logo.png'),
      ),
    );

    final email = TextFormField(
      keyboardType: TextInputType.emailAddress,
      autofocus: false,
      initialValue: 'abc@gmail.com',
      onSaved: (String value) {
        //titleValue = value;
        user['email'] = value;
      },
      validator: (String value) {
        if (value.isEmpty || value.length < 5) return 'email invalid';
      },
      decoration: InputDecoration(
        hintText: 'Email',
        contentPadding: EdgeInsets.fromLTRB(20.0, 10.0, 20.0, 10.0),
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(32.0),
        ),
      ),
    );

    final password = TextFormField(
      obscureText: true,
      autofocus: false,
//      initialValue: 'something',
      onSaved: (String value) {
        user['password'] = value;
      },
      validator: (String value) {
        if (value.isEmpty || value.length < 5) return 'password invalid';
      },
      controller: _passwordTextController,
      decoration: InputDecoration(
        hintText: 'password',
        contentPadding: EdgeInsets.fromLTRB(20.0, 10.0, 20.0, 10.0),
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(32.0),
        ),
      ),
    );

    final confirm_password = TextFormField(
      obscureText: true,
      autofocus: false,
      onSaved: (String value) {
        _password = value;
      },
      validator: (String value) {
        if (_passwordTextController.text != value) {
          return 'please enter valid passwords';
        }
      },
      decoration: InputDecoration(
        hintText: 'confirm password',
        contentPadding: EdgeInsets.fromLTRB(20.0, 10.0, 20.0, 10.0),
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(32.0),
        ),
      ),
    );

    void authform(Function authenticate2) async {
      if (!_formkey.currentState.validate()) {
        return;
      }
      _formkey.currentState.save();
      if (_authMode == AuthMode.Signup_party) user['party_admin'] = true;

      final Map<String, dynamic> successInformation =
          await authenticate2(user, _authMode);
      if (successInformation['success']) {
        // Navigator.pushReplacementNamed(context, '/');
      } else {
        showDialog(
            context: context,
            builder: (BuildContext context) {
              return AlertDialog(
                title: Text('Error'),
                content: Text(successInformation['message']),
                actions: <Widget>[
                  FlatButton(
                    child: Text('OK'),
                    onPressed: () => Navigator.of(context).pop(),
                  ),
                ],
              );
            });
      }
    }

    final loginbutton = ScopedModelDescendant<MainModel>(
      builder: (BuildContext context, Widget child, MainModel model) {
        return model.isLoading
            ? Center(child: CircularProgressIndicator())
            : Padding(
                padding: EdgeInsets.symmetric(vertical: 16.0),
                child: Material(
                  borderRadius: BorderRadius.circular(30.0),
                  shadowColor: Colors.lightBlueAccent.shade100,
                  elevation: 5.0,
                  child: MaterialButton(
                    //onPressed: () => authform(model.authenticate2),
                    minWidth: 200.0,
                    height: 42.0,
                    color: Colors.lightBlueAccent,
                    child: Text(
                      '${_authMode == AuthMode.login ? 'login' : 'Signup'}',
                      style: TextStyle(color: Colors.white),
                    ),
                  ),
                ),
              );
      },
    );

    final Widget fname = TextFormField(
      keyboardType: TextInputType.emailAddress,
      autofocus: false,
      onSaved: (String value) {
        //titleValue = value;
        user['fname'] = value;
      },
      validator: (String value) {
        if (value.isEmpty || value.length < 1) return 'fname needed';
      },
      decoration: InputDecoration(
        hintText: 'first name',
        contentPadding: EdgeInsets.fromLTRB(20.0, 10.0, 20.0, 10.0),
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(32.0),
        ),
      ),
    );

    final Widget lname = TextFormField(
      keyboardType: TextInputType.emailAddress,
      autofocus: false,
      onSaved: (String value) {
        //titleValue = value;
        user['lname'] = value;
      },
      validator: (String value) {
        if (value.isEmpty || value.length < 1) return 'lname needed';
      },
      decoration: InputDecoration(
        hintText: 'last name',
        contentPadding: EdgeInsets.fromLTRB(20.0, 10.0, 20.0, 10.0),
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(32.0),
        ),
      ),
    );

    final Widget location = TextFormField(
      keyboardType: TextInputType.emailAddress,
      autofocus: false,
      onSaved: (String value) {
        //titleValue = value;
        user['location'] = value;
      },
      validator: (String value) {
        if (value.isEmpty || value.length < 1) return 'location needed';
      },
      decoration: InputDecoration(
        hintText: 'location',
        contentPadding: EdgeInsets.fromLTRB(20.0, 10.0, 20.0, 10.0),
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(32.0),
        ),
      ),
    );

    final Widget gender = TextFormField(
      keyboardType: TextInputType.emailAddress,
      autofocus: false,
      onSaved: (String value) {
        //titleValue = value;
        user['gender'] = value;
      },
      validator: (String value) {
        if (value.isEmpty || value.length < 1) return 'gender needed';
      },
      decoration: InputDecoration(
        hintText: 'gender',
        contentPadding: EdgeInsets.fromLTRB(20.0, 10.0, 20.0, 10.0),
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(32.0),
        ),
      ),
    );

    final Widget party = TextFormField(
      keyboardType: TextInputType.emailAddress,
      autofocus: false,
      onSaved: (String value) {
        //titleValue = value;
        user['party'] = value;
      },
      validator: (String value) {
        if (value.isEmpty || value.length < 1) return 'party needed';
      },
      decoration: InputDecoration(
        hintText: 'party name',
        contentPadding: EdgeInsets.fromLTRB(20.0, 10.0, 20.0, 10.0),
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(32.0),
        ),
      ),
    );

    final Widget phnumber = TextFormField(
      keyboardType: TextInputType.emailAddress,
      autofocus: false,
      onSaved: (String value) {
        //titleValue = value;
        user['phnumber'] = value;
      },
      validator: (String value) {
        if (value.isEmpty || value.length < 1) return 'phone number needed';
      },
      decoration: InputDecoration(
        hintText: 'contact',
        contentPadding: EdgeInsets.fromLTRB(20.0, 10.0, 20.0, 10.0),
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(32.0),
        ),
      ),
    );

    final Widget description = TextFormField(
      keyboardType: TextInputType.emailAddress,
      autofocus: false,
      onSaved: (String value) {
        //titleValue = value;
        user['description'] = value;
      },
      validator: (String value) {
        if (value.isEmpty || value.length < 1) return 'description needed';
      },
      decoration: InputDecoration(
        hintText: 'party description',
        contentPadding: EdgeInsets.fromLTRB(20.0, 10.0, 20.0, 10.0),
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(0.0),
        ),
      ),
    );

    final Widget login = ListView(
      children: <Widget>[
        SizedBox(
          height: deviceWidth * 0.1,
        ),
        logo,
        SizedBox(
          height: 48.0,
        ),

        //required fields
        email,
        SizedBox(
          height: 8.0,
        ),
        password,
        SizedBox(
          height: 8.0,
        ),
        FlatButton(
          onPressed: () {
            setState(
              () {
                _authMode = AuthMode.Signup;
              },
            );
          },
          child: Text('Signup'),
        ),
        SizedBox(
          height: 8.0,
        ),
        loginbutton,
      ],
    );

    final Widget Signup = ListView(
      children: <Widget>[
        SizedBox(
          height: deviceWidth * 0.1,
        ),
        logo,
        SizedBox(
          height: 48.0,
        ),

        //required fields
        email,
        SizedBox(
          height: 8.0,
        ),
        password,
        SizedBox(
          height: 8.0,
        ),

        confirm_password,
        SizedBox(
          height: 8.0,
        ),
        fname,
        SizedBox(
          height: 8.0,
        ),
        lname,
        SizedBox(
          height: 8.0,
        ),
        phnumber,
        SizedBox(
          height: 8.0,
        ),
        location,
        SizedBox(
          height: 8.0,
        ),
        gender,
        SizedBox(
          height: 8.0,
        ),
        FlatButton(
          onPressed: () {
            setState(
              () {
                _authMode = AuthMode.Signup_party;
              },
            );
          },
          child: Text('Signup as a party admin'),
        ),
        SizedBox(
          height: 8.0,
        ),

        FlatButton(
          onPressed: () {
            setState(
              () {
                _authMode = AuthMode.login;
              },
            );
          },
          child: Text('login'),
        ),
        SizedBox(
          height: 8.0,
        ),
        loginbutton,
      ],
    );

    final Widget Signup_party = ListView(
      children: <Widget>[
        SizedBox(
          height: deviceWidth * 0.1,
        ),
        logo,
        SizedBox(
          height: 48.0,
        ),

        //required fields
        email,
        SizedBox(
          height: 8.0,
        ),
        password,
        SizedBox(
          height: 8.0,
        ),

        confirm_password,
        SizedBox(
          height: 8.0,
        ),
        fname,
        SizedBox(
          height: 8.0,
        ),
        lname,
        SizedBox(
          height: 8.0,
        ),
        party,
        SizedBox(
          height: 8.0,
        ),
        description,
        SizedBox(
          height: 8.0,
        ),

        FlatButton(
          onPressed: () {
            setState(
              () {
                _authMode = AuthMode.login;
              },
            );
          },
          child: Text('login'),
        ),
        SizedBox(
          height: 8.0,
        ),

        FlatButton(
          onPressed: () {
            setState(
              () {
                _authMode = AuthMode.Signup;
              },
            );
          },
          child: Text('Signup as a citizen'),
        ),
        SizedBox(
          height: 8.0,
        ),
        loginbutton,
      ],
    );

    Widget form() {
      if (_authMode == AuthMode.login) {
        return login;
      } else if (_authMode == AuthMode.Signup) {
        return Signup;
      }
      return Signup_party;
    }

    // TODO: implement build
    return Scaffold(
      backgroundColor: Colors.white,
      body: Center(
        child: Form(
          key: _formkey,
          child: Container(
            padding: EdgeInsets.all(targetPadding),
            child: form(),
          ),
        ),
      ),
    );
  }
}
