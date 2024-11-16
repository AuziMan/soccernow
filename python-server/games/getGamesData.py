from bson.json_util import dumps, loads
from flask import Flask, jsonify, request, Blueprint
from pymongo import MongoClient
import os
from datetime import datetime, date, time, timedelta
from dotenv import load_dotenv
import pytz
from common.common import user_time_zone
from common.db import start_db_connection

load_dotenv()

games_blueprint = Blueprint('games', __name__)

#  create mongo db connection
games_collection = start_db_connection()

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


@games_blueprint.route('/past-games', methods=['GET'])
def get_past_games():
    try:

        #set current Dates
        current_date = datetime.now(pytz.utc) + timedelta(days=1) - timedelta(days=1)
        three_days_behind = current_date - timedelta(days=7)

        #function to format dates to match stored format
        def formatDateTimes(inputDate):
            return inputDate.isoformat()

        current_date_str = formatDateTimes(current_date)
        three_days_behind_str = formatDateTimes(three_days_behind)


        print(current_date_str)
        print(three_days_behind_str)
        #Query to mongo
        query = {
            'fixture_date':{
                '$gte': three_days_behind_str,
                '$lte': current_date_str
           }
        }

        results = list(games_collection.find(query))

        past_games = dumps(results)

        return past_games, 200, {'Content-Type': 'application/json'}
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'error': 'An error occurred while fetching the games.'}), 500


# Get Upcoming games from DB based on date. All games returned will be 1+ days ahead of the current day.
@games_blueprint.route('/upcoming-games', methods=['GET'])
def get_upcoming_games():
    try:

        #set current Dates
        current_date = datetime.now(pytz.utc) + timedelta(days=1)
        two_weeks_ahead = current_date + timedelta(weeks=2)

        #function to format dates to match stored format
        def formatDateTimes(inputDate):
            return inputDate.isoformat()

        current_date_str = formatDateTimes(current_date)
        two_weeks_ahead_str = formatDateTimes(two_weeks_ahead)

        #Query to mongo
        query = {
            'fixture_date':{
                '$gt': current_date_str,
                '$lt': two_weeks_ahead_str
           }
        }

       # Fetch all docusments from the 'games' collection
        results = list(games_collection.find(query))

        # for doc in results:
        #     print(doc)
        # Convert MongoDB documents to JSON-serializable format
        upcoming_games = dumps(results)

        return upcoming_games, 200, {'Content-Type': 'application/json'}
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'error': 'An error occurred while fetching the games.'}), 500



@games_blueprint.route('/games-today', methods=['GET'])
def get_games_today():
    try:

        #set Todays Date
        today_date = datetime.combine(date.today(), time.min)
        today_date_iso = today_date.isoformat()        

        end_of_today = today_date + timedelta(days=1)
        end_of_today_iso = end_of_today.isoformat()

        #Query to mongo
        query = {
            'fixture_date':{
                '$gte': today_date_iso,
                '$lt': end_of_today_iso
           }
        }

        results = list(games_collection.find(query))

        games_today = dumps(results)

        return games_today, 200, {'Content-Type': 'application/json'}
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'error': 'An error occurred while fetching the games.'}), 500