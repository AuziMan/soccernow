import os
from flask import jsonify
from pymongo import MongoClient



MONGO_USERNAME = os.getenv('MONGO-USERNAME')
MONGO_PASSWORD = os.getenv('MONGO-PASSWORD')
MONGO_CLUSTER = os.getenv('MONGO-CLUSTER')

def create_db_conection():
    mongo_uri = f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_CLUSTER}/soccernow?retryWrites=true&w=majority"
    try:
        client = MongoClient(mongo_uri)
        db = client['soccernow']
        games_collection = db['games']
        teams_collection = db['teams']
        print("Successfully connected to MongoDB")
        return games_collection, teams_collection
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")

# Store fixtures in mongo
def store_fixture_data(fixtures):
    for fixture in fixtures:
        db_connection = create_db_conection()
        game_id = fixture.get("game_id")
        fixture.pop("_id", None)
        result = db_connection.games_collection.update_one(
            {"game_id": game_id},
            {'$set': fixture},
            upsert=True
        )

    if result.upserted_id:
        print(f"Inserted new document with id {result.upserted_id}")
    else:
        print(f"Updated existing document with id {result.upserted_id}")


# Get game_id
def get_game_id(home_team_id, away_team_id, fixture_date):
    try:

        db_connection = create_db_conection()
        query = {
            '$or': [
                {'team_id': home_team_id},
                {'team_id': away_team_id}
            ]
        }

        result = list(db_connection.teams_collection.find(query))

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
    except ValueError:
        # Handle invalid team_id (non-integer) input
        return jsonify({'error': 'Invalid team_id. It must be an integer.'}), 400
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'error': 'An error occurred while fetching the games.'}), 500