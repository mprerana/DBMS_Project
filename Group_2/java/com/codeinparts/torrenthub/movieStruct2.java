package com.codeinparts.torrenthub;

import com.google.gson.annotations.SerializedName;

public class movieStruct2 {
    @SerializedName("movie")
    private String MovieName;
    private String Quality;
    @SerializedName("poster")
    private String PosterImg;
    private String released;
    private int year;
    public movieStruct2(String movie_name,String Posterlink, String quality,int year){
        this.MovieName=movie_name;
        this.Quality=quality;
        this.PosterImg=Posterlink;
        this.year=year;
    }


    public String getReleased() {
        return released;
    }

    public void setReleased(String released) {
        this.released = released;
    }


    public String getPosterImg() {
        return PosterImg;
    }

    public void setPosterImg(String posterImg) {
        PosterImg = posterImg;
    }

    public int getYear() {
        return Integer.parseInt(released.substring(released.length()-4));
    }

    public void setYear(int year) {
        this.year = year;
    }

    public String getMovieName() {
        return MovieName;
    }

    public String getQuality() {
        return Quality;
    }

    public void setMovieName(String movieName) {
        MovieName = movieName;
    }

    public void setQuality(String quality) {
        Quality = quality;
    }
}
