package com.codeinparts.torrenthub;

import com.google.gson.annotations.SerializedName;
/* {"id":22,
"trailer":"https:\/\/www.youtube.com\/watch?v=EXeTwQWrcwY",
"released":"18 Jul 2008",
"runtime":"152 min",
"movie":"The Dark Knight",
poster":"https:\/\/m.media-amazon.com\/images\/M\/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SX300.jpg",
"genre":"Action, Crime, Drama, Thriller",
"imdb_rating":"9.0"}
 */
public class movieStruct {
    private String movie;
    @SerializedName("genre")
    private String Genre;
    private String poster;
    private String runtime,trailer;
    private  String Quality;
    private String imdb_rating;
    private int noPeers;
    private int movieSize;
    public movieStruct(String movie,String genre,String poster,String quality,String runtime,String trailer,int np,int size_of_movie){
        this.movieSize=size_of_movie;
        this.movie=movie;
        this.Genre=genre;
        this.Quality=quality;
        this.noPeers=np;
        this.runtime=runtime;
        this.trailer=trailer;
        this.poster=poster;
    }

    public String  getImdb_rating() {
        return imdb_rating;
    }

    public void setImdb_rating(String imdb_rating) {
        this.imdb_rating = imdb_rating;
    }

    public int getMovieSize() {
        return movieSize;
    }

    public String getPoster() {
        return poster;
    }

    public void setPoster(String poster) {
        this.poster = poster;
    }

    public int getNoPeers() {
        return noPeers;
    }

    public String getGenre() {
        return Genre;
    }

    public String getmovie() {
        return movie;
    }

    public String getRuntime() {
        return runtime;
    }

    public String getTrailer() {
        return trailer;
    }

    public void setRuntime(String runtime) {
        this.runtime = runtime;
    }

    public void setTrailer(String trailer) {
        this.trailer = trailer;
    }

    public String getQuality() {
        return Quality;
    }

    public void setGenre(String genre) {
        Genre = genre;
    }

    public void setmovie(String movie) {
        movie = movie;
    }

    public void setMovieSize(int movieSize) {
        this.movieSize = movieSize;
    }

    public void setNoPeers(int noPeers) {
        this.noPeers = noPeers;
    }

    public void setQuality(String quality) {
        Quality = quality;
    }
}
