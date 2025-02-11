
from datetime import datetime
from flask import jsonify
import requests
import os
from dotenv import load_dotenv
import json
from jsonschema import validate, ValidationError
from pymongo import MongoClient
from bson.json_util import dumps
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.validation import format_api_response

load_dotenv()

API_KEY = os.getenv('API-KEY')
MONGO_USERNAME = os.getenv('MONGO-USERNAME')
MONGO_PASSWORD = os.getenv('MONGO-PASSWORD')
MONGO_CLUSTER = os.getenv('MONGO-CLUSTER')

mongo_uri = f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_CLUSTER}/soccernow?retryWrites=true&w=majority"
try:
    client = MongoClient(mongo_uri)
    db = client['soccernow']
    games_collection = db['games']
    teams_collection = db['teams']
    print("Successfully connected to MongoDB")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")


apiKeys = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': API_KEY
    }

# Function used in each API call.
def return_response(response): 
    if response['results'] == 0:
        noResponse = {
                "result": 0
        }
        #print(noResponse)
        return (noResponse)
    else:
        return response
    
def get_game_id(home_team_id, away_team_id, fixture_date):
    try:

        query = {
            '$or': [
                {'team_id': home_team_id},
                {'team_id': away_team_id}
            ] 
        }

        result = list(teams_collection.find(query))

        home_team_code = None
        away_team_code = None

        for team in result:
            if team['team_id'] == home_team_id:
                home_team_code = team.get('team_code')
            elif team['team_id'] == away_team_id:
                away_team_code = team.get('team_code')

        # Check if both team codes were found
        if home_team_code is None or away_team_code is None:
            raise ValueError("Could not find codes for both teams.")
        
        game_id = f"{home_team_code}-{away_team_code}-{fixture_date}"

        print (game_id)
        
        return game_id
    except ValueError as ve:
        # Handle invalid team_id (non-integer) input
        print(f"Invalid team_id error: {ve}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Open schema file
with open(os.path.join(os.path.dirname(__file__),'game-schema.json'), 'r') as schema_file:
    game_schema = json.load(schema_file)


# validate each document against schema

def validate_document(document):
    try:
        validate(instance=document, schema=game_schema)
    except ValidationError as e:
        print(f"Validation Error: {e.message}")
        return False
    return True


# Store fixtures in mongo
def store_fixture_data(fixtures):
    for fixture in fixtures:
        game_id = fixture.get("game_id")
        fixture.pop("_id", None)
        result = games_collection.update_one(
            {"game_id": game_id},
            {'$set': fixture},
            upsert=True
        )

    if result.upserted_id:
        print(f"Inserted new document with id {result.upserted_id}")
    else:
        print(f"Updated existing document with id {result.upserted_id}")


# def get_up_games(fixture_count, legue_id):
def get_up_games(fixture_count, league_id):
    # Shared api keys
    endpoint = f"https://v3.football.api-sports.io/fixtures/?league={league_id}&season=2024&last={fixture_count}"
    response = requests.get(endpoint, headers=apiKeys)
    data = response.json()
    if response.status_code == 200 and data['results'] > 0:
        formatted_fixtures = format_api_response(data)
        fixtures_to_ingest = []
        for fixture in formatted_fixtures:
            if validate_document(fixture):
                # print(type(fixture))
                fixture_home_id = fixture["fixture_teams"]["home"]["id"]
                fixture_away_id = fixture["fixture_teams"]["away"]["id"]
                fixture_date = fixture["fixture_date"]

                # Parse the string into a datetime object
                dt_object = datetime.fromisoformat(fixture_date)
                formatted_date_str = dt_object.strftime("%Y-%m-%d")


                game_id = get_game_id(fixture_home_id, fixture_away_id, formatted_date_str)

                fixture["game_id"] = game_id

                fixtures_to_ingest.append(fixture)
                print(fixtures_to_ingest)
            else:
                print("Invalid Document")
        
        store_fixture_data(fixtures_to_ingest)

    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None


list_of_leagues = [253, 255, 39]

for x in list_of_leagues:
    print(x)
    get_up_games(10, x)



