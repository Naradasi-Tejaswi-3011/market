import os
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

load_dotenv()

# MongoDB Connection
MONGO_URI = os.getenv('MONGODB_URI')
DB_NAME = os.getenv('MONGODB_DB', 'marketai_suite')

try:
    client = MongoClient(MONGO_URI, server_api=ServerApi('1'))
    db = client[DB_NAME]
    
    # Verify connection
    client.admin.command('ping')
    print("[OK] MongoDB connected successfully")
except Exception as e:
    print(f"[ERROR] MongoDB connection failed: {e}")
    db = None


def init_db():
    """Initialize database collections with indexes"""
    if db is None:
        print("Database not connected")
        return
    
    try:
        # Create collections if they don't exist
        
        # Users collection
        if 'users' not in db.list_collection_names():
            db.create_collection('users')
        db.users.create_index('email', unique=True)
        
        # Campaigns collection
        if 'campaigns' not in db.list_collection_names():
            db.create_collection('campaigns')
        db.campaigns.create_index([('user_id', 1), ('created_at', -1)])
        
        # Pitches collection
        if 'pitches' not in db.list_collection_names():
            db.create_collection('pitches')
        db.pitches.create_index([('user_id', 1), ('created_at', -1)])
        
        # Leads collection
        if 'leads' not in db.list_collection_names():
            db.create_collection('leads')
        db.leads.create_index([('user_id', 1), ('created_at', -1)])
        
        # Activity logs collection
        if 'activity_logs' not in db.list_collection_names():
            db.create_collection('activity_logs')
        db.activity_logs.create_index([('user_id', 1), ('created_at', -1)])
        
        print("[OK] Database collections initialized")
    except Exception as e:
        print(f"[ERROR] Database initialization error: {e}")


def get_db():
    """Get database instance"""
    return db


def close_db():
    """Close database connection"""
    if client:
        client.close()
        print("[OK] MongoDB connection closed")
