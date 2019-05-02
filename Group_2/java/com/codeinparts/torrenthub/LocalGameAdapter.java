package com.codeinparts.torrenthub;

import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.support.annotation.NonNull;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import java.util.ArrayList;

public class LocalGameAdapter extends RecyclerView.Adapter<LocalGameAdapter.gameHolder> {
    private Context context;
    private ArrayList<LocalGameAdapter.localGameStruct> localGameStructs=new ArrayList<LocalGameAdapter.localGameStruct>();
    public LocalGameAdapter(Context context){
        this.context=context;
        readData();
    }
    @NonNull
    @Override
    public LocalGameAdapter.gameHolder onCreateViewHolder(@NonNull ViewGroup viewGroup, int i) {
        LayoutInflater inflater=LayoutInflater.from(context);
        System.out.print("readData called");

        return new LocalGameAdapter.gameHolder(inflater.inflate(R.layout.game_list,viewGroup,false));
    }

    @Override
    public void onBindViewHolder(@NonNull LocalGameAdapter.gameHolder viewHolder, int i) {
        LocalGameAdapter.localGameStruct gameStruct=localGameStructs.get(i);
        viewHolder.game.setText(gameStruct.getGame_name());
        viewHolder.Size.setText("Size : "+gameStruct.getSize());
    }

    @Override
    public int getItemCount() {
        System.out.print("\n\n\n\n"+localGameStructs.size()+"\n\n\n");
        return
                localGameStructs.size();
    }

    public class gameHolder extends RecyclerView.ViewHolder{
        public TextView game,Size,Qlty,Lang;
        public gameHolder(@NonNull View itemView) {
            super(itemView);
            game=itemView.findViewById(R.id.gameName);
            Size=itemView.findViewById(R.id.size);
        }
    }

    public class localGameStruct{
        private String game_name,size;
        public localGameStruct(String a,String d){
            this.game_name=a;
            this.size=d;
        }



        public String getGame_name() {
            return game_name;
        }

        public String getSize() {
            return size;
        }


        public void setGame_name(String game_name) {
            this.game_name = game_name;
        }

        public void setSize(String size) {
            this.size = size;
        }
    }

    public void readData(){
        gameDBHelper dbHelper=new gameDBHelper(this.context);
        System.out.print("In Here");
        SQLiteDatabase db=dbHelper.getReadableDatabase();

        Cursor cursor = dbHelper.readGames(db);

        while (cursor.moveToNext()){
            localGameStructs.add(new localGameStruct(cursor.getString(cursor.getColumnIndex(games_Database.gameEntry.COLUMN_NAME_GAME)),
                    cursor.getString(cursor.getColumnIndex(games_Database.gameEntry.COLUMN_NAME_SIZE))));
        }
    }

}
























