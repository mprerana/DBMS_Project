import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:splash_tokenauth/common/apifunctions/requestLoginAPI.dart';
import 'package:flutter/services.dart';


class LoginScreen extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    return new LoginScreenState();
  }
}

class LoginScreenState extends State<LoginScreen> {

  final TextEditingController _userNameController = TextEditingController();
  final TextEditingController _passwordController = TextEditingController();

  @override
  void initState() {
    super.initState();
    _saveCurrentRoute("/LoginScreen");
  }

  _saveCurrentRoute(String lastRoute) async {
    SharedPreferences preferences = await SharedPreferences.getInstance();
    await preferences.setString('LastScreenRoute', lastRoute);
  }

  Widget _showLogo(){
    return new Hero(
      tag: 'hero' ,
      child: Padding(
        padding: EdgeInsets.fromLTRB(80.0, 0.0, 80.0, 0.0),
        child: Image.asset('assets/quazapp_logo1.jpg'),
      ),
    );
  }


  @override
  Widget build(BuildContext context) {
    return WillPopScope(
      onWillPop: () {
        if(Navigator.canPop(context)) {
          Navigator.of(context).pushNamedAndRemoveUntil('/HomeScreen', (Route<dynamic> route) => false);
        } else {
          Navigator.of(context).pushReplacementNamed('/HomeScreen');
        }
      },
      child: Scaffold(
        appBar:  AppBar(
          title: Text("LOGIN",
            style: TextStyle(fontSize: 30.0, color: Colors.white,),
          ),
          centerTitle: true,
          backgroundColor: Colors.blue,
        ),

        backgroundColor: Colors.white,

        body: Container(
          child: Padding(
            padding: EdgeInsets.fromLTRB(30.0, 0.0, 30.0, 0.0),
            child: ListView(
              children: <Widget>[
                Container(alignment: Alignment.topCenter,
                    child: Padding(padding: EdgeInsets.fromLTRB(0.0, 25.0, 0.0, 10.0),
                      child: Text("QuazApp", style: TextStyle(fontSize: 40.0, color: Colors.blue),),
                    )
                ),
                _showLogo(),


                Padding(padding: EdgeInsets.fromLTRB(0.0, 0.0, 0.0, 10.0),
                  child: RichText(
                    text: TextSpan( text: "Login" ),
                  ),
                ),
                Padding(
                  padding: EdgeInsets.fromLTRB(0.0, 0.0, 0.0, 0.0),
                  child: TextField(
                    controller: _userNameController,
                    decoration: InputDecoration(
                      labelText: "Email",
                    ),
                    style: TextStyle(fontSize: 22.0, color: Colors.black, fontWeight: FontWeight.bold, ),
                  ),
                ),

                Padding(
                  padding: EdgeInsets.fromLTRB(0.0, 10.0, 0.0, 0.0),
                  child: TextField(
                    controller: _passwordController,
                    decoration: InputDecoration(
                      labelText: 'Password',
                    ),
                    obscureText: true,
                    style: TextStyle(fontSize: 22.0, color: Colors.black, fontWeight: FontWeight.bold, ),
                  ),
                ),

                Padding(
                  padding: EdgeInsets.fromLTRB(70.0, 70.0, 70.0, 0.0),
                  child: Container(height: 50.0,
                    child: RaisedButton(
                        onPressed: () {
                          SystemChannels.textInput.invokeMethod('TextInput.hide');
                          requestLoginAPI(context, _userNameController.text, _passwordController.text);
                        },
                        child: Text("LOGIN", style: TextStyle(color: Colors.white, fontSize: 22.0)
                        ),
                      color: Colors.blue,
                    ),
                  ),
                ),
                 Padding(
                  padding: EdgeInsets.fromLTRB(40.0, 10.0, 40.0, 0.0),
                  child: Container(height: 70.0,
                    child: Opacity(opacity: 0.8, child: RaisedButton(
                        disabledColor: Colors.blue,
                        onPressed: () {
                          SystemChannels.textInput.invokeMethod('TextInput.hide');
                          Navigator.of(context).pushReplacementNamed('/SignupScreen');
                        },
                        child: Text("Don't have an Account?\n              Sign Up", style: TextStyle(color: Colors.white, fontSize: 20.0)
                        ),
                      color: Colors.blue,
                    ),
                    )
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}

