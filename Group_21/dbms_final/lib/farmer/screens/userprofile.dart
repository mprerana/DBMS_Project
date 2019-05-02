import 'dart:async';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:dbms_final/utils/dbhelper.dart';
import 'package:dbms_final/login/models/user.dart';
import 'package:dbms_final/login/screens/register1.dart';
import 'package:dbms_final/login/screens/register2.dart';
import 'package:dbms_final/login/screens/login.dart';
import 'package:dbms_final/login/screens/register.dart';
import 'package:dbms_final/utils/datbasefiles/usersCRUD.dart';

var StreetName;

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
  String _email;
  String _password;
  String _usertype;
  String _firstname;
  String _lastname;
  String _streetname;
  String _pincode;
  String _state;
  String _city;
 
 

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
    Map<String, dynamic> userMap =
        await Usercrudoperations().getUserwithEmail(emailid);
    User user = User.fromMapObject(userMap);
    return user;
  }
  Future<User> getUser()async{
    return getUserFromEmail();
  }
  void g2() async {
    String emailid = await _getUserAuthEmail();
    Map<String, dynamic> userMap =
        await Usercrudoperations().getUserwithEmail(emailid);
    _user = User.fromMapObject(userMap);

    setState(() {
      _email = _user.email;
      _usertype = _user.usertype;
      _firstname = _user.firstname;
      _lastname = _user.lastname;
      _city = _user.city;
      _streetname = _user.streetname;
      _state = _user.state;
      _pincode = _user.pincode;
      print(_user);
    });
    print(_email);
  }

  void update() async {
    String emailid = await _getUserAuthEmail();
    Map<String, dynamic> userMap =
        await Usercrudoperations().getUserwithEmail(emailid);
            User user = User.fromMapObject(userMap);
        await Usercrudoperations().updateUser(user);


  }


  List<String> MaptoList(Map<String, dynamic> map) {
    var _list = map.values.toList();
     //return [
    //   map['Firstname'],
    //   map['Lastname'],
    //   map['city'],
    //   map['Streetname'],
    //   map['State'],
    //   map['Pincode'],
    //   map['usertype']
    // // ];

    return _list;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        resizeToAvoidBottomPadding: false,
        appBar: AppBar(
          title: Text('Profile Page'),
        ),
        backgroundColor:Color.fromRGBO(40, 80, 40, 0.8),
        body: Padding(
            padding: EdgeInsets.all(30.0),
            child: SingleChildScrollView(
                child: Form(
                    key: formkey,
                    child: Column(children: <Widget>[
                      TextFormField(
                        decoration: InputDecoration(
                            labelText: _email,
                            icon: new Icon(
                              Icons.email,
                              color: Colors.grey,
                            )),
                            onSaved: (value) => _email = value),
                      
                      TextFormField(
                        decoration: InputDecoration(
                            labelText: _firstname,
                            icon: new Icon(
                              Icons.email,
                              color: Colors.grey,
                            )),
                        validator: (value) =>
                            value.isEmpty ? null : null,
                            onSaved: (value) => value.isEmpty ? value = _firstname : _firstname = value,
                      ),
                      /*
                      TextFormField(
                        decoration: InputDecoration(
                            labelText:_Lastname,
                            icon: new Icon(
                              Icons.email,
                              color: Colors.grey,
                            )),
                        validator: (value) =>
                            value.isEmpty ? null : null,
                            onSaved: (value) =>value.isEmpty ? value = _Lastname: _Lastname = value
                      ),*/

                      //NOTE : I AM NOT ABLE TO UPDATE THE LAST NAME //
                    
                    
                      TextFormField(
                        decoration: InputDecoration(
                            labelText: _streetname,
                            icon: new Icon(
                              Icons.email,
                              color: Colors.grey,
                            )),
                        validator: (value) =>
                            value.isEmpty ?  null : null,
                            onSaved: (value) => value.isEmpty ? value = _streetname :_streetname = value,
                      ),

                      
                      TextFormField(
                        decoration: InputDecoration(
                            labelText: _city,
                            icon: new Icon(
                              Icons.email,
                              color: Colors.grey,
                            )),
                        validator: (value) =>
                            value.isEmpty ? null : null,
                            onSaved: (value) => value.isEmpty ?  value = _city : _city = value,
                      ),
                      TextFormField(
                        decoration: InputDecoration(
                            labelText: _state,
                            icon: new Icon(
                              Icons.email,
                              color: Colors.grey,
                            )),
                        validator: (value) =>
                            value.isEmpty ? null : null,
                            onSaved: (value) =>value.isEmpty ? value = _state : _state = value,
                      ),
                      TextFormField(
                        decoration: InputDecoration(
                            labelText: _pincode,
                            icon: new Icon(
                              Icons.email,
                              color: Colors.grey,
                            )),
                        validator: (value) =>
                            value.isEmpty ? null : null,
                            onSaved: (value) => value.isEmpty ? value = _pincode : _pincode = value,
                      ),
                      
                      RaisedButton(
                child: Text('Update Profile'),
                onPressed:(){
                       bool validator = validateForm();
                       if(validator == true){
                  //databaseHelper.updateEmailll(_email,_user);
                  Usercrudoperations().updateFname(_firstname,_user);
                  Usercrudoperations().updateLname(_lastname,_user);
                  Usercrudoperations().updateStreetname(_streetname,_user);
                  Usercrudoperations().updateCity(_city,_user);
                  Usercrudoperations().updateState(_state,_user);
                  Usercrudoperations().updatePincode(_pincode,_user);
                  print('Email updated : $_email');
                  print('FirstName Updated : $_firstname ');
                  print('LastName Updated : $_lastname ');
                  print('StreetName Updated $_streetname');
                  print('User : $_user');
                       }
                       else{
                         print('Not Validated');
                       }
             
                    //update();
                    
                  
                } ,
                color: Colors.green[300],
                  padding: const EdgeInsets.all(8.0),
                  textColor: Colors.white,
  
              ),
                    ])))));
  }

  void button(){
    
  }
bool validateForm() {
  final FormState form = formkey.currentState;
  if (form.validate()) {
    form.save();
    return true;
  }
  else
    return false;
  }
}
