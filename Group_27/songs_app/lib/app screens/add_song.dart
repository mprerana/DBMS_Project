import 'package:flutter/material.dart';

class AddSong extends StatefulWidget {
  
  @override
  State<StatefulWidget> createState() {
    return AddSongState();
  }
  
}

class AddSongState extends State<AddSong> {

  static var _genres = ['Love', 'Relegious', 'Romantic', 'Energetic', 'Melody'];

  TextEditingController titleController = TextEditingController();

  @override
  Widget build(BuildContext context) {

    TextStyle textStyle = Theme.of(context).textTheme.title;

    return Scaffold(
      appBar: AppBar(
        title: Text('Edit Song Details'),
      ),

      body: Padding(
        padding: EdgeInsets.only(top: 15.0, left: 10.0, right: 10.0),
        child: ListView(
          children: <Widget>[

            // Genre Selection...
            ListTile(
              title: DropdownButton(
                
                items: _genres.map(
                  (String dropDownString) {
                    return DropdownMenuItem(
                      value: dropDownString,
                      child: Text(dropDownString),
                    );
                  }
                ).toList(),

                style: textStyle,

                value: null,

                onChanged: (changedValue) {
                  setState(() {
                    debugPrint('User Selected $changedValue');
                  });
                },

              )
            ),

            // Song Name...
				    Padding(

					    padding: EdgeInsets.only(top: 15.0, bottom: 15.0),
					    
              child: TextField(
						    controller: titleController,  
						    style: textStyle,
						    onChanged: (value) {
						    	debugPrint('Song name changed in the field');
						    },
						    decoration: InputDecoration(
							    labelText: 'Song Name',
							    labelStyle: textStyle,
							    border: OutlineInputBorder(
								    borderRadius: BorderRadius.circular(5.0)
							    )
						    ),
					    ),

				    ),
            // .........................................................

            // Artist Name...
				    Padding(

					    padding: EdgeInsets.only(top: 15.0, bottom: 15.0),
					    
              child: TextField(
						    controller: titleController,  
						    style: textStyle,
						    onChanged: (value) {
						    	debugPrint('Artist name changed in the field');
						    },
						    decoration: InputDecoration(
							    labelText: 'Artist Name',
							    labelStyle: textStyle,
							    border: OutlineInputBorder(
								    borderRadius: BorderRadius.circular(5.0)
							    )
						    ),
					    ),

				    ),
            // .........................................................

            // Album Name...
				    Padding(

					    padding: EdgeInsets.only(top: 15.0, bottom: 15.0),
					    
              child: TextField(
						    controller: titleController,  
						    style: textStyle,
						    onChanged: (value) {
						    	debugPrint('Album name changed in the field');
						    },
						    decoration: InputDecoration(
							    labelText: 'Album name',
							    labelStyle: textStyle,
							    border: OutlineInputBorder(
								    borderRadius: BorderRadius.circular(5.0)
							    )
						    ),
					    ),

				    ),
            // .........................................................

            // Save & Cancel Buttons...
            Padding(

              padding: EdgeInsets.only(top: 15.0, bottom: 15.0),
              child: Row(
                children: <Widget>[
                  
                  Expanded(
                    child: RaisedButton(
                      
                      color: Theme.of(context).primaryColorDark,
                      textColor: Theme.of(context).primaryColorLight,
                      child: Text('Save', textScaleFactor: 1.5,),
                      onPressed: (){
                        setState(() {
                          debugPrint('Database Not yet added');
                        });
                      },

                    ),
                  ),

                  Expanded(
                    child: RaisedButton(
                      
                      color: Theme.of(context).primaryColorDark,
                      textColor: Theme.of(context).primaryColorLight,
                      child: Text('Cancel', textScaleFactor: 1.5,),
                      onPressed: (){
                        goToLastScreen();
                      },

                    ),
                  )
                
                ],
              ),

            )
            // .........................................................
            
          ],
        ),
      ),

    );
  }

  void goToLastScreen() {
    Navigator.pop(context, true);
  }

}