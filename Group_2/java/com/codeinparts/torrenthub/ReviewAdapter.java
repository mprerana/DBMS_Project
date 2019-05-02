package com.codeinparts.torrenthub;


import android.content.Context;
import android.os.AsyncTask;
import android.support.annotation.NonNull;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;
import com.android.volley.RequestQueue;
import com.android.volley.toolbox.Volley;
import java.util.ArrayList;
import java.util.List;

public class ReviewAdapter extends RecyclerView.Adapter<ReviewAdapter.ReviewHolder> {

    private static Context context;
    private ArrayList<ReviewStruct> list=new ArrayList<ReviewStruct>();

    public ReviewAdapter(Context cntx,ArrayList<ReviewAdapter.ReviewStruct> list){
        this.context=cntx;
        this.list=list;
    }

    @NonNull
    @Override
    public ReviewHolder onCreateViewHolder(@NonNull ViewGroup viewGroup, int i) {
        LayoutInflater layoutInflater= LayoutInflater.from(context);
        View v=layoutInflater.inflate(R.layout.review,viewGroup,false);
        return new ReviewHolder(v);
    }

    @Override
    public void onBindViewHolder(@NonNull ReviewHolder reviewHolder, int i) {
        ReviewStruct reviewStruct=list.get(i);
        System.out.println(reviewStruct.getComment());
        reviewHolder.comment.setText(reviewStruct.getComment());
        reviewHolder.dateNTime.setText(reviewStruct.getDate()+" "+reviewStruct.getTime());
    }

    @Override
    public int getItemCount() {
        return 0;
    }

    public class ReviewHolder extends RecyclerView.ViewHolder{
        public TextView dateNTime,comment;
        public ReviewHolder(@NonNull View itemView) {
            super(itemView);
            dateNTime=itemView.findViewById(R.id.date_time_tv);
            comment=itemView.findViewById(R.id.review_tv);
        }
    }

    public static class ReviewStruct{
        private String date,time,comment;

        public ReviewStruct(String date0,String time0,String comment0){
            this.date=date0;
            this.time=time0;
            this.comment=comment0;
        }

        public String getTime() {
            return time;
        }

        public String getComment() {
            return comment;
        }

        public String getDate() {
            return date;
        }

        public void setComment(String comment) {
            this.comment = comment;
        }

        public void setDate(String date) {
            this.date = date;
        }

        public void setTime(String time) {
            this.time = time;
        }
    }

}

