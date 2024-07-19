import requests
from flask import Flask, jsonify
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
API_KEY = os.getenv('API-KEY')


# League ID's
euroLeageId = 4
copaAmericaId = 10
mlsLeageId = 253

@app.route('/euro-games')
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



@app.route('/mls-games')
def get_mls_games():
    # Shared api keys
    
    apiKeys = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': API_KEY
    }

    endpoint = f"https://v3.football.api-sports.io/fixtures/?league={mlsLeageId}&season=2024&next=3"
    response = requests.get(endpoint, headers=apiKeys)

    data = response.json()
    #print(data);

    
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=5000)