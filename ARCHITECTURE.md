# MarketAI Suite - Architecture & Design Document

## System Overview

MarketAI Suite is a production-grade, explainable AI platform for sales and marketing intelligence. The architecture emphasizes **trustworthiness through transparency**, with AI reasoning integrated into every decision.

---

## 🏗️ High-Level Architecture

```
┌─────────────────────────────────────────────────────┐
│                   CLIENT TIER                        │
│  HTML5/CSS3 + Vanilla JS (SPA-style, no build)      │
├─────────────────────────────────────────────────────┤
│                  API TIER (Flask)                    │
│  RESTful endpoints with JWT authentication           │
├─────────────────────────────────────────────────────┤
│              APPLICATION LOGIC TIER                  │
│  ├─ Authentication (auth.py)                        │
│  ├─ AI Engine (ai_engine.py)                        │
│  ├─ Database Utilities (utils.py)                   │
│  └─ Models (models.py)                              │
├─────────────────────────────────────────────────────┤
│                  INTEGRATION TIER                    │
│  ├─ Groq API (LLaMA 3.x 70B)                        │
│  └─ MongoDB (persistent storage)                    │
└─────────────────────────────────────────────────────┘
```

---

## 🔐 Authentication Flow

```
USER REGISTRATION
  ↓
  Input: email, password
  ↓
  Hash password using bcrypt
  ↓
  Store in MongoDB users collection
  ↓
  Return user_id

USER LOGIN
  ↓
  Input: email, password
  ↓
  Find user in MongoDB
  ↓
  Verify password hash
  ↓
  Generate JWT token (valid 30 days)
  ↓
  Return token to frontend
  ↓
  Frontend stores in localStorage

AUTHENTICATED REQUEST
  ↓
  Client sends: Authorization: Bearer <JWT>
  ↓
  Flask @jwt_required() decorator validates
  ↓
  Extract user_id from token
  ↓
  Return user-specific data
```

---

## 🧠 AI Generation Pipeline

### Campaign Generation Pipeline

```
INPUTS (User Form)
  ├─ Product description
  ├─ Target audience
  ├─ Platform (LinkedIn, Facebook, etc.)
  └─ Industry (SaaS, Retail, etc.)
        ↓
        ↓ PROMPT ENGINEERING
        ↓
        ├─ Inject industry tone mapping
        ├─ Request structured JSON output
        ├─ Include explainability requirements
        └─ Add business metric requests
        ↓
        ↓ GROQ API CALL
        ↓
        ├─ Model: LLaMA 3.x 70B
        ├─ Max tokens: 2000
        ├─ Temperature: default (for consistency)
        └─ Timeout: 30 seconds
        ↓
        ↓ RESPONSE PARSING
        ↓
        ├─ Remove markdown if present
        ├─ Parse JSON structure
        ├─ Validate required fields
        └─ Handle errors gracefully
        ↓
        ↓ OUTPUT TO FRONTEND
        ↓
        ├─ Campaign objective
        ├─ Content ideas (5 items)
        ├─ Ad copy variants (3 items)
        ├─ CTA suggestions
        ├─ Posting strategy
        ├─ ROI estimate
        ├─ Conversion probability
        ├─ Reasoning (explainability section)
        └─ Recommended next actions
        ↓
        ↓ SAVE TO DATABASE
        ↓
        ├─ Insert document in campaigns collection
        ├─ Attach user_id
        ├─ Add timestamp
        └─ Log activity
```

### Lead Scoring Pipeline

```
INPUTS (User Form)
  ├─ Budget
  ├─ Business need
  ├─ Urgency level
  ├─ Decision authority
  └─ Industry
        ↓
        ↓ STRUCTURED PROMPT
        ↓
        ├─ Request lead_score (0-100)
        ├─ Request category (Hot/Warm/Cold)
        ├─ Request conversion_probability
        ├─ Request breakdown by dimension
        ├─ Request risk factors
        └─ Request detailed reasoning
        ↓
        ↓ AI ANALYSIS
        ↓
        ├─ Budget fit analysis
        ├─ Business need clarity assessment
        ├─ Urgency signal interpretation
        ├─ Authority level evaluation
        ├─ Industry-specific patterns
        └─ Risk factor identification
        ↓
        ↓ SCORING BREAKDOWN
        ↓
        ├─ Budget fit: 0-100
        ├─ Need clarity: 0-100
        ├─ Urgency level: 0-100
        ├─ Authority score: 0-100
        └─ Industry fit: 0-100
        ↓
        ↓ OVERALL CALCULATION
        ↓
        └─ Weighted average → Lead Score (0-100)
        ↓
        ↓ CATEGORY ASSIGNMENT
        ↓
        ├─ Score 80-100 → Hot (30+ days)
        ├─ Score 50-79 → Warm (60+ days)
        └─ Score <50 → Cold (follow-up later)
        ↓
        ↓ OUTPUT
        ↓
        ├─ Lead score with category
        ├─ Conversion probability
        ├─ Score breakdown with reasoning
        ├─ Risk factors (if any)
        ├─ Priority recommendation
        └─ Recommended next actions
```

---

## 💾 Data Flow & Persistence

### Campaign Persistence
```
generate_campaign() 
  ↓ Returns AI output
    ↓
save_campaign_to_db()
  ├─ Create Campaign model instance
  ├─ Insert into MongoDB campaigns collection
  ├─ Log activity to activity_logs
  └─ Return campaign_id
    ↓
get_user_campaigns()
  ├─ Query: campaigns collection where user_id = <ID>
  ├─ Sort by created_at descending
  ├─ Limit 10 results
  └─ Convert ObjectIds to strings for JSON
```

### Activity Tracking
```
Every AI generation triggers:
  ├─ insert_one() in activity_logs
  ├─ Action: 'campaign_created', 'pitch_created', 'lead_scored'
  ├─ Details: input parameters and key outputs
  └─ Timestamp: UTC

User can view timeline:
  └─ get_user_activity() returns last 20 activities
```

---

## 🌐 API Endpoint Architecture

### Authentication Endpoints
```
POST /api/auth/register
  Request: { email, password }
  Response: { user_id, email, message }
  Status: 201 Created

POST /api/auth/login  
  Request: { email, password }
  Response: { access_token, user_id, email }
  Status: 200 OK

GET /api/auth/me (requires JWT)
  Response: { user_id, email }
  Status: 200 OK
```

### Campaign Endpoints
```
POST /api/campaigns/generate (requires JWT)
  Request: { product, audience, platform, industry }
  Response: { campaign_id, campaign, message }
  Status: 201 Created
  
GET /api/campaigns (requires JWT)
  Response: { campaigns: [...], count: N }
  Status: 200 OK
  
GET /api/campaigns/<id> (requires JWT)
  Response: { _id, user_id, product, ... }
  Status: 200 OK
```

### Error Response Format
```json
{
  "error": "Human-readable error message"
}
```
Status: 400 (validation), 401 (auth), 403 (permission), 500 (server)

---

## 🗂️ Database Indexes

For performance optimization:

```javascript
// users collection
db.users.createIndex({ email: 1 }, { unique: true })

// campaigns collection
db.campaigns.createIndex({ user_id: 1, created_at: -1 })

// pitches collection
db.pitches.createIndex({ user_id: 1, created_at: -1 })

// leads collection
db.leads.createIndex({ user_id: 1, created_at: -1 })

// activity_logs collection
db.activity_logs.createIndex({ user_id: 1, created_at: -1 })
```

These indexes enable:
- Fast lookups by user_id
- Efficient sorting by creation date
- Chronological activity retrieval

---

## 🧩 Module Responsibilities

### db.py
**Responsibility**: MongoDB connection and initialization
- Connects to MongoDB Atlas
- Creates collections if missing
- Creates indexes for performance
- Provides get_db() singleton

### models.py
**Responsibility**: Data structure definitions
- User: authentication data
- Campaign: campaign generation output
- Pitch: pitch generation output
- Lead: lead scoring output
- ActivityLog: user action tracking
- Each model includes to_dict() for serialization

### auth.py
**Responsibility**: Authentication logic
- hash_password(): bcrypt hashing
- verify_password(): bcrypt comparison
- register_user(): user creation
- login_user(): JWT token generation
- get_current_user(): extract from JWT
- require_auth: decorator for protected routes

### ai_engine.py
**Responsibility**: AI generation and prompting
- generate_campaign(): creates marketing campaigns
- generate_pitch(): creates sales pitches
- score_lead(): evaluates lead quality
- Industry-aware tone mapping
- JSON parsing and validation
- Error handling for API calls

### utils.py
**Responsibility**: Database operations and helpers
- save_campaign_to_db()
- save_pitch_to_db()
- save_lead_to_db()
- get_user_campaigns()
- get_user_pitches()
- get_user_leads()
- get_user_activity()
- get_*_by_id() functions

### app.py
**Responsibility**: Flask application and routing
- App initialization
- Database setup
- JWT configuration
- CORS setup
- All API endpoints
- Static file serving
- Error handlers

---

## 🔄 Request Lifecycle (Example: Generate Campaign)

```
1. USER SUBMITS FORM
   └─ JavaScript captures form data

2. API CALL
   └─ fetch('/api/campaigns/generate', {
       method: 'POST',
       headers: { 'Authorization': 'Bearer <token>' },
       body: JSON.stringify(formData)
     })

3. FLASK ROUTING
   └─ @app.route('/api/campaigns/generate', methods=['POST'])
       └─ @jwt_required() validates token
       └─ get_jwt_identity() extracts user_id

4. INPUT VALIDATION
   └─ Check all required fields present

5. AI GENERATION
   └─ ai_engine.generate_campaign(product, audience, platform, industry)
       └─ Build structured prompt
       └─ Call Groq API
       └─ Parse JSON response
       └─ Return { campaign_id, campaign_data }

6. DATABASE PERSISTENCE
   └─ utils.save_campaign_to_db(...)
       └─ Insert into MongoDB
       └─ Log activity
       └─ Return campaign_id

7. RESPONSE
   └─ return { campaign_id, campaign, message }
       └─ Status: 201 Created

8. FRONTEND DISPLAY
   └─ JavaScript renders campaign output
   └─ Shows explainability section
   └─ Displays recommended actions
   └─ Adds to previous campaigns list
```

---

## 🔍 Explainability Architecture

Every AI output includes:

```json
{
  "primary_output": "...",
  
  "reasoning": {
    "why_this_choice": "Detailed explanation",
    "context_considerations": "Industry/size/needs",
    "business_logic": "How this aligns with goal",
    "success_metrics": "How to measure success"
  },
  
  "score_breakdown": {
    "dimension_1": {
      "score": 85,
      "reasoning": "Why this score"
    }
  },
  
  "recommended_next_actions": [
    "Specific, actionable step 1",
    "Specific, actionable step 2"
  ]
}
```

This ensures:
- Users understand AI recommendations
- Builds trust through transparency
- Provides audit trail for decisions
- Enables critical thinking by users

---

## 🏃 Performance Considerations

### Frontend
- No build step (vanilla JS)
- Lazy loading of templates
- Client-side caching of user data
- Spinner during AI calls (UX)

### Backend
- MongoDB indexes on frequently queried fields
- JWT stateless (no server session lookup)
- Single Groq API call per feature
- JSON response caching possible

### Database
- Indexes on (user_id, created_at) for fast retrieval
- Document size: <50KB typical
- Scalable: sharding by user_id if needed

---

## 🔒 Security Architecture

### Layers
1. **Transport**: HTTPS in production
2. **Authentication**: JWT with 30-day expiration
3. **Authorization**: user_id verification for data access
4. **Password**: bcrypt hashing with salt
5. **SQL Injection**: Not applicable (MongoDB documents)
6. **CSRF**: Disabled CORS for same-origin (Flask-CORS)
7. **Data Privacy**: User data isolated by user_id

### Threat Mitigation
```
Threat              Mitigation
─────────────────────────────────
Weak passwords      Client-side validation + bcrypt
Token theft         Expires in 30 days
Unauthorized access @jwt_required() decorator
Data breach         user_id isolation queries
                    Both in frontend & backend
```

---

## 📊 Scalability Architecture

### Current State (MVP)
- Single MongoDB instance
- Single Flask server
- Single Groq API call queue

### Scaling Path
1. **Horizontal**: Add Flask instances behind load balancer
2. **Database**: MongoDB sharding by user_id
3. **Caching**: Redis for frequent queries
4. **Async**: Celery for long-running AI tasks
5. **CDN**: CloudFront for static assets
6. **API**: Rate limiting per user tier

---

## 🧪 Testing Strategy

### Unit Tests (Recommended)
```python
# test_auth.py
- test_password_hashing()
- test_password_verification()
- test_jwt_generation()
- test_jwt_validation()

# test_ai_engine.py
- test_campaign_json_parsing()
- test_pitch_json_parsing()
- test_lead_score_parsing()

# test_models.py
- test_campaign_serialization()
- test_pitch_serialization()
```

### Integration Tests
```
- Full auth flow (register → login → logout)
- Campaign generation → save → retrieve
- Pitch generation with pricing data
- Lead scoring with all parameters
```

### Load Testing
```
- 100 concurrent users
- Campaign generation response time < 15s
- API response time < 2s (excluding AI)
```

---

## 📈 Monitoring & Logging

### Recommended Additions
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

# Log AI calls
logger.info(f"Campaign generated for user {user_id}")

# Log errors
logger.error(f"AI generation failed: {error}")

# Log performance
logger.info(f"Response time: {elapsed_time}ms")
```

---

## 🚀 Deployment Checklist

- [ ] Set Flask to production mode
- [ ] Generate strong SECRET_KEY
- [ ] Generate strong JWT_SECRET_KEY
- [ ] Configure MongoDB Atlas IP whitelist
- [ ] Enable HTTPS on domain
- [ ] Set X-Frame-Options headers
- [ ] Set Content-Security-Policy
- [ ] Configure CORS origins
- [ ] Set up error monitoring (Sentry)
- [ ] Set up log aggregation (CloudWatch)
- [ ] Configure database backups
- [ ] Set up API rate limiting
- [ ] SSL certificate from Let's Encrypt
- [ ] Cache headers for static assets

---

## 🔄 Future Enhancement Roadmap

### Phase 2
- [ ] Email campaign tracking
- [ ] A/B testing suggestions
- [ ] Sales call recording integration
- [ ] CRM sync (Salesforce, HubSpot)
- [ ] Export to PDF/CSV

### Phase 3
- [ ] Real-time collaboration
- [ ] Team analytics dashboard
- [ ] AI model fine-tuning
- [ ] Custom industry models
- [ ] Whitelabel solution

### Phase 4
- [ ] Mobile app (React Native)
- [ ] Voice-based input
- [ ] Video pitch generation
- [ ] Marketplace of templates
- [ ] Advanced analytics

---

## 📚 Architecture Decision Record (ADR)

### ADR-001: Use MongoDB instead of SQL
**Decision**: MongoDB
**Rationale**: 
- Flexible schema for AI outputs
- Fast horizontal scaling
- Document-oriented fits AI responses
- Atlas provides managed hosting

### ADR-002: Vanilla JS instead of React
**Decision**: Vanilla JavaScript
**Rationale**:
- No build process (simpler deployment)
- Smaller bundle size
- Sufficient for MVP scope
- Future: Easy to migrate to React if needed

### ADR-003: Groq instead of OpenAI
**Decision**: Groq API
**Rationale**:
- Faster response times
- Cheaper cost per token
- LLaMA 70B model quality matches GPT-3.5
- Good for real-time applications

### ADR-004: JWT instead of sessions
**Decision**: JWT
**Rationale**:
- Stateless (no server session lookup)
- Scales horizontally
- Works with distributed systems
- Secure 30-day expiration

---

**Architecture Version**: 1.0  
**Last Updated**: February 2026  
**Status**: Production Ready ✅

---

