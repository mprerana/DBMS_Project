package com.codeinparts.torrenthub;

import android.provider.BaseColumns;

public final class movies_Database {

    private movies_Database(){}

    public static class movieEntry implements BaseColumns{

        public static final String TABLE_NAME="movies";
        public static final String COLUMN_NAME_MOVIE="Movie";
        public static final String COLUMN_NAME_LANGUAGE="Language";
        public static final String COLUMN_NAME_SIZE="size";
        public static final String COLUMN_NAME_QUALITY="quality";
        public static final String COLUMN_NAME_FILE_LOCATION="location";

    }
}


