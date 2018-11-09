import json
import requests
from models import *


url = "https://fantasy.premierleague.com/drf/bootstrap-static"

def get_json_data(url):
    response = requests.get(url)
    jobs = response.json()
    return jobs

#filter out players with less than 330
all_players = get_json_data(url)['elements']
all_teams = get_json_data(url)['teams']
positions = get_json_data(url)['element_types']

main_players = list(filter(lambda player: player['minutes'] > 330, all_players))

def attach_team_and_position(main_players, all_teams, positons):
    players = main_players.copy()
    for team in all_teams:
        for player in players:
            if team['code'] == player['team_code']:
                player['team_name'] = team['name']
    for position in positions:
        for player in players:
            if position['id'] == player['element_type']:
                player['position'] = position['singular_name']
    for player in players:
        if player['status'] == "a":
            player['status'] = "available"
        elif player['status'] == "d":
            player['status'] = "doubtful"
        elif player['status'] == "i":
            player['status'] = "injured"
        elif player['status'] == "s":
            player['status'] = "suspended"
    return players

player_positions_teams = attach_team_and_position(main_players, all_teams, positions)

def final_list(player_positions_teams):
    players = player_positions_teams.copy()
    for player in players:
        player['team_code'] = player['team_code']
        player['team_name'] = player['team_name']
        player['name'] = player['first_name'] + " " + player['second_name']
        player['status'] = player['status']
        player['position'] = player['position']
        player['cost'] = (player['now_cost'])/10
        player['total_points'] = player['total_points']
        player['roi'] = round((player['total_points'] / player['now_cost'])*10), 2)
        bonus = Column(Integer)
        red_cards = Column(Integer)
        minutes = Column(Integer)
        transfers_out = Column(Integer)
        transfers_in = Column(Integer)


class DataBaseBuilder:

# class DataBaseBuilder:
#
#     def __init__(self):
#         self.country = country
#         self.region = region
#
#     def run(self):
#         es = EventScraper()
#         events = es.find_events(self.country, self.region)
#         global_event_list = []
#         unique_artists = []
#         unique_venues =[]
#         for event in events:
#             event_info = EventInfo(event)
#             artist_list = [Artist(name=artist) for artist in event_info.get_artist()]
#             if not global_event_list:
#                 global_event_list += artist_list
#             else:
#                 unique_artists += list(map(lambda item: item.name, artist_list))
#                 unique_artists = list(set(unique_artists))
#             for artist in artist_list:
#                 if artist.name in unique_artists
#                     unique_object = list(filter(lambda item: item.name == name]], global_event_list))
#                     pdb.set_trace()
#                     artist_list.remove(artist)
#                     global_event_list += artist_list
#                     artist_list.append(unique_object[0])
#                 else:
#                     global_event_list += artist_list
#             current_venue = Venue(name=event_info.get_event_venue())
#             for item in global_event_list:
#                 if item.name == current_venue.name:
#                     curren_venue = item
#                 else:
#                     global_event_list.append(current_venue)
#             event_name = Event(name=event_info.get_event_name(), venue=current_venue, artists=artist_list)
#             global_event_list.append(event_name)
#         return global_event_list
#
#
# class EventInfo:
#     def __init__(self, event):
#         self.html = event
#
#     def get_event_name(self):
#         info = self.html.find("h1", {'class': "event-title"}).text
#         info_tup = info.partition(' at ')
#         self.name = info_tup[0]
#         return self.name
#
#     def get_event_venue(self):
#             info = self.html.find("h1", {'class': "event-title"}).text
#             info_tup = info.partition(' at ')
#             self.venue = info_tup[2]
#             return self.venue
#
#     def get_artist(self):
#         try:
#             return self.html.find('div', {'class':'grey event-lineup'}).text.split(',')
#         except:
#             return ['TBA']
#
# class EventScraper:
#     def get_soup(self, url):
#         r = requests.get(url)
#         c = r.content
#         return BeautifulSoup(c, 'html.parser')
#
#     def find_events(self, country = '', region=''):
#         base = 'https://www.residentadvisor.net'
#         url = base + '/events/' + country+ '/' + region
#         soup = self.get_soup(url)
#     #     events = soup.find_all('h1', {'class':'event-title'})
#         events = soup.find_all('div', {'class':'bbox'})
#         events = events[2:] #first 2 are empty
#         self.events = events
#         return self.events
#
#
# engine = create_engine('sqlite:///events.db')
# Base.metadata.create_all(engine)
