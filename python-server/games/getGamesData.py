from flask import Flask, jsonify, request
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# MongoDB setup
MONGO_USERNAME = os.getenv('MONGO-USERNAME')
MONGO_PASSWORD = os.getenv('MONGO-PASSWORD')
MONGO_CLUSTER = os.getenv('MONGO-CLUSTER')

mongo_uri = f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_CLUSTER}/soccernow?retryWrites=true&w=majority"
client = MongoClient(mongo_uri)
db = client.soccernow

games_collection = db.games
teams_collection = db.teams

@app.route('/games', methods=['GET'])
def get_all_games():
    games = games_collection.find()
    game_list = []
    for game in games:
        game_list.append({
            'game_id': game.get('_id'),
            'home_team': game.get('home_team'),
            'away_team': game.get('away_team'),
            'score': game.get('score'),
            'date': game.get('date')
        })
    return jsonify(game_list)

