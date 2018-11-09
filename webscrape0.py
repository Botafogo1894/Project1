import json
import requests

url = "https://fantasy.premierleague.com/drf/bootstrap-static"

def get_json_data(url):
    response = requests.get(url)
    jobs = response.json()
    return jobs

https://fantasy.premierleague.com/drf/bootstrap-static
