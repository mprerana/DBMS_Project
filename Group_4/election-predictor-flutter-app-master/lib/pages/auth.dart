import 'package:flutter/material.dart';
import 'package:scoped_model/scoped_model.dart';
import 'dart:async';
import 'package:url_launcher/url_launcher.dart';


import '../scoped_models/main.dart';
import '../models/auth.dart';

class AuthPage extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    // TODO: implement createState
    return _AuthPageState();
  }
}

Future _launchURL(String url) async {
  if(await canLaunch(url)){
    launch(url, forceSafariVC: true, forceWebView: true);
  }else{
    print('cant launch ${url}');
  }
}

class _AuthPageState extends State<AuthPage> {
  String _email = 'saurabh@gmail.com';
  String _password = 'kuch bhi';
  final GlobalKey<FormState> _formkey = GlobalKey<FormState>();
  final TextEditingController _passwordTextController = TextEditingController();
  AuthMode _authMode = AuthMode.login;

  Map<String, dynamic> user = {
    'email': 'email',
    'password': 'password',
    'phone': 1,
    'username': 'batman',
    'number_plate': 'KA 000 JQ 1999',
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

    final username = TextFormField(
      keyboardType: TextInputType.text,
      initialValue: 'saurabh',
      autofocus: false,
      onSaved: (String value) {
        //titleValue = value;
        user['username'] = value;
      },
      validator: (String value) {
        if (value.isEmpty || value.length < 4) return 'username invalid';
      },
      decoration: InputDecoration(
        hintText: 'username',
        contentPadding: EdgeInsets.fromLTRB(20.0, 10.0, 20.0, 10.0),
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(32.0),
        ),
      ),
    );

    final number_plate = TextFormField(
      keyboardType: TextInputType.text,
      autofocus: false,
      onSaved: (String value) {
        //titleValue = value;
        user['number_plate'] = value;
      },
      validator: (String value) {
        if (value.isEmpty || value.length < 8) return 'username invalid';
      },
      decoration: InputDecoration(
        hintText: 'number plate',
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

    final phone = TextFormField(
      autofocus: false,
//      initialValue: 'something',
      onSaved: (String value) {
        user['phone'] = int.parse(value);
      },
      validator: (String value) {
        if (value.isEmpty || value.length < 10) return 'phone invalid';
      },
      keyboardType: TextInputType.number,
      decoration: InputDecoration(
        hintText: 'phone number',
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

    void authform(Function authenticate) async {
      print(user);
      if (!_formkey.currentState.validate()) {
        return;
      }
      _formkey.currentState.save();

      final Map<String, dynamic> successInformation = await authenticate(
          user['email'],
          user['password'],
          user['phone'],
          user['username'],
          user['number_plate'],
          _authMode);
      if (successInformation['success']) {
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
          },
        );
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
              onPressed: () => authform(model.authenticate),
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

    return Scaffold(
      backgroundColor: Colors.white,
      body: Center(
        child: Form(
          key: _formkey,
          child: Container(
            padding: EdgeInsets.all(targetPadding),
            child: ListView(
              children: <Widget>[
                SizedBox(
                  height: deviceWidth * 0.1,
                ),
                logo,
                SizedBox(
                  height: 48.0,
                ),

                username, //zt login

                SizedBox(
                  height: 8.0,
                ),

                _authMode == AuthMode.login
                    ? SizedBox(
                  height: 0.0,
                )
                    : email, //at signup

                SizedBox(
                  height: 8.0,
                ),
                password,
                SizedBox(
                  height: 8.0,
                ),

                _authMode == AuthMode.login
                    ? SizedBox(
                  height: 0.0,
                )
                    : confirm_password, //at signup

                SizedBox(
                  height: 8.0,
                ),

                _authMode == AuthMode.login
                    ? SizedBox(
                  height: 0.0,
                )
                    : phone,
                SizedBox(
                  height: 8.0,
                ),

                _authMode == AuthMode.login
                    ? SizedBox(
                  height: 0.0,
                )
                    : number_plate,

                SizedBox(
                  height: 24.0,
                ),

                FlatButton(
                  onPressed: () {

                    _launchURL('http://127.0.0.1:8000/auth/register_user/');

                  },
                  child: Text('switch to Signup'),
                ),

                loginbutton,
              ],
            ),
          ),
        ),
      ),
    );
  }
}

