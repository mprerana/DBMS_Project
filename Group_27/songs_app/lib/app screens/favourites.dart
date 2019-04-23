import 'package:flutter/material.dart';

class Favourites extends StatefulWidget {
  @override
  State<StatefulWidget> createState(){
    return FavouritesState();
  }
}

class FavouritesState extends State<Favourites> {

  int count = 0;
  
  @override

  Widget build(BuildContext context) {
    return Scaffold(

      appBar: AppBar(
        title: Text('Online Music Store'),
      ),
      body: musicListView(),

      floatingActionButton: FloatingActionButton(
		    
        onPressed: () {
		      debugPrint('FAB clicked');
		    },
		    tooltip: 'Add Music',
		    child: Icon(Icons.add),

	    ),

    );
  }

  ListView musicListView() {
    
    TextStyle titleStyle = Theme.of(context).textTheme.subhead;

    return ListView.builder(

      itemCount: count,
      itemBuilder: (BuildContext context, int position){
        return Card(
          color: Colors.white,
          elevation: 2.0,
          child: ListTile(

            leading: CircleAvatar(
              backgroundColor: Colors.teal,
              child: Icon(Icons.play_circle_outline),
            ),
            title: Text('Title', style: titleStyle,),
            subtitle: Text('Subtitle'),
            trailing: Icon(Icons.thumb_up),

            onLongPress: () {
              debugPrint('Song not yet added to database!');
            },

          ),
        );
      },
    
    );
  }

}