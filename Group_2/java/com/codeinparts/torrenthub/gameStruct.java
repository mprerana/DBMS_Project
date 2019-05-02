package com.codeinparts.torrenthub;

import com.google.gson.annotations.SerializedName;
/* {"id":22,
"trailer":"https:\/\/www.youtube.com\/watch?v=EXeTwQWrcwY",
"released":"18 Jul 2008",
"runtime":"152 min",
"game":"The Dark Knight",
poster":"https:\/\/m.media-amazon.com\/images\/M\/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SX300.jpg",
"genre":"Action, Crime, Drama, Thriller",
"imdb_rating":"9.0"}
 */
public class gameStruct {
    private String game;
    @SerializedName("genre")
    private String Genre;
    private String poster;
    private String runtime,trailer;
    private  String Quality;
    private int noPeers;
    private int gameSize;
    public gameStruct(String game,String genre,String poster,String quality,String runtime,String trailer,int np,int size_of_game){
        this.gameSize=size_of_game;
        this.game=game;
        this.Genre=genre;
        this.Quality=quality;
        this.noPeers=np;
        this.runtime=runtime;
        this.trailer=trailer;
        this.poster=poster;
    }
    public int getgameSize() {
        return gameSize;
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

    public String getgame() {
        return game;
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

    public void setgame(String game) {
        game = game;
    }

    public void setgameSize(int gameSize) {
        this.gameSize = gameSize;
    }

    public void setNoPeers(int noPeers) {
        this.noPeers = noPeers;
    }

    public void setQuality(String quality) {
        Quality = quality;
    }
}
