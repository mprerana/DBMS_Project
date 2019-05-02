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


public class bookFragment extends Fragment {
    private Session session;
    private  Boolean loadmore=true,stopLoading=false;
    private bookAdapter bookAdapter0;
    private RequestQueue requestQueue;
    private List<bookStruct2> bookList;
    private  GridView gridView;
    private ArrayList bookStructArrayList=new ArrayList<bookStruct2>();
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        View v = inflater.inflate(R.layout.fragment_book, container, false);
        gridView=v.findViewById(R.id.gridview_book);
        session=new Session(getContext());
        requestQueue= Volley.newRequestQueue(getContext());
        getInfo();
        /*this.bookStructArrayList.add(new bookStruct2("Aquaman","1.jpg","1080p HD",2019));
        this.bookStructArrayList.add(new bookStruct2("Bumblebee","8.jpg","1080p HD",2018));
        this.bookStructArrayList.add(new bookStruct2("Triple threat","9.jpg","1080p HD",2018));
        this.bookStructArrayList.add(new bookStruct2("Mortal Engines","2.jpg","1080p HD",2019));
        this.bookStructArrayList.add(new bookStruct2("Fantastic Beast The crimes of grindelwald","3.jpg","1080p HD",2019));
        this.bookStructArrayList.add(new bookStruct2("Spider Man Into the the spider-verse","4.jpg","1080p HD",2019));
        this.bookStructArrayList.add(new bookStruct2("Pokemon Detective Pikachu","5.jpg","1080p HD",2019));
        this.bookStructArrayList.add(new bookStruct2("Total Dhamaal","6.jpg","1080p HD",2019));
        this.bookStructArrayList.add(new bookStruct2("URI The surgical Strike","7.jpg","1080p HD",2019));
        this.bookStructArrayList.add(new bookStruct2("Captain Marvel","8.jpeg","1080p HD",2019));*/

        /*gridView.setOnScrollListener(new AbsListView.OnScrollListener() {
            @Override
            public void onScrollStateChanged(AbsListView view, int scrollState) {

            }

            @Override
            public void onScroll(AbsListView view, int firstVisibleItem, int visibleItemCount, int totalItemCount) {
                int lastinScreen=firstVisibleItem+visibleItemCount;
                if(lastinScreen==totalItemCount){
                    if (stopLoading==false){
                        /*bookStructArrayList.add(new bookStruct2("Aquaman","1.jpg","1080p HD",2019));
                        bookStructArrayList.add(new bookStruct2("Bumblebee","8.jpg","1080p HD",2018));
                        bookAdapter0.notifyDataSetChanged();
                    }
                }
            }
        });*/

        return v;

    }

    private void getInfo(){
        String url ="http://"+session.getHost_address()+":8000/bookapi20/?format=json";
        StringRequest stringRequest=new StringRequest(
                Request.Method.GET,
                url,
                new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {
                        GsonBuilder builder=new GsonBuilder();
                        Gson gson = builder.create();
                        bookList= Arrays.asList(gson.fromJson(response,bookStruct2[].class));
                        bookAdapter0 = new bookAdapter(getContext(),getActivity(),bookList);
                        gridView.setAdapter(bookAdapter0);



                        //youTubePlayerView.initialize(API_KEY, );
                        //List<bookStruct> bookStruct0;
                        //bookStruct0 = Arrays.asList(gson.fromJson(response,bookStruct[].class));
                        System.out.println(bookStructArrayList);//"hala bole haaaalaaaaaaaaa madrid"+bookStruct0+"\n "+bookStruct0.get(0)+"\n "+bookStruct0.get(0).getTrailer());
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
