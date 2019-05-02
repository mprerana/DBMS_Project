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

public class gameAdapter extends BaseAdapter {
    //private ArrayList<gameStruct2> gameStructArrayList=new ArrayList<gameStruct2>();
    private List<gameStruct2> gameList= new ArrayList<gameStruct2>();
    private Context cntx;
    private Activity activity;
    private Session session;
    public gameAdapter(Context context, Activity activity2 ,List<gameStruct2> gameStruct2s){
        this.cntx=context;
        this.activity=activity2;
        this.gameList=gameStruct2s;
        this.session=new Session(context);

    }
    @Override
    public int getCount() {
        return gameList.size() ;
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

        final gameStruct2 gameStruct= (gameStruct2) gameList.get(position);
        System.out.print(gameStruct);
        LayoutInflater inflater = LayoutInflater.from(cntx);
        v = inflater.inflate(R.layout.tranding_games, parent, false);
        ImageView imageView_game_poster=v.findViewById(R.id.game_poster);
        TextView textView_game_name=v.findViewById(R.id.game_name);
        TextView textView_game_year=v.findViewById(R.id.game_year);
        TextView textView_game_quality=v.findViewById(R.id.game_quality);
        Picasso.with(this.cntx).load(gameStruct.getPosterImg()).into(imageView_game_poster);
        textView_game_name.setText(gameStruct.getgameName());
        textView_game_quality.setText(gameStruct.getQuality());
        textView_game_year.setText(gameStruct.getYear()+"");
        v.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                Intent intent=new Intent(activity,game_description.class);
                intent.putExtra("game_pass",gameStruct.getgameName());
                activity.startActivity(intent);


            }
        });
        return v;
    }
}
