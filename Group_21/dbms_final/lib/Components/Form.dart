import 'package:flutter/material.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:dbms_final/login/screens/register.dart';
import 'package:dbms_final/login/screens/view_users.dart';

import 'package:dbms_final/login/screens/view_farmer.dart';

class LoginPage extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    return _LoginPageState();
  }
} 

class _LoginPageState extends State<LoginPage> {

  final GlobalKey<FormState> formkey =GlobalKey<FormState>();

  String _email; 
  String _password; 
  String _person;
  List _Persons =
  ["Farmer","Customer", "AgricultureExpert"];

  List<DropdownMenuItem<String>> _dropDownMenuItems;
  
  @override
  void initState() {
    _dropDownMenuItems = getDropDownMenuItems();
    _person = _dropDownMenuItems[0].value;
    super.initState();
  }

  List<DropdownMenuItem<String>> getDropDownMenuItems() {
    List<DropdownMenuItem<String>> items = new List();
    for (String person in _Persons) {
      items.add(new DropdownMenuItem(
          value: person,
          child: new Text(person)
      ));
    }
    return items;
  }
   Widget build(BuildContext context) {
    return (new Container(
      margin: new EdgeInsets.symmetric(horizontal: 20.0),
      child: new Column(
        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
        children: <Widget>[
          new Form(
              child: new Column(
            mainAxisAlignment: MainAxisAlignment.spaceAround,
            children: <Widget>[
               TextFormField(
                  style: TextStyle(
                      color: Colors.white,
                    ),

                  decoration: InputDecoration(labelText: 'Email',),
                  
                  validator: (value) => value.isEmpty ? 'Email can\'t be empty' : null,
                  onSaved: (value) {
                    _email = value;
                  },
                ),
               TextFormField(
                   style: TextStyle(
                      color: Colors.white,
                    ),

                  decoration: InputDecoration(labelText: 'Password'),
                  obscureText: true,
                  validator: (value) => value.isEmpty ? 'Password can\'t be empty' : null,
                  onSaved: (value) {
                    _password = value;
                  },
                ),
                new DropdownButton(
                
                value: _person,
                items: _dropDownMenuItems,
                onChanged: changedDropDownItem,
                
                 
              ),
             // FlatButton(
               //   child: Text('Register', style: TextStyle(fontSize: 15.0),),
                 // onPressed: moveToRegisterScreen,
               // ),
                FlatButton(
                child: Text('View All Users'),
                  onPressed: moveToUsersViewScreen,
                ),
               FlatButton(
                  
                  child: Text('View All farmers'),
                  onPressed: moveTofarmersViewScreen,
                ),
            ],
          )),
        ],
      ),
    ));
  }
  bool validateLoginForm() {
    final FormState form = formkey.currentState;
    if (form.validate()) {
      form.save();
      // debugPrint('Email : $_email\nPassword: $_password');
      return true;
    }
    else
      return false;
  }
   void validateAndSubmit() async {
    if(validateLoginForm()) {
      // debugPrint('Validated the form');
      try {
        
                FirebaseUser user = await FirebaseAuth.instance.signInWithEmailAndPassword(
                email: _email,
                password: _password,
                
        
      );
      
    
      debugPrint('Successfully logged into user: ${user.uid}');
      
      }
      
      catch (error) {
        print('error: $error');
      }
    }
    else {
      debugPrint('Form not validated');
    }
  }
  void changedDropDownItem(String selectedrole) {
    setState(() {
      _person = selectedrole;
    });
  }
  void moveToRegisterScreen() {
    Navigator.push(context, MaterialPageRoute(builder: (context) {
      return RegisterPage();
    }));
  }

  void moveToUsersViewScreen() {
    Navigator.push(context, MaterialPageRoute(builder: (context) {
      return ViewUsers();
    }));
  }
  void moveTofarmersViewScreen() {
    Navigator.push(context, MaterialPageRoute(builder: (context) {
      return Viewfarmers();
    }));
  }


}
/*

import 'package:flutter/material.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:dbms_final/login/screens/register.dart';
import 'package:dbms_final/login/screens/view_users.dart';
import 'package:dbms_final/Components/InputFields.dart';
import 'package:dbms_final/login/screens/view_farmer.dart';

class LoginPage extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    return _LoginPageState();
  }
} 

class _LoginPageState extends State<LoginPage> {

  final GlobalKey<FormState> formkey =GlobalKey<FormState>();

  String _email; 
  String _password; 
  String _person;
  List _Persons =
  ["Farmer","Customer", "AgricultureExpert"];

  List<DropdownMenuItem<String>> _dropDownMenuItems;
  

  @override
  void initState() {
    _dropDownMenuItems = getDropDownMenuItems();
    _person = _dropDownMenuItems[0].value;
    super.initState();
  }

  List<DropdownMenuItem<String>> getDropDownMenuItems() {
    List<DropdownMenuItem<String>> items = new List();
    for (String person in _Persons) {
      items.add(new DropdownMenuItem(
          value: person,
          child: new Text(person)
      ));
    }
    return items;
  }


  @override 
  Widget build(BuildContext context) {
    return(new Scaffold(
      body: new Container(
       
         margin: new EdgeInsets.symmetric(horizontal: 20.0),
         child: new Column(
        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
        children: <Widget>[
          new Form(
             key: formkey,
              child: new Column(
            mainAxisAlignment: MainAxisAlignment.spaceAround,
            children: <Widget>[
          
             
           
            
          
               new InputFieldArea(
                 hint: 'Email',
                  decoration: InputDecoration(labelText: 'Email',),
                  validator: (value) => value.isEmpty ? 'Email can\'t be empty' : null,
                  onSaved: (value) {
                    _email = value;
                  },
                ),
                TextFormField(
                  decoration: InputDecoration(labelText: 'Password'),
                  obscureText: true,
                  validator: (value) => value.isEmpty ? 'Password can\'t be empty' : null,
                  onSaved: (value) {
                    _password = value;
                  },
                ),
                new DropdownButton(
                value: _person,
                items: _dropDownMenuItems,
                onChanged: changedDropDownItem,
                
                 
              ),
         
                RaisedButton(
                  child: Text('Login'),
                   onPressed:(){
                  validateAndSubmit();
                  
   
                },
               color: Colors.green[300],
                  padding: const EdgeInsets.all(8.0),
                  textColor: Colors.white,
                  
                ),
                FlatButton(
                  child: Text('Register', style: TextStyle(fontSize: 15.0),),
                  onPressed: moveToRegisterScreen,
                ),
                FlatButton(
                  child: Text('View All Users'),
                  onPressed: moveToUsersViewScreen,
                ),
               FlatButton(
                  child: Text('View All farmers'),
                  onPressed: moveTofarmersViewScreen,
                ),
              ],
            ),
          )
        ]) )
        )
      );
  }
  void changedDropDownItem(String selectedrole) {
    setState(() {
      _person = selectedrole;
    });
  }


  bool validateLoginForm() {
    final FormState form = formkey.currentState;
    if (form.validate()) {
      form.save();
      // debugPrint('Email : $_email\nPassword: $_password');
      return true;
    }
    else
      return false;
  }
   void validateAndSubmit() async {
    if(validateLoginForm()) {
      // debugPrint('Validated the form');
      try {
        
                FirebaseUser user = await FirebaseAuth.instance.signInWithEmailAndPassword(
                email: _email,
                password: _password,
                
        
      );
      
    
      debugPrint('Successfully logged into user: ${user.uid}');
      
      }
      
      catch (error) {
        print('error: $error');
      }
    }
    else {
      debugPrint('Form not validated');
    }
  }
  
  void moveToRegisterScreen() {
    Navigator.push(context, MaterialPageRoute(builder: (context) {
      return RegisterPage();
    }));
  }

  void moveToUsersViewScreen() {
    Navigator.push(context, MaterialPageRoute(builder: (context) {
      return ViewUsers();
    }));
  }
  void moveTofarmersViewScreen() {
    Navigator.push(context, MaterialPageRoute(builder: (context) {
      return Viewfarmers();
    }));
  }

Widget logo(){
     return new Container(
       height:150,
       width:300,
       
         alignment: Alignment.center,
      decoration: new BoxDecoration(

      image: DecorationImage(
          image: AssetImage('images/flutter-icon.jpg'),
          fit: BoxFit.fill
      ),
    ),
     );

}
}
*/