import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def start_db_connection():  

    MONGO_USERNAME = os.getenv('MONGO-USERNAME')
    MONGO_PASSWORD = os.getenv('MONGO-PASSWORD')
    MONGO_CLUSTER = os.getenv('MONGO-CLUSTER')

      # Connection string
    mongo_uri = f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_CLUSTER}/soccernow?retryWrites=true&w=majority"
    
    # Initialize the MongoDB client and the database
    client = MongoClient(mongo_uri)
    db = client['soccernow']
    
    # Return the collection you need
    games_collection = db['games']
    
    return games_collection



