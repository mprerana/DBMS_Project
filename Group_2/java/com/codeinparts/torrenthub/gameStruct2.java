package com.codeinparts.torrenthub;

import com.google.gson.annotations.SerializedName;

public class gameStruct2 {
    @SerializedName("game")
    private String gameName;
    private String Quality;
    @SerializedName("poster")
    private String PosterImg;
    private String released;
    private int year;
    public gameStruct2(String game_name,String Posterlink, String quality,int year){
        this.gameName=game_name;
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
        return 2008;//Integer.parseInt(released.substring(released.length()-4));
    }

    public void setYear(int year) {
        this.year = year;
    }

    public String getgameName() {
        return gameName;
    }

    public String getQuality() {
        return Quality;
    }

    public void setgameName(String gameName) {
        gameName = gameName;
    }

    public void setQuality(String quality) {
        Quality = quality;
    }
}
