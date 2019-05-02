package com.codeinparts.torrenthub;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.text.Editable;
import android.text.TextWatcher;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.TextView;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONObject;

public class connect_server extends AppCompatActivity {
    private TextView error_msg,lable;
    private EditText server_add;
    private Button btn;
    private Session session;
    private RequestQueue requestQueue;
    private ImageView error_img;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_connect_server);
        requestQueue= Volley.newRequestQueue(this);

        //JsonObjectRequest objectRequest=new JsonObjectRequest(Request.Method.GET,)
        error_img=findViewById(R.id.error_img);
        error_msg=findViewById(R.id.error_tf);
        lable=findViewById(R.id.lable_tf);
        server_add=findViewById(R.id.server_add_tf);
        btn=findViewById(R.id.connect_btn);
        session=new Session(getApplicationContext());
        quickcheck();
        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String url = "http://"+server_add.getText().toString()+":8000/admin/";
                StringRequest stringRequest = new StringRequest(Request.Method.GET, url,
                        new Response.Listener<String>() {
                            @Override
                            public void onResponse(String response) {
                                session.setHost_address(server_add.getText().toString());
                                // Display the first 500 characters of the response string.
                                goToHome();
                            }
                        }, new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        error0(1);
                    }
                });

                requestQueue.add(stringRequest);

            }
        });

        server_add.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {

            }

            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {

            }

            @Override
            public void afterTextChanged(Editable s) {
                if (s.length() != 0){
                    lable.setVisibility(View.VISIBLE);
                }
                else {
                    lable.setVisibility(View.INVISIBLE);
                }
            }
        });

    }
    private void error0(int i){
        if(i==0){
            error_msg.setVisibility(View.INVISIBLE);
            error_img.setVisibility(View.INVISIBLE);
        }
        else{
            error_msg.setVisibility(View.VISIBLE);
            error_img.setVisibility(View.VISIBLE);
        }
    }

    private void goToHome(){
        Intent intent=new Intent(this,home.class);
        this.startActivity(intent);
    }

    private void quickcheck(){
        String url = "http://"+session.getHost_address()+":8000/admin";
        StringRequest stringRequest = new StringRequest(Request.Method.GET, url,
                new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {
                        //session.setHost_address(server_add.getText().toString());
                        // Display the first 500 characters of the response string.
                        goToHome();
                    }
                }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {

            }
        });

        requestQueue.add(stringRequest);
    }
}
















