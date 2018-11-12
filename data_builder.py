from models import *
from EPL_table_scrape import *
from player_stats_scrape import *
from sqlalchemy import create_engine
import pdb

def inst_teams():
    teams = final_teams_list(url1)
    empty = []
    for item in teams:
        team = Team(position = item['position'], name = item['team']['name'], logo = item['team']['crestUrl'], games_played = item['playedGames'], W = item['won'], D = item['draw'], L = item['lost'], points = item['points'], GF = item['goalsFor'], GA = item['goalsAgainst'], GD = item['goalDifference'], players = [])
        empty.append(team)
    return empty

def inst_players():
    players = final_players_list(player_positions_teams)
    teams = inst_teams()
    empty = []
    pdb.set_trace()
    for team in teams:
        for item in players:
            if team.name == item['team_name']:
                player = Player(team = team, name = item['name'], position = item['position'], cost = item['cost'], total_points = item['total_points'], roi = item['roi'], bonus = item['bonus'], red_cards = item['red_cards'], minutes = item['minutes'], transfers_out = item['transfers_out'], transfers_in = item['transfers_in'])
                empty.append(player)
    return empty

engine = create_engine('sqlite:///EPL_fantasy.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


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
