from flask import Blueprint, jsonify, request
from datetime import datetime, timedelta
import pytz
from bson.json_util import dumps

time_zone_blueprint = Blueprint('time_zone', __name__)

# Global variable to store user's time zone
user_time_zone = 'UTC'  # Set default value to 'UTC'

@time_zone_blueprint.route('/set-time-zone', methods=['POST'])
def set_time_zone():
    global user_time_zone
    try:
        data = request.get_json()
        user_time_zone = data.get('timeZone', 'UTC')  # Ensure default is 'UTC'
        return jsonify({'status': 'Time zone set'}), 200
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'error': 'An error occurred while setting the time zone.'}), 500
