package com.codeinparts.torrenthub;

import android.Manifest;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.database.sqlite.SQLiteDatabase;
import android.graphics.PorterDuff;
import android.os.Build;
import android.support.annotation.NonNull;
import android.support.constraint.ConstraintLayout;
import android.support.v4.content.ContextCompat;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.text.Editable;
import android.text.TextWatcher;
import android.view.View;
import android.view.Window;
import android.view.WindowManager;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.TextView;
import android.widget.Toolbar;

import com.nbsp.materialfilepicker.MaterialFilePicker;
import com.nbsp.materialfilepicker.ui.FilePickerActivity;

import java.util.Objects;

public class local_movie_dash extends AppCompatActivity {
    private TextView language,name,Quality,location,curtain;
    private ConstraintLayout layout;

    @Override
    public void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (data!=null)
        location.setText(data.getStringExtra(FilePickerActivity.RESULT_FILE_PATH));
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_local_movie_dash);

        Window window=this.getWindow();
        window.clearFlags(WindowManager.LayoutParams.FLAG_TRANSLUCENT_STATUS);
        window.addFlags(WindowManager.LayoutParams.FLAG_DRAWS_SYSTEM_BAR_BACKGROUNDS);
        window.setStatusBarColor(ContextCompat.getColor(this,R.color.colorPrimaryDark));

        if(Build.VERSION.SDK_INT > Build.VERSION_CODES.M && checkSelfPermission(Manifest.permission.WRITE_EXTERNAL_STORAGE) != PackageManager.PERMISSION_GRANTED) {
            requestPermissions(new String[]{Manifest.permission.WRITE_EXTERNAL_STORAGE},10001);
        }

        final RecyclerView recyclerView=findViewById(R.id.local_movie_recycler);
        recyclerView.setAdapter(new LocalMovieAdapter(getApplicationContext()));
        recyclerView.setLayoutManager(new LinearLayoutManager(getApplicationContext()));

        Button add=findViewById(R.id.addButton);
        layout=findViewById(R.id.upload_movie);
        Button cancel=findViewById(R.id.cancelButton);
        ImageButton plus=findViewById(R.id.buttonplus);
        ImageButton pick =findViewById(R.id.pickButton);
        name=findViewById(R.id.movie_name);
        language=findViewById(R.id.movieLanguage);
        Quality=findViewById(R.id.movieQuality);
        location=findViewById(R.id.fLocation);
        curtain=findViewById(R.id.curtain);

        Toolbar toolbar=(Toolbar) findViewById(R.id.toolbar2);
        setActionBar(toolbar);
        Objects.requireNonNull(getActionBar()).setDisplayHomeAsUpEnabled(true);
        getActionBar().setDisplayShowCustomEnabled(true);

        toolbar.getNavigationIcon().setColorFilter(getResources().getColor(R.color.white), PorterDuff.Mode.SRC_ATOP);


        final TextView namelbl=findViewById(R.id.movieLable);
        final TextView langlbl=findViewById(R.id.LanguageLable);
        final TextView qltylbl=findViewById(R.id.qualityLabel);
        final TextView loclbl=findViewById(R.id.fileLocationLabel);

        name.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {

            }

            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {

            }

            @Override
            public void afterTextChanged(Editable s) {
                if (s.length() != 0){
                    namelbl.setVisibility(View.VISIBLE);
                }
                else {
                    namelbl.setVisibility(View.INVISIBLE);
                }
            }
        });

        language.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {

            }

            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {

            }

            @Override
            public void afterTextChanged(Editable s) {
                if (s.length() != 0){
                    langlbl.setVisibility(View.VISIBLE);
                }
                else {
                    langlbl.setVisibility(View.INVISIBLE);
                }
            }
        });

        Quality.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {

            }

            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {

            }

            @Override
            public void afterTextChanged(Editable s) {
                if (s.length() != 0){
                    qltylbl.setVisibility(View.VISIBLE);
                }
                else {
                    qltylbl.setVisibility(View.INVISIBLE);
                }
            }
        });

        location.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {

            }

            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {

            }

            @Override
            public void afterTextChanged(Editable s) {
                if (s.length() != 0){
                    loclbl.setVisibility(View.VISIBLE);
                }
                else {
                    loclbl.setVisibility(View.INVISIBLE);
                }
            }
        });

        pick.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                new MaterialFilePicker().withActivity(local_movie_dash.this).withRequestCode(1).withFilterDirectories(true).withHiddenFiles(true).start();
            }
        });

        plus.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                layout.setVisibility(View.VISIBLE);
                curtain.setVisibility(View.VISIBLE);
            }
        });

        cancel.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                layout.setVisibility(View.INVISIBLE);
                curtain.setVisibility(View.INVISIBLE);
            }
        });

        add.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                movieDBHelper dbHelper=new movieDBHelper(getApplicationContext());
                SQLiteDatabase db=dbHelper.getWritableDatabase();
                dbHelper.addMovie(name.getText().toString(),language.getText().toString(),"1.4GB",Quality.getText().toString(),location.getText().toString(),db);
                name.setText("");
                location.setText("");
                language.setText("");
                Quality.setText("");
                recyclerView.setAdapter(new LocalMovieAdapter(getApplicationContext()));
                layout.setVisibility(View.INVISIBLE);
                curtain.setVisibility(View.INVISIBLE);
            }
        });




    }

}
