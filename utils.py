from datetime import datetime
from bson.objectid import ObjectId
from db import get_db
from models import ActivityLog


def log_activity(user_id, action, details):
    """Log user activity to database"""
    db = get_db()
    activity = ActivityLog(user_id, action, details)
    db.activity_logs.insert_one(activity.to_dict())


def save_campaign_to_db(user_id, product, audience, platform, industry, ai_output):
    """Save campaign to MongoDB"""
    from models import Campaign
    db = get_db()
    
    campaign = Campaign(user_id, product, audience, platform, industry, ai_output)
    result = db.campaigns.insert_one(campaign.to_dict())
    
    log_activity(user_id, 'campaign_created', {
        'product': product,
        'audience': audience,
        'platform': platform,
        'industry': industry
    })
    
    return str(result.inserted_id)


def save_pitch_to_db(user_id, product, persona, industry, company_size, budget_range, ai_output):
    """Save pitch to MongoDB"""
    from models import Pitch
    db = get_db()
    
    pitch = Pitch(user_id, product, persona, industry, company_size, budget_range, ai_output)
    result = db.pitches.insert_one(pitch.to_dict())
    
    log_activity(user_id, 'pitch_created', {
        'product': product,
        'persona': persona,
        'industry': industry,
        'company_size': company_size
    })
    
    return str(result.inserted_id)


def save_lead_to_db(user_id, budget, business_need, urgency, authority, industry, ai_output):
    """Save lead score to MongoDB"""
    from models import Lead
    db = get_db()
    
    lead = Lead(user_id, budget, business_need, urgency, authority, industry, ai_output)
    result = db.leads.insert_one(lead.to_dict())
    
    log_activity(user_id, 'lead_scored', {
        'budget': budget,
        'business_need': business_need,
        'urgency': urgency,
        'authority': authority,
        'industry': industry,
        'lead_score': ai_output.get('lead_score', 0)
    })
    
    return str(result.inserted_id)


def get_user_campaigns(user_id, limit=10):
    """Get user's campaigns from database"""
    db = get_db()
    campaigns = list(db.campaigns.find(
        {'user_id': ObjectId(user_id)}
    ).sort('created_at', -1).limit(limit))
    
    # Convert ObjectId to string
    for campaign in campaigns:
        campaign['_id'] = str(campaign['_id'])
        campaign['user_id'] = str(campaign['user_id'])
    
    return campaigns


def get_user_pitches(user_id, limit=10):
    """Get user's pitches from database"""
    db = get_db()
    pitches = list(db.pitches.find(
        {'user_id': ObjectId(user_id)}
    ).sort('created_at', -1).limit(limit))
    
    # Convert ObjectId to string
    for pitch in pitches:
        pitch['_id'] = str(pitch['_id'])
        pitch['user_id'] = str(pitch['user_id'])
    
    return pitches


def get_user_leads(user_id, limit=10):
    """Get user's scored leads from database"""
    db = get_db()
    leads = list(db.leads.find(
        {'user_id': ObjectId(user_id)}
    ).sort('created_at', -1).limit(limit))
    
    # Convert ObjectId to string
    for lead in leads:
        lead['_id'] = str(lead['_id'])
        lead['user_id'] = str(lead['user_id'])
    
    return leads


def get_user_activity(user_id, limit=20):
    """Get user's activity log"""
    db = get_db()
    activities = list(db.activity_logs.find(
        {'user_id': ObjectId(user_id)}
    ).sort('created_at', -1).limit(limit))
    
    # Convert ObjectId to string
    for activity in activities:
        activity['_id'] = str(activity['_id'])
        activity['user_id'] = str(activity['user_id'])
    
    return activities


def get_campaign_by_id(campaign_id):
    """Get campaign by ID"""
    db = get_db()
    campaign = db.campaigns.find_one({'_id': ObjectId(campaign_id)})
    
    if campaign:
        campaign['_id'] = str(campaign['_id'])
        campaign['user_id'] = str(campaign['user_id'])
    
    return campaign


def get_pitch_by_id(pitch_id):
    """Get pitch by ID"""
    db = get_db()
    pitch = db.pitches.find_one({'_id': ObjectId(pitch_id)})
    
    if pitch:
        pitch['_id'] = str(pitch['_id'])
        pitch['user_id'] = str(pitch['user_id'])
    
    return pitch


def get_lead_by_id(lead_id):
    """Get lead by ID"""
    db = get_db()
    lead = db.leads.find_one({'_id': ObjectId(lead_id)})
    
    if lead:
        lead['_id'] = str(lead['_id'])
        lead['user_id'] = str(lead['user_id'])
    
    return lead
