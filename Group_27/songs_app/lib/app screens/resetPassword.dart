import 'package:flutter/material.dart';

import 'package:songs_app/services/loader.dart';
import 'package:songs_app/services/authentication.dart';

class ResetPassword extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    return _ResetPasswordState();
  }
}

class _ResetPasswordState extends State<ResetPassword> {
  final GlobalKey<FormState> _formKey = GlobalKey<FormState>();

  String _email;

  final BaseAuth _auth = BaseAuth();
  bool _isLoading = false;

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
        debugPrint('Exiting reset Pasword page');
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
                    margin: EdgeInsets.only(top: 50, bottom: 20),
                    child: Text(
                      'RESET PASSWORD',
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
                      width: 200,
                      margin: EdgeInsets.only(top: 20, bottom: 0.0),
                      child: RaisedButton(
                        child: Text(
                          'Reset Password',
                          style: TextStyle(color: Colors.white),
                        ),
                        onPressed: () {
                          _validateAndSubmit();
                        },
                        color: Colors.indigo,
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
    } else {
      return false;
    }
  }

  void _validateAndSubmit() async {
    if(_validateAndSave()) {
      debugPrint('Validated the form');
      setState(() {
       _isLoading = true; 
      });
      try {
        await _auth.resetPassword(_email);
        setState(() {
         _isLoading = false; 
        });
        // Navigator.popUntil(context, ModalRoute.withName('/loginPage'));
        _showAlertDialog('Password Reset Mail Sent', 'Check your mail inbox to reset your password');
      } catch(error) {
        print('error: $error');
        _showAlertDialog('Error', error.toString());
        setState(() {
          _isLoading = false;
        });
      }
    }
  }

  void _showAlertDialog(String title, String message) {
    AlertDialog alertDialog = AlertDialog(
      title: Text(title),
      content: Text(message),
      actions: <Widget>[
        FlatButton(
          child: Text('OK'),
          onPressed: () {
            Navigator.of(context).pushNamedAndRemoveUntil('/loginPage', (Route<dynamic> route) => false);
          },
        ),
      ],
    );
    showDialog(
        context: context,
        builder: (_) {
          return alertDialog;
        });
  }
}
