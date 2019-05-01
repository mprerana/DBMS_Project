import 'package:flutter/material.dart';

class myItems extends StatelessWidget {
  final String txt;
  final IconData icon;
  final int color;
  final String nav;

  myItems(this.icon, this.txt, this.color, [this.nav = null]);

  notify(BuildContext context){
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
            title: Text('alert box'),
            content: Text(txt),
            actions: <Widget>[
              FlatButton(
                child: Text('discard'),
                onPressed: () {
                  Navigator.pop(context);
                },
              ),
              FlatButton(
                child: Text('delete'),
                onPressed: () {
                  Navigator.pop(context);
                },
              ),
            ]);
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    // TODO: implement build
    return GestureDetector(
      onDoubleTap: (){
        notify(context);
      },
      onTap: (){
        if(nav != null){
          print('push huya at ${nav}');
          Navigator.pushNamed(context, nav);
        }
      },
      child: Material(
        color: Colors.white,
        elevation: 14.0,
        shadowColor: Color(0x802196F3),
        borderRadius: BorderRadius.circular(24.0),
        child: Center(
          child: Padding(
            padding: const EdgeInsets.all(8.0),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: <Widget>[
                    Text(
                      txt,
                      style: TextStyle(color: new Color(color), fontSize: 20.0),
                    ),

                    //icon

                    Material(
                      color: new Color(color),
                      borderRadius: BorderRadius.circular(24.0),
                      child: Padding(
                        padding: const EdgeInsets.all(16.0),
                        child: Icon(
                          icon,
                          color: Colors.white,
                          size: 30.0,
                        ),
                      ),
                    )
                  ],
                )
              ],
            ),
          ),
        ),
      ),
    );
  }
}
