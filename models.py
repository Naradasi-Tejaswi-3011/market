from datetime import datetime
from bson.objectid import ObjectId

class User:
    """User model for authentication and profile"""
    def __init__(self, email, password_hash, created_at=None):
        self.email = email
        self.password_hash = password_hash
        self.created_at = created_at or datetime.utcnow()
    
    def to_dict(self):
        return {
            'email': self.email,
            'password_hash': self.password_hash,
            'created_at': self.created_at
        }


class Campaign:
    """Campaign AI output model"""
    def __init__(self, user_id, product, audience, platform, industry, 
                 ai_output, created_at=None):
        self.user_id = user_id
        self.product = product
        self.audience = audience
        self.platform = platform
        self.industry = industry
        self.ai_output = ai_output  # JSON with campaign details
        self.created_at = created_at or datetime.utcnow()
    
    def to_dict(self):
        return {
            'user_id': self.user_id,
            'product': self.product,
            'audience': self.audience,
            'platform': self.platform,
            'industry': self.industry,
            'ai_output': self.ai_output,
            'created_at': self.created_at
        }


class Pitch:
    """Sales pitch AI output model"""
    def __init__(self, user_id, product, description, persona, industry, customer_type,
                 budget_preference, ai_output, created_at=None):
        self.user_id = user_id
        self.product = product
        self.description = description
        self.persona = persona
        self.industry = industry
        self.customer_type = customer_type
        self.budget_preference = budget_preference
        self.ai_output = ai_output  # JSON with pitch details
        self.created_at = created_at or datetime.utcnow()
    
    def to_dict(self):
        return {
            'user_id': self.user_id,
            'product': self.product,
            'description': self.description,
            'persona': self.persona,
            'industry': self.industry,
            'customer_type': self.customer_type,
            'budget_preference': self.budget_preference,
            'ai_output': self.ai_output,
            'created_at': self.created_at
        }


class Lead:
    """Lead scoring AI output model"""
    def __init__(self, user_id, budget, business_need, urgency, authority,
                 industry, ai_output, created_at=None):
        self.user_id = user_id
        self.budget = budget
        self.business_need = business_need
        self.urgency = urgency
        self.authority = authority
        self.industry = industry
        self.ai_output = ai_output  # JSON with lead scoring details
        self.created_at = created_at or datetime.utcnow()
    
    def to_dict(self):
        return {
            'user_id': self.user_id,
            'budget': self.budget,
            'business_need': self.business_need,
            'urgency': self.urgency,
            'authority': self.authority,
            'industry': self.industry,
            'ai_output': self.ai_output,
            'created_at': self.created_at
        }


class Feedback:
    """User feedback model for AI generations"""
    def __init__(self, user_id, item_id, item_type, rating, reasons=None, details=None, created_at=None):
        self.user_id = user_id
        self.item_id = item_id  # ID of the campaign, pitch, or lead
        self.item_type = item_type  # 'campaign', 'pitch', or 'lead'
        self.rating = rating  # 1 for thumbs up, -1 for thumbs down
        self.reasons = reasons or [] # List of reasons for negative feedback
        self.details = details # Optional detailed feedback
        self.created_at = created_at or datetime.utcnow()
    
    def to_dict(self):
        return {
            'user_id': self.user_id,
            'item_id': self.item_id,
            'item_type': self.item_type,
            'rating': self.rating,
            'reasons': self.reasons,
            'details': self.details,
            'created_at': self.created_at
        }


class ActivityLog:
    """Activity tracking model"""
    def __init__(self, user_id, action, details, created_at=None):
        self.user_id = user_id
        self.action = action  # 'campaign_created', 'pitch_created', 'lead_scored', 'social_post_created'
        self.details = details
        self.created_at = created_at or datetime.utcnow()
    
    def to_dict(self):
        return {
            'user_id': self.user_id,
            'action': self.action,
            'details': self.details,
            'created_at': self.created_at
        }


class SocialPost:
    """Post creation AI output model"""
    def __init__(self, user_id, product, dept, description, contact, others, 
                 ai_output, created_at=None):
        self.user_id = user_id
        self.product = product
        self.dept = dept
        self.description = description
        self.contact = contact
        self.others = others
        self.ai_output = ai_output  # JSON with captions and image_url
        self.created_at = created_at or datetime.utcnow()
    
    def to_dict(self):
        return {
            'user_id': self.user_id,
            'product': self.product,
            'dept': self.dept,
            'description': self.description,
            'contact': self.contact,
            'others': self.others,
            'ai_output': self.ai_output,
            'created_at': self.created_at
        }
