
import mysql.connector

# conn = mysql.connector.connect(
#   host='localhost',
#   user='root',
#   passwd='Sujala@123',
#   #database="db4",
#   )
# #SET GLOBAL sql_mode=''
# mcursor=conn.cursor()
# mcursor.execute("CREATE DATABASE dbp")
def checkSetup():
    conn = mysql.connector.connect(
      host='localhost',
      user='root',
      passwd='Sujala@123',
      database="trial17",
      autocommit=True
    )

    #conn = mysql.connect('gas.db')
    cursor = conn.cursor()
    
    
    #cursor.execute("SELECT name FROM db2 WHERE type='table' AND name='instructors'")
    result = cursor.fetchone()
    conn.close()
    if result is None:
        return False
    return True


def setup():
    conn = mysql.connector.connect(
      host='localhost',
      user='root',
      passwd='Sujala@123',
      database="trial17",
      )

    #conn = sqlite3.connect('gas.db')
    cursor = conn.cursor()
    create_instructors_table = """
        CREATE TABLE IF NOT EXISTS instructors (
          id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
          #id int NOT NULL DEFAULT 1 PRIMARY KEY,
          name varchar(50) NOT NULL,
          hours int NOT NULL,
          schedule varchar(5000) NOT NULL,
          active BOOLEAN NOT NULL DEFAULT 1 CHECK (
            active IN (0, 1)
          )
          -- PRIMARY KEY (id);
        );
    """
    create_rooms_table = """
        CREATE TABLE IF NOT EXISTS rooms (
          id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
          name varchar(50) NOT NULL,
          type varchar(50) NOT NULL,
          schedule varchar(5000) NOT NULL,
          active boolean NOT NULL DEFAULT 1 CHECK (
            active IN (0, 1)
          )
        );
    """
    create_subjects_table = """
        CREATE TABLE IF NOT EXISTS subjects (
          id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
          name varchar(50) NOT NULL,
          hours varchar(50) NOT NULL,
          code varchar(50) NOT NULL,
          description varchar(50) NOT NULL,
          instructors varchar(50) NOT NULL,
          divisible boolean NOT NULL DEFAULT 1 CHECK (
            divisible IN (0, 1)
           ),
          type varchar(20) NOT NULL
        );
    """

    create_subjects_instructors_table = """
        CREATE TABLE IF NOT EXISTS subjects_instructors (
          id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
          subjectid int NOT NULL ,#foreign key(subjectid) references subjects(id) on delete cascade,
          instructorid int NOT NULL, #foreign key(instructorid) references instructors(id) on delete cascade,
          foreign key subjects_instructors_subjectid(subjectid)
          references subjects(id) 
          on delete cascade 
          on update cascade , 
          foreign key subjects_instructors_instructorid(instructorid) 
          references instructors(id) 
          on delete cascade 
          on update cascade

          );
          """

    create_sections_table = """
        CREATE TABLE IF NOT EXISTS sections (
          id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
          name varchar(50) NOT NULL,
          schedule varchar(5000) NOT NULL,
          subjects varchar(50) NOT NULL, 
          active boolean NOT NULL DEFAULT 1 CHECK (
            active IN (0, 1)
          ),
          stay boolean NOT NULL DEFAULT 0 CHECK (
            active IN (0, 1)
          ),
          foreign key sections_subjects(subjects) 
          references subjects(id) 
          on delete cascade 
          on update cascade
        );
    """
    create_sharing_table = """
        CREATE TABLE IF NOT EXISTS sharings (
          id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
          subjectId int NOT NULL,
          sections varchar(50) NOT NULL,
          final boolean NOT NULL DEFAULT 0 CHECK (
            final IN (0, 1)
          )
        );
    """
    create_results_table = """
        CREATE TABLE IF NOT EXISTS results (
          id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
          content BLOB NOT NULL,
          timestamp DATETIME DEFAULT CURRENT_TIMESTAMP()
        );
    """

    create_deleted_subj_table = """
        CREATE TABLE IF NOT EXISTS subj_del (
          id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
          subj varchar(50) NOT NULL,
          timestamp DATETIME DEFAULT CURRENT_TIMESTAMP()
        );
    """




    create_trigger_subj_del="""
        CREATE TRIGGER subj_del22
        AFTER DELETE ON subjects
        FOR EACH ROW 
        BEGIN
          INSERT INTO del_subj (subj)
          #set action="delete"
          VALUES (OLD.name);

        END

    """




    create_deleted_instructor_table = """
        CREATE TABLE IF NOT EXISTS instructor_del (
          id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
          instructor varchar(50) NOT NULL,
          timestamp DATETIME DEFAULT CURRENT_TIMESTAMP()
        );
    """

    create_trigger_instructor_del="""
        CREATE TRIGGER  instructor_del22 
        AFTER DELETE ON instructors
        FOR EACH ROW 
        BEGIN
          INSERT INTO instructor_del (instructor)
          #set action="delete"
          VALUES (OLD.name);

        END

    """


    create_sch_events="""

        CREATE EVENT instructor_update18 
        ON SCHEDULE AT CURRENT_TIMESTAMP+INTERVAL 1 year
        DO 
          DELETE FROM instructor_del WHERE CURRENT_TIMESTAMP()-timestamp=3600


    """


    create_materialized_view_table = """

    

    CREATE TABLE IF NOT EXISTS mvInstructor (
        id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
        name varchar(50) NOT NULL,

    );

    CREATE INDEX Iid ON mvInstructor(id)

    CREATE VIEW vinstructors AS
        SELECT * FROM mvInstructor;

    """

    update_materialized_view_table="""

    DELIMITER |

    CREATE TRIGGER trig_mviInstructor AFTER INSERT ON instructors
       FOR EACH ROW BEGIN
          INSERT INTO mvInstructor
             SELECT id,name
             FROM instructors
       END;
    |

    CREATE TRIGGER trig_mvdInstructor AFTER DELETE ON instructors
       FOR EACH ROW BEGIN
          DELETE FROM mvInstructor
          WHERE id=OLD.id;
       END;
    |
    CREATE TRIGGER trig_mvuInstructor AFTER UPDATE ON instructors
       FOR EACH ROW BEGIN
          UPDATE mvInstructor SET name=NEW.name, id=NEW.id
          WHERE id=NEW.id;
       END;
    |

    
    DELIMITER ;





    """
    
    
    cursor.execute(create_instructors_table)
    cursor.execute(create_rooms_table)
    cursor.execute(create_subjects_table)
    cursor.execute(create_sections_table)
    cursor.execute(create_sharing_table)
    cursor.execute(create_results_table)
    cursor.execute(create_subjects_instructors_table)
    cursor.execute(create_deleted_subj_table)
    cursor.execute(create_trigger_subj_del)
    cursor.execute(create_deleted_instructor_table)
    cursor.execute(create_trigger_instructor_del)
    cursor.execute(create_sch_events)
    cursor.execute(create_materialized_view_table)
    cursor.execute(update_materialized_view_table)

    
    
    conn.commit()
    conn.close()


def getConnection():
    conn = mysql.connector.connect(
      host='localhost',
      user='root',
      passwd='Sujala@123',
      database="trial17",
      )

    return conn


