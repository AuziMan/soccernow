import requests
from flask import Flask, jsonify, Blueprint
from dotenv import load_dotenv
import os
import json
from pymongo import MongoClient

load_dotenv()

MONGO_USERNAME = os.getenv('MONGO-USERNAME')
MONGO_PASSWORD = os.getenv('MONGO-PASSWORD')
MONGO_CLUSTER = os.getenv('MONGO-CLUSTER')

mongo_uri = f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_CLUSTER}/soccernow?retryWrites=true&w=majority"
try:
    client = MongoClient(mongo_uri)
    db = client['soccernow']
    games_collection = db['games']
    print("Successfully connected to MongoDB")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")

ingest_blueprint = Blueprint('ingest', __name__)


API_KEY = os.getenv('API-KEY')

# League ID's
euroLeageId = 4
copaAmericaId = 10
mlsLeageId = 253


@ingest_blueprint.route('/euro-games')
def get_euro_games():
    # Shared api keys
    
    apiKeys = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': API_KEY
    }

    endpoint = f"https://v3.football.api-sports.io/fixtures/?league={euroLeageId}&season=2024&next=3"
    response = requests.get(endpoint, headers=apiKeys)

    data = response.json()
    if data['results'] == 0:
        noResponse = {
            "result": 0
        }
        #print(noResponse)
        return (noResponse)
    else:
        return jsonify(data)



@ingest_blueprint.route('/up-mls-games')
def get_up_mls_games():
    # Shared api keys
    
    apiKeys = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': API_KEY
    }

    endpoint = f"https://v3.football.api-sports.io/fixtures/?league={mlsLeageId}&season=2024&next=10"
    response = requests.get(endpoint, headers=apiKeys)
    print(response)
    data = response.json()
    #print(data);
    return jsonify(data)


@ingest_blueprint.route('/prev-mls-games')
def get_prev_mls_games():
    # Shared api keys
    
    apiKeys = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': API_KEY
    }

    endpoint = f"https://v3.football.api-sports.io/fixtures/?league={mlsLeageId}&season=2024&last=5"
    response = requests.get(endpoint, headers=apiKeys)

    data = response.json()
    #print(data);
    return jsonify(data)


@ingest_blueprint.route('/all-live-games')
def get_all_live_games():
    # Shared api keys
    
    apiKeys = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': API_KEY
    }

    endpoint = f"https://v3.football.api-sports.io/fixtures/?&season=2024&live=all"
    response = requests.get(endpoint, headers=apiKeys)

    data = response.json()
    if data['results'] == 0:
        noResponse = {
                "result": 0
        }
        #print(noResponse)
        return (noResponse)
    else:
        return jsonify(data)

@ingest_blueprint.route('/live-mls-games')
def get_live_mls_games():
    # Shared api keys
    
    apiKeys = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': API_KEY
    }

    endpoint = f"https://v3.football.api-sports.io/fixtures/?league=253&season=2024&live=all"
    response = requests.get(endpoint, headers=apiKeys)

    data = response.json()
    if data['results'] == 0:
        noResponse = {
                "result": 0
        }
        #print(noResponse)
        return (noResponse)
    else:
        return jsonify(data)


def get_mls_fixtures(fixture_count):
     
    apiKeys = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': API_KEY
    }

    endpoint = f"https://v3.football.api-sports.io/fixtures/?league=253&season=2024&next={fixture_count}"
    response = requests.get(endpoint, headers=apiKeys)

    if response.status_code == 200:
        data = response.json()

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

        return json.dumps(fixtures, indent=4)
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None
    
def store_fixture_info(fixture_count):

    fixture_data = get_mls_fixtures(fixture_count)

    if fixture_data:
        fixtures = json.loads(fixture_data)

        for fixture_info in fixtures:
            result = games_collection.update_one(
                {'fixture_id': fixture_info['fixture_id']},
                {'$set': fixture_info},
                upsert=True
            )

        print(f"Inserted new documents")
           
    else:
        print("No Squad data found")


# mls_fixtures = store_fixture_info(30)
# print(mls_fixtures)