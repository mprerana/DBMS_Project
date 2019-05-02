package com.codeinparts.torrenthub;

import com.google.gson.annotations.SerializedName;

public class bookStruct2 {
    @SerializedName("book")
    private String bookName;
    private String Quality;
    @SerializedName("poster")
    private String PosterImg;
    @SerializedName("published")
    private String released;
    private int year;
    public bookStruct2(String book_name, String Posterlink, String quality, int year){
        this.bookName=book_name;
        this.Quality=quality;
        this.PosterImg=Posterlink;
        this.year=2005;
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

    public String getbookName() {
        return bookName;
    }

    public String getQuality() {
        return Quality;
    }

    public void setbookName(String bookName) {
        bookName = bookName;
    }

    public void setQuality(String quality) {
        Quality = quality;
    }
}
