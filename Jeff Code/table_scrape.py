from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

url = 'https://www.standard.co.uk/sport/football/epl-table-and-results-201819-premier-league-scores-fixtures-results-golden-boot-standings-gameweek-a3986596.html'
html_page = requests.get(url) #Make a get request to retrieve the page
soup = BeautifulSoup(html_page.content, 'html.parser')

#or

albums = soup.findAll("td", class_= 'rtecenter')
albums = list(albums)

txt_format = [item.text for item in albums]
keys = txt_format[:8]
values = txt_format[8:160]




def table_dict(data):
    pass
