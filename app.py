import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from dotenv import load_dotenv
from bson.objectid import ObjectId

import auth
import db
from ai_engine import generate_campaign, generate_pitch, score_lead
from utils import (
    save_campaign_to_db, save_pitch_to_db, save_lead_to_db,
    get_user_campaigns, get_user_pitches, get_user_leads,
    get_campaign_by_id, get_pitch_by_id, get_lead_by_id,
    get_user_activity
)

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'jwt-secret-key')

CORS(app)
jwt = JWTManager(app)

# Initialize database
db.init_db()


# ============= AUTHENTICATION ROUTES =============

@app.route('/api/auth/register', methods=['POST'])
def register():
    """User registration endpoint"""
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    if not email or not password:
        return jsonify({'error': 'Email and password required'}), 400
    
    result, status = auth.register_user(email, password)
    return jsonify(result), status


@app.route('/api/auth/login', methods=['POST'])
def login():
    """User login endpoint"""
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    if not email or not password:
        return jsonify({'error': 'Email and password required'}), 400
    
    result, status = auth.login_user(email, password)
    return jsonify(result), status


@app.route('/api/auth/me', methods=['GET'])
@jwt_required()
def get_user():
    """Get current user endpoint"""
    user = auth.get_current_user()
    if user:
        return jsonify(user), 200
    return jsonify({'error': 'User not found'}), 404


# ============= CAMPAIGN ROUTES =============

@app.route('/api/campaigns/generate', methods=['POST'])
@jwt_required()
def generate_campaign_handler():
    """Generate marketing campaign"""
    user_id = get_jwt_identity()
    data = request.get_json()
    
    product = data.get('product')
    audience = data.get('audience')
    platform = data.get('platform')
    industry = data.get('industry')
    
    if not all([product, audience, platform, industry]):
        return jsonify({'error': 'Missing required fields'}), 400
    
    # Generate campaign using AI
    ai_result = generate_campaign(product, audience, platform, industry)
    
    if ai_result['status'] != 'success':
        return jsonify(ai_result), 500
    
    # Save to database
    campaign_id = save_campaign_to_db(
        ObjectId(user_id),
        product, audience, platform, industry,
        ai_result['campaign']
    )
    
    return jsonify({
        'campaign_id': campaign_id,
        'campaign': ai_result['campaign'],
        'message': 'Campaign generated successfully'
    }), 201


@app.route('/api/campaigns', methods=['GET'])
@jwt_required()
def get_campaigns():
    """Get user's campaigns"""
    user_id = get_jwt_identity()
    campaigns = get_user_campaigns(user_id)
    
    return jsonify({
        'campaigns': campaigns,
        'count': len(campaigns)
    }), 200


@app.route('/api/campaigns/<campaign_id>', methods=['GET'])
@jwt_required()
def get_campaign(campaign_id):
    """Get specific campaign"""
    user_id = get_jwt_identity()
    campaign = get_campaign_by_id(campaign_id)
    
    if not campaign:
        return jsonify({'error': 'Campaign not found'}), 404
    
    if str(campaign['user_id']) != user_id:
        return jsonify({'error': 'Unauthorized'}), 403
    
    return jsonify(campaign), 200


# ============= PITCH ROUTES =============

@app.route('/api/pitches/generate', methods=['POST'])
@jwt_required()
def generate_pitch_handler():
    """Generate sales pitch"""
    user_id = get_jwt_identity()
    data = request.get_json()
    
    product = data.get('product')
    description = data.get('description')
    persona = data.get('persona')
    industry = data.get('industry')
    customer_type = data.get('customer_type')
    budget_preference = data.get('budget_preference')
    language = data.get('language', 'English')
    
    if not all([product, description, persona, industry, customer_type, budget_preference]):
        return jsonify({'error': 'Missing required fields'}), 400
    
    # Generate pitch using AI
    ai_result = generate_pitch(product, description, persona, industry, customer_type, budget_preference, language)
    
    if ai_result['status'] != 'success':
        return jsonify(ai_result), 500
    
    # Save to database
    pitch_id = save_pitch_to_db(
        ObjectId(user_id),
        product, description, persona, industry, customer_type, budget_preference,
        ai_result['pitch']
    )
    
    return jsonify({
        'pitch_id': pitch_id,
        'pitch': ai_result['pitch'],
        'message': 'Pitch generated successfully'
    }), 201


@app.route('/api/pitches', methods=['GET'])
@jwt_required()
def get_pitches():
    """Get user's pitches"""
    user_id = get_jwt_identity()
    pitches = get_user_pitches(user_id)
    
    return jsonify({
        'pitches': pitches,
        'count': len(pitches)
    }), 200


@app.route('/api/pitches/<pitch_id>', methods=['GET'])
@jwt_required()
def get_pitch(pitch_id):
    """Get specific pitch"""
    user_id = get_jwt_identity()
    pitch = get_pitch_by_id(pitch_id)
    
    if not pitch:
        return jsonify({'error': 'Pitch not found'}), 404
    
    if str(pitch['user_id']) != user_id:
        return jsonify({'error': 'Unauthorized'}), 403
    
    return jsonify(pitch), 200


# ============= LEAD SCORING ROUTES =============

@app.route('/api/leads/score', methods=['POST'])
@jwt_required()
def score_lead_handler():
    """Score a lead"""
    user_id = get_jwt_identity()
    data = request.get_json()
    
    budget = data.get('budget')
    business_need = data.get('business_need')
    urgency = data.get('urgency')
    authority = data.get('authority')
    industry = data.get('industry')
    
    if not all([budget, business_need, urgency, authority, industry]):
        return jsonify({'error': 'Missing required fields'}), 400
    
    # Score lead using AI
    ai_result = score_lead(budget, business_need, urgency, authority, industry)
    
    if ai_result['status'] != 'success':
        return jsonify(ai_result), 500
    
    # Save to database
    lead_id = save_lead_to_db(
        ObjectId(user_id),
        budget, business_need, urgency, authority, industry,
        ai_result['lead_score']
    )
    
    return jsonify({
        'lead_id': lead_id,
        'lead_score': ai_result['lead_score'],
        'message': 'Lead scored successfully'
    }), 201


@app.route('/api/leads', methods=['GET'])
@jwt_required()
def get_leads():
    """Get user's scored leads"""
    user_id = get_jwt_identity()
    leads = get_user_leads(user_id)
    
    return jsonify({
        'leads': leads,
        'count': len(leads)
    }), 200


@app.route('/api/leads/<lead_id>', methods=['GET'])
@jwt_required()
def get_lead(lead_id):
    """Get specific lead score"""
    user_id = get_jwt_identity()
    lead = get_lead_by_id(lead_id)
    
    if not lead:
        return jsonify({'error': 'Lead not found'}), 404
    
    if str(lead['user_id']) != user_id:
        return jsonify({'error': 'Unauthorized'}), 403
    
    return jsonify(lead), 200


# ============= ACTIVITY ROUTES =============

@app.route('/api/activity', methods=['GET'])
@jwt_required()
def get_activity():
    """Get user's activity log"""
    user_id = get_jwt_identity()
    activities = get_user_activity(user_id)
    
    return jsonify({
        'activities': activities,
        'count': len(activities)
    }), 200


# ============= STATIC PAGES =============

@app.route('/')
def index():
    """Dashboard page"""
    return render_template('dashboard.html')


@app.route('/login')
def login_page():
    """Login page"""
    return render_template('login.html')


@app.route('/register')
def register_page():
    """Register page"""
    return render_template('register.html')


@app.route('/campaign')
def campaign_page():
    """Campaign generator page"""
    return render_template('campaign.html')


@app.route('/pitch')
def pitch_page():
    """Pitch generator page"""
    return render_template('pitch.html')


@app.route('/lead')
def lead_page():
    """Lead scoring page"""
    return render_template('lead.html')


# ============= ERROR HANDLERS =============

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5001)
