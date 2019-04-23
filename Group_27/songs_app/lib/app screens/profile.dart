import 'package:flutter/material.dart';

// import 'package:songs_app/app screens/home.dart';

class Profile extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    return ProfileState();
  }
}

// Profile State...
class ProfileState extends State<Profile> {
  @override
  Widget build(BuildContext context) {

    Size screenSize = MediaQuery.of(context).size;
    String userName = 'Dua Lipa';
    String email = 'dualipa@gmail.com';

    return Scaffold(
      body: Stack(
        children: <Widget>[
          
          buildCoverPicture(),
          SafeArea(
            child: SingleChildScrollView(
              child: Column(
                children: <Widget>[
                  SizedBox(height: screenSize.height / 6.4,),
                  Row(
                    children: <Widget>[

                      buildProfilePicture(),
                      Container(
                        margin: EdgeInsets.only(left: 30, top: 30),
                        child: Column(
                          children: <Widget>[

                            Text(
                              userName.toUpperCase(),
                              style: TextStyle(
                                fontSize: (screenSize.width * 1.35) / userName.length,
                                fontFamily: 'Halfomania-Regular', 
                                fontWeight: FontWeight.bold, 
                                color: Colors.white
                              ),
                            ),
                            Text(
                              email,
                              style: TextStyle(
                                fontFamily: 'Magnificent',
                                fontSize: (screenSize.width * 0.65) / email.length,
                                color: Colors.white
                              ),
                            )

                          ],
                        ),
                      ),

                    ],
                  ),
                ],
              ),
            ),
          ),
          
        ],
      ),
      backgroundColor: Colors.black,
    );
  }

  // Cover Picture...
  Widget buildCoverPicture() {
    return Container(
      child: Image.asset('assets/msc-bg-3.jpg', fit: BoxFit.cover, width: double.infinity, height: 250,),
    );
  }

  // Profile Picture...
  Widget buildProfilePicture() {
    return Container(
      margin: EdgeInsets.only(left: 20),
      width: 140.0,
      height: 140.0,
      decoration: BoxDecoration(
        image: DecorationImage(
          image: AssetImage('assets/artists/duaLipa.jpg'),
          fit: BoxFit.cover
        ),
        borderRadius: BorderRadius.circular(80),
        border: Border.all(
          color: Colors.white,
          width: 5.0,
        )
      ),
    );
  }
}
