from flask import Flask
from flask_cors import CORS

from games.ingestGamesData import ingest_blueprint, store_fixture_info
from games.getGamesData import games_blueprint
from teams.getTeamsData import teams_blueprint
from teams.getTeamsData import league_blueprint
from common.common import time_zone_blueprint


app = Flask(__name__)
CORS(app)

# Register blueprints
app.register_blueprint(ingest_blueprint, url_prefix='/ingest')
app.register_blueprint(games_blueprint, url_prefix='/games')
app.register_blueprint(teams_blueprint, url_prefix='/teams')
app.register_blueprint(league_blueprint, url_prefix='/leagues')
app.register_blueprint(time_zone_blueprint, url_prefix='/time-zone')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)

# lsof -i :5000
# kill -9 <PID>


