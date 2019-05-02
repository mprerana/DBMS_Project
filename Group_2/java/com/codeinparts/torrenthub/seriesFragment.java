package com.codeinparts.torrenthub;
import android.content.Intent;
import android.os.Bundle;
import android.support.constraint.ConstraintLayout;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.AbsListView;
import android.widget.AdapterView;
import android.widget.GridView;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;


public class seriesFragment extends Fragment {
    private Session session;
    private  Boolean loadmore=true,stopLoading=false;
    private seriesAdapter seriesAdapter0;
    private RequestQueue requestQueue;
    private List<seriesStruct2> seriesList;
    private  GridView gridView;
    private ArrayList seriesStructArrayList=new ArrayList<seriesStruct2>();
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        View v = inflater.inflate(R.layout.fragment_series, container, false);
        gridView=v.findViewById(R.id.gridview_series);
        session=new Session(getContext());
        requestQueue= Volley.newRequestQueue(getContext());
        getInfo();
        /*this.seriesStructArrayList.add(new seriesStruct2("Aquaman","1.jpg","1080p HD",2019));
        this.seriesStructArrayList.add(new seriesStruct2("Bumblebee","8.jpg","1080p HD",2018));
        this.seriesStructArrayList.add(new seriesStruct2("Triple threat","9.jpg","1080p HD",2018));
        this.seriesStructArrayList.add(new seriesStruct2("Mortal Engines","2.jpg","1080p HD",2019));
        this.seriesStructArrayList.add(new seriesStruct2("Fantastic Beast The crimes of grindelwald","3.jpg","1080p HD",2019));
        this.seriesStructArrayList.add(new seriesStruct2("Spider Man Into the the spider-verse","4.jpg","1080p HD",2019));
        this.seriesStructArrayList.add(new seriesStruct2("Pokemon Detective Pikachu","5.jpg","1080p HD",2019));
        this.seriesStructArrayList.add(new seriesStruct2("Total Dhamaal","6.jpg","1080p HD",2019));
        this.seriesStructArrayList.add(new seriesStruct2("URI The surgical Strike","7.jpg","1080p HD",2019));
        this.seriesStructArrayList.add(new seriesStruct2("Captain Marvel","8.jpeg","1080p HD",2019));*/

        /*gridView.setOnScrollListener(new AbsListView.OnScrollListener() {
            @Override
            public void onScrollStateChanged(AbsListView view, int scrollState) {

            }

            @Override
            public void onScroll(AbsListView view, int firstVisibleItem, int visibleItemCount, int totalItemCount) {
                int lastinScreen=firstVisibleItem+visibleItemCount;
                if(lastinScreen==totalItemCount){
                    if (stopLoading==false){
                        /*seriesStructArrayList.add(new seriesStruct2("Aquaman","1.jpg","1080p HD",2019));
                        seriesStructArrayList.add(new seriesStruct2("Bumblebee","8.jpg","1080p HD",2018));
                        seriesAdapter0.notifyDataSetChanged();
                    }
                }
            }
        });*/

        return v;

    }

    private void getInfo(){
        String url ="http://"+session.getHost_address()+":8000/seriesapi20/?format=json";
        StringRequest stringRequest=new StringRequest(
                Request.Method.GET,
                url,
                new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {
                        GsonBuilder builder=new GsonBuilder();
                        Gson gson = builder.create();
                        seriesList= Arrays.asList(gson.fromJson(response,seriesStruct2[].class));
                        seriesAdapter0 = new seriesAdapter(getContext(),getActivity(),seriesList);
                        gridView.setAdapter(seriesAdapter0);



                        //youTubePlayerView.initialize(API_KEY, );
                        //List<seriesStruct> seriesStruct0;
                        //seriesStruct0 = Arrays.asList(gson.fromJson(response,seriesStruct[].class));
                        System.out.println(seriesStructArrayList);//"hala bole haaaalaaaaaaaaa madrid"+seriesStruct0+"\n "+seriesStruct0.get(0)+"\n "+seriesStruct0.get(0).getTrailer());
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        System.out.println(error.getMessage());
                    }
                }
        );
        requestQueue.add(stringRequest);
    }
}
