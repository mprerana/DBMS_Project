package com.codeinparts.torrenthub;

import android.content.Context;
import android.content.SharedPreferences;
import android.preference.PreferenceManager;

public class Session {
    private SharedPreferences apref;
    private String host_address;
    public Session(Context cnt) {
        apref = PreferenceManager.getDefaultSharedPreferences(cnt);
    }

    public void setHost_address(String host_address) {
        apref.edit().putString("server_address",host_address).apply();
    }

    public String getHost_address() {
        return apref.getString("server_address","");
    }
}

