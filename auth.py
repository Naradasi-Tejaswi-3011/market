import bcrypt
import os
from datetime import timedelta
from functools import wraps
from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from db import get_db
from models import User

def hash_password(password):
    """Hash password using bcrypt"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


def verify_password(password, password_hash):
    """Verify password against hash"""
    return bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8'))


def register_user(email, password):
    """Register new user"""
    db = get_db()
    
    # Check if user exists
    existing_user = db.users.find_one({'email': email})
    if existing_user:
        return {'error': 'User already exists'}, 400
    
    # Hash password and create user
    password_hash = hash_password(password)
    user = User(email, password_hash)
    
    result = db.users.insert_one(user.to_dict())
    
    return {
        'message': 'Registration successful',
        'user_id': str(result.inserted_id),
        'email': email
    }, 201


def login_user(email, password):
    """Authenticate user and return JWT token"""
    db = get_db()
    
    # Find user
    user = db.users.find_one({'email': email})
    if not user:
        return {'error': 'Invalid credentials'}, 401
    
    # Verify password
    if not verify_password(password, user['password_hash']):
        return {'error': 'Invalid credentials'}, 401
    
    # Create JWT token
    access_token = create_access_token(
        identity=str(user['_id']),
        expires_delta=timedelta(days=30)
    )
    
    return {
        'message': 'Login successful',
        'access_token': access_token,
        'user_id': str(user['_id']),
        'email': user['email']
    }, 200


def get_current_user():
    """Get current authenticated user"""
    db = get_db()
    user_id = get_jwt_identity()
    
    from bson.objectid import ObjectId
    user = db.users.find_one({'_id': ObjectId(user_id)})
    
    if not user:
        return None
    
    return {
        'user_id': str(user['_id']),
        'email': user['email']
    }


def require_auth(f):
    """Decorator to require authentication"""
    @wraps(f)
    @jwt_required()
    def decorated_function(*args, **kwargs):
        return f(*args, **kwargs)
    return decorated_function
