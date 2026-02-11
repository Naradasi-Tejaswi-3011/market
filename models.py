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
    def __init__(self, user_id, product, persona, industry, company_size,
                 budget_range, ai_output, created_at=None):
        self.user_id = user_id
        self.product = product
        self.persona = persona
        self.industry = industry
        self.company_size = company_size
        self.budget_range = budget_range
        self.ai_output = ai_output  # JSON with pitch details
        self.created_at = created_at or datetime.utcnow()
    
    def to_dict(self):
        return {
            'user_id': self.user_id,
            'product': self.product,
            'persona': self.persona,
            'industry': self.industry,
            'company_size': self.company_size,
            'budget_range': self.budget_range,
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


class ActivityLog:
    """Activity tracking model"""
    def __init__(self, user_id, action, details, created_at=None):
        self.user_id = user_id
        self.action = action  # 'campaign_created', 'pitch_created', 'lead_scored'
        self.details = details
        self.created_at = created_at or datetime.utcnow()
    
    def to_dict(self):
        return {
            'user_id': self.user_id,
            'action': self.action,
            'details': self.details,
            'created_at': self.created_at
        }
