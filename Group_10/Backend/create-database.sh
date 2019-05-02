#!/bin/bash

if [[ -z "$QUAZAPP_DATABASE_UNAME" ]]; then
    UNAME="testuser"
else
    UNAME="$QUAZAPP_DATABASE_UNAME"
fi

if [[ -z "$QUAZAPP_DATABASE_PASSWRD" ]]; then
    PASS="royya123"
else
    PASS="$QUAZAPP_DATABASE_PASSWRD"
fi

if [[ -z "$QUAZAPP_DATABASE_DB" ]]; then
    DBNAME="testdb"
else
    DBNAME="$QUAZAPP_DATABASE_DB"
fi

echo $UNAME $PASS $DBNAME

sudo -u postgres -H psql postgres -c "CREATE DATABASE $DBNAME" 

if [[ $? -ne 0 ]]; then 
    echo "Database $DBNAME already exists"
    echo "Press 1. to continue with the same database"
    echo "Press 2. to delete and re-create the database"
    echo "Press 3. to exit"
    read -p "" op

    case $op in 
        2 )
            sudo -u postgres -H psql postgres -c "DROP DATABASE $DBNAME" 
            sudo -u postgres -H psql postgres -c "CREATE DATABASE $DBNAME"
        ;;

        3 )
            exit 0
        ;;

        1 ) 
        ;;

        * ) 
            echo "Invalid Input"
            exit 1
        ;;
    esac
fi


sudo -u postgres -H psql postgres -c "CREATE USER $UNAME WITH PASSWORD '$PASS'"

if [[ $? -ne 0 ]]; then
    echo "User $UNAME already exists"
    echo "Press 1. to continue"
    echo "Press 2. to exit"
    read -p "" op

    case $op in
        1 )
        ;;
    
        2 )
            exit 0
        ;;

        * )
            exit 1
    esac
fi

sudo -u postgres -H psql postgres -c "GRANT ALL PRIVILEGES ON DATABASE $DBNAME TO $UNAME"
