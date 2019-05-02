from django.db import models

class movie(models.Model):
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
    theatre_name = models.CharField(max_length=50)
    adressline1 = models.CharField(max_length=50)
    adressline2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)
    theatre_rating = models.CharField(max_length=50)
    no_of_screens=models.CharField(max_length=50)
    theatre_merchant_id = models.CharField(max_length=50)

class screen(models.Model):
    theatre_id = models.ForeignKey(theatre, on_delete=models.CASCADE)
    screen_no = models.CharField(max_length=5)
    seat_string = models.TextField()

class ticket_price_and_time(models.Model):
    screen_id = models.ForeignKey(screen, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(movie, on_delete=models.CASCADE,related_name='movie')
    show_timings = models.TimeField(null=False)
    date = models.DateField(null=False)
    language=models.CharField(max_length=50)
    screen_type=models.CharField(max_length=50)
    seat_class = models.CharField(max_length=50)
    price = models.CharField(max_length=100)

class booked_tickets(models.Model):
    ticket_seat_no = models.TextField()
    movie_details = models.ForeignKey(ticket_price_and_time, on_delete=models.CASCADE)
    ticket_book_from = models.CharField(max_length=50)
    ticket_booking_website = models.CharField(max_length=100)
    ticket_booking_tranc_id = models.CharField(max_length=100)
    ticket_booking_username = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    ticked_id = models.CharField(max_length=200)

class movie_update(models.Model):
    movie_id=models.CharField(max_length=50)
    last_change = models.DateTimeField(null=False)

class changes_on_theaters(models.Model):
    theatre_id=models.CharField(max_length=50)
    last_change = models.DateTimeField(null=False)
    change_type=models.CharField(max_length=50)

class changes_on_screens(models.Model):
    screen_id=models.CharField(max_length=50)
    last_change = models.DateTimeField(null=False)
    change_type=models.CharField(max_length=50)

class ticket_update(models.Model):
    ticket_price_and_time_id=models.CharField(max_length=50)
    last_change = models.DateTimeField(null=False)



#________________________________________________________________________________________________________________________

create_trigger_movie= """    
    CREATE TRIGGER on_update_movies 
    AFTER INSERT ON movie_and_cinema_data_movie
    FOR EACH ROW 
    BEGIN
       INSERT INTO movie_and_cinema_data_movie_update(movie_id,last_change)
          VALUES (NEW.id,CURRENT_TIMESTAMP());
    END
"""

#________________________________________________________________________________________________________________________

create_trigger_insert_theatre= """    
    CREATE TRIGGER inserts_on_theaters_table 
    AFTER INSERT ON movie_and_cinema_data_theatre
    FOR EACH ROW 
    BEGIN
       INSERT INTO movie_and_cinema_data_changes_on_theaters(theatre_id,last_change,change_type)
          VALUES (NEW.id,CURRENT_TIMESTAMP(),'inserted');
    END

"""

create_trigger_update_theatre= """    
    CREATE TRIGGER updates_on_theaters_table 
    AFTER UPDATE ON movie_and_cinema_data_theatre
    FOR EACH ROW 
    BEGIN
       INSERT INTO movie_and_cinema_data_changes_on_theaters(theatre_id,last_change,change_type)
          VALUES (NEW.id,CURRENT_TIMESTAMP(),'updated');
    END
"""

create_trigger_delete_theatre= """    
    CREATE TRIGGER deletions_on_theaters_table 
    AFTER DELETE ON movie_and_cinema_data_theatre
    FOR EACH ROW 
    BEGIN
       INSERT INTO movie_and_cinema_data_changes_on_theaters(theatre_id,last_change,change_type)
          VALUES (OLD.id,CURRENT_TIMESTAMP(),'deleted');
    END
"""

#________________________________________________________________________________________________________________________

create_trigger_insert_screen= """    
    CREATE TRIGGER inserts_on_screens_table 
    AFTER INSERT ON movie_and_cinema_data_screen
    FOR EACH ROW 
    BEGIN
       INSERT INTO movie_and_cinema_data_changes_on_screens(screen_id,last_change,change_type)
          VALUES (NEW.id,CURRENT_TIMESTAMP(),'inserted');
    END

"""

create_trigger_update_screen= """    
    CREATE TRIGGER updates_on_screens_table 
    AFTER UPDATE ON movie_and_cinema_data_screen
    FOR EACH ROW 
    BEGIN
       INSERT INTO movie_and_cinema_data_changes_on_screens(screen_id,last_change,change_type)
          VALUES (NEW.id,CURRENT_TIMESTAMP(),'updated');
    END
"""

create_trigger_delete_screen= """    
    CREATE TRIGGER deletions_on_screens_table 
    AFTER DELETE ON movie_and_cinema_data_screen
    FOR EACH ROW 
    BEGIN
       INSERT INTO movie_and_cinema_data_changes_on_screens(screen_id,last_change,change_type)
          VALUES (OLD.id,CURRENT_TIMESTAMP(),'deleted');
    END
"""

#________________________________________________________________________________________________________________________

create_trigger_ticket= """    
    CREATE TRIGGER on_update_tickets 
    AFTER INSERT ON movie_and_cinema_data_ticket_price_and_time
    FOR EACH ROW 
    BEGIN
       INSERT INTO movie_and_cinema_data_ticket_update(ticket_price_and_time_id,last_change)
          VALUES (NEW.id,CURRENT_TIMESTAMP());
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


from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

# This code is triggered whenever a new user has been created and saved to the database
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
       Token.objects.create(user=instance)

