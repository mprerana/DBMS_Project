from imdb import IMDb
from bs4 import BeautifulSoup
import requests
import csv
import datetime
import math
import random

city_list=['hyderabad']#,'mumbai','chennai']
movie_booking_suffix=['hyd','mumbai','chen']

csv_file_theatres=open('theatre_showtimings.csv','w',newline='')
csv_writer_theatre_showtime=csv.writer(csv_file_theatres)
csv_writer_theatre_showtime.writerow(['city','theatre','date','title','language','format','timings'])

csv_file_city_theatres=open('city_theatres.csv','w',newline='')
csv_writer_city_theatre=csv.writer(csv_file_city_theatres)
csv_writer_city_theatre.writerow(['city','theatre'])


csv_file_movies_model=open('movies.csv','w',newline='')
csv_current_movies=csv.writer(csv_file_movies_model)
csv_current_movies.writerow(['title','reldate','ageres','cover','plot','trailers','duration','likes','name'])

csv_file_movies_model=open('movies_dir.csv','w',newline='')
csv_current_dir=csv.writer(csv_file_movies_model)
csv_current_dir.writerow(['title','director'])


csv_file_movies_city_model=open('movies_cities.csv','w',newline='')
csv_current_movies_city=csv.writer(csv_file_movies_city_model)

csv_movie_cast_crew_model=open('current_movies_cast_crew.csv','w',newline='')
csv_current_movies_cast_crew=csv.writer(csv_movie_cast_crew_model)
csv_current_movies_cast_crew.writerow(['title','cast_name','cast_img_link'])


csv_movie_language_model=open('movie_language.csv','w',newline='')
csv_movie_language=csv.writer(csv_movie_language_model)
csv_movie_language.writerow(['title','language'])

csv_movie_dimension_model=open('movie_format.csv','w',newline='')
csv_movie_dimension=csv.writer(csv_movie_dimension_model)
csv_movie_dimension.writerow(['title','dimension'])

csv_movie_genre_model=open('movie_genre.csv','w',newline='')
csv_movie_genre=csv.writer(csv_movie_genre_model)
csv_movie_genre.writerow(['title','genre'])



for city_iteration in range(0,len(city_list)):
    city_url=f'https://in.bookmyshow.com/{city_list[city_iteration]}/movies' 
    
    source=requests.get(city_url).text
    soup=BeautifulSoup(source,'lxml')
    movie_name_delimeter="-"

    trailer_link="N/A"
    status=1

    for movie_card in soup.find_all('div',class_='card-container wow fadeIn movie-card-container'):

        img_src=movie_card.find('img',class_='__poster __animated')['data-src']
        movie_title=movie_card.find('div',class_='card-title').h4.text
        language=movie_card.find('div',class_='card-tag').span.li.text.strip().split(',')
        
        try:    
            censor=movie_card.find('div',class_='card-tag').span.span.text.split('|')[0]     
        except:
            censor=None

        try:
            genre=movie_card['data-genre-filter'].split('|')
        except:
            genre=None    

        genre_already_added=[]
        genres=[]
        for gen_iteration in range(1,len(genre)):
            if(genre[gen_iteration] not in genre_already_added):
                # csv_movie_genre.writerow([movie_title,genre[gen_iteration]])
                genres.append(genre[gen_iteration])
                genre_already_added.append(genre[gen_iteration])    
        csv_movie_genre.writerow([movie_title,genres])
        try:
            dimension=movie_card['data-dimension-filter'].strip().split('|')
        except:
            dimension=None

        # #Creating a two csv files which stores the information of languages and dimensions

        for lang in language:
            try:
                if (lang != ''):
                    csv_movie_language.writerow([movie_title,lang])
            except:
                pass

        for dim_iteration in range(1,len(dimension)):
            csv_movie_dimension.writerow([movie_title,dimension[dim_iteration]])


    # #Individual Movie Synopsis extraction starts here

        movie_name_in_url=movie_card['data-search-filter'].split('-')
        movie_name_in_url.remove('movies')
        movie_name_in_url=movie_name_delimeter.join(movie_name_in_url).lower()


        movie_ID=movie_card.find('img',class_='__poster __animated')['data-src'].split("/")
        movie_ID=movie_ID[len(movie_ID)-1]
        movie_ID=movie_ID.split("-")
        movie_ID=movie_ID[len(movie_ID)-7].upper()

        individual_movie_url=f'https://in.bookmyshow.com/{city_list[city_iteration]}/movies/{movie_name_in_url}/{movie_ID}'

        individual_movie_source1=requests.get(individual_movie_url).text
        individual_movie_soup=BeautifulSoup(individual_movie_source1,'lxml')

        summary_reviews=individual_movie_soup.find('div',class_="summary-reviews")
        movie_synopsis=summary_reviews.find('div',class_="synopsis").blockquote.text.strip().split('\n')[0]
        
        try:   
            duration=individual_movie_soup.find('div',class_="movie-synopsis-content-wrapper").find('div',class_="clock-time").find('span',class_="__time").text
        except:
            duration="N/A" 

        try:
            release_date=individual_movie_soup.find('div',class_="movie-synopsis-content-wrapper").find('div',class_='calander-date').find('span',class_='__release-date').text
        except:
            release_date='N/A'       
        
        try:
            likes=individual_movie_soup.find('div',class_="movie-synopsis-content-wrapper").find('div',class_="review-ratings").find('div',class_="__votes").text.split()[0]
        except:
            likes=0
        
        csv_current_movies_city.writerow([city_list[city_iteration],movie_title])
        csv_current_movies.writerow([movie_title,release_date,censor,img_src,movie_synopsis,trailer_link,duration,likes,movie_title.strip()])
        

    
    ##Individual movie Synopsis retrieval and storing in file completed  

        

    ##Movie Theatres and timings are found here
        movie_ticket_booking_name=movie_card.find('img',class_='__poster __animated')['data-src'].split("/")
        movie_ticket_booking_name=movie_ticket_booking_name[len(movie_ticket_booking_name)-1].split("-")
        movie_ticket_booking_name=movie_ticket_booking_name[:len(movie_ticket_booking_name)-7]
        movie_ticket_booking_name=movie_name_delimeter.join(movie_ticket_booking_name)

        present_date=str(datetime.datetime.today().strftime('%Y-%m-%d'))

        cost_iteration=1
        i=0

        for i in range(0,5):
            
            
            present_date=str(present_date)

            date_of_finding_theatre=present_date.split("-")
            date_of_finding_theatre="".join(date_of_finding_theatre)


            movie_ticket_booking_page_url=f'https://in.bookmyshow.com/buytickets/{movie_ticket_booking_name}-{city_list[city_iteration]}/movie-{movie_booking_suffix[city_iteration]}-{movie_ID}-MT/{date_of_finding_theatre}'
            # print(movie_ticket_booking_page_url)
            ticket_booking_source=requests.get(movie_ticket_booking_page_url).text
            ticket_booking_soup=BeautifulSoup(ticket_booking_source,'lxml')

            link_list=[]
            lable_list=[]

            for lang_dim_theatre in ticket_booking_soup.find_all('li',class_='languages'):
                link=lang_dim_theatre.a['href']
                lable=lang_dim_theatre.a.label.text
                link_list.append(link)
                lable_list.append(lable)


            for link_iteration in range(0,len(link_list)):
                movie_ticket_booking_page_url=f'https://in.bookmyshow.com{link_list[link_iteration]}'
                ticket_booking_source=requests.get(movie_ticket_booking_page_url).text
                ticket_booking_soup=BeautifulSoup(ticket_booking_source,'lxml')
                print(movie_ticket_booking_page_url)
                
                theatre_block=ticket_booking_soup.find('ul',id='venuelist')
                language=lable_list[link_iteration].split('-')[0].strip()
                format_dim=lable_list[link_iteration].split('-')[1].strip()

                
                for theatres_iteration in theatre_block.find_all('li'):
                    theatre=theatres_iteration.find('a',class_='__venue-name').text.strip()

                    #Storing city and theatre in a file
                    csv_writer_city_theatre.writerow([city_list[city_iteration],theatre])

                    for timings_list in theatres_iteration.find_all('div',class_="_sold _past _off-avail"):
                        t1=timings_list.a.text
                        seat_layout=random.randint(1,3)
                        csv_writer_theatre_showtime.writerow([city_list[city_iteration],theatre,seat_layout,present_date,movie_title,language,format_dim,t1])
                    for timings_list in theatres_iteration.find_all('div',class_='_sold _soldout'):
                        t2=timings_list.a.text
                        seat_layout=random.randint(1,3)
                        csv_writer_theatre_showtime.writerow([city_list[city_iteration],theatre,seat_layout,present_date,movie_title,language,format_dim,t2])
                    for timings_list in theatres_iteration.find_all('a',class_='__showtime-link time_vrcenter'):
                        t3=timings_list.text.strip()  
                        seat_layout=random.randint(1,3)
                        csv_writer_theatre_showtime.writerow([city_list[city_iteration],theatre,seat_layout,present_date,movie_title,language,format_dim,t3])    
            
        #     ##Incrementing day by one till a week completes starts here
            present_date=datetime.datetime.strptime(present_date,"%Y-%m-%d")
            date_interval=datetime.timedelta(days=1)    #Incrementing date by one day
            present_date=present_date+date_interval
            present_date=str(present_date.date())   #Date object should always be converted to string before processing it
        
            


    ##End of movie theatres and timings
  


    coming_soon_link=f'https://in.bookmyshow.com/{city_list[city_iteration]}/movies/comingsoon'
    source=requests.get(coming_soon_link).text
    soup=BeautifulSoup(source,'lxml')


    num_coming_soon=1
    for movie_card in soup.find_all('aside',class_='wow card-container movie-card-container'):
        img_src=movie_card.find('img',class_='__poster __animated')['data-src']
        movie_title=movie_card.find('div',class_='card-title').h4.text
        language=movie_card.find('div',class_='card-tag').span.li.text.strip().split(',')
        releasing_year=movie_card['data-year']    
        
        try:    
            releasing_date=movie_card.find('div',class_='card-tag').span.span.text.split('|')[0]  
            if releasing_date == releasing_year:
                releasing_date="N/A"   
        except:
            releasing_date=None


        censor="N/A"
        duration="N/A"
        status=0

        try:
            genre=movie_card['data-genre-filter'].split('|')
            # csv_movie_genre.writerow([movie_title,genre])
        except:
            genre="N/A"    

        genre_already_added=[]
        genres=[]
        for gen_iteration in range(1,len(genre)):
            if(genre[gen_iteration] not in genre_already_added):
                # csv_movie_genre.writerow([movie_title,genre[gen_iteration]])
                genres.append(genre[gen_iteration])
                genre_already_added.append(genre[gen_iteration])    
        csv_movie_genre.writerow([movie_title,genres])
        try:
            dimension=movie_card['data-dimension-filter'].strip().split('|')
        except:
            dimension="N/A"
            
        csv_movie_dimension.writerow([movie_title,dimension])        


        #Creating a two csv files which stores the information of languages and dimensions

        for lang in language:
            try:
                if (lang !=''):
                    csv_movie_language.writerow([movie_title,lang])
            except:
                pass


    # #Individual Movie Synopsis extraction starts here

        movie_name_in_url=movie_card.a['href'].split('/')
        movie_name_in_url=movie_name_in_url[len(movie_name_in_url)-2]

        movie_ID=movie_card.a['href'].split('/')
        movie_ID=movie_ID[len(movie_ID)-1]

        individual_movie_url=f'https://in.bookmyshow.com/{city_list[city_iteration]}/movies/{movie_name_in_url}/{movie_ID}'

        individual_movie_source1=requests.get(individual_movie_url).text
        individual_movie_soup=BeautifulSoup(individual_movie_source1,'lxml')

        summary_reviews=individual_movie_soup.find('div',class_="summary-reviews")
        movie_synopsis=summary_reviews.blockquote.text.strip().split('\n')[0]

        try:
            likes=individual_movie_soup.find('div',class_="mv-coming-soon").find('span',class_="__votes").text
        except:
            likes=0    
   

    # #Individual movie Synopsis retrieval and sporing in file completed  
        csv_current_movies_city.writerow([city_list[city_iteration],movie_title])
        csv_current_movies.writerow([movie_title,release_date,censor,img_src,movie_synopsis,trailer_link,duration,likes,movie_title.strip()])
        
        num_coming_soon=num_coming_soon+1
        if(num_coming_soon==149):
            break



for city_iteration in range(0,len(city_list)):

    city_url=f'https://in.bookmyshow.com/{city_list[city_iteration]}/movies' 
    
    source=requests.get(city_url).text
    soup=BeautifulSoup(source,'lxml')
    movie_name_delimeter="-"

    trailer_link="N/A"
    status=1
    ##Getting information of cast and crew along with image link of them starts here
    for movie_card in soup.find_all('div',class_='card-container wow fadeIn movie-card-container'):
        print("Hi")
        movie_title=movie_card.find('div',class_='card-title').h4.text

        movie_ticket_booking_name=movie_card.find('img',class_='__poster __animated')['data-src'].split("/")
        movie_ticket_booking_name=movie_ticket_booking_name[len(movie_ticket_booking_name)-1].split("-")
        movie_ticket_booking_name=movie_ticket_booking_name[:len(movie_ticket_booking_name)-7]
        movie_ticket_booking_name=movie_name_delimeter.join(movie_ticket_booking_name)


        movie_ID=movie_card.find('img',class_='__poster __animated')['data-src'].split("/")
        movie_ID=movie_ID[len(movie_ID)-1]
        movie_ID=movie_ID.split("-")
        movie_ID=movie_ID[len(movie_ID)-7].upper()

        present_date=str(datetime.datetime.today().strftime('%Y-%m-%d'))

        present_date=str(present_date)

        date_of_finding_theatre=present_date.split("-")
        date_of_finding_theatre="".join(date_of_finding_theatre)

        movie_ticket_booking_page_url=f'https://in.bookmyshow.com/buytickets/{movie_ticket_booking_name}-{city_list[city_iteration]}/movie-{movie_booking_suffix[city_iteration]}-{movie_ID}-MT/{date_of_finding_theatre}'
        print(movie_ticket_booking_page_url)

        ticket_booking_source=requests.get(movie_ticket_booking_page_url).text
        ticket_booking_soup=BeautifulSoup(ticket_booking_source,'lxml')

        try:
            director=ticket_booking_soup.find('span',class_="__director-name wow fadeIn").img
            director_img=director['data-src']
            director_name=director['title']
            csv_current_dir.writerow([movie_title,director_name])    
        except:
            director_img="N/A"
            director_name="N/A"
            csv_current_movies_cast_crew.writerow([movie_title,director_name,director_img])
        


        cast_crew=ticket_booking_soup.find('div',class_="__crew-info")
        try:
            crew_members=[]
            crew_members_image=[]
            for crew_member in cast_crew.find_all('span',class_="__cast-img-name wow fadeIn"):
                crew_member_name=crew_member.img['title']
                crew_member_image=crew_member.img['data-src']
                crew_members.append(crew_member_name)
                crew_members_image.append(crew_member_image)
            csv_current_movies_cast_crew.writerow([movie_title,crew_members,crew_members_image])
        except:
            pass
            


#For current movies
csv_file_theatres.close()
csv_file_city_theatres.close()


csv_movie_genre_model.close()
csv_movie_language_model.close()
csv_movie_dimension_model.close() 


#For cast_crew
csv_movie_cast_crew_model.close()
csv_file_movies_model.close()
csv_file_movies_city_model.close()





##Scraping reviews
ia=IMDb()

movies_file=open('movies.csv','r')
movies_reader=csv.reader(movies_file)

movie_review_file=open('movie_reviews.csv','w',newline='')
movie_review_writer=csv.writer(movie_review_file)
movie_review_writer.writerow(['title','comments'])

movies_already_reviewed=[]

for line in movies_reader:   
    print('Hi')
    if(line[0] not in movies_already_reviewed):
        try:
            movie=ia.search_movie(line[0])
            movie_id=movie[0].movieID
        except:
            pass
        
        if(movie_id):    
            imdb_movie_url=f'https://www.imdb.com/title/tt{movie_id}/reviews?ref_=tt_ql_3'
            source1=requests.get(imdb_movie_url).text   
            soup1=BeautifulSoup(source1,'lxml')
            comments=[]
            for p in soup1.find_all('div',class_="lister-item-content"):
                try:
                    rating=p.find('div',class_="ipl-ratings-bar").span.span.text
                    rating=int(math.ceil(float(rating)/2))
                except:
                    rating=0
                comment={'user':'Yuvraj','date':'5-1-2019'}
                review=p.find('div',class_="text show-more__control").text.strip()
                comment['cmnt']=review
                # try:
                #     movie_review_writer.writerow([line[0],review])
                # except:
                #     pass   
                comments.append(comment)
            try:
                movie_review_writer.writerow([line[0],comments])
            except:
                pass
            # movie_review_writer.writerow([line[0],comments])
        else:
            print("Entered else")
            movie_review_writer.writerow([line[0],"N/A","N/A"])

        movies_already_reviewed.append(line[0])



movie_review_file.close()
movies_file.close()