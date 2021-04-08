'''
This will be the main script of the main project.
Maybe a class will be created


Notes:
    ctrl+shift+i interactive URL window
    Van stock level anélkül is hogy meg kéne nyisd a munchot
    értékelést is ki lehet szedni star-rating class
    gtm4wp_productdata ebben van:
        price
        name
        stocklevel
    Mikor vehető át azt is ki lehet szedni de az csak egy text azon a classon belül amin belül ez a sok mindenség van
    Sale mértékét is le lehetne szedni akár
        onsale class-ban van
    Kéne egy location is
        Vagy keress rá és azt rendeld hozzá
        Vagy találj valami attributeumot
        Vagy csinálj egy mappinget
            Kigyűjtöd az URL-jüket és a végén a distinct URL ekre nyomsz egy keresést és ott van egy cím mindhez
    Nyitvatartas
        Ugyanúgy a végén egész könnyen ki lehet gyűjteni valószínűleg



    Új összegzés

    Dinamikusan változó attributumok:
        -Stock
    Nem dinamikus infok:
        -Name
        -URL
        -Category
        -Price
        -Rating
        -Discount
        -Opening time
        -Location

    Notes:
        -Nagyon gyorsan szed le infokat miutan mar megvan a connection --> ki lehet szedni statikus infokat is folyamat
        -

        Végén leszedni:
            -Opening time & Location egy classban van class = "sku"

        Dinamikusan leszedni:
            -Stock
            -Name
            -URL
            -Category
            -Price
            -Rating

        Lehet erdemes nem pont 10 percenkent hanem akörül egy kis véletlen számmal


# Idea:
    - To create a list of dicts where every dict contains info about the munch

# TO Learn
    -Better understand to extract string from string

# Keep in mind!
    -Charity munch speciális se rating se discount se location

# TODO:
    -Exportalt Date legyen pontosabb és kompatibilis excellel
    -Nevek kódolása legyen olvasható CSV-ben is
    -Rendes nyitvatartási időt leszedni googleről

# Progress
    -Error handling included

'''

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import pandas as pd
import time

starter = datetime.now()

# setting up the driver
chr_driver = r'C:\Python\Chrome_driver_for_selenium\chromedriver.exe'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("disable-notifications")  # only disables notification window, one still remains
driver = webdriver.Chrome(chr_driver, options=chrome_options)

# driver.get('https://munch.hu/terkep/')
# # driver.quit()  # close whole window
# print(driver.title)

# li classes contain all the info that we need about a munch
munches = driver.find_elements_by_tag_name('li')

page_left = True
page_number = 1


driver.get('https://munch.hu/terkep/')
print(driver.title)

dicts_list = []

while page_left:

    print("\nExtracting page: {pag}\n".format(pag=page_number))
    munches = driver.find_elements_by_tag_name('li')

    for munch in munches:

        munch_info = {}

        munch_main = munch.find_elements_by_xpath(
            './/a[@class = "woocommerce-LoopProduct-link woocommerce-loop-product__link"]')

        # there are li class elements that don't refer to a munch hence we don't need
        if munch_main.__len__() > 0:
            try:
                core_data = munch_main[0].find_elements_by_xpath('.//span[@class = "gtm4wp_productdata"]')
                print(core_data[0].get_attribute('data-gtm4wp_product_name'))
                print(core_data[0].get_attribute('data-gtm4wp_product_price'))
                print(core_data[0].get_attribute('data-gtm4wp_product_cat'))
                print(core_data[0].get_attribute('data-gtm4wp_product_url'))
                print(core_data[0].get_attribute('data-gtm4wp_product_stocklevel'))

                munch_info.update({'Name': core_data[0].get_attribute("data-gtm4wp_product_name")})
                munch_info.update({'Price': core_data[0].get_attribute("data-gtm4wp_product_price")})
                munch_info.update({'Category': core_data[0].get_attribute("data-gtm4wp_product_cat")})
                munch_info.update({'URL': core_data[0].get_attribute("data-gtm4wp_product_url")})
                munch_info.update({'Stock': core_data[0].get_attribute("data-gtm4wp_product_stocklevel")})

                print('End of core info')
            except IndexError:
                print('No Core data')

            try:
                discount = munch_main[0].find_elements_by_xpath('.//span[@class = "onsale"]')[0].text
                print('Discount: {dis}'.format(dis=discount))
                munch_info.update({'Discount': munch_main[0].find_elements_by_xpath('.//span[@class = "onsale"]')[0].text})
            except IndexError:
                print('No discount for this product')
                discount = 0

            try:
                rating_element = munch_main[0].find_elements_by_xpath('.//div[@class = "star-rating"]')
                rating_str = rating_element[0].get_attribute('aria-label')
                rating = rating_str.split(": ", 1)[1].split(" /", 1)[0]
                print("Rating: {rate}".format(rate=rating))
                munch_info.update({'Rating': rating})
            except IndexError:
                print('No rating for this product')

            munch_info.update({'Page': page_number})
            munch_info.update({'Time': datetime.now()})
            # number of the extraction should be added as well

            dicts_list.append(munch_info)

            print('End of munch\n')



# Stock data is not the same as on the own page of the munch
# you can select more than the stock but you wont be able to buy it (error is on web page's side)
# correct stock number is extracted

    if page_number == 1:
        # # disabling discount pop-up
        # time.sleep(3)
        # try:
        #     driver.find_elements_by_xpath('.//i[@class = "eicon-close"]')[0].click()
        # except IndexError:
        #     print('Window not yet available')

        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, './/i[@class = "eicon-close"]'))).click()
        # na ez azért sokkal elegánsabb

    # navigating to next page
    page_number += 1
    driver.get('https://munch.hu/terkep/page/{num}/'.format(num=page_number))
    print(driver.title)

    if driver.title == 'Az oldal nem található - Munch.hu':
        page_left = False
        break

# Creating data frame
df = pd.DataFrame(dicts_list)

# Exporting dataframe
actual_time = datetime.now().strftime("%Y-%m-%d_%H%M%S")
df.to_csv(path_or_buf='C:/Python/Output/Munch_info_{tim}.csv'.format(tim=actual_time),
          index=False, encoding='UTF-8', header=True, sep=";")




# # Getting Opening time and location
# driver.get('https://munch.hu/termek/friss-pekseg/')
#
# print(driver.title)
#
# munch_loc_open = driver.find_elements_by_xpath('.//span[@class = "sku"]')[0].text
#
# # getting rid of the emoji at the beginning
# munch_loc_open_tidy = munch_loc_open.split(" ", 1)[1]
#
# # location
# location = munch_loc_open_tidy.split("|", 1)[0]
# city, address, postal_code = location.split(', ')
# print(location)
# print(city)
# print(address)
# print(postal_code)
#
# # opening-closing time
# opening_closing = munch_loc_open_tidy.split("| ", 1)[1].split(" átvehető")[0]
# opening, closing = opening_closing.split("-")
# print(opening_closing)
# print(opening)
# print(closing)

# time.sleep(3)
# try:
#     driver.find_elements_by_xpath('.//i[@class = "eicon-close"]')[0].click()
# except IndexError:
#     print('Window not yet available')
# popup_subscribe = []
# popup_subscribe = driver.find_elements_by_xpath('.//div[@class = "dialog-close-button dialog-lightbox-close-button"]')
# ActionChains(driver).click(popup_subscribe).perform()
# doesn't popup immediately


# turning pages

# https://munch.hu/terkep/page/2/
# driver.get('https://munch.hu/terkep/page/2/')
# print(driver.title)
# time.sleep(3)
# driver.get('https://munch.hu/terkep/page/3/')
# print(driver.title)
# Az oldal nem található - Munch.hu
# ha erre futunk akkor nincs több oldal



# driver.quit()  # close whole window


ender = datetime.now()

dur_whole = ender-starter

print('Process finished\nDuration: {dur}'.format(dur=dur_whole))
