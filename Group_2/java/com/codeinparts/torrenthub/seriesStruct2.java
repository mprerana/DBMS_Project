package com.codeinparts.torrenthub;

import com.google.gson.annotations.SerializedName;

public class seriesStruct2 {
    @SerializedName("tv_series")
    private String seriesName;
    private String Quality;
    @SerializedName("poster")
    private String PosterImg;
    private String released;
    private int year0;
    public seriesStruct2(String series_name, String Posterlink, String quality, int year){
        this.seriesName=series_name;
        this.Quality=quality;
        this.PosterImg=Posterlink;
        this.year0=year;
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
        return 2018;//Integer.parseInt(released.substring(released.length()-4));
    }

    public void setYear0(int year) {
        this.year0= year;
    }

    public String getseriesName() {
        return seriesName;
    }

    public String getQuality() {
        return Quality;
    }

    public void setseriesName(String seriesName) {
        seriesName = seriesName;
    }

    public void setQuality(String quality) {
        Quality = quality;
    }
}
