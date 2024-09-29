from flask import Flask, jsonify, Blueprint
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

teams_blueprint = Blueprint('teams', __name__)
league_blueprint = Blueprint('leagues', __name__)

# MongoDB setup
MONGO_USERNAME = os.getenv('MONGO-USERNAME')
MONGO_PASSWORD = os.getenv('MONGO-PASSWORD')
MONGO_CLUSTER = os.getenv('MONGO-CLUSTER')

mongo_uri = f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_CLUSTER}/soccernow?retryWrites=true&w=majority"
client = MongoClient(mongo_uri)
db = client.soccernow

teams_collection = db.teams

@teams_blueprint.route('/teams', methods=['GET'])
def get_all_games():
    teams = teams_collection.find()
    team_list = []
    for team in teams:
        team_list.append({
            'team_id': team.get('team_id'),
            'team_name': team.get('team_name'),
            'team_logo': team.get('team_logo'),
            'team_squad': team.get('squad'),

        })
    return jsonify(team_list)


@teams_blueprint.route('/<int:team_id>', methods=['GET'])
def get_team_by_id(team_id):
    print(f'Searched for team_id:{team_id}')
    team = teams_collection.find_one({'team_id': team_id})
    if team:
        return jsonify({
            'team_id': team.get('team_id'),
            'team_name': team.get('team_name'),
            'team_logo': team.get('team_logo'),
            'team_squad': team.get('squad')
        })
    else:
        return jsonify({'error': 'Team not found'}), 404
    

@league_blueprint.route('/<int:league_id>', methods=['GET'])
def get_league_id(league_id):
    print(f'Searched for league_id:{league_id}')
    teams = teams_collection.find({'league_id': league_id})

    if teams:
        result = []
        for team in teams:
            result.append ({
                'league_id': team.get('league_id'),
                'team_id': team.get('team_id'),
                'team_name': team.get('team_name'),
                'team_logo': team.get('team_logo'),
                'team_squad': team.get('squad')
            })
        return jsonify(result)
    else:
        return jsonify({'error': 'League not found'}), 404



@league_blueprint.route('/list', methods=['GET'])
def get_league_list():
    league_ids = teams_collection.distinct('league_id')
    
    if league_ids:
        leagues = []
        for league_id in league_ids:
            league = teams_collection.find_one({'league_id': league_id})
            if league:
                leagues.append(league)
        
        return jsonify(leagues)
    else:
        return jsonify({'error': 'League not found'}), 404
    