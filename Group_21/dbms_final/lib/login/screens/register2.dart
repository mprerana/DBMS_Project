import 'package:flutter/material.dart';
import 'package:dbms_final/utils/dbhelper.dart';
import 'package:dbms_final/login/models/agro.dart';
import 'package:dbms_final/login/screens/login.dart';
import 'package:dbms_final/utils/datbasefiles/agrocrud.dart';
import 'package:dbms_final/utils/datbasefiles/usersCRUD.dart';
import 'styles.dart';
class RegisterPage2 extends StatefulWidget {
  
  @override
  State<StatefulWidget> createState() {
    return _RegisterPageState2();
  }
}  

class _RegisterPageState2 extends State<RegisterPage2> {
  DatabaseHelper databaseHelper = DatabaseHelper();
  final GlobalKey<FormState> formkey =GlobalKey<FormState>();
 String _qualifications;

  @override
  Widget build(BuildContext context) {
return Scaffold(
       resizeToAvoidBottomPadding: false,

     appBar: AppBar(
           backgroundColor: Color.fromRGBO(40,80, 40, 0.8),
        title: Text('Qualifications'),
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
                            child:
                            new Column(
                            children: <Widget>[
              TextFormField(

               
                
                decoration: InputDecoration(labelText: 'qualifications', icon: new Icon(
              Icons.school,
              color: Colors.grey,
            )),
                validator: (value) => value.isEmpty ? 'fields can\'t be empty' : null,
                onSaved: (value) {
                  _qualifications=value;
                },
              ),
              new SizedBox(
           width:250,
               child:
             RaisedButton(
                child: Text('Create agroexpert account'),
                shape: new RoundedRectangleBorder(borderRadius: new BorderRadius.circular(30.0)),
                onPressed:(){
                  validateAndSubmit();
                  Navigator.of(context)
                .push(MaterialPageRoute<Null>(builder: (BuildContext context) {
              return new LoginPage();
            
                }
                )
                );
                  
   
                },
                color: Color.fromRGBO(40,80,40,0.8),
                  padding: const EdgeInsets.all(8.0),
                  textColor: Colors.white,
  
              ), )
            ],
                          ),
                          
                          )],
                          
                      ),
                    ],
                      
                  ))),
        );
  }
  void _saveUserToDatabase() async {
    // Navigator.pop(context);
    int dummyid = await Usercrudoperations().getid();
    Agro expert1 =Agro(dummyid,_qualifications);
    
    
    int result = await Agrocrudoperations().insertagro(expert1);

    if(result == 0) {
      _showAlertDialog('Status','Problem saving user to database');
    }
    else {
      _showAlertDialog('Status','Successfully saved user to database');
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
        debugPrint('successfully registered User');
        _saveUserToDatabase();
      }
      
    }


}