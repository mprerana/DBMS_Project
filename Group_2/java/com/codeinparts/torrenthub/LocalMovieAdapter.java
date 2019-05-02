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

public class LocalMovieAdapter extends RecyclerView.Adapter<LocalMovieAdapter.movieHolder> {
    private Context context;
    private ArrayList<LocalMovieAdapter.localMovieStruct> localMovieStructs=new ArrayList<LocalMovieAdapter.localMovieStruct>();
    public LocalMovieAdapter(Context context){
        this.context=context;
        readData();
    }
    @NonNull
    @Override
    public LocalMovieAdapter.movieHolder onCreateViewHolder(@NonNull ViewGroup viewGroup, int i) {
        LayoutInflater inflater=LayoutInflater.from(context);
        System.out.print("readData called");

        return new LocalMovieAdapter.movieHolder(inflater.inflate(R.layout.movie_list,viewGroup,false));
    }

    @Override
    public void onBindViewHolder(@NonNull LocalMovieAdapter.movieHolder viewHolder, int i) {
        LocalMovieAdapter.localMovieStruct movieStruct=localMovieStructs.get(i);
        viewHolder.movie.setText(movieStruct.getMovie_name());
        viewHolder.Size.setText("Size : "+movieStruct.getSize());
        viewHolder.Qlty.setText("Quality : "+movieStruct.getQuality());
        viewHolder.Lang.setText("Language : "+movieStruct.getLanguage());


    }

    @Override
    public int getItemCount() {
        System.out.print("\n\n\n\n"+localMovieStructs.size()+"\n\n\n");
        return
                localMovieStructs.size();
    }

    public class movieHolder extends RecyclerView.ViewHolder{
        public TextView movie,Size,Qlty,Lang;
        public movieHolder(@NonNull View itemView) {
            super(itemView);
            movie=itemView.findViewById(R.id.movieName);
            Size=itemView.findViewById(R.id.size);
            Qlty=itemView.findViewById(R.id.Quality);
            Lang=itemView.findViewById(R.id.language);
        }
    }

    public class localMovieStruct{
        private String movie_name,Quality,size,language;
        public localMovieStruct(String a,String b,String c, String d){
            this.movie_name=a;
            this.Quality=b;
            this.language=c;
            this.size=d;
        }

        public String getQuality() {
            return Quality;
        }

        public String getLanguage() {
            return language;
        }

        public String getMovie_name() {
            return movie_name;
        }

        public String getSize() {
            return size;
        }

        public void setQuality(String quality) {
            Quality = quality;
        }

        public void setLanguage(String language) {
            this.language = language;
        }

        public void setMovie_name(String movie_name) {
            this.movie_name = movie_name;
        }

        public void setSize(String size) {
            this.size = size;
        }
    }

    public void readData(){
        movieDBHelper dbHelper=new movieDBHelper(this.context);
        System.out.print("In Here");
        SQLiteDatabase db=dbHelper.getReadableDatabase();

        Cursor cursor = dbHelper.readMovies(db);

        while (cursor.moveToNext()){
            localMovieStructs.add(new localMovieStruct(cursor.getString(cursor.getColumnIndex(movies_Database.movieEntry.COLUMN_NAME_MOVIE)),
                    cursor.getString(cursor.getColumnIndex(movies_Database.movieEntry.COLUMN_NAME_QUALITY)),
                    cursor.getString(cursor.getColumnIndex(movies_Database.movieEntry.COLUMN_NAME_LANGUAGE)),
                    cursor.getString(cursor.getColumnIndex(movies_Database.movieEntry.COLUMN_NAME_SIZE))));
        }
    }

}
























