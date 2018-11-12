# api.football-data.org/v2/competitions/PL/standings
import http.client
import requests
import json

url1 = 'api.football-data.org'

def get_table(url1):
    connection = http.client.HTTPConnection(url1)
    headers = { 'X-Auth-Token': '2a9a431414744c4a87048d64b726442f' }
    connection.request('GET', '/v2/competitions/PL/standings', None, headers )
    response = json.loads(connection.getresponse().read().decode())
    return response

def final_teams_list(url1):
    return get_table(url1)['standings'][0]['table']

test = final_teams_list(url1)














# class PL_table:
#     connection = http.client.HTTPConnection('api.football-data.org')
#     headers = { 'X-Auth-Token': '2a9a431414744c4a87048d64b726442f' }
#     connection.request('GET', '/v2/competitions/PL/standings', None, headers )
#     response = json.loads(connection.getresponse().read().decode())
# table = BeautifulSoup(response)
    # return response
# PL/standings
# /v2/competitions/{id}/standings
#
# class CraigsListScraper:
#     def webpage_html(self, url = 'https://newyork.craigslist.org/search/brk/aap'):
#         craigslist_request = requests.get(url)
#         self.craigslist_html = craigslist_request.text
#         return self.craigslist_html
#
#     def listings_html(self, craigslist_html = None):
#         craigslist_html = craigslist_html or self.craigslist_html
#         craigslist_soup = BeautifulSoup(craigslist_html)
#         listings =  craigslist_soup.findAll('li', {'class':"result-row"})
#         self.listings = listings
#         return self.listings
