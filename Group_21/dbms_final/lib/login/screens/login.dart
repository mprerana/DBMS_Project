import 'package:dbms_final/agricultureexpert/agriculture.dart';
import 'package:flutter/material.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:dbms_final/login/screens/register.dart';
import 'package:dbms_final/login/screens/view_users.dart';
import 'package:dbms_final/farmer/screens/farmerinterface.dart';
import 'package:dbms_final/login/screens/view_farmer.dart';
import 'package:dbms_final/login/screens/viewagricultures.dart';
import 'styles.dart';
import '../../Components/WhiteTick.dart';
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
  List _persons =
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
    return Scaffold(
        appBar: AppBar(
           backgroundColor: Color.fromRGBO(40,80, 40, 0.8),
        title: Text('Login Here'),
      ),
          body: new Container(
              decoration: new BoxDecoration(
                image: backgroundImage,
                
              ),
              
              child: new Container(

                padding: EdgeInsets.fromLTRB(20.0,0,20,0),
                  decoration: new BoxDecoration(
                      gradient: new LinearGradient(
                    colors: <Color>[
                      const Color.fromRGBO(255,250, 250, 0.8),
                      const Color.fromRGBO(255, 255, 255, 0.9),
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
    
                 Tick(image: tick),
                TextFormField(
                  cursorColor: Color.fromRGBO(40, 80, 40, 0.8),
                  
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
         new SizedBox(
           width:250,
               child: RaisedButton(
                  child: Text('Login'),
                  
                  shape: new RoundedRectangleBorder(borderRadius: new BorderRadius.circular(30.0)),
                   onPressed:(){
                  validateAndSubmit();
                  
   
                },
               color: Color.fromRGBO(40, 80, 40, 0.8),
                  padding: const EdgeInsets.all(8.0),
                  textColor: Colors.white30,
                  
                ),),
                                FlatButton(
                                  textColor: Colors.white30,
                  child: Text('dont have an account? Register', style: TextStyle(fontSize: 15.0),),
                  onPressed: moveToRegisterScreen,
                ),
                FlatButton(
                  child: Text('View All Users'),
                  textColor: Colors.white30,
                  onPressed: moveToUsersViewScreen,
                ),
               FlatButton(
                  child: Text('View All farmers'),
                  textColor: Colors.white30,
                  onPressed: moveTofarmersViewScreen,
                ),
                FlatButton(
                  child: Text('View All agricultures'),
                  textColor: Colors.white30,
                  onPressed: moveToagriculturesViewScreen,
                ),
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
       if(_person=='Farmer')
      {
        print('enterd into farmer intrefcae');
          Navigator.of(context)
                .push(MaterialPageRoute<Null>(builder: (BuildContext context) {
              return new Farmerinterface();
                }
                )
                );
                  
      }
     else if(_person=='AgricultureExpert')
      {
        print('enterd into agriculture intrefcae');
          Navigator.of(context)
                .push(MaterialPageRoute<Null>(builder: (BuildContext context) {
              return new Viewagro();
                }
                )
                );
                  
      }
    else{
       print('enterd into customer intrefcae');
          Navigator.of(context)
                .push(MaterialPageRoute<Null>(builder: (BuildContext context) {
              return new Viewagro();
                }
                )
                );
       

    }
    
     
      
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
void moveToagriculturesViewScreen() {

    Navigator.push(context, MaterialPageRoute(builder: (context) {
      return Viewagricultures();
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
