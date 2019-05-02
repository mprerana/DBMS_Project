package com.codeinparts.torrenthub;

import android.content.Context;
import android.support.annotation.NonNull;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ProgressBar;
import android.widget.TextView;

import java.util.ArrayList;

public class DownloadAdapter extends RecyclerView.Adapter<DownloadAdapter.DownloadHolder> {

    private Context context;
    private ArrayList<DownloadAdapter.downloadStuct>downloadStuctArrayList;

    public DownloadAdapter(Context context){
        this.context=context;
        downloadStuctArrayList=new ArrayList<>();
        downloadStuctArrayList.add(new downloadStuct("Avengers End game","540kbps","5Mbps","60%"));
        downloadStuctArrayList.add(new downloadStuct("Red Dead Redemption 2","140kbps","2Mbps","15%"));
        downloadStuctArrayList.add(new downloadStuct("Pattern Classification by Duda and Hart","5Kbps","50Kbps","48%"));
        downloadStuctArrayList.add(new downloadStuct("GOT Season 8 Episode 3","50kbps","1.5Mbps","10%"));
    }

    @NonNull
    @Override
    public DownloadAdapter.DownloadHolder onCreateViewHolder(@NonNull ViewGroup viewGroup, int i) {
        LayoutInflater layoutInflater=LayoutInflater.from(context);
        View view=layoutInflater.inflate(R.layout.download,viewGroup,false);
        return new DownloadHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull DownloadAdapter.DownloadHolder viewHolder, int i) {
        downloadStuct downloadStuct0=downloadStuctArrayList.get(i);
        viewHolder.mname.setText(downloadStuct0.getFilename());
        viewHolder.comp.setText(downloadStuct0.getCompletion());
        viewHolder.down.setText(downloadStuct0.getUpSpeed());
        viewHolder.up.setText(downloadStuct0.getDownSpeed());
        viewHolder.pb.setProgress(Integer.parseInt(downloadStuct0.Completion.substring(0,2)));
    }

    @Override
    public int getItemCount() {
        return 4;
    }

    public class DownloadHolder extends RecyclerView.ViewHolder{
        public TextView mname,down,up,comp;
        public ProgressBar pb;
        public DownloadHolder(@NonNull View itemView) {
            super(itemView);
            mname=itemView.findViewById(R.id.Fname);
            down=itemView.findViewById(R.id.downSpeed);
            up=itemView.findViewById(R.id.upSpeed);
            comp=itemView.findViewById(R.id.comptext);
            pb=itemView.findViewById(R.id.complProg);
        }
    }

    public class downloadStuct{
        private String filename,upSpeed,downSpeed,Completion;

        public downloadStuct(String FileName,String UpSpeed,String DownSpeed,String completion)
        {
            this.filename=FileName;
            this.upSpeed=UpSpeed;
            this.downSpeed=DownSpeed;
            this.Completion=completion;
        }

        public String getCompletion() {
            return Completion;
        }

        public String getDownSpeed() {
            return downSpeed;
        }

        public String getFilename() {
            return filename;
        }

        public String getUpSpeed() {
            return upSpeed;
        }

        public void setCompletion(String completion) {
            Completion = completion;
        }

        public void setDownSpeed(String downSpeed) {
            downSpeed = downSpeed;
        }

        public void setFilename(String filename) {
            this.filename = filename;
        }

        public void setUpSpeed(String upSpeed) {
            this.upSpeed = upSpeed;
        }
    }
}
