package com.codeinparts.torrenthub;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ImageView;
import android.widget.TextView;

import com.squareup.picasso.Picasso;

import java.util.ArrayList;
import java.util.List;
import java.util.zip.Inflater;

public class movieAdapter extends BaseAdapter {
    //private ArrayList<movieStruct2> movieStructArrayList=new ArrayList<movieStruct2>();
    private List<movieStruct2> movieList= new ArrayList<movieStruct2>();
    private Context cntx;
    private Activity activity;
    private Session session;
    public movieAdapter(Context context, Activity activity2 ,List<movieStruct2> movieStruct2s){
        this.cntx=context;
        this.activity=activity2;
        this.movieList=movieStruct2s;
        this.session=new Session(context);

    }
    @Override
    public int getCount() {
        return movieList.size() ;
    }

    @Override
    public Object getItem(int position) {
        return null;
    }

    @Override
    public long getItemId(int position) {
        return 0;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        View v;
        System.out.print(position);

            final movieStruct2 movieStruct= (movieStruct2) movieList.get(position);
            System.out.print(movieStruct);
            LayoutInflater inflater = LayoutInflater.from(cntx);
            v = inflater.inflate(R.layout.tranding_movies, parent, false);
            ImageView imageView_movie_poster=v.findViewById(R.id.movie_poster);
            TextView textView_movie_name=v.findViewById(R.id.movie_name);
            TextView textView_movie_year=v.findViewById(R.id.movie_year);
            TextView textView_movie_quality=v.findViewById(R.id.movie_quality);
            Picasso.with(this.cntx).load(movieStruct.getPosterImg()).into(imageView_movie_poster);
            textView_movie_name.setText(movieStruct.getMovieName());
            textView_movie_quality.setText(movieStruct.getQuality());
            textView_movie_year.setText(movieStruct.getYear()+"");
            v.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {

                    Intent intent=new Intent(activity,movie_description.class);
                    intent.putExtra("movie_pass",movieStruct.getMovieName());
                    activity.startActivity(intent);


                }
            });
        return v;
    }
}
