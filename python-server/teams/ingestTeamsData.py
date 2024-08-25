import requests
import json
from dotenv import load_dotenv
import os
from pymongo import MongoClient


load_dotenv()


MONGO_USERNAME = os.getenv('MONGO-USERNAME')
MONGO_PASSWORD = os.getenv('MONGO-PASSWORD')
MONGO_CLUSTER = os.getenv('MONGO-CLUSTER')
API_KEY = os.getenv('API-KEY')



mongo_uri = f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_CLUSTER}/soccernow?retryWrites=true&w=majority"
try:
    client = MongoClient(mongo_uri)
    db = client['soccernow']
    teams_collection = db['teams']
    print("Successfully connected to MongoDB")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")



def get_league_teams(league_id):
    # Shared api keys
    apiKeys = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': API_KEY
    }

    endpoint = f"https://v3.football.api-sports.io/teams/?league={league_id}&season=2024"
    response = requests.get(endpoint, headers=apiKeys)
    if response.status_code == 200:
        data = response.json()

        teams = [];

        for item in data.get('response', []):
            team_info = item.get('team', {})
            team_id = team_info.get('id')
            team_name = team_info.get('name')
            team_logo = team_info.get('logo')

            if team_id and team_name:
                teams.append({
                    'team_id': team_id,
                    'team_name': team_name,
                    'league_id': league_id,
                    'team_logo': team_logo
                })
        print(teams)
        print("Extracted Team data:")

        return teams
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
    

def get_team_squads(team_id):
    # Shared api keys
    apiKeys = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': API_KEY
    }

    endpoint = f"https://v3.football.api-sports.io/players/squads?team={team_id}"
    response = requests.get(endpoint, headers=apiKeys)
    if response.status_code == 200:
        data = response.json()

        squad = [];
        team_info = None

        for item in data.get('response', []):
            if not team_info:
                team_info = item.get('team', {})
                team_name = team_info.get('name')
                team_logo = team_info.get('logo')

            squad_list = item.get('players', [])
            for player in squad_list:
                player_id = player.get('id')
                player_name = player.get('name')
                player_number = player.get('number')
                player_position = player.get('position')

                if player_id and player_name:
                    squad.append({
                        'id': player_id,
                        'name': player_name,
                        'number': player_number,
                        'position': player_position
                    })
        return {
            'team_id': team_id,
            'team_name': team_name,
            'team_logo' : team_logo,
            'squad': squad
        }
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

def store_leage_teams(team_id):
    #call the get_mls_team_squads function
    team_data = get_league_teams(team_id)

    if team_data:
        for team in team_data:
            team_info = {
                'team_id': team['team_id'],
                'team_name': team['team_name'],
                'league_id': team['league_id'],
                'team_logo': team['team_logo']
            }

            result = teams_collection.update_one(
                {'team_id': team['team_id']},
                {'$set': team_info},
                upsert=True
            )

            if result.upserted_id:
                print(f"Inserted new document with id {result.upserted_id}")
            else:
                print("Updated existing document")
    else:
        print("No Squad data found")



def store_team_squads(team_id):
    #call the get_mls_team_squads function
    team_data = get_team_squads(team_id)
 
    if team_data:
        # Insert the team info into DB
        team_info = {
            'team_id': team_data['team_id'],
            'team_name': team_data['team_name'],
            'team_logo': team_data['team_logo'],
            'squad': team_data['squad']
        }

        result = teams_collection.update_one(
            {'team_id': team_id},
            {'$set': team_info},
            upsert=True
        )

        if result.upserted_id:
            print(f"Inserted new document with id {result.upserted_id}")
        else:
            print("Updated existing document")
    else:
        print("No Squad data found")


#league_teams = get_league_teams(255)

#stored_league_teams = store_leage_teams(39)

team_squads = store_team_squads(3996)
print (team_squads)


