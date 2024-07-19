import pprint
import requests

#endpoint = "https://v3.football.api-sports.io/fixtures/?league=4&season=2024&live=all""""  """
endpoint = "https://v3.football.api-sports.io/fixtures?id=1151043"

apikeys = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "440982861822176e08d197484dde1917"
    }

response = requests.request("GET", endpoint, headers=apikeys)


#pprint(response.text)
livematch = response.json()
#print(livematch)

#print(f"{livematch['league:name']}")
#matchresponse = [k for k in livematch["response"]]
#
league_data = livematch['response'][0]['league'] 
#
team_data = livematch['response'][0]['teams']
fixture_info = livematch['response'][0]['fixture']
goal_info = livematch['response'][0]['goals']
home_info = team_data['home'] 
away_info = team_data['away']
goal_home = goal_info['home']
goal_away = goal_info['away']
print("League - ", league_data['name'])
print("Home Team - ", home_info['name'], " ", goal_home)
print("Away Team - ", away_info['name'], " ", goal_away)