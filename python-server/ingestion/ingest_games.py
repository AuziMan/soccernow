
from flask import jsonify
import requests
import os
from dotenv import load_dotenv
import json
from jsonschema import validate, ValidationError
from pymongo import MongoClient


load_dotenv()


API_KEY = os.getenv('API-KEY')
MONGO_USERNAME = os.getenv('MONGO-USERNAME')
MONGO_PASSWORD = os.getenv('MONGO-PASSWORD')
MONGO_CLUSTER = os.getenv('MONGO-CLUSTER')


copaAmericaId = 10
mlsLeageId = 253
ulsLeageId =  255
epl = 39

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
    
def get_game_id(home_team_id, away_team_id):
    try: 
        home_team_id = teams_collection.find_one({'team_id': home_team_id})
        away_team_id = teams_collection.find_one({'team_id': away_team_id})
    
        game_id = f'home_team_id + '-' + away_team_id '
        return game_id

    except ValueError:
        # Handle invalid team_id (non-integer) input
        return jsonify({'error': 'Invalid team_id. It must be an integer.'}), 400
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'error': 'An error occurred while fetching the games.'}), 500
    

def format_api_response(data):

    fixtures = [];

    for item in data.get('response', []):
        fixture_info = item.get('fixture', {})
        fixture_id = fixture_info.get('id')
        fixture_date = fixture_info.get('date')
        fixture_referee = fixture_info.get('referee')

        fixture_venue_info = fixture_info.get('venue', {})
        fixture_venue_name = fixture_venue_info.get('name')
        fixture_venue_city = fixture_venue_info.get('city')

        fixture_status_info = item.get('status', {}) 
        fixture_status = fixture_status_info.get('long')
        fixture_time_elapsed = fixture_status_info.get('elapsed')

        fixture_league_info = item.get('league', {})

        fixture_teams = item.get('teams', []) 
        fixture_goals= item.get('goals', [])
        fixture_score = item.get('score', [])

        # fixture_home_team = fixture_teams.get()

        # game_id = get_game_id()

        fixtures.append ({
            'fixture_id': fixture_id,
            'fixture_date': fixture_date,
            'fixture_referee': fixture_referee,
            'fixture_venue_name': fixture_venue_name,
            'fixture_venue_city': fixture_venue_city,
            'fixture_status': fixture_status,
            'fixture_time_elapsed': fixture_time_elapsed,
            'fixture_league_info': fixture_league_info,
            'fixture_teams': fixture_teams,
            'fixture_goals': fixture_goals,
            'fixture_score': fixture_score
        })

    return fixtures

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
def store_fixture_data(fixture_to_store):
    for fixture_info in fixture_to_store:
        result = games_collection.update_one(
            {'fixture_id': fixture_info['fixture_id']},
            {'$set': fixture_info},
            upsert=True
        )

    if result.upserted_id:
        print(f"Inserted new document with id {result.upserted_id}")
    else:
        print(f"Updated existing document with id {result.upserted_id}")


def get_up_games(fixture_count, legue_id):
    # Shared api keys

    endpoint = f"https://v3.football.api-sports.io/fixtures/?league={legue_id}&season=2024&next={fixture_count}"
    # endpoint = f'http://127.0.0.1:4000/games/past-games'
    response = requests.get(endpoint, headers=apiKeys)

    data = response.json()


    if response.status_code == 200 and data['results'] > 0:

        formatted_fixtures = format_api_response(data)

        fixtures_to_ingest = []

        for fixture in formatted_fixtures:
            if validate_document(fixture):
                # print(type(fixture))
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
    # print(x)
    get_up_games(10, x)

