import requests
from flask import Flask, jsonify, Blueprint
from dotenv import load_dotenv
import os

load_dotenv()

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
