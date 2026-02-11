import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# Initialize Groq client safely
try:
    client = Groq(api_key=os.getenv('GROQ_API_KEY'))
    MODEL = os.getenv('GROQ_MODEL', 'llama-3.1-70b-versatile')
    GROQ_AVAILABLE = True
except Exception as e:
    print(f"[WARNING] Groq initialization error: {e}")
    client = None
    MODEL = None
    GROQ_AVAILABLE = False

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
        if not GROQ_AVAILABLE:
            raise Exception("Groq client not available")
            
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
    
    except Exception as e:
        print(f"[FALLBACK] Campaign generation error: {e}")
        return _intelligent_campaign_fallback(product_desc, audience, platform, industry)


def generate_pitch(product, description, persona, industry, customer_type, budget_preference, language='English'):
    """
    Generate personalized sales pitch using Groq AI with explainability.
    Returns pitch data with confidence scoring.
    """
    
    tone = INDUSTRY_TONES.get(industry, 'professional')
    
    prompt = f"""You are a master sales strategist. Create a personalized sales pitch.

INPUTS:
- Product Name: {product}
- Product Description: {description}
- Customer Persona: {persona}
- Industry: {industry}
- Customer Type: {customer_type}
- Budget Preference: {budget_preference}
- Tone: {tone}
- Language: {language}

IMPORTANT: Generate the ENTIRE pitch in {language} language. 
CRITICAL: Use native scripts for the output (e.g., Devanagari for Hindi, Telugu script for Telugu). Do NOT use Romanized script (English letters).

Return ONLY valid JSON (no markdown, no code blocks):
{{
  "elevator_pitch": "Compelling 1-minute+ pitch in {language} (150-180 words)",
  "value_proposition": "Clear value statement in {language}",
  "key_differentiators": [
    "Differentiator 1 in {language}",
    "Differentiator 2 in {language}",
    "Differentiator 3 in {language}"
  ],
  "personalized_cta": "Call-to-action in {language}",
  "deal_confidence_score": 75,
  "confidence_breakdown": {{
    "budget_alignment": "Analysis in {language}",
    "pain_point_fit": "Analysis in {language}",
    "authority_match": "Analysis in {language}",
    "timeline_fit": "Analysis in {language}"
  }},
  "reasoning": {{
    "why_this_pitch": "Reasoning in {language}",
    "industry_nuances": "Analysis in {language}",
    "size_considerations": "Analysis in {language}",
    "objection_handling": "Handling in {language}"
  }},
  "recommended_next_actions": [
    "Action 1 in {language}",
    "Action 2 in {language}",
    "Action 3 in {language}"
  ]
}}

CRITICAL: Return ONLY the JSON object, nothing else."""

    try:
        if not GROQ_AVAILABLE:
            raise Exception("Groq client not available")

        message = client.chat.completions.create(
            model=MODEL,
            max_tokens=3000,
            temperature=0.7,
            messages=[{"role": "user", "content": prompt}]
        )
        
        response_text = message.choices[0].message.content.strip()
        
        # Remove markdown if present
        if response_text.startswith('```'):
            lines = response_text.split('\n')
            response_text = '\n'.join(lines[1:-1]) if len(lines) > 2 else response_text
            if response_text.startswith('json'):
                response_text = response_text[4:].strip()
        
        # Clean up response
        response_text = response_text.strip()
        if response_text.endswith('```'):
            response_text = response_text[:-3].strip()
        
        ai_data = json.loads(response_text)
        
        return {
            'status': 'success',
            'pitch': ai_data,
            'ai_model': MODEL
        }
    
    except Exception as e:
        print(f"[FALLBACK] Pitch generation error: {e}")
        return _intelligent_pitch_fallback(product, description, persona, industry, customer_type, budget_preference, language)


def score_lead(budget, business_need, urgency, authority, industry):
    """
    Score and categorize leads using Groq AI with detailed reasoning.
    Returns lead score (0-100) with reasoning, varying based on BANT factors.
    """
    
    # Enhanced prompt that emphasizes dynamic scoring
    prompt = f"""You are an expert B2B lead scoring analyst. Analyze this specific lead and provide a detailed, BANT-based score.

BANT ANALYSIS CRITERIA:
- B = Budget (capacity for investment)
- A = Authority (decision-making power)
- N = Need (business problem fit)
- T = Timeline (urgency/buying timeline)

SPECIFIC LEAD PROFILE TO ANALYZE:
- Budget: {budget}
- Business Need: {business_need}
- Urgency (Timeline): {urgency}
- Authority Level: {authority}
- Industry: {industry}

Based on this specific lead, return ONLY valid JSON (no markdown):
{{
  "lead_score": <integer 1-100, specifically calculated for this lead>,
  "lead_category": <"Hot" if score 70-100, "Warm" if 40-69, "Cold" if below 40>,
  "conversion_probability": <integer 1-100 based on BANT alignment>,
  "detailed_reasoning": {{
    "budget_analysis": "<specific analysis of this budget amount relative to industry and solution area>",
    "need_alignment": "<how well this business need aligns with available solutions>",
    "urgency_signal": "<what this specific timeline tells us about buying readiness>",
    "authority_assessment": "<capability of this authority level to move deal forward>",
    "industry_context": "<specific dynamics in the {industry} industry>",
    "bant_summary": "<overall BANT alignment assessment>"
  }},
  "score_breakdown": {{
    "budget_fit": {{
      "score": <0-100>,
      "reasoning": "<specific budget analysis>"
    }},
    "need_clarity": {{
      "score": <0-100>,
      "reasoning": "<business need clarity assessment>"
    }},
    "urgency_level": {{
      "score": <0-100>,
      "reasoning": "<timeline readiness assessment>"
    }},
    "authority_level": {{
      "score": <0-100>,
      "reasoning": "<decision-making capability>"
    }},
    "industry_fit": {{
      "score": <0-100>,
      "reasoning": "<industry-specific opportunity assessment>"
    }}
  }},
  "priority_recommendation": "<specific A/B/C tier recommendation with action timeline>",
  "sales_strategy": "<comprehensive sales strategy based on BANT alignment>",
  "risk_level": "<Low, Medium, or High>",
  "next_actions": [
    "<specific tactic 1 for this lead>",
    "<specific tactic 2 for this lead>",
    "<specific tactic 3 for this lead>"
  ],
  "risk_factors": ["<specific risk 1>", "<specific risk 2>"]
}}

IMPORTANT: 
- Generate DIFFERENT scores for different leads
- Base scores specifically on the Budget, Authority, Need, Timeline provided
- Lower scores if timeline is vague or authority is low
- Higher scores if Primary Decision Maker + High urgency + Clear need + Strong budget
- Return ONLY the JSON, nothing else"""

    try:
        if not GROQ_AVAILABLE:
            raise Exception("Groq client not available")
            
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
    
    except Exception as e:
        # Fallback to intelligent mock scoring based on BANT factors
        return _intelligent_lead_score_fallback(budget, business_need, urgency, authority, industry)


def _intelligent_lead_score_fallback(budget, business_need, urgency, authority, industry):
    """
    Fallback scoring when Groq is unavailable. Still generates dynamic scores based on BANT factors.
    """
    # Calculate score components based on inputs
    budget_score = _calculate_budget_score(budget)
    urgency_score = _calculate_urgency_score(urgency)
    authority_score = _calculate_authority_score(authority)
    need_score = _calculate_need_score(business_need)
    industry_score = _calculate_industry_score(industry)
    
    # Weighted BANT calculation
    lead_score = int((budget_score * 0.3 + urgency_score * 0.3 + authority_score * 0.2 + need_score * 0.2))
    conversion_prob = int(lead_score * 0.9)
    
    # Determine category
    if lead_score >= 70:
        category = "Hot"
        priority = "A-Tier"
        timeline = "within 24 hours"
    elif lead_score >= 45:
        category = "Warm"
        priority = "B-Tier"
        timeline = "within 3 days"
    else:
        category = "Cold"
        priority = "C-Tier"
        timeline = "nurture sequence"
    
    return {
        'status': 'success',
        'lead_score': {
            'lead_score': lead_score,
            'lead_category': category,
            'conversion_probability': conversion_prob,
            'detailed_reasoning': {
                'budget_analysis': f"Budget: {budget}. Assessment: {_get_budget_analysis(budget)}",
                'need_alignment': f"Need: {business_need}. Clarity: {_get_need_alignment(business_need)}",
                'urgency_signal': f"Urgency: {urgency}. Readiness: {_get_urgency_analysis(urgency)}",
                'authority_assessment': f"Authority: {authority}. Capability: {_get_authority_analysis(authority)}",
                'industry_context': f"Industry: {industry}. Fit: {_get_industry_analysis(industry)}",
                'bant_summary': f"BANT Alignment: Budget {budget_score}/100, Authority {authority_score}/100, Need {need_score}/100, Timeline {urgency_score}/100"
            },
            'score_breakdown': {
                'budget_fit': {'score': budget_score, 'reasoning': _get_budget_analysis(budget)},
                'need_clarity': {'score': need_score, 'reasoning': _get_need_alignment(business_need)},
                'urgency_level': {'score': urgency_score, 'reasoning': _get_urgency_analysis(urgency)},
                'authority_level': {'score': authority_score, 'reasoning': _get_authority_analysis(authority)},
                'industry_fit': {'score': industry_score, 'reasoning': _get_industry_analysis(industry)}
            },
            'priority_recommendation': f"PRIORITY: {priority} Tier. Contact {timeline}. {'Immediate action recommended.' if category == 'Hot' else 'Strong opportunity.' if category == 'Warm' else 'Monitor and nurture.'}",
            'next_actions': _get_next_actions(category, authority, business_need),
            'risk_factors': _get_risk_factors(budget, authority, urgency, business_need)
        },
        'ai_model': 'Intelligent Fallback (BANT-based)'
    }


def _calculate_budget_score(budget):
    """Score budget from 0-100"""
    budget_lower = budget.lower()
    if 'over $1m' in budget_lower:
        return 100
    elif '$500k - $1m' in budget_lower:
        return 95
    elif '$150k - $500k' in budget_lower:
        return 85
    elif '$50k - $150k' in budget_lower:
        return 70
    elif 'under $50k' in budget_lower:
        return 50
    else:
        return 40  # Unknown


def _calculate_urgency_score(urgency):
    """Score urgency/timeline from 0-100"""
    urgency_lower = urgency.lower()
    if 'immediately' in urgency_lower or 'high' in urgency_lower:
        return 100
    elif '3 months' in urgency_lower or 'medium' in urgency_lower:
        return 80
    elif '6+ months' in urgency_lower or 'low' in urgency_lower:
        return 50
    elif 'exploring' in urgency_lower:
        return 40
    else:
        return 60


def _calculate_authority_score(authority):
    """Score decision-making authority from 0-100"""
    auth_lower = authority.lower()
    if 'primary decision maker' in auth_lower:
        return 100
    elif 'budget approver' in auth_lower:
        return 90
    elif 'technical influencer' in auth_lower or 'influencer' in auth_lower:
        return 70
    elif 'end user' in auth_lower:
        return 50
    else:
        return 60


def _calculate_need_score(business_need):
    """Score business need clarity from 0-100"""
    need_lower = business_need.lower()
    # Score based on specificity
    specificity_words = ['crm', 'marketing', 'sales', 'automation', 'analytics', 'inventory', 'platform', 'system', 'management']
    matched_words = sum(1 for word in specificity_words if word in need_lower)
    score = min(100, 40 + (matched_words * 12))
    return score if len(business_need) > 10 else 30


def _calculate_industry_score(industry):
    """Score industry-specific fit from 0-100"""
    industry_lower = industry.lower()
    industry_scores = {
        'saas': 90,
        'healthcare': 80,
        'fintech': 85,
        'edtech': 75,
        'retail': 70,
        'other': 50
    }
    return industry_scores.get(industry_lower, 50)


def _get_budget_analysis(budget):
    return f"Investment capacity: {budget} indicates {'enterprise-level' if '500k' in budget.lower() or '1m' in budget.lower() else 'mid-market' if '150k' in budget.lower() else 'SMB'} purchasing power."


def _get_need_alignment(need):
    return f"Clear business need identified. Alignment potential: {'High' if len(need) > 30 else 'Medium' if len(need) > 15 else 'Needs clarification'}."


def _get_urgency_analysis(urgency):
    if 'immediately' in urgency.lower() or 'high' in urgency.lower():
        return "Immediate buying window. High procurement readiness."
    elif '3' in urgency.lower():
        return "Medium-term timeline. Reasonable decision cycle."
    else:
        return "Extended timeline. Early-stage opportunity."


def _get_authority_analysis(authority):
    auth_lower = authority.lower()
    if 'primary decision maker' in auth_lower:
        return "Direct decision authority. Fast deal closure likely."
    elif 'budget' in auth_lower:
        return "Strong budget control. Key stakeholder."
    elif 'technical' in auth_lower or 'influencer' in auth_lower:
        return "Influential in process. Secondary approval needed."
    else:
        return "End user perspective. Approval chain required."


def _get_industry_analysis(industry):
    return f"{industry} sector shows strong adoption of solutions. Market-fit confirmed."


def _get_next_actions(category, authority, business_need):
    """Generate context-specific next actions"""
    actions = []
    
    if 'primary decision maker' in authority.lower():
        actions.append("Schedule executive-level demo with decision maker")
    else:
        actions.append("Identify and engage primary decision maker")
    
    actions.append(f"Prepare business case addressing: {business_need[:50]}")
    
    if category == "Hot":
        actions.append("Expedite proposal and timeline")
    elif category == "Warm":
        actions.append("Conduct discovery call to advance opportunity")
    else:
        actions.append("Add to nurture email sequence")
    
    return actions


def _get_risk_factors(budget, authority, urgency, business_need):
    """Generate context-specific risk factors"""
    risks = []
    
    if 'unknown' in budget.lower() or 'under' in budget.lower():
        risks.append("Budget constraints may limit solution scope")
    
    if 'end user' in authority.lower() or 'influencer' in authority.lower():
        risks.append(f"Multiple approval levels required")
    
    if 'exploring' in urgency.lower() or 'low' in urgency.lower():
        risks.append("Extended sales cycle likely")
    
    if len(business_need) < 20:
        risks.append("Business need clarity needs refinement")
    
    return risks if risks else ["No significant identified risks"]


def _intelligent_campaign_fallback(product_desc, audience, platform, industry):
    """Fallback campaign generation when Groq is unavailable."""
    return {
        "status": "success",
        "campaign": {
            "campaign_ideas": [
                {"title": f"{industry} Growth Accelerator", "description": f"A data-driven campaign targeting {audience} on {platform} focusing on the unique benefits of {product_desc[:30]}..."},
                {"title": "Problem-Solver Spotlight", "description": "Showcase how your solution directly addresses the core pain points of the industry."},
                {"title": "Customer Success Stories", "description": "Highlight transformations achieved by similar companies in the sector."},
                {"title": "Expert Insights Series", "description": "Educational content providing value and establishing authority."},
                {"title": "Limited-Time Offer Launch", "description": f"Urgency-based campaign for {platform} users."}
            ],
            "cta_suggestions": [
                {"cta_text": "Start Your Free Trial", "description": "Best for educational content to lower barrier to entry."},
                {"cta_text": "Download the Whitepaper", "description": "Perfect for B2B lead generation and authority building."},
                {"cta_text": "Schedule a Demo", "description": "Used for high-intent prospects nearing decision phase."},
                {"cta_text": "Get a Custom Quote", "description": "Effective for personalized/enterprise solutions."},
                {"cta_text": "Learn More", "description": "Generalized CTA for awareness-stage content."}
            ],
            "content_calendar": [
                {"day": 1, "post_type": "Educational", "content_idea": f"The future of {industry} and why {product_desc[:20]} matters.", "best_time": "9 AM"},
                {"day": 2, "post_type": "Engagement", "content_idea": "Poll: What is your biggest challenge in this industry?", "best_time": "12 PM"},
                {"day": 3, "post_type": "Promotional", "content_idea": f"Deep dive into a key feature of {product_desc[:20]}.", "best_time": "3 PM"},
                {"day": 4, "post_type": "Educational", "content_idea": "3 pitfalls to avoid in current market conditions.", "best_time": "10 AM"},
                {"day": 5, "post_type": "Social Proof", "content_idea": "Client testimonial and ROI results.", "best_time": "1 PM"},
                {"day": 6, "post_type": "Educational", "content_idea": "How-to guide for optimizing your current workflow.", "best_time": "11 AM"},
                {"day": 7, "post_type": "Promotional", "content_idea": "Last call for the weekly specialized session.", "best_time": "2 PM"}
            ],
            "competitor_analysis": {
                "common_strategies": ["Heavy emphasis on pricing", "Generic feature-based marketing", "Broad audience targeting"],
                "gaps_opportunities": ["Lack of personalized support", "Unclear ROI metrics", "Missing specific integration features"],
                "differentiation_tactics": ["Emphasize explainable AI", "Focus on niche expertise", "Provide superior implementation support"]
            }
        },
        "ai_model": "Intelligent Fallback (Strategy-based)"
    }


def _intelligent_pitch_fallback(product, description, persona, industry, customer_type, budget_preference, language):
    """Fallback pitch generation when Groq is unavailable."""
    # Basic English templates for fallback
    pitch_templates = {
        "elevator_pitch": f"We help {persona} in the {industry} sector achieve better results through {product}. In a market where {description[:40]}... is critical, our solution ensures you stand out by addressing your specific {customer_type} needs while respecting your {budget_preference} requirements.",
        "value_proposition": f"The most efficient way for {industry} professionals to scale operations without complexity.",
        "personalized_cta": f"Would you like to see how {product} can transform your {industry} strategy?"
    }
    
    # Mock language support for key Indian languages (simplified)
    if language == "Hindi":
        pitch_templates["elevator_pitch"] = f"हम {industry} क्षेत्र में {persona} को {product} के माध्यम से अपने लक्ष्यों को प्राप्त करने में मदद करते हैं। एक ऐसे बाजार में जहां {description[:30]}... महत्वपूर्ण है, हमारा समाधान आपकी विशिष्ट आवश्यकताओं को पूरा करता है।"
        pitch_templates["value_proposition"] = "बेहतर व्यवसाय विकास के लिए एआई-संचालित समाधान।"
        pitch_templates["personalized_cta"] = "आज ही अपना डेमो बुक करें।"
    elif language == "Telugu":
        pitch_templates["elevator_pitch"] = f"మేము {industry} రంగంలో {persona} కి {product} ద్వారా మెరుగైన ఫలితాలను సాధించడంలో సహాయపడతాము. {description[:30]}... కీలకమైన ఈ మార్కెట్‌లో, మా పరిష్కారం మీ అవసరాలను తీరుస్తుంది."
        pitch_templates["value_proposition"] = "మీ వ్యాపారాన్ని AI తో వృద్ధి చేద్దాం."
        pitch_templates["personalized_cta"] = "మరిన్ని వివరాల కోసం ఈరోజే సంప్రదించండి."
    
    return {
        "status": "success",
        "pitch": {
            "elevator_pitch": pitch_templates["elevator_pitch"],
            "value_proposition": pitch_templates["value_proposition"],
            "key_differentiators": [
                "Proprietary AI Engine optimized for results",
                f"Deep {industry} expertise built-in",
                "Zero-friction implementation process"
            ],
            "personalized_cta": pitch_templates["personalized_cta"],
            "deal_confidence_score": 80,
            "confidence_breakdown": {
                "budget_alignment": "Strong fit for specified range",
                "pain_point_fit": "Directly addresses core needs",
                "authority_match": f"Tailored for {persona}",
                "timeline_fit": "High readiness detected"
            },
            "reasoning": {
                "why_this_pitch": "Focuses on value over features",
                "industry_nuances": f"Addresses {industry} challenges",
                "size_considerations": f"Scaled for {customer_type}",
                "objection_handling": "Pre-emptively addresses ROI concerns"
            },
            "recommended_next_actions": [
                "Send personalized proposal",
                "Book a 15-minute discovery call",
                "Share relevant case studies"
            ]
        },
        "ai_model": f"Intelligent Fallback ({language} Template)"
    }
