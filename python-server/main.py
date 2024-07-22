from flask import Flask
from games.ingestGamesData import ingest_blueprint
from games.getGamesData import games_blueprint
from teams.getTeamsData import teams_blueprint

app = Flask(__name__)

# Register blueprints
app.register_blueprint(ingest_blueprint, url_prefix='/ingest')
app.register_blueprint(games_blueprint, url_prefix='/games')
app.register_blueprint(teams_blueprint, url_prefix='/teams')

if __name__ == '__main__':
    app.run(port=5000)  # Start the Flask server on port 5000