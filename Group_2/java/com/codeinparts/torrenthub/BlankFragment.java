package com.codeinparts.torrenthub;


import android.content.Intent;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.text.Editable;
import android.text.TextWatcher;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.TextView;

import com.nbsp.materialfilepicker.MaterialFilePicker;
import com.nbsp.materialfilepicker.ui.FilePickerActivity;


/**
 * A simple {@link Fragment} subclass.
 */
public class BlankFragment extends Fragment {
    private TextView location;
    public BlankFragment() {
        // Required empty public constructor
    }


    @Override
    public void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        location.setText(data.getStringExtra(FilePickerActivity.RESULT_FILE_PATH));
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        View v= inflater.inflate(R.layout.fragment_blank, container, false);
        Button add=v.findViewById(R.id.addButton);
        Button cancel=v.findViewById(R.id.cancelButton);
        ImageButton pick =v.findViewById(R.id.pickButton);
        EditText name=v.findViewById(R.id.movie_name);
        EditText language=v.findViewById(R.id.movieLanguage);
        EditText Quality=v.findViewById(R.id.movieQuality);
        location=v.findViewById(R.id.fLocation);
        final TextView namelbl=v.findViewById(R.id.movieLable);
        final TextView langlbl=v.findViewById(R.id.LanguageLable);
        final TextView qltylbl=v.findViewById(R.id.qualityLabel);
        final TextView loclbl=v.findViewById(R.id.fileLocationLabel);
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
                new MaterialFilePicker().withActivity(getActivity()).withRequestCode(1).withHiddenFiles(true).start();
            }
        });


        cancel.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

            }
        });

        return v;
    }

}
