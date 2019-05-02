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


public class gamesFragment extends Fragment {
    private Session session;
    private  Boolean loadmore=true,stopLoading=false;
    private gameAdapter gameAdapter0;
    private RequestQueue requestQueue;
    private List<gameStruct2> gameList;
    private  GridView gridView;
    private ArrayList gameStructArrayList=new ArrayList<gameStruct2>();
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        View v = inflater.inflate(R.layout.fragment_games, container, false);
        gridView=v.findViewById(R.id.gridview_Games);
        session=new Session(getContext());
        requestQueue= Volley.newRequestQueue(getContext());
        getInfo();
        /*this.gameStructArrayList.add(new gameStruct2("Aquaman","1.jpg","1080p HD",2019));
        this.gameStructArrayList.add(new gameStruct2("Bumblebee","8.jpg","1080p HD",2018));
        this.gameStructArrayList.add(new gameStruct2("Triple threat","9.jpg","1080p HD",2018));
        this.gameStructArrayList.add(new gameStruct2("Mortal Engines","2.jpg","1080p HD",2019));
        this.gameStructArrayList.add(new gameStruct2("Fantastic Beast The crimes of grindelwald","3.jpg","1080p HD",2019));
        this.gameStructArrayList.add(new gameStruct2("Spider Man Into the the spider-verse","4.jpg","1080p HD",2019));
        this.gameStructArrayList.add(new gameStruct2("Pokemon Detective Pikachu","5.jpg","1080p HD",2019));
        this.gameStructArrayList.add(new gameStruct2("Total Dhamaal","6.jpg","1080p HD",2019));
        this.gameStructArrayList.add(new gameStruct2("URI The surgical Strike","7.jpg","1080p HD",2019));
        this.gameStructArrayList.add(new gameStruct2("Captain Marvel","8.jpeg","1080p HD",2019));*/

        /*gridView.setOnScrollListener(new AbsListView.OnScrollListener() {
            @Override
            public void onScrollStateChanged(AbsListView view, int scrollState) {

            }

            @Override
            public void onScroll(AbsListView view, int firstVisibleItem, int visibleItemCount, int totalItemCount) {
                int lastinScreen=firstVisibleItem+visibleItemCount;
                if(lastinScreen==totalItemCount){
                    if (stopLoading==false){
                        /*gameStructArrayList.add(new gameStruct2("Aquaman","1.jpg","1080p HD",2019));
                        gameStructArrayList.add(new gameStruct2("Bumblebee","8.jpg","1080p HD",2018));
                        gameAdapter0.notifyDataSetChanged();
                    }
                }
            }
        });*/

        return v;

    }

    private void getInfo(){
        String url ="http://"+session.getHost_address()+":8000/gameapi20/?format=json";
        StringRequest stringRequest=new StringRequest(
                Request.Method.GET,
                url,
                new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {
                        GsonBuilder builder=new GsonBuilder();
                        Gson gson = builder.create();
                        gameList= Arrays.asList(gson.fromJson(response,gameStruct2[].class));
                        gameAdapter0 = new gameAdapter(getContext(),getActivity(),gameList);
                        gridView.setAdapter(gameAdapter0);



                        //youTubePlayerView.initialize(API_KEY, );
                        //List<gameStruct> gameStruct0;
                        //gameStruct0 = Arrays.asList(gson.fromJson(response,gameStruct[].class));
                        System.out.println(gameStructArrayList);//"hala bole haaaalaaaaaaaaa madrid"+gameStruct0+"\n "+gameStruct0.get(0)+"\n "+gameStruct0.get(0).getTrailer());
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
