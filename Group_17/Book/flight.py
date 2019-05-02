from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

flights=[]
def flight_data(origin_para,destination_para,date_para,adults_para):
    my_url = 'https://www.makemytrip.com/flight/search?itinerary={}-{}-{}&tripType=O&paxType=A-{}_C-0_I-0&intl=false&=&cabinClass=E'.format(origin_para,destination_para,date_para,adults_para)
    chrome_path = r"C:\Users\Dell\Desktop\web scraping\chromedriver.exe"
    driver = webdriver.Chrome(chrome_path)
    driver.get(my_url)

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'fli_list_item6'))
        )

        print("page is loaded..")

        driver.execute_script("window.scrollTo(0,1366);")

        html = driver.page_source

        page_soup = soup(html, 'lxml')
        # print(page_soup)
        # print(page_soup.prettify())
        c = 0

        for container in page_soup.find_all('div', class_='fli-list one-way'):
            list=[]
            c += 1
            # print(container.prettify())
            flight_name = container.find('span', class_='airways-name').text
            flight_code = container.find('p', class_='fli-code').text
            dept_city = container.find('p', class_='dept-city').text
            dept_time = container.find('div', class_='dept-time').text
            no_of_stops = container.find('p', class_='fli-stops-desc').text
            reach_time = container.find('p', class_='reaching-time append_bottom3').text
            duration = container.find('p', class_='fli-duration').text
            arrival_city = container.find('p', class_='arrival-city').text
            price = container.find('span', class_='actual-price').text
            list.append(flight_name)
            list.append(flight_code)
            list.append(dept_city)
            list.append(dept_time)
            list.append(no_of_stops)
            list.append(reach_time)
            list.append(duration)
            list.append(arrival_city)
            list.append(price)
            flights.append(list)

            print(c)
            print(flight_name, '\t', flight_code, '\n', dept_city, ' - ', arrival_city, '\n', dept_time, ' - ', reach_time,
                   '\t', duration, '\t', no_of_stops, '\n', price)
            print('\n\n')

        driver.quit()
        print(flights)

    except:
        pass
    return flights

