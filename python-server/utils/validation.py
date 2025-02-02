from jsonschema import validate, ValidationError
import os
import json

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
with open(os.path.join(os.path.dirname(__file__),'../ingestion/game-schema.json'), 'r') as schema_file:
    game_schema = json.load(schema_file)

# validate each document against schema

def validate_document(document):
    try:
        validate(instance=document, schema=game_schema)
    except ValidationError as e:
        print(f"Validation Error: {e.message}")
        return False
    return True