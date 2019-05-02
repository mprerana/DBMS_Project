#https://www.cleartrip.com/hotels/details/223892

from bs4 import BeautifulSoup as soup
from selenium import webdriver
def room_book(my_url):
    a=[]
    b=[]
    chrome_path= r"C:\Users\Dell\Desktop\web scraping\chromedriver.exe"
    driver = webdriver.Chrome(chrome_path)
    driver.get(my_url)
    html = driver.page_source
    page_soup = soup(html,'lxml')
    pics=[]
    reviews=[]
    container=page_soup.find('div',class_='hotelTitle row').h1.text
    container2=page_soup.find('div',class_='hotelTitle row').h1.small.text
    for pic in page_soup.find_all('img',class_='coverImage fullWidthImg lazy'):
        pics.append(pic['src'])

    gmimg=page_soup.find('div',class_='col locationCard col15').img['src']
    hinfo=page_soup.find('div',class_='hInfo row').text
    check_items = page_soup.find('ul', class_='checkList row').text
    hinfolist = []
    checkitemslist=[]
    hinfolist = hinfo.split("\n")
    while ("" in hinfolist):
        hinfolist.remove("")
    checkitemslist = check_items.split("\n")
    while ("" in checkitemslist):
        checkitemslist.remove("")



    for review in page_soup.find_all('div',class_='hReview'):
        review_title=review.h5.text
        review_date=review.p.small.text
        review_review=review.find('p',class_='truncateReviewText').text.replace('\t','').replace('\n','')
        r=[]
        r.append(review_title)
        r.append(review_date)
        r.append(review_review)
        reviews.append(r)

    container=container.replace('\t','').replace('\n','')
    container2=container2.replace('\n','').replace('\t','')
    hotel_name=container.replace(container2,'')
    hotel_address=container2
    a.append(hotel_name)
    a.append(hotel_address)
    a.append(pics)
    a.append(gmimg)
    a.append(hinfolist)
    a.append(checkitemslist)
    a.append(reviews)

    print(a)
    b.append(a)

    driver.quit()
    return b

#room_book('https://www.cleartrip.com/hotels/details/2434012?c=200619|210619&r=2,0&compId=&fr=2&ur=2&urt=featured&stp=chmm#')