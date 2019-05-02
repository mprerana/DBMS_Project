from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class movie(models.Model):
    movie_api_id = models.CharField(max_length=50)
    movie_name = models.CharField(max_length=100)
    movie_genre = models.CharField(max_length=100)
    movie_release_date = models.DateField(null=False)
    movie_age_rating = models.CharField(max_length=100)
    movie_duration_mins = models.CharField(max_length=100)
    movie_language = models.CharField(max_length=100)
    movie_actors = models.CharField(max_length=100)
    movie_directors = models.CharField(max_length=100)
    movie_producers = models.CharField(max_length=100)
    movie_writers = models.CharField(max_length=100)
    imdb_movie_rating = models.CharField(max_length=50)
    movie_description = models.TextField()
    movie_trailer_link = models.CharField(max_length=100)
    movie_poster_1 = models.ImageField(upload_to='poster_1',blank=True)
    movie_poster_2 = models.ImageField(upload_to='poster_2', blank=True)

class theatre(models.Model):
    theatre_api_id=models.CharField(max_length=50)
    theatre_name = models.CharField(max_length=50)
    adressline1 = models.CharField(max_length=50)
    adressline2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)
    theatre_rating = models.CharField(max_length=50)
    no_of_screens=models.CharField(max_length=50)

class screen(models.Model):
    screen_api_id = models.CharField(max_length=50)
    theatre_id = models.ForeignKey(theatre, on_delete=models.CASCADE)
    screen_no = models.CharField(max_length=5)
    seat_string = models.TextField()

class ticket_price_and_time(models.Model):
    ticket_api_id = models.CharField(max_length=50)
    screen_id = models.ForeignKey(screen, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(movie, on_delete=models.CASCADE,related_name='movie')
    show_timings = models.TimeField(null=False)
    date = models.DateField(null=False)
    language = models.CharField(max_length=50)
    screen_type = models.CharField(max_length=50)
    seat_class = models.CharField(max_length=50)
    price = models.CharField(max_length=100)

class booking_history(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    movie_id = models.ForeignKey(movie,on_delete=models.CASCADE)
    theatre_name = models.CharField(max_length=50)
    theatre_address = models.CharField(max_length=250)
    screen_no = models.CharField(max_length=5)
    show_date_and_time = models.DateTimeField(null=False)
    seat_no= models.CharField(max_length=50)
    no_of_seats=models.IntegerField(null=False)
    price_per_ticket=models.IntegerField(null=False)
    total_price= models.IntegerField(null=False)
    date_and_time_of_booking= models.DateTimeField(null=False)

class update_on_database(models.Model):
    last_update=models.DateTimeField(null=False)

class update_on_movie(models.Model):
    last_update_on_movie = models.DateTimeField(null=False)

class update_on_theatre(models.Model):
    last_update_on_theatre = models.DateTimeField(null=False)

class update_on_screen(models.Model):
    last_update_on_screen = models.DateTimeField(null=False)

class update_on_ticket(models.Model):
    last_update_on_ticket = models.DateTimeField(null=False)

class movie_search(models.Model):
    movie_id=models.OneToOneField(movie, on_delete=models.CASCADE,related_name='movie_id')
    inserted_date=models.DateTimeField(null=False)
    no_of_searches=models.IntegerField(null=False)


class transaction(models.Model):
    user = models.CharField(null=False, max_length=50)
    ticket_id = models.CharField(max_length=50)
    selected_seats = models.CharField(max_length=50)
    date_and_time = models.DateTimeField(null=False, default=timezone.now())
    price = models.IntegerField(null=False)
    txn_status = models.CharField(max_length=50)
#________________________________________________________________________________________________________________________

create_trigger_movie= """    
    CREATE TRIGGER on_update_movies 
    AFTER INSERT ON movies_and_cinemas_movie
    FOR EACH ROW 
    BEGIN
       INSERT INTO movies_and_cinemas_update_on_movie(last_update_on_movie)
          VALUES (CURRENT_TIMESTAMP());
       INSERT INTO movies_and_cinemas_update_on_database(last_update)
          VALUES (CURRENT_TIMESTAMP());  
       INSERT INTO movies_and_cinemas_movie_search(movie_id_id,inserted_date,no_of_searches)
          VALUES (NEW.id,CURRENT_TIMESTAMP(),0);      
    END
"""

#________________________________________________________________________________________________________________________

create_trigger_insert_theatre= """    
    CREATE TRIGGER inserts_on_theaters_table 
    AFTER INSERT ON movies_and_cinemas_theatre
    FOR EACH ROW 
    BEGIN
       INSERT INTO movies_and_cinemas_update_on_theatre(last_update_on_theatre)
          VALUES (CURRENT_TIMESTAMP());
       INSERT INTO movies_and_cinemas_update_on_database(last_update)
          VALUES (CURRENT_TIMESTAMP());   
    END

"""

create_trigger_update_theatre= """    
    CREATE TRIGGER updates_on_theaters_table 
    AFTER UPDATE ON movies_and_cinemas_theatre
    FOR EACH ROW 
    BEGIN
       INSERT INTO movies_and_cinemas_update_on_theatre(last_update_on_theatre)
          VALUES (CURRENT_TIMESTAMP());
       INSERT INTO movies_and_cinemas_update_on_database(last_update)
          VALUES (CURRENT_TIMESTAMP());   
    END
"""

create_trigger_delete_theatre= """    
    CREATE TRIGGER deletions_on_theaters_table 
    AFTER DELETE ON movies_and_cinemas_theatre
    FOR EACH ROW 
    BEGIN
       INSERT INTO movies_and_cinemas_update_on_theatre(last_update_on_theatre)
          VALUES (CURRENT_TIMESTAMP());
       INSERT INTO movies_and_cinemas_update_on_database(last_update)
          VALUES (CURRENT_TIMESTAMP());   
    END
"""

#________________________________________________________________________________________________________________________

create_trigger_insert_screen= """    
    CREATE TRIGGER inserts_on_screens_table 
    AFTER INSERT ON movies_and_cinemas_screen
    FOR EACH ROW 
    BEGIN
       INSERT INTO movies_and_cinemas_update_on_screen(last_update_on_screen)
          VALUES (CURRENT_TIMESTAMP());
       INSERT INTO movies_and_cinemas_update_on_database(last_update)
          VALUES (CURRENT_TIMESTAMP());   
    END

"""

create_trigger_update_screen= """    
    CREATE TRIGGER updates_on_screens_table 
    AFTER UPDATE ON movies_and_cinemas_screen
    FOR EACH ROW 
    BEGIN
       INSERT INTO movies_and_cinemas_update_on_screen(last_update_on_screen)
          VALUES (CURRENT_TIMESTAMP());
       INSERT INTO movies_and_cinemas_update_on_database(last_update)
          VALUES (CURRENT_TIMESTAMP());   
    END
"""

create_trigger_delete_screen= """    
    CREATE TRIGGER deletions_on_screens_table 
    AFTER DELETE ON movies_and_cinemas_screen
    FOR EACH ROW 
    BEGIN
       INSERT INTO movies_and_cinemas_update_on_screen(last_update_on_screen)
          VALUES (CURRENT_TIMESTAMP());
       INSERT INTO movies_and_cinemas_update_on_database(last_update)
          VALUES (CURRENT_TIMESTAMP());   
    END
"""

#________________________________________________________________________________________________________________________

create_trigger_ticket= """    
    CREATE TRIGGER on_update_tickets 
    AFTER INSERT ON movies_and_cinemas_ticket_price_and_time
    FOR EACH ROW 
    BEGIN
       INSERT INTO movies_and_cinemas_update_on_ticket(last_update_on_ticket)
          VALUES (CURRENT_TIMESTAMP());
       INSERT INTO movies_and_cinemas_update_on_database(last_update)
          VALUES (CURRENT_TIMESTAMP());   
    END
"""

#________________________________________________________________________________________________________________________

create_show_view="""

CREATE VIEW show_view AS
  SELECT  m.id as movie_id,m.movie_name,t.theatre_name,CONCAT(t.adressline1, ', ', t.adressline2, ', ', t.city, ', ', t.state, ', ', t.pincode) as theatre_address,s.screen_no,tic.date,tic.show_timings
  FROM  movies_and_cinemas_ticket_price_and_time as tic
  INNER JOIN movies_and_cinemas_movie as m ON tic.movie_id_id = m.id
  INNER JOIN movies_and_cinemas_screen as s ON tic.screen_id_id = s.id
  INNER JOIN movies_and_cinemas_theatre as t ON s.theatre_id_id = t.id
  
"""

create_top_search_view="""

CREATE VIEW top_search_view AS
  SELECT  m.id as movie_id , ROUND((m.no_of_searches * 1825 ) / DATEDIFF( m.inserted_date, CURRENT_TIMESTAMP()) , 3) as search_rate
  FROM  movies_and_cinemas_movie_search as m
  

"""

create_booking_history_view = """

CREATE VIEW booking_history_view AS
  SELECT  u.id,m.movie_name,CONCAT(b.theatre_name,' : ',b.theatre_address),b.no_of_seats,b.total_price
  FROM  movies_and_cinemas_booking_history as b 
  INNER JOIN movies_and_cinemas_movie as m ON b.movie_id_id = m.id
  INNER JOIN auth_user as u ON b.user_id = u.id
  

"""

create_ticket_expire_view="""

CREATE VIEW ticket_expire_view AS
  SELECT  tic.id, CONCAT( tic.date,' ',tic.show_timings ) as expire_date_time
  FROM  movies_and_cinemas_ticket_price_and_time as  tic



"""
#________________________________________________________________________________________________________________________

create_index_on_movie="""
CREATE INDEX movie_index
  ON movies_and_cinemas_movie (movie_name)
"""
create_index_on_theatre="""
CREATE INDEX theatre_index
  ON movies_and_cinemas_theatre (theatre_name)
"""
create_index_on_screen="""
CREATE INDEX screen_index
  ON movies_and_cinemas_screen (theatre_id_id)
"""
create_index_on_ticket="""
CREATE INDEX ticket_index
  ON movies_and_cinemas_ticket_price_and_time (movie_id_id,screen_id_id)
"""

#________________________________________________________________________________________________________________________

"""
create_booking_history_procedure=

CREATE PROCEDURE booking_history_procedure
(IN userid int(11),IN movie int(11),IN theatrename varchar(50) ,IN theatreaddress varchar(250) ,IN  screenno varchar(5),IN show_date date,IN time_ time(6),IN  seatno int(11),IN no_of_seat int(11) ,IN price_of_ticket int(11),IN datetime_of_booking datetime(6))
BEGIN
         INSERT INTO movies_and_cinemas_booking_history(user_id,movie_id_id,theatre_name,theatre_address,screen_no,show_date_and_time,seat_no,no_of_seats,price_per_ticket,total_price,date_and_time_of_booking)
         VALUES (userid,movie,theatrename,theatreaddress,screenno,(CAST(show_date AS DATETIME) + CAST(time_ AS DATETIME)),seatno,no_of_seat,price_of_ticket,(no_of_seat * price_of_ticket),datetime_of_booking);
END 

"""


#________________________________________________________________________________________________________________________

from django.db import connection
cursor = connection.cursor()
#cursor.execute(create_trigger_movie)
#cursor.execute(create_trigger_insert_theatre)
#cursor.execute(create_trigger_update_theatre)
#cursor.execute(create_trigger_delete_theatre)
#cursor.execute(create_trigger_insert_screen)
#cursor.execute(create_trigger_update_screen)
#cursor.execute(create_trigger_delete_screen)
#cursor.execute(create_trigger_ticket)
#cursor.execute(create_show_view)
#cursor.execute(create_index_on_movie)
#cursor.execute(create_index_on_theatre)
#cursor.execute(create_index_on_screen)
#cursor.execute(create_index_on_ticket)
#cursor.execute(create_top_search_view)
#cursor.execute(create_booking_history_view)
#cursor.execute(create_ticket_expire_view)
