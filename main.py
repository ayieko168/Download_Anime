from selenium import webdriver
from bs4 import BeautifulSoup
import os

selected_url = "http://justdubs.org/watch-one-punch-man-season-2-english-dubbed"

options = webdriver.ChromeOptions() 
options.add_argument("user-data-dir=C:\\Users\\ayieko\\AppData\\Local\\Google\\Chrome\\User Data") #Path to your chrome profile
browser = webdriver.Chrome(executable_path="C:\\webdrivers\\chromedriver.exe", chrome_options=options)

browser.get(selected_url)

page_html = browser.page_source
page_title = browser.title

browser.quit()

# with open("source.html", "r") as htmlFo:
#     page_html = htmlFo.read()

# get list of epsodes and their url links
soup = BeautifulSoup(page_html, "html.parser")

list_element = soup.find("div", {"class": "col-xs-12 col-sm-8"})
episodes_elements = list_element.findAll("a", {"class": "list-group-item"})

for episode_elem in episodes_elements:

    episode_page_link = episode_elem.get("href")
    episode_title = episode_elem.findAll("div")[1].text

    # visit episode url
    browser = webdriver.Chrome(executable_path="C:\\webdrivers\\chromedriver.exe", chrome_options=options)
    browser.get(episode_page_link)

    episode_page_html = browser.page_source
    episode_page_title = browser.title

    download_button = browser.find_element_by_xpath("Download")
    



    print("download button elemenut =  ", download_button)





    break





































