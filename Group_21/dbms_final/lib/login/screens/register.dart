
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:dbms_final/utils/dbhelper.dart';
import 'package:dbms_final/login/models/user.dart';
import 'package:dbms_final/login/screens/register1.dart';
import 'package:dbms_final/login/screens/register2.dart';
import 'package:dbms_final/login/screens/login.dart';
import 'package:dbms_final/utils/datbasefiles/usersCRUD.dart';
import 'styles.dart';
class RegisterPage extends StatefulWidget {
  
  @override
  State<StatefulWidget> createState() {
    return _RegisterPageState(); 
  }
}  

class _RegisterPageState extends State<RegisterPage> {
  
  DatabaseHelper databaseHelper = DatabaseHelper();
  final GlobalKey<FormState> formkey =GlobalKey<FormState>();
  
  String _email;
  String _password;
  String _usertype;
  String _firstname;
  String _lastname;
  String _streetname;
  String _pincode;
  String _state;
  String _city;
  String _mobileno;
DateTime selectedDate = DateTime.now();

  
List _persons =
  ["Farmer","Customer", "AgricultureExpert"];

  List<DropdownMenuItem<String>> _dropDownMenuItems;
  

  @override
  void initState() {
    _dropDownMenuItems = getDropDownMenuItems();
    _usertype = _dropDownMenuItems[0].value;
    super.initState();
  }

  List<DropdownMenuItem<String>> getDropDownMenuItems() {
    List<DropdownMenuItem<String>> items = new List();
    for (String person in _persons) {
      items.add(new DropdownMenuItem(
          value: person,
          child: new Text(person)
      ));
    }
    return items;
  }

  @override
  Widget build(BuildContext context) {
    return  new Scaffold(
         appBar: AppBar(
           backgroundColor: Color.fromRGBO(40,80, 40, 0.8),
        title: Text('Register Here'),
      ),
          body: new Container(
              decoration: new BoxDecoration(
                image: backgroundImage,
                
              ),
              
              child: new Container(
                padding: EdgeInsets.all(20.0),
                  decoration: new BoxDecoration(
                      gradient: new LinearGradient(
                    colors: <Color>[
                      const Color.fromRGBO(255,250, 250, 0.8),
                      const Color.fromRGBO(0, 0, 0, 0.9),
                    ],
                    stops: [0.2, 1.0],
                    begin: const FractionalOffset(0.0, 0.0),
                    end: const FractionalOffset(0.0, 1.0),
                  )),
                  child: new ListView(
                    padding: const EdgeInsets.all(0.0),
                    
                    children: <Widget>[
                      new Stack(
                        
                        alignment: AlignmentDirectional.bottomCenter,
                        children: <Widget>[
                          new Form(
                            key:formkey,
                            child:Column(
                            //mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                            children: <Widget>[
    
              TextFormField(
  decoration: InputDecoration(labelText: 'Email', icon: new Icon(
              Icons.email,
              color: Colors.grey,
            )),
                validator: (value) => value.isEmpty ? 'Email can\'t be empty' : null,
                onSaved: (value) {
                  _email = value;
                },
              ),
              TextFormField(
                decoration: InputDecoration(labelText: 'Password', icon: new Icon(
              Icons.lock,
              color: Colors.grey,
            ),),
                obscureText: true,
                validator: (value) => (value.isEmpty || value.length < 6) ? 'Password can\'t be empty and at least 6 letters' : null,
                onSaved: (value) {
                  _password = value;
                },
              ),
              
          TextFormField(decoration: new InputDecoration(
            labelText: 'Firstname',
            icon: new Icon(
              Icons.person,
              color: Colors.grey,
            )),
        validator: (value) => value.isEmpty ? 'firstname can\'t be empty' : null,
        onSaved: (value) => _firstname = value,
      ),
      TextFormField(decoration: new InputDecoration(
            labelText: 'Lastname',
            icon: new Icon(
              Icons.person,
              color: Colors.grey,
            )),
        validator: (value) => value.isEmpty ? 'Lastname can\'t be empty' : null,
        onSaved: (value) => _lastname = value,
      ),
      TextFormField(decoration: new InputDecoration(
            labelText: 'Phone',
            icon: new Icon(
              Icons.phone,
              color: Colors.grey,
            )),
         validator: (value) => (value.isEmpty || value.length != 10) ? 'Mobile Number can\'t be empty' : null,
        onSaved: (value) => _mobileno = value,
      ),
      TextFormField(decoration: new InputDecoration(
            labelText: 'Streetname',
            icon: new Icon(
              Icons.streetview,
              color: Colors.grey,
            )),
        validator: (value) => value.isEmpty ? 'Streetname can\'t be empty' : null,
        onSaved: (value) => _streetname = value,
      ),
       TextFormField(decoration: new InputDecoration(
            labelText: 'City',
            icon: new Icon(
              Icons.location_city,
              color: Colors.grey,
            )),
        validator: (value) => value.isEmpty ? 'City Name can\'t be empty' : null,
        onSaved: (value) => _city = value,
      ),

    TextFormField(decoration: new InputDecoration(
            labelText: 'State',
            icon: new Icon(
              Icons.location_city,
              color: Colors.grey,
            )),
        validator: (value) => value.isEmpty ? 'State Name can\'t be empty' : null,
        onSaved: (value) => _state = value,
      ),
      TextFormField(
        keyboardType: TextInputType.number,
        decoration: new InputDecoration(
            labelText: 'pincode',
            icon: new Icon(
              Icons.confirmation_number,
              color: Colors.grey,
            )),
        validator: (value) => (value.isEmpty)? 'enter valid pincode' : null,
        onSaved: (value) => _pincode = value,
      
      ),
      
      
         
       
              
              new DropdownButton(
                value: _usertype,
                items: _dropDownMenuItems,
                onChanged: changedDropDownItem,
                 
              ),
         
        new SizedBox(
           width:250,
               child:
       
    
              RaisedButton(
                child: Text('Create account'),
                shape: new RoundedRectangleBorder(borderRadius: new BorderRadius.circular(30.0)),
                onPressed:(){
             validateAndSubmit();
                        } ,
                color: Color.fromRGBO(40,80,40,0.8),
                  padding: const EdgeInsets.all(8.0),
                  textColor: Colors.white30,
  
              ),)
            
                            ],
                          ),
                          
                          )],
                          
                      ),
                    ],
                      
                  ))),
        );
  }
  void changedDropDownItem(String selectedrole) {
    setState(() {
      _usertype = selectedrole;
    });
  }
bool validateLoginForm() {
  final FormState form = formkey.currentState;
  if (form.validate()) {
    form.save();
    return true;
  }
  else
    return false;
  }

  void validateAndSubmit() async {
    if(validateLoginForm()) {
      debugPrint('Validated the form');
      try {
        FirebaseUser user = await FirebaseAuth.instance.createUserWithEmailAndPassword(
        email: _email,
        password: _password,
        
      
        );
        debugPrint('successfully registered User : ${user.uid}');
        _saveUserToDatabase(user);
      }
      catch (error) {
         
        print('error: '+error);
       
      }
    }
  }

  void _saveUserToDatabase(FirebaseUser fuser) async {
    // Navigator.pop(context);
    User user = User(fuser.email, _password,_firstname,_lastname,_streetname,_city,_state,_pincode,_usertype,_mobileno);
     int result = await Usercrudoperations().insertUser(user);
    
    if(result == 0) {
      _showAlertDialog('Status','Problem saving user to database');
    }
    else {
      
      if(_usertype=='Farmer'){
                   
              
                    Navigator.of(context)
                .push(MaterialPageRoute<Null>(builder: (BuildContext context) {
              return new RegisterPage1();
            
                }
                )
                );
                  }
                  
                  else if (_usertype=='AgricultureExpert'){
              
                     Navigator.of(context)
                .push(MaterialPageRoute<Null>(builder: (BuildContext context) {
              return new RegisterPage2();
            
                }
                )
                );
                
    }
    else{
      Navigator.of(context)
                .push(MaterialPageRoute<Null>(builder: (BuildContext context) {
              return new LoginPage();
            
                }
                )
                );
    }
  }
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
      }
    );
  }
}
