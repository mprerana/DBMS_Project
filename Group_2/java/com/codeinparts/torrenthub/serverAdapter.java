package com.codeinparts.torrenthub;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;

public class serverAdapter extends BaseAdapter {
    private Context cntx;
    public serverAdapter(Context c){
        this.cntx=c;
    }
    @Override
    public int getCount() {
        return 10;
    }

    @Override
    public Object getItem(int position) {
        return null;
    }

    @Override
    public long getItemId(int position) {
        return 0;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        LayoutInflater inflater = LayoutInflater.from(cntx);
         View v = inflater.inflate(R.layout.device_info, parent, false);
        return v;

    }
}
