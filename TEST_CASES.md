# MarketAI Suite - Test Cases & Expected Outputs

This document outlines all test cases with expected behaviors and outputs.

---

## 🔐 Authentication Test Cases

### TC-001: User Registration - Success
**Steps**:
1. Navigate to `/register`
2. Enter email: `test@company.com`
3. Enter password: `SecurePass123`
4. Enter confirm password: `SecurePass123`
5. Click "Create Account"

**Expected Result**:
- ✓ User account created
- ✓ Redirect to login page
- ✓ Success message displayed
- ✓ MongoDB users collection has new document with bcrypt-hashed password

---

### TC-002: User Registration - Validation Errors
**Steps**:
1. Try to register with passwords that don't match
2. Try to register with duplicate email

**Expected Results**:
- ✓ "Passwords do not match" error message
- ✓ "User already exists" error message
- ✓ No user created in database

---

### TC-003: User Login - Success
**Steps**:
1. Navigate to `/login`
2. Enter email: `test@company.com`
3. Enter password: `SecurePass123`
4. Click "Sign In"

**Expected Result**:
- ✓ JWT token generated
- ✓ Token stored in localStorage
- ✓ Redirect to dashboard `/`
- ✓ User email displayed in dashboard
- ✓ Activity counts loaded

---

### TC-004: User Login - Invalid Credentials
**Steps**:
1. Enter wrong password
2. Try non-existent email

**Expected Results**:
- ✓ "Invalid credentials" error
- ✓ Not redirected to dashboard
- ✓ No token stored

---

### TC-005: Session Persistence
**Steps**:
1. Login successfully
2. Refresh page
3. Close tab and reopen

**Expected Result**:
- ✓ User remains logged in
- ✓ Dashboard loads with user info
- ✓ Token retrieved from localStorage

---

### TC-006: Logout
**Steps**:
1. Login successfully
2. Click "Logout" button

**Expected Result**:
- ✓ Token removed from localStorage
- ✓ Redirect to `/login`
- ✓ "Unauthorized" if trying to access protected routes

---

## 📊 Campaign Generator Test Cases

### TC-C01: Campaign Generation - SaaS/LinkedIn
**Input**:
```
Product: "AI email marketing automation tool"
Audience: "Small business owners (1-50 employees)"
Platform: "LinkedIn"
Industry: "SaaS"
```

**Expected Output**:
```json
{
  "campaign_objective": "Convert SaaS-aware SMBs to trial users within Q2",
  "content_ideas": [
    {
      "title": "ROI Calculator Interactive Post",
      "description": "Show time saved using tool..."
    },
    // ... 4 more ideas
  ],
  "ad_copy_variants": [
    {
      "headline": "Save 20 Hours Weekly on Email Campaigns",
      "description": "Professional SMB-focused copy..."
    },
    // ... 2 more variants
  ],
  "cta_suggestions": ["Try Free Trial", "Request Demo", "See Pricing"],
  "posting_strategy": "3x weekly on Tuesday-Thursday, 9-11 AM EST",
  "roi_estimate": "15-25% increase in qualified leads",
  "conversion_probability": "12% estimated conversion to trial",
  "reasoning": {
    "objective_why": "SMBs care about efficiency and ROI...",
    "content_strategy": "LinkedIn audiences value professional education...",
    "platform_fit": "LinkedIn is ideal for B2B SaaS...",
    "industry_considerations": "SaaS market is competitive, need differentiation...",
    "success_metrics": "Track trial signups, demo bookings, cost per acquisition..."
  },
  "recommended_next_actions": [
    "Create carousel posts with each benefit highlighted",
    "Set up A/B testing with different CTAs",
    "Schedule posts in content calendar"
  ]
}
```

**Assertions**:
- ✓ Campaign has all required fields
- ✓ 5 unique content ideas
- ✓ 3 different ad copy variants
- ✓ SMB-focused tone evident in copy
- ✓ LinkedIn-specific strategy (posting times, format)
- ✓ ROI estimate is reasonable (15-25% range)
- ✓ Conversion probability is realistic
- ✓ Reasoning explains each decision
- ✓ Next actions are specific and actionable
- ✓ Data saved to MongoDB with user_id

---

### TC-C02: Campaign Generation - Retail/Instagram
**Input**:
```
Product: "Seasonal clothing line"
Audience: "Fashion-conscious women 25-40"
Platform: "Instagram"
Industry: "Retail"
```

**Expected Output**:
- ✓ Visually-focused content ideas (not detailed copy)
- ✓ Influencer collaboration suggestions
- ✓ Hashtag strategy included
- ✓ Posting frequency: daily or 4-5x weekly
- ✓ Retail-specific metrics (conversion value, AOV)
- ✓ Trend awareness in reasoning
- ✓ User-generated content strategy

---

### TC-C03: Campaign History
**Steps**:
1. Generate campaign for SaaS/LinkedIn
2. Return to campaign page
3. Scroll to "Previous Campaigns"

**Expected Result**:
- ✓ Previous campaign appears in list
- ✓ Shows product, audience, platform, created date
- ✓ Limit of 10 campaigns shown
- ✓ Sorted by most recent first

---

### TC-C04: Campaign Error Handling
**Steps**:
1. Submit campaign form with missing fields
2. Simulate network error (DevTools)
3. Simulate invalid AI response

**Expected Results**:
- ✓ Validation error: "Missing required fields"
- ✓ Network error: "Network error. Please try again."
- ✓ AI error: Error message displayed to user
- ✓ No campaign saved to database

---

## 🎤 Sales Pitch Generator Test Cases

### TC-P01: Pitch Generation - Operations Director/Retail
**Input**:
```
Product: "Inventory management software"
Persona: "Operations Director"
Industry: "Retail"
Company Size: "Mid-Market (500-5000)"
Budget Range: "$50K - $150K/year"
```

**Expected Output**:
```json
{
  "elevator_pitch": "Reduce manual inventory counts by 80% and cut stockouts by half with real-time inventory visibility across all locations.",
  "value_proposition": "Transform inventory from a liability into a competitive advantage through AI-powered demand forecasting",
  "key_differentiators": [
    "Real-time visibility across all locations",
    "AI-powered demand forecasting",
    "Integrates with existing POS systems"
  ],
  "personalized_cta": "Schedule a 15-minute demo with your team lead",
  "recommended_next_step": "Get Operations Director and Finance VP on demo call (decision makers)",
  "deal_confidence_score": 78,
  "confidence_breakdown": {
    "budget_alignment": "Budget ($50-150K) is perfect fit for mid-market retail software",
    "pain_point_fit": "Inventory management is critical pain point for this role",
    "authority_match": "Operations Director is decision influencer but may need CFO approval",
    "timeline_fit": "Mid-market decisions typically 4-6 weeks"
  },
  "reasoning": {
    "why_this_pitch": "Focus on operational efficiency and bottom-line impact...",
    "industry_nuances": "Retail has unique multi-location complexity...",
    "size_considerations": "Mid-market needs ROI validation and integration support...",
    "objection_handling": "Expect concerns about implementation time and staff training..."
  },
  "recommended_next_actions": [
    "Prepare comparison to their current manual process",
    "Get customer testimonial from similar size retail",
    "Demo should focus on integration with their POS"
  ]
}
```

**Assertions**:
- ✓ 30-second elevator pitch is concise and compelling
- ✓ Value proposition addresses business impact
- ✓ 3 differentiators specific to retail operations
- ✓ CTA personalized to persona and size
- ✓ Deal confidence score is realistic (70-85 range typical)
- ✓ Confidence breakdown explains each score
- ✓ Reasoning includes industry and size specifics
- ✓ Objection handling is thoughtful and realistic
- ✓ Next actions are sales-team ready

---

### TC-P02: Pitch Different Industry - EdTech/Founder
**Input**:
```
Product: "Learning management system"
Persona: "Founder/CEO"
Industry: "EdTech"
Company Size: "Startup (1-50)"
Budget Range: "Under $50K/year"
```

**Expected Changes**:
- ✓ Pitch focuses on growth and scale potential
- ✓ Budget implications about bootstrap/funding stage
- ✓ Founder-specific language (not administrator-focused)
- ✓ ROI focus: cost per student, retention metrics
- ✓ EdTech tone: engagement, learning outcomes
- ✓ Confidence score lower (startups less predictable)
- ✓ Next actions include integration roadmap

---

### TC-P03: Pitch History
**Steps**:
1. Generate 3 different pitches
2. Scroll to "Previous Pitches"

**Expected Result**:
- ✓ All 3 pitches listed
- ✓ Format: "Product → Persona"
- ✓ Shows creation timestamp
- ✓ Most recent first

---

### TC-P04: Low Confidence Score Handling
**Input**:
```
Product: "Enterprise data warehouse"
Persona: "Junior IT Staff"
Company Size: "Startup"
Budget: "Under $50K"
```

**Expected Result**:
- ✓ Deal confidence score: 25-35 (very low)
- ✓ Reasoning explains: "Decision authority limited, budget mismatch, role not decision-maker"
- ✓ Next actions focus on: "Get executive sponsor, involve CFO early"
- ✓ Clear messaging: This is not a high-probability deal

---

## ⭐ Lead Scoring Test Cases

### TC-L01: Lead Scoring - Hot Lead
**Input**:
```
Budget: "$150,000"
Business Need: "Inventory management system replacement"
Urgency: "High - Need immediately"
Authority: "Decision maker"
Industry: "Retail"
```

**Expected Output**:
```json
{
  "lead_score": 87,
  "lead_category": "Hot",
  "conversion_probability": 74,
  "detailed_reasoning": {
    "budget_analysis": "$150K is substantial for retail software, indicates serious intent",
    "need_alignment": "Clear, specific need signals pain point",
    "urgency_signal": "High urgency = likely to move quickly through sales cycle",
    "authority_assessment": "Decision maker = can approve without further buy-in",
    "industry_context": "Retail vertical is strong fit for this solution"
  },
  "score_breakdown": {
    "budget_fit": {"score": 90, "reasoning": "Budget perfectly aligned"},
    "need_clarity": {"score": 85, "reasoning": "Clear business need"},
    "urgency_level": {"score": 88, "reasoning": "High urgency indicates readiness"},
    "authority_level": {"score": 95, "reasoning": "Direct decision maker"},
    "industry_fit": {"score": 80, "reasoning": "Good fit for retail"}
  },
  "priority_recommendation": "Contact within 24 hours, escalate to senior AE, prepare contract",
  "next_actions": [
    "Schedule discovery call today",
    "Prepare ROI calculator for retail",
    "Get legal review on contract"
  ],
  "risk_factors": []
}
```

**Assertions**:
- ✓ Score 85+: "Hot" category
- ✓ Conversion probability 70%+
- ✓ All 5 dimensions scored 80+
- ✓ No risk factors identified
- ✓ Priority says "contact within 24 hours"
- ✓ Next actions are urgent and specific

---

### TC-L02: Lead Scoring - Warm Lead
**Input**:
```
Budget: "$50K"
Business Need: "Email marketing platform"
Urgency: "Medium - Within 3 months"
Authority: "Budget influence (recommends, CFO approves)"
Industry: "SaaS"
```

**Expected Result**:
- ✓ Lead score: 55-75
- ✓ Category: "Warm"
- ✓ Budget fit: 70 (adequate but not substantial)
- ✓ Urgency: 60 (Medium)
- ✓ Authority: 60 (influencer, not sole decision maker)
- ✓ Conversion probability: 45-55%
- ✓ Priority: "Follow up in 1-2 weeks"
- ✓ Risk factors: "May need CFO approval"

---

### TC-L03: Lead Scoring - Cold Lead
**Input**:
```
Budget: "Under $50K"
Business Need: "Exploring options for future reference"
Urgency: "Low - 6+ months"
Authority: "End user (no budget approval power)"
Industry: "Finance"
```

**Expected Result**:
- ✓ Lead score: 25-40
- ✓ Category: "Cold"
- ✓ Conversion probability: 15-25%
- ✓ Priority: "Add to nurture list, touch every 3 months"
- ✓ Risk factors: 
  - "No immediate need"
  - "Limited authority"
  - "Budget constraints"
- ✓ Next actions: Nurture content, education materials

---

### TC-L04: Lead Score Consistency
**Steps**:
1. Score a lead with specific inputs
2. Score the same lead again with identical inputs
3. Compare results

**Expected Result**:
- ✓ Scores are very similar (±2 points max)
- ✓ Categories are identical
- ✓ Reasoning is consistent
- ✓ Later model improvements may change slightly

---

### TC-L05: Lead History
**Steps**:
1. Score 5 different leads
2. Scroll to "Previous Leads"

**Expected Result**:
- ✓ All 5 leads appear in list
- ✓ Shows: Score, Category, Business Need, Created Date
- ✓ Most recent first
- ✓ Visual score indicators (color-coded)

---

## 🎯 Dashboard & Activity Test Cases

### TC-D01: Dashboard Load
**Steps**:
1. Login successfully
2. Dashboard loads

**Expected Result**:
- ✓ User email displayed
- ✓ Feature cards visible (Campaign, Pitch, Lead)
- ✓ Counters show correct numbers (0 initially)
- ✓ "Recent Activity" section loads

---

### TC-D02: Dashboard Counts Update
**Steps**:
1. Start with 0 campaigns
2. Generate 1 campaign
3. Return to dashboard
4. Check counter

**Expected Result**:
- ✓ Counter updates from "0 campaigns" to "1 campaign"
- ✓ No page refresh needed
- ✓ Activity list shows new entry

---

### TC-D03: Cross-Feature Navigation
**Steps**:
1. Generate campaign on /campaign page
2. Click "Dashboard" link
3. Click "Pitch" link
4. Generate pitch
5. Return to dashboard

**Expected Result**:
- ✓ Both campaign and pitch counts show correct numbers
- ✓ Activity shows both actions
- ✓ No data loss between navigation

---

## 🔍 Explainability Test Cases

### TC-E01: Campaign Reasoning Verification
**Steps**:
1. Generate campaign
2. Scroll to "Why AI Generated This?" section

**Expected Content**:
- ✓ "Objective Strategy": Why this objective fits the inputs
- ✓ "Content Approach": Why these content types
- ✓ "Platform Selection": Why platform is ideal
- ✓ "Industry Considerations": How industry affects strategy
- ✓ "Success Metrics": How to measure success

**Quality Checks**:
- ✓ Reasoning must be non-generic
- ✓ Should reference specific inputs (product, audience)
- ✓ Should not be obvious/superficial
- ✓ Should provide learning value

---

### TC-E02: Lead Score Reasoning Verification
**Steps**:
1. Score a lead
2. Check "Detailed Analysis" section

**Expected Content**:
- ✓ Budget analysis with specific number analysis
- ✓ Need alignment with business logic
- ✓ Urgency signal interpretation
- ✓ Authority assessment with implications
- ✓ Industry context with specific patterns

**Quality Checks**:
- ✓ Each explanation must be substantive
- ✓ Must help user understand scoring
- ✓ Should enable user to agree/disagree with score
- ✓ Must address user inputs directly

---

### TC-E03: Risk Disclosure
**Steps**:
1. Generate outputs with moderate scores
2. Check for risk factors or disclaimers

**Expected Result**:
- ✓ Campaign: "Estimated ROI is AI-assisted, not guaranteed"
- ✓ Pitch: "Confidence score is probability estimate"
- ✓ Lead: Risk factors clearly listed if present
- ✓ All include: "AI estimation disclaimer"

---

## 🚀 Performance Test Cases

### TC-PERF01: Campaign Generation Speed
**Criteria**:
- Input to spinner: < 500ms
- AI generation: < 15 seconds typically
- Display: < 200ms
- **Total**: < 16 seconds acceptable

---

### TC-PERF02: Dashboard Load Speed
**Criteria**:
- Initial page: < 2 seconds
- Fetch activity: < 1 second
- Fetch counts: < 1 second
- **Total**: < 2 seconds acceptable

---

### TC-PERF03: API Response Time
**Criteria**:
- Login: < 500ms
- Fetch campaigns: < 500ms
- Save campaign: < 500ms
- (Excludes AI generation time)

---

## 🔒 Security Test Cases

### TC-SEC01: JWT Token Validation
**Steps**:
1. Login and capture token
2. Try API call with invalid token
3. Try API call with expired token
4. Try API call without token

**Expected Results**:
- ✓ Invalid token: 401 Unauthorized
- ✓ Expired token: 401 Unauthorized (requires re-login)
- ✓ No token: 401 Unauthorized
- ✓ Valid token: 200 OK

---

### TC-SEC02: User Data Isolation
**Steps**:
1. User A logs in, generates campaign
2. User B logs in, generates campaign
3. User A checks own campaigns (should see 1)
4. Try to access User B's campaign via URL

**Expected Results**:
- ✓ User A sees only their campaign
- ✓ User B sees only their campaign
- ✓ User A cannot access User B's campaign (403 Forbidden)
- ✓ Database enforces user_id in queries

---

### TC-SEC03: Password Security
**Steps**:
1. Register user
2. Check database for password

**Expected Result**:
- ✓ Database contains bcrypt hash, NOT plaintext password
- ✓ Hash starts with "$2b$" (bcrypt prefix)
- ✓ Cannot reverse hash to get original password

---

## 📱 Responsive Design Test Cases

### TC-RESP01: Mobile View (375px width)
**Tests**:
- [ ] Input forms stack vertically
- [ ] Campaign output cards responsive
- [ ] Navigation menu collapses to hamburger
- [ ] Buttons are touch-friendly (48px+ height)
- [ ] Text is readable (16px+)
- [ ] No horizontal scroll

---

### TC-RESP02: Tablet View (768px width)
**Tests**:
- [ ] Content grid adjusts to 1 column
- [ ] Forms display properly
- [ ] Charts/metrics responsive
- [ ] No text overflow

---

### TC-RESP03: Desktop View (1200px+ width)
**Tests**:
- [ ] 2-column layout (form + output)
- [ ] Multi-column grids display
- [ ] Full feature utilization
- [ ] Proper spacing maintained

---

## ✅ Acceptance Criteria - Full Application

For the application to be considered "production ready":

- [ ] All 35+ test cases pass
- [ ] No console errors in browser DevTools
- [ ] No server errors in Flask logs
- [ ] User data persists across sessions
- [ ] AI outputs are relevant and high quality
- [ ] Explainability sections provide real value
- [ ] Mobile view works correctly
- [ ] Code has no hardcoded secrets
- [ ] README is complete and accurate
- [ ] ARCHITECTURE.md explains all components

---

**Test Document Version**: 1.0  
**Last Updated**: February 2026  
**Status**: Ready for QA ✅

---
