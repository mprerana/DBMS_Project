package com.codeinparts.torrenthub;

import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;
import android.widget.Toolbar;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;
import com.google.android.youtube.player.YouTubeBaseActivity;
import com.google.android.youtube.player.YouTubeInitializationResult;
import com.google.android.youtube.player.YouTubePlayer;
import com.google.android.youtube.player.YouTubePlayerView;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.squareup.picasso.Picasso;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Objects;

import static com.google.android.youtube.player.YouTubePlayer.*;
import static java.lang.Thread.sleep;

public class movie_description extends YouTubeBaseActivity {
    public static final String API_KEY = "AIzaSyBhByaDJ429-n4dWFFQLCKeziyy_hzcDLM";
    private Session session;
    private RequestQueue requestQueue;
    private RecyclerView recyclerView;
    public String VIDEO_ID = "Cg8sbRFS3zU";
    public String movie_pass;
    private ImageView movie_poster;
    private String type="movie";
    private TextView movie_name_tf,movie_rating_tf,movie_duration,imdb,movieGenre;

    private YouTubePlayerView youTubePlayerView;
    @Override
    public boolean onNavigateUp() {
        return super.onNavigateUp();
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_movie_description);
        Intent intent=getIntent();
        movie_pass=intent.getStringExtra("movie_pass");
        session=new Session(getApplicationContext());
        requestQueue= Volley.newRequestQueue(this);
        movie_poster=findViewById(R.id.moviePoster);
        movie_name_tf=findViewById(R.id.movieName);
        movie_duration=findViewById(R.id.duration);
        movieGenre=findViewById(R.id.movieGenre);
        imdb=findViewById(R.id.imdbRating);
        recyclerView=findViewById(R.id.movie_revie_reycler);
        youTubePlayerView = (YouTubePlayerView) findViewById(R.id.movie_trailer);

        getdata();
        //getRequest a=new getRequest();
        //a.execute(2);
        Toolbar toolbar=(Toolbar) findViewById(R.id.toolbar1);
        setActionBar(toolbar);
        Objects.requireNonNull(getActionBar()).setDisplayHomeAsUpEnabled(true);
        getActionBar().setDisplayShowCustomEnabled(true);

        //System.out.println("comment"+reviewStructs.get(1).getComment());

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
        String url ="http://"+session.getHost_address()+":8000/movie/?format=json&name="+movie_pass;
        StringRequest stringRequest=new StringRequest(
                Request.Method.GET,
                url,
                new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {
                        GsonBuilder builder=new GsonBuilder();
                        Gson gson = builder.create();
                        movieStruct movieStruct0=gson.fromJson(response,movieStruct.class);
                        VIDEO_ID=getApiKey(movieStruct0.getTrailer());
                        movie_name_tf.setText(movieStruct0.getmovie());
                        imdb.setText(movieStruct0.getImdb_rating());
                        movieGenre.setText(getGenre(movieStruct0.getGenre()));
                        movie_duration.setText(getDuration(movieStruct0.getRuntime()));
                        recyclerView.setLayoutManager(new LinearLayoutManager(getApplicationContext(),LinearLayoutManager.HORIZONTAL,false));
                        ArrayList<ReviewAdapter.ReviewStruct> reviewStructs=new ArrayList<ReviewAdapter.ReviewStruct>();
                        reviewStructs.add(new ReviewAdapter.ReviewStruct("1 May 2018","2:51 PM","Just an overal good movie. The story could have been a bit better and the villans were not Thanos-level but it just does the job. I wanted more actually, because the CGI was really good. Also this is one of the funniest mcu movies, so if you want a good laugh I recommend this.   I applaud Paul Rudd and Micheal Douglas, great performance!   If you're a marvel fan this will satisfy you 100% and even if you just want to relax and enjoy this movie with the family, that's cool too."));
                        reviewStructs.add(new ReviewAdapter.ReviewStruct("1 May 2018","2:52 PM","I saw a lot of people hating this movie, because he didn't have a connection with Infinity War or Avengers 4. I thought the movie was truly amazing, it's funny, but can be emotional at the same time. Well, of course it will not have awnsers to Infinity War events, because it his BEFORE Infinity War. Why can't people just understand that? If you haven't seen it yet, I recommend it very much. For me, it was even better than the first one."));
                        recyclerView.setAdapter(new ReviewAdapter(getApplicationContext(),reviewStructs));
                        Picasso.with(getApplicationContext()).load(movieStruct0.getPoster()).into(movie_poster);
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
                        //List<movieStruct> movieStruct0;
                        //movieStruct0 = Arrays.asList(gson.fromJson(response,movieStruct[].class));
                        System.out.println(movieStruct0.getTrailer());//"hala bole haaaalaaaaaaaaa madrid"+movieStruct0+"\n "+movieStruct0.get(0)+"\n "+movieStruct0.get(0).getTrailer());
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
    private String getDuration(String mint0){

        int mint=Integer.parseInt(mint0.trim().substring(0,3).trim());
        int hr=0,mi=0;
        hr=(int)mint/60;

        mi=mint%60;
        return hr +" hr "+ mi +" min";
    }

    private String getApiKey(String url){
        int index_of_equal=url.indexOf('=');
        return url.substring(index_of_equal+1);
    }

    private String getGenre(String genre){
        try {
            return genre.substring(0, genre.indexOf(' ')).replace('/', '\0').replace(',', '\0').trim();
        }
        catch (StringIndexOutOfBoundsException e){
            return genre.substring(0, genre.indexOf(',')).replace(',', '\0').trim();
        }
    }

    public List<ReviewAdapter.ReviewStruct> getReviews() {
        String url ="http://"+session.getHost_address()+":8000/comments/?format=json&name=Ant-Man and the Wasp&type=Movie";
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

    public class getRequest extends AsyncTask<Integer,Integer,Integer> {
        @Override
        protected void onPreExecute() {
            super.onPreExecute();
        }

        @Override
        protected void onPostExecute(Integer integer) {
            super.onPostExecute(integer);

        }

        @Override
        protected Integer doInBackground(Integer... integers) {
            try {
                sleep(1);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            return 1 ;
        }
    }



}

