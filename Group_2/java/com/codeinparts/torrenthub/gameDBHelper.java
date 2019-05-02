package com.codeinparts.torrenthub;

import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;
import android.util.Log;

public class gameDBHelper extends SQLiteOpenHelper {

    public static final String DATABASE_NAME="torrenthub";

    public static final int DATABASE_VERSION=1;

    public static final String CREATE_TABLE="create table "+games_Database.gameEntry.TABLE_NAME+
            "("+games_Database.gameEntry.COLUMN_NAME_GAME+" text ,"+ games_Database.gameEntry.COLUMN_NAME_LANGUAGE+" text,"+
            games_Database.gameEntry.COLUMN_NAME_SIZE+" text"+ ", "+games_Database.gameEntry.COLUMN_NAME_QUALITY+ " text"+
            ", "+games_Database.gameEntry.COLUMN_NAME_FILE_LOCATION+" text"+
            ");";

    public static final String DropTable = "drop table if exists "+games_Database.gameEntry.TABLE_NAME+";";


    public gameDBHelper(Context context){
        super(context,DATABASE_NAME,null,DATABASE_VERSION);
        Log.d("database operation","Database created...:)");
        System.out.print("Database Created sucessfully :) :)");
    }

    public void addGame(String game,String lang,String size,String quality,String Location,SQLiteDatabase db){

        System.out.println("\n\n\n\n Inserted Sucessfully \n\n\n\n");

        ContentValues contentValues=new ContentValues();
        contentValues.put(games_Database.gameEntry.COLUMN_NAME_GAME,game);
        contentValues.put(games_Database.gameEntry.COLUMN_NAME_LANGUAGE,lang);
        contentValues.put(games_Database.gameEntry.COLUMN_NAME_SIZE,size);
        contentValues.put(games_Database.gameEntry.COLUMN_NAME_QUALITY,quality);
        contentValues.put(games_Database.gameEntry.COLUMN_NAME_FILE_LOCATION,Location);
        db.insert(games_Database.gameEntry.TABLE_NAME,null,contentValues);

    }

    @Override
    public void onCreate(SQLiteDatabase db) {
        Log.d("database operation","Game Table sucessfully created...:)");
        System.out.print("Table Created sucessfully :) :)");
        db.execSQL(CREATE_TABLE);

    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        db.execSQL(DropTable);
        onCreate(db);
    }

    public Cursor readGames(SQLiteDatabase db){
        String[] projection={games_Database.gameEntry.COLUMN_NAME_GAME,games_Database.gameEntry.COLUMN_NAME_QUALITY,games_Database.gameEntry.COLUMN_NAME_LANGUAGE,games_Database.gameEntry.COLUMN_NAME_SIZE};
        Cursor cursor=db.query(games_Database.gameEntry.TABLE_NAME,projection,null,null,null,null,null);
        return cursor;
    }

}
