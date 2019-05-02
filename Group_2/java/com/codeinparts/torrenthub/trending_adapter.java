package com.codeinparts.torrenthub;

import android.content.Context;
import android.support.annotation.NonNull;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

public class trending_adapter extends RecyclerView.Adapter<trending_adapter.mViewHolder4movie> {
    private Context cntx;
    public trending_adapter(Context context){
        this.cntx=context;
    }
    @NonNull
    @Override
    public mViewHolder4movie onCreateViewHolder(@NonNull ViewGroup viewGroup, int i) {
        LayoutInflater inflater=LayoutInflater.from(this.cntx);
        View view= inflater.inflate(R.layout.movie_list, viewGroup, false);
        //return trending_adapter.mViewHolder4movie(view);
        return null;
    }

    @Override
    public void onBindViewHolder(@NonNull mViewHolder4movie mViewHolder4movie, int i) {

    }


    @Override
    public int getItemCount() {
        return 0;
    }


    public class  mViewHolder4movie extends  RecyclerView.ViewHolder{

        public mViewHolder4movie(@NonNull View itemView) {
            super(itemView);
        }
    }
}
