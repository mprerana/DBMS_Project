package com.codeinparts.torrenthub;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ImageView;
import android.widget.TextView;

import com.squareup.picasso.Picasso;

import java.util.ArrayList;
import java.util.List;
import java.util.function.BooleanSupplier;

public class bookAdapter extends BaseAdapter {
    //private ArrayList<bookStruct2> bookStructArrayList=new ArrayList<bookStruct2>();
    private List<bookStruct2> bookList= new ArrayList<bookStruct2>();
    private Context cntx;
    private Activity activity;
    private Session session;
    public bookAdapter(Context context, Activity activity2 , List<bookStruct2> bookStruct2s){
        this.cntx=context;
        this.activity=activity2;
        this.bookList=bookStruct2s;
        this.session=new Session(context);

    }
    @Override
    public int getCount() {
        return bookList.size() ;
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
        View v;
        System.out.print(position);

            final bookStruct2 bookStruct= (bookStruct2) bookList.get(position);
            System.out.print(bookStruct);
            LayoutInflater inflater = LayoutInflater.from(cntx);
            v = inflater.inflate(R.layout.tranding_books, parent, false);
            ImageView imageView_book_poster=v.findViewById(R.id.book_poster);
            TextView textView_book_name=v.findViewById(R.id.book_name);
            TextView textView_book_year=v.findViewById(R.id.book_year);
            TextView textView_book_quality=v.findViewById(R.id.book_quality);
            Picasso.with(this.cntx).load(bookStruct.getPosterImg()).into(imageView_book_poster);
            textView_book_name.setText(bookStruct.getbookName());
            textView_book_quality.setText(bookStruct.getQuality());
            textView_book_year.setText(bookStruct.getYear()+"");
            v.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {

                    Intent intent=new Intent(activity, BookDescription.class);
                    intent.putExtra("book_pass",bookStruct.getbookName());
                    activity.startActivity(intent);


                }
            });
        return v;
    }
}
