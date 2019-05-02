package com.codeinparts.torrenthub;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;
import android.widget.Toolbar;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;
import com.google.android.youtube.player.YouTubeBaseActivity;
import com.google.android.youtube.player.YouTubeInitializationResult;
import com.google.android.youtube.player.YouTubePlayer;
import com.google.android.youtube.player.YouTubePlayerView;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.squareup.picasso.Picasso;

import org.json.JSONObject;

import java.util.Arrays;
import java.util.List;
import java.util.Objects;

import static com.google.android.youtube.player.YouTubePlayer.*;

public class game_description extends YouTubeBaseActivity {
    public static final String API_KEY = "AIzaSyBhByaDJ429-n4dWFFQLCKeziyy_hzcDLM";
    private Session session;
    private RequestQueue requestQueue;
    public String VIDEO_ID = "Cg8sbRFS3zU";
    public String game_pass;
    private ImageView game_poster;
    private TextView game_name_tf,game_rating_tf,game_duration;

    private YouTubePlayerView youTubePlayerView;
    @Override
    public boolean onNavigateUp() {
        return super.onNavigateUp();
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_game_description);
        Intent intent=getIntent();
        game_pass=intent.getStringExtra("game_pass");
        session=new Session(getApplicationContext());
        requestQueue= Volley.newRequestQueue(this);
        game_poster=findViewById(R.id.gamePoster);
        game_name_tf=findViewById(R.id.gameName);
        youTubePlayerView = (YouTubePlayerView) findViewById(R.id.game_trailer);
        getdata();

        Toolbar toolbar=(Toolbar) findViewById(R.id.toolbar1);
        setActionBar(toolbar);
        Objects.requireNonNull(getActionBar()).setDisplayHomeAsUpEnabled(true);
        getActionBar().setDisplayShowCustomEnabled(true);


        /** Initializing YouTube Player View **/



    }



    private PlaybackEventListener playbackEventListener = new PlaybackEventListener() {
        @Override
        public void onBuffering(boolean arg0) {
        }
        @Override
        public void onPaused() {
        }
        @Override
        public void onPlaying() {
        }
        @Override
        public void onSeekTo(int arg0) {
        }
        @Override
        public void onStopped() {
        }
    };

    private PlayerStateChangeListener playerStateChangeListener = new PlayerStateChangeListener() {
        @Override
        public void onAdStarted() {
        }
        @Override
        public void onError(ErrorReason arg0) {
        }
        @Override
        public void onLoaded(String arg0) {
        }
        @Override
        public void onLoading() {
        }
        @Override
        public void onVideoEnded() {
        }
        @Override
        public void onVideoStarted() {
        }
    };

    private void getdata(){
        String url ="http://"+session.getHost_address()+":8000/game/?format=json&name="+game_pass;
        StringRequest stringRequest=new StringRequest(
                Request.Method.GET,
                url,
                new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {
                        GsonBuilder builder=new GsonBuilder();
                        Gson gson = builder.create();
                        gameStruct gameStruct0=gson.fromJson(response,gameStruct.class);
                        VIDEO_ID=getApiKey(gameStruct0.getTrailer());
                        game_name_tf.setText(gameStruct0.getgame());
                        Picasso.with(getApplicationContext()).load(gameStruct0.getPoster()).into(game_poster);
                        youTubePlayerView.initialize(API_KEY, new OnInitializedListener() {
                            @Override
                            public void onInitializationFailure(Provider provider, YouTubeInitializationResult result) {
                                Toast.makeText(getApplicationContext(), "Failured to Initialize!", Toast.LENGTH_LONG).show();
                            }

                            @Override
                            public void onInitializationSuccess(Provider provider, YouTubePlayer player, boolean wasRestored) {
                                /** add listeners to YouTubePlayer instance **/
                                player.setPlayerStateChangeListener(playerStateChangeListener);
                                player.setPlaybackEventListener(playbackEventListener);

                                /** Start buffering **/
                                if (!wasRestored) {
                                    player.cueVideo(VIDEO_ID);
                                }
                            }
                        });
                        //youTubePlayerView.initialize(API_KEY, );
                        //List<gameStruct> gameStruct0;
                        //gameStruct0 = Arrays.asList(gson.fromJson(response,gameStruct[].class));
                        System.out.println(gameStruct0.getTrailer());//"hala bole haaaalaaaaaaaaa madrid"+gameStruct0+"\n "+gameStruct0.get(0)+"\n "+gameStruct0.get(0).getTrailer());
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
    private String getDuration(int mint){
        int hr=0,mi=0;
        hr=(int)mint/60;
        mi=mint%60;
        return 0+" hr "+ mi +" min";
    }
    private String getApiKey(String url){
        int index_of_equal=url.indexOf('=');
        return url.substring(index_of_equal+1);
    }


}

