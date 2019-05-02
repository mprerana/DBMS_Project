import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';

import 'package:songs_app/app screens/profile/widgets.dart';
import 'package:songs_app/models/users.dart';
import 'package:songs_app/utils/database_files/usersCRUD.dart';

import 'package:songs_app/services/loader.dart';

// Profile Widget...
class Profile extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    return ProfileState();
  }
}

// Profile State...
class ProfileState extends State<Profile> {

  bool _isLoading = true;

  User _user;

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
    Map<String, dynamic> userMap = await UsersCRUD().getUserMapByEmail(emailid);
    User user = User.fromMaptoUser(userMap);
    return user;
  }

  Future<void> getUser() async {
    _user = await getUserFromEmail();
    setState(() {_isLoading = false;});
  }

  @override
  void initState() {
    super.initState();
    getUser();
  }

  @override
  Widget build(BuildContext context) {
    return _isLoading ? Loader() :
    WillPopScope(
      child: Scaffold(
        appBar: appBar(context),
        body: Column(
          children: <Widget>[
            // goBackButton(context),
            Stack(
              children: <Widget>[
                buildCoverPicture(),
                userImgName(context, 'assets/artists/duaLipa.jpg', _user.firstName, _user.email),
              ],
            ),
            
          ],
        ),
        backgroundColor: Colors.black,
      ),
      onWillPop: () {
        Navigator.of(context).pop();
      },
    );
  }
}
