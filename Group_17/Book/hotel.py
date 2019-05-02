from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def hotel_show(city_para,state_para,chk_in_para,chk_out_para):

    my_url = 'https://www.cleartrip.com/hotels/results?city={}&state={}&country=IN&area=&poi=&hotelId=&hotelName=&SearchTag=&chk_in={}&chk_out={}&adults1=2&children1=0&num_rooms=1'.format(city_para,state_para,chk_in_para,chk_out_para)

    chrome_path= r"C:\Users\Dell\Desktop\web scraping\chromedriver.exe"
    driver = webdriver.Chrome(chrome_path)
    driver.get(my_url)


    # print("start :) ")
    element = WebDriverWait(driver, 10).until(

        EC.presence_of_element_located((By.CLASS_NAME, "rsImg"))



    )

    # print("page is loaded..")

    html = driver.page_source
    page_soup = soup(html,'lxml')

    All_hotels=[]
    for container in page_soup.find_all('section', class_='clearFix flex'):
        hotel = []
        name=container.find('a',class_='hotelDetails').text
        # print(name)
        address=container.find('small',class_='areaName truncate')['data-area']
        # print(address)
        hotel_id='https://www.cleartrip.com'+container.find('button',class_='button booking hotelDetails')['href']
        # print(hotel_id)
        try:
            pic=container.find('img',class_='rsImg')['src']
        except:
            pic='false'
        # print(pic)
        hotel.append(name)
        hotel.append(address)
        hotel.append(hotel_id)
        hotel.append(pic)

        All_hotels.append(hotel)

    driver.quit()
    return All_hotels