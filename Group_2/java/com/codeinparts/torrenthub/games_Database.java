package com.codeinparts.torrenthub;

import android.provider.BaseColumns;

public final class games_Database {

    private games_Database(){}

    public static class gameEntry implements BaseColumns{

        public static final String TABLE_NAME="games";
        public static final String COLUMN_NAME_GAME="Movie";
        public static final String COLUMN_NAME_LANGUAGE="Language";
        public static final String COLUMN_NAME_SIZE="size";
        public static final String COLUMN_NAME_QUALITY="quality";
        public static final String COLUMN_NAME_FILE_LOCATION="location";

    }
}


