from bson.json_util import dumps, loads
from flask import Flask, jsonify, request, Blueprint
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

games_blueprint = Blueprint('games', __name__)

# MongoDB setup
MONGO_USERNAME = os.getenv('MONGO-USERNAME')
MONGO_PASSWORD = os.getenv('MONGO-PASSWORD')
MONGO_CLUSTER = os.getenv('MONGO-CLUSTER')

mongo_uri = f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_CLUSTER}/soccernow?retryWrites=true&w=majority"
client = MongoClient(mongo_uri)
db = client.soccernow

games_collection = db.games

@games_blueprint.route('/', methods=['GET'])
def get_all_games():
    try:
       # Fetch all documents from the 'games' collection
        all_games = list(games_collection.find())
        
        # Convert MongoDB documents to JSON-serializable format
        all_games_json = dumps(all_games)
        
        return all_games_json, 200, {'Content-Type': 'application/json'}

    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'error': 'An error occurred while fetching the games.'}), 500


@games_blueprint.route('/<int:team_id>', methods=['GET'])
def get_games_by_team(team_id):
    try:
        # Query the games collection for games containing the given team_id
        query = {
            '$or': [
                {'fixture_teams.home.id': team_id},
                {'fixture_teams.away.id': team_id}
            ]
        }
        games = list(games_collection.find(query))
        
        # Convert MongoDB documents to JSON-serializable format
        games_json = dumps(games)
        
        return games_json, 200, {'Content-Type': 'application/json'}

    except ValueError:
        # Handle invalid team_id (non-integer) input
        return jsonify({'error': 'Invalid team_id. It must be an integer.'}), 400
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'error': 'An error occurred while fetching the games.'}), 500