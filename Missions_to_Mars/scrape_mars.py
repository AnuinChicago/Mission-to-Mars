from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import pandas as pd

from splinter import Browser
from bs4 import BeautifulSoup
import time

app = Flask(__name__)

# open chrome browser

def init_browser():
    executable_path = {'executable_path': 'C:/Users/aguha/Downloads/chromedriver_win32/chromedriver.exe'}    
    return Browser('chrome', **executable_path, headless=False)

def scrape():
    browser = init_browser()
    
    # define url
    #Get the URL for NASA Mars News
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    
    # create beautiful soup object 
    html = browser.html
    soup1 = BeautifulSoup(html, 'html.parser')

    #Find the Latest news Title
    article = soup1.find("div", class_='list_text')
    news_title = article.find("div", class_="content_title").text
    

    #Find the Latest news paragraph
    news_p =soup1.body.find("div", class_="article_teaser_body").text
    
    time.sleep(3)

    url2 ='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url2)

    # click on the Full Image button. 
    browser.click_link_by_id('full_image')

    # #click on more info to get the full image
    browser.click_link_by_partial_text('more info')

    # create the soup item
    image_html = browser.html
    soup2 = BeautifulSoup(image_html, 'html.parser')
    
   
    # the large image is within the figure element with class = lede
    result2= soup2.find(class_="lede")

    #the href is within the 'a' element, add the base url part to get the full url to the full size image
    featured_image_url=result2.a
    featured_image_url = 'https://www.jpl.nasa.gov' + featured_image_url['href']
    featured_image_url

    
    # ## Mars Weather

    # open url in browser
    
    time.sleep(3)


    # define url
    url4='https://space-facts.com/mars/'

    #get the tables in the url
    tables = pd.read_html(url4)

    # It returns 3 tables. The first has the data needed, so will convert to a dataframe and clean up naming
    df = tables[0]
    df.columns = ["Description", "Value"]

   #convert the dataframe to a HTML table
    html_table = df.to_html(index=False)
    html_table

    # ## Mars Hemispheres

    # define url and open in browser
    time.sleep(3)
    url5='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url5)

    # #### Cerberus hemisphere

    # click on the link for the Cerberus hemisphere

    browser.click_link_by_partial_text('Cerberus')

    # click on the open button to get to enhanced picture
    browser.click_link_by_partial_text('Open')

    # create the soup item
    hemis_html = browser.html
    soup5 = BeautifulSoup(hemis_html, 'html.parser')

    #Find the Full image link
    results5= soup5.body.find('img',class_ ='wide-image')
    img_url1= 'https://astrogeology.usgs.gov'+ results5['src']

    #Find the Title
    title1= soup5.body.find('h2',class_ ='title').text
    #title1=title1.replace('Enhanced', '')

    # #### Schiaperelli hemisphere

    # define url and open in browser

    time.sleep(3)

    url6='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url6)

    # click on the link for the Cerberus hemisphere
    browser.click_link_by_partial_text('Schiaparelli')

    # click on the open button to get to enhanced picture
    browser.click_link_by_partial_text('Open')

    # create the soup item
    hemis_html = browser.html
    soup6 = BeautifulSoup(hemis_html, 'html.parser')

    #Find the Full image link
    results6= soup6.body.find('img',class_ ='wide-image')
    img_url2= 'https://astrogeology.usgs.gov'+ results6['src']
    
    #Find the Title
    title2= soup6.body.find('h2',class_ ='title').text
    title2=title2.replace('Enhanced', '')

    # #### Syrtis hemisphere

    # define url and open in browser

    time.sleep(3)

    url7='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url7)

    # click on the link for the Cerberus hemisphere

    browser.click_link_by_partial_text('Syrtis')

    # click on the link for the Cerberus hemisphere

    browser.click_link_by_partial_text('Open')

    # create the soup item
    hemis_html = browser.html
    soup7 = BeautifulSoup(hemis_html, 'html.parser')

    #Find the Full image link
    results7= soup7.body.find('img',class_ ='wide-image')
    img_url3= 'https://astrogeology.usgs.gov'+ results7['src']

    title3= soup7.body.find('h2',class_ ='title').text
    title3=title3.replace('Enhanced', '')

    # #### Valles hemisphere

    # define url and open in browser

    time.sleep(3)

    url8='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url8)

    # click on the link for the Valles hemisphere

    browser.click_link_by_partial_text('Valles')

    # click on the link for the Valles hemisphere

    browser.click_link_by_partial_text('Open')

    # create the soup item
    hemis_html = browser.html
    soup8 = BeautifulSoup(hemis_html, 'html.parser')

    #Find the Full image link
    results8= soup8.body.find('img',class_ ='wide-image')
    img_url4= 'https://astrogeology.usgs.gov'+ results8['src']

    #Find the Title
    title4= soup8.body.find('h2',class_ ='title').text
    title4=title4.replace('Enhanced', '')

    #### Define list of dictionaries that include each hemisphere
    hemisphere_image_urls = [
    {"title": title1, "img_url": img_url1},
    {"title": title2, "img_url": img_url2},
    {"title": title3, "img_url": img_url3},
    {"title": title4, "img_url": img_url4},
    ]
    
    mars_dict = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "fact_table": html_table,
        "title1": title1, "img_url1": img_url1,
        "title2": title2, "img_url2": img_url2,
        "title3": title3, "img_url3": img_url3,
        "title4": title4, "img_url4": img_url4
    }

    browser.quit()
    return mars_dict
    