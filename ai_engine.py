import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv('GROQ_API_KEY'))
MODEL = os.getenv('GROQ_MODEL', 'llama-3-70b-versatile')

# Industry tone mappings for dynamic adaptation
INDUSTRY_TONES = {
    'SaaS': 'professional, data-driven, growth-focused, technical',
    'Healthcare': 'clinical, compliant, patient-centric, evidence-based',
    'EdTech': 'engaging, learner-centric, outcome-focused, innovative',
    'Retail': 'customer-centric, trend-aware, conversion-focused, practical',
    'FinTech': 'secure, compliant, ROI-focused, sophisticated'
}

def generate_campaign(product_desc, audience, platform, industry):
    """
    Generate marketing campaign using Groq AI with explainability.
    Returns campaign data with AI reasoning.
    """
    
    tone = INDUSTRY_TONES.get(industry, 'professional and engaging')
    
    prompt = f"""You are an expert AI Marketing Strategist specialized in digital campaigns.

Generate a marketing campaign plan for {platform} platform.

INPUT DETAILS:
Product/Service: {product_desc}
Industry: {industry}
Target Audience: {audience}
Platform: {platform}

Return ONLY valid JSON (no markdown, no code blocks) with this exact structure:
{{
  "campaign_ideas": [
    {{"title": "Campaign Idea 1", "description": "2-3 lines describing the campaign idea"}},
    {{"title": "Campaign Idea 2", "description": "2-3 lines describing the campaign idea"}},
    {{"title": "Campaign Idea 3", "description": "2-3 lines describing the campaign idea"}},
    {{"title": "Campaign Idea 4", "description": "2-3 lines describing the campaign idea"}},
    {{"title": "Campaign Idea 5", "description": "2-3 lines describing the campaign idea"}}
  ],
  "cta_suggestions": [
    {{"cta_text": "Call to Action 1", "description": "When and why to use this CTA"}},
    {{"cta_text": "Call to Action 2", "description": "When and why to use this CTA"}},
    {{"cta_text": "Call to Action 3", "description": "When and why to use this CTA"}},
    {{"cta_text": "Call to Action 4", "description": "When and why to use this CTA"}},
    {{"cta_text": "Call to Action 5", "description": "When and why to use this CTA"}}
  ],
  "content_calendar": [
    {{"day": 1, "post_type": "Educational/Promotional/Engagement", "content_idea": "Specific post idea", "best_time": "9 AM"}},
    {{"day": 2, "post_type": "Educational/Promotional/Engagement", "content_idea": "Specific post idea", "best_time": "12 PM"}},
    {{"day": 3, "post_type": "Educational/Promotional/Engagement", "content_idea": "Specific post idea", "best_time": "3 PM"}},
    {{"day": 4, "post_type": "Educational/Promotional/Engagement", "content_idea": "Specific post idea", "best_time": "10 AM"}},
    {{"day": 5, "post_type": "Educational/Promotional/Engagement", "content_idea": "Specific post idea", "best_time": "1 PM"}},
    {{"day": 6, "post_type": "Educational/Promotional/Engagement", "content_idea": "Specific post idea", "best_time": "11 AM"}},
    {{"day": 7, "post_type": "Educational/Promotional/Engagement", "content_idea": "Specific post idea", "best_time": "2 PM"}}
  ],
  "competitor_analysis": {{
    "common_strategies": ["Strategy 1 competitors use", "Strategy 2 competitors use", "Strategy 3 competitors use"],
    "gaps_opportunities": ["Gap 1 you can exploit", "Gap 2 you can exploit", "Gap 3 you can exploit"],
    "differentiation_tactics": ["How to stand out 1", "How to stand out 2", "How to stand out 3"]
  }}
}}

IMPORTANT:
- Campaign ideas specific to {platform}
- CTAs action-oriented
- Hashtags relevant to {industry} and trending on {platform}
- Content calendar with 7 days (can be repeated for 30 days)
- Competitor analysis based on {industry} standards

CRITICAL: Return ONLY the JSON object, nothing else."""

    try:
        message = client.chat.completions.create(
            model=MODEL,
            max_tokens=4000,
            messages=[{"role": "user", "content": prompt}]
        )
        
        response_text = message.choices[0].message.content.strip()
        
        # Remove markdown if present
        if response_text.startswith('```'):
            response_text = response_text.split('```')[1]
            if response_text.startswith('json'):
                response_text = response_text[4:]
        
        ai_data = json.loads(response_text)
        
        return {
            'status': 'success',
            'campaign': ai_data,
            'ai_model': MODEL
        }
    
    except json.JSONDecodeError as e:
        return {
            'status': 'error',
            'error': f'AI response parsing error: {str(e)}',
            'raw_response': response_text if 'response_text' in locals() else None
        }
    except Exception as e:
        return {
            'status': 'error',
            'error': f'AI generation error: {str(e)}'
        }


def generate_pitch(product, persona, industry, company_size, budget_range):
    """
    Generate personalized sales pitch using Groq AI with explainability.
    Returns pitch data with confidence scoring.
    """
    
    tone = INDUSTRY_TONES.get(industry, 'professional')
    
    prompt = f"""You are a master sales strategist. Create a personalized sales pitch with explicit reasoning.

INPUTS:
- Product/Solution: {product}
- Customer Persona: {persona}
- Industry: {industry}
- Company Size: {company_size}
- Budget Range: {budget_range}
- Tone: {tone}

Return ONLY valid JSON (no markdown, no code blocks):
{{
  "elevator_pitch": "Compelling 30-second pitch",
  "value_proposition": "Clear value statement",
  "key_differentiators": [
    "Differentiator 1",
    "Differentiator 2",
    "Differentiator 3"
  ],
  "personalized_cta": "Specific call-to-action for this persona",
  "recommended_next_step": "Specific follow-up action",
  "deal_confidence_score": 75,
  "confidence_breakdown": {{
    "budget_alignment": "How budget matches value",
    "pain_point_fit": "How well solution fits their needs",
    "authority_match": "How well we match their authority/role",
    "timeline_fit": "How well we match their timeline"
  }},
  "reasoning": {{
    "why_this_pitch": "Why this approach works for this persona",
    "industry_nuances": "How industry affects pitch",
    "size_considerations": "How company size affects pitch",
    "objection_handling": "Likely objections and responses"
  }},
  "recommended_next_actions": [
    "Action 1",
    "Action 2",
    "Action 3"
  ]
}}

CRITICAL: Return ONLY the JSON object, nothing else."""

    try:
        message = client.chat.completions.create(
            model=MODEL,
            max_tokens=2000,
            messages=[{"role": "user", "content": prompt}]
        )
        
        response_text = message.choices[0].message.content.strip()
        
        # Remove markdown if present
        if response_text.startswith('```'):
            response_text = response_text.split('```')[1]
            if response_text.startswith('json'):
                response_text = response_text[4:]
        
        ai_data = json.loads(response_text)
        
        return {
            'status': 'success',
            'pitch': ai_data,
            'ai_model': MODEL
        }
    
    except json.JSONDecodeError as e:
        return {
            'status': 'error',
            'error': f'AI response parsing error: {str(e)}',
            'raw_response': response_text if 'response_text' in locals() else None
        }
    except Exception as e:
        return {
            'status': 'error',
            'error': f'AI generation error: {str(e)}'
        }


def score_lead(budget, business_need, urgency, authority, industry):
    """
    Score and categorize leads using Groq AI with detailed reasoning.
    Returns lead score (0-100) with reasoning.
    """
    
    prompt = f"""You are a lead scoring expert. Analyze this lead and provide a comprehensive score with reasoning.

LEAD PROFILE:
- Budget: {budget}
- Business Need: {business_need}
- Urgency: {urgency}
- Authority: {authority}
- Industry: {industry}

Return ONLY valid JSON (no markdown, no code blocks):
{{
  "lead_score": 85,
  "lead_category": "Hot",
  "conversion_probability": 72,
  "detailed_reasoning": {{
    "budget_analysis": "Budget is sufficient for ... because ...",
    "need_alignment": "Strong alignment because ...",
    "urgency_signal": "High urgency indicates ...",
    "authority_assessment": "Decision maker status means ...",
    "industry_context": "In {industry}, this indicates ..."
  }},
  "score_breakdown": {{
    "budget_fit": {{
      "score": 90,
      "reasoning": "Budget sufficient"
    }},
    "need_clarity": {{
      "score": 85,
      "reasoning": "Clear business need"
    }},
    "urgency_level": {{
      "score": 80,
      "reasoning": "High urgency signals readiness"
    }},
    "authority_level": {{
      "score": 95,
      "reasoning": "Direct decision maker"
    }},
    "industry_fit": {{
      "score": 75,
      "reasoning": "Good fit for {industry} vertical"
    }}
  }},
  "priority_recommendation": "Contact within 24 hours",
  "next_actions": [
    "Action 1",
    "Action 2",
    "Action 3"
  ],
  "risk_factors": [
    "Potential risk 1",
    "Potential risk 2"
  ]
}}

CRITICAL: Return ONLY the JSON object, nothing else."""

    try:
        message = client.chat.completions.create(
            model=MODEL,
            max_tokens=2000,
            messages=[{"role": "user", "content": prompt}]
        )
        
        response_text = message.choices[0].message.content.strip()
        
        # Remove markdown if present
        if response_text.startswith('```'):
            response_text = response_text.split('```')[1]
            if response_text.startswith('json'):
                response_text = response_text[4:]
        
        ai_data = json.loads(response_text)
        
        return {
            'status': 'success',
            'lead_score': ai_data,
            'ai_model': MODEL
        }
    
    except json.JSONDecodeError as e:
        return {
            'status': 'error',
            'error': f'AI response parsing error: {str(e)}',
            'raw_response': response_text if 'response_text' in locals() else None
        }
    except Exception as e:
        return {
            'status': 'error',
            'error': f'AI generation error: {str(e)}'
        }
