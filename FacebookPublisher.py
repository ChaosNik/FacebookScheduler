import os
import time
import datetime
import pyautogui
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from random import randint
date = datetime.datetime.now()

test = False
username = ***
password = ***
post = "#souvenirs #woodworking #artworks #gifts #painting #suveniri #drvodelja #umjetnost #pokloni #darovi #oslikavanje"
pictures = "D:\Moje -- Programi\IGZen\Pictures"
number = 10
date = datetime.datetime(2020, 7, 1)
hours = "13"
minutes = "11"

path, dirs, files = next(os.walk(pictures))
pictureCount = len(files)

firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
browser = webdriver.Firefox(firefox_profile=firefox_profile);
browser.get("https://www.facebook.com/login/?next=%2Fcreatorstudio%2F%3Freference%3Dvisit_from_seo")
'''
clickPlace = browser.find_element_by_css_selector(""); #
clickPlace.click();
'''
clickPlace = browser.find_element_by_css_selector("#email") #username
clickPlace.send_keys(username)
clickPlace = browser.find_element_by_css_selector("#pass") #password
clickPlace.send_keys(password)
clickPlace = browser.find_element_by_css_selector("#loginbutton") #login
clickPlace.click();
clickPlace = browser.find_element_by_css_selector("#media_manager_chrome_bar_facebook_icon"); #facebook ikonica
clickPlace.click();

clickPlace = browser.find_element_by_css_selector("#mediaManagerPagesSelector"); #heder za odabir naloga
clickPlace.click();
clickPlace = browser.find_element_by_css_selector("a._1ede:nth-child(2)"); #ponisti izbor svega
clickPlace.click();
clickPlace = browser.find_element_by_css_selector("div._7pfi:nth-child(2)"); #izaberi suvenirkarpic
clickPlace.click();
clickPlace = browser.find_element_by_css_selector("._7xej > div:nth-child(2)"); #potvrdi
clickPlace.click();

count = 0
while(count < number):
    photo = pictures + "\(" + str(randint(1, pictureCount)) + ").jpg"
    dateString = (date + datetime.timedelta(days=count)).strftime("%d.%m.%Y")

    #time.sleep(1)
    #pyautogui.click(100, 170)
    #time.sleep(1)
    clickPlace = browser.find_element_by_css_selector("#mediaManagerFacebookComposerLeftNavButton"); #napraviObjavu
    clickPlace.click();

    #clickPlace = browser.find_element_by_css_selector("#js_d > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)"); #create post
    #clickPlace.click();

    time.sleep(1)
    pyautogui.click(140, 220) #create post

    #writing post
    time.sleep(10)
    pyautogui.click(1000, 250)
    pyautogui.typewrite(post)
    time.sleep(4)
    #pyautogui.click(600, 200)
    #time.sleep(1)

    #pyautogui.click(1023, 600) #scroll bar
    #time.sleep(1)
    pyautogui.click(950, 380) #add item
    time.sleep(1)
    pyautogui.click(700, 450) #upload
    time.sleep(1)

    pyautogui.typewrite(photo) #picture location
    time.sleep(1)
    pyautogui.hotkey("enter")
    time.sleep(45)

    pyautogui.click(1315, 700) #arrow down
    time.sleep(1)
    pyautogui.click(1300, 600) #schedule
    time.sleep(1)

    pyautogui.click(550, 530) #date time
    time.sleep(1)
    pyautogui.typewrite(dateString)
    pyautogui.hotkey("tab")
    pyautogui.typewrite(hours)
    pyautogui.hotkey("tab")
    pyautogui.typewrite(minutes)
    time.sleep(2)

    pyautogui.click(850, 710) #schedule
    time.sleep(10)

    if test != True:
        time.sleep(45)

    print(dateString)
    count+=1

#browser.close()