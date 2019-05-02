package com.codeinparts.torrenthub;

import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class BookDescription extends AppCompatActivity {
    private RecyclerView recyclerView;
    private Session session;
    private RequestQueue requestQueue;
    private final String type="book";
    private String value;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_book_description);
        recyclerView.findViewById(R.id.review_recycler);
        session=new Session(getApplicationContext());
        getRequest request=new getRequest();
        request.execute(0);

    }
    public List<ReviewAdapter.ReviewStruct> getReviews() {
        String url ="http://"+session.getHost_address()+":8000/"+type+"/?format=json&name="+value;
        final List<ReviewAdapter.ReviewStruct>[] reviewStructs = new List[]{new ArrayList<ReviewAdapter.ReviewStruct>()};
        StringRequest stringRequest=new StringRequest(
                Request.Method.GET,
                url,
                new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {
                        GsonBuilder builder = new GsonBuilder();
                        Gson gson = builder.create();
                        reviewStructs[0] = Arrays.asList(gson.fromJson(response,ReviewAdapter.ReviewStruct.class));
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {

                    }
                });
        requestQueue.add(stringRequest);
        return reviewStructs[0];
    }

    public class getRequest extends AsyncTask<Integer,Integer,List<ReviewAdapter.ReviewStruct>> {
        @Override
        protected void onPreExecute() {
            super.onPreExecute();
        }

        @Override
        protected void onPostExecute(List<ReviewAdapter.ReviewStruct> reviewStructs) {
            super.onPostExecute(reviewStructs);
            recyclerView.setLayoutManager(new LinearLayoutManager(getApplicationContext(),LinearLayoutManager.HORIZONTAL,false));
            //recyclerView.setAdapter(new ReviewAdapter(getApplicationContext(),reviewStructs));
        }

        @Override
        protected List<ReviewAdapter.ReviewStruct> doInBackground(Integer... integers) {
            return getReviews();
        }
    }
}
