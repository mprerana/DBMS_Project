package com.codeinparts.torrenthub;

import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;
import android.os.DropBoxManager;
import android.util.Log;

public class movieDBHelper extends SQLiteOpenHelper {

    public static final String DATABASE_NAME="torrenthub";

    public static final int DATABASE_VERSION=1;

    public static final String CREATE_TABLE="create table "+movies_Database.movieEntry.TABLE_NAME+
            "("+movies_Database.movieEntry.COLUMN_NAME_MOVIE+" text ,"+ movies_Database.movieEntry.COLUMN_NAME_LANGUAGE+" text,"+
            movies_Database.movieEntry.COLUMN_NAME_SIZE+" text"+ ", "+movies_Database.movieEntry.COLUMN_NAME_QUALITY+ " text"+
            ", "+movies_Database.movieEntry.COLUMN_NAME_FILE_LOCATION+" text"+
            ");";

    public static final String DropTable = "drop table if exists "+movies_Database.movieEntry.TABLE_NAME+";";


    public movieDBHelper(Context context){
        super(context,DATABASE_NAME,null,DATABASE_VERSION);
        Log.d("database operation","Database created...:)");
        System.out.print("Database Created sucessfully :) :)");
    }

    public void addMovie(String movie,String lang,String size,String quality,String Location,SQLiteDatabase db){

        System.out.println("\n\n\n\n Inserted Sucessfully \n\n\n\n");

        ContentValues contentValues=new ContentValues();
        contentValues.put(movies_Database.movieEntry.COLUMN_NAME_MOVIE,movie);
        contentValues.put(movies_Database.movieEntry.COLUMN_NAME_LANGUAGE,lang);
        contentValues.put(movies_Database.movieEntry.COLUMN_NAME_SIZE,size);
        contentValues.put(movies_Database.movieEntry.COLUMN_NAME_QUALITY,quality);
        contentValues.put(movies_Database.movieEntry.COLUMN_NAME_FILE_LOCATION,Location);
        db.insert(movies_Database.movieEntry.TABLE_NAME,null,contentValues);

    }

    @Override
    public void onCreate(SQLiteDatabase db) {
        Log.d("database operation","Movie Table sucessfully created...:)");
        System.out.print("Table Created sucessfully :) :)");
        db.execSQL(CREATE_TABLE);

    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        db.execSQL(DropTable);
        onCreate(db);
    }

    public Cursor readMovies(SQLiteDatabase db){
        String[] projection={movies_Database.movieEntry.COLUMN_NAME_MOVIE,movies_Database.movieEntry.COLUMN_NAME_QUALITY,movies_Database.movieEntry.COLUMN_NAME_LANGUAGE,movies_Database.movieEntry.COLUMN_NAME_SIZE};
        Cursor cursor=db.query(movies_Database.movieEntry.TABLE_NAME,projection,null,null,null,null,null);
        return cursor;
    }

}
