package com.codeinparts.torrenthub;

import com.google.gson.annotations.SerializedName;

/* {"id":22,
"trailer":"https:\/\/www.youtube.com\/watch?v=EXeTwQWrcwY",
"released":"18 Jul 2008",
"runtime":"152 min",
"series":"The Dark Knight",
poster":"https:\/\/m.media-amazon.com\/images\/M\/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SX300.jpg",
"genre":"Action, Crime, Drama, Thriller",
"imdb_rating":"9.0"}
 */

public class seriesStruct {
    @SerializedName("tv_series")
    private String series;
    @SerializedName("genre")
    private String Genre;
    private String poster;
    private String runtime,trailer;
    private  String Quality;
    private int noPeers;
    private int seriesSize;
    @SerializedName("imdb_rating")
    private float rating;
    public seriesStruct(String series,float rating,String genre, String poster, String quality, String runtime, String trailer, int np, int size_of_series){
        this.seriesSize=size_of_series;
        this.series=series;
        this.Genre=genre;
        this.Quality=quality;
        this.noPeers=np;
        this.runtime=runtime;
        this.trailer=trailer;
        this.poster=poster;
        this.rating=rating;
    }

    public float getRating() {
        return rating;
    }

    public void setRating(float rating) {
        this.rating = rating;
    }

    public int getMovieSize() {
        return seriesSize;
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

    public String getseries() {
        return series;
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

    public void setseries(String series) {
        series = series;
    }

    public void setMovieSize(int seriesSize) {
        this.seriesSize = seriesSize;
    }

    public void setNoPeers(int noPeers) {
        this.noPeers = noPeers;
    }

    public void setQuality(String quality) {
        Quality = quality;
    }
}
