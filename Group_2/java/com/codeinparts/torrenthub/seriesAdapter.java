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

public class seriesAdapter extends BaseAdapter {
    //private ArrayList<seriesStruct2> seriesStructArrayList=new ArrayList<seriesStruct2>();
    private List<seriesStruct2> seriesList= new ArrayList<seriesStruct2>();
    private Context cntx;
    private Activity activity;
    private Session session;
    public seriesAdapter(Context context, Activity activity2 , List<seriesStruct2> seriesStruct2s){
        this.cntx=context;
        this.activity=activity2;
        this.seriesList=seriesStruct2s;
        this.session=new Session(context);

    }
    @Override
    public int getCount() {
        return seriesList.size() ;
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

            final seriesStruct2 seriesStruct= (seriesStruct2) seriesList.get(position);
            System.out.print(seriesStruct);
            LayoutInflater inflater = LayoutInflater.from(cntx);
            v = inflater.inflate(R.layout.tranding_series, parent, false);
            ImageView imageView_series_poster=v.findViewById(R.id.series_poster);
            TextView textView_series_name=v.findViewById(R.id.series_name);
            TextView textView_series_year=v.findViewById(R.id.series_year);
            TextView textView_series_quality=v.findViewById(R.id.series_quality);
            Picasso.with(this.cntx).load(seriesStruct.getPosterImg()).into(imageView_series_poster);
            textView_series_name.setText(seriesStruct.getseriesName());
            textView_series_quality.setText(seriesStruct.getQuality());
            textView_series_year.setText(seriesStruct.getYear()+"");
            v.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {

                    Intent intent=new Intent(activity,series_discription.class);
                    intent.putExtra("series_pass",seriesStruct.getseriesName());
                    activity.startActivity(intent);


                }
            });
        return v;
    }
}
