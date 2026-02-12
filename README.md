# MarketAI Suite

PPT Link: https://www.canva.com/design/DAHA_SMZOe4/58JX_lDmdYkUk4O5UAV_jw/edit?utm_content=DAHA_SMZOe4&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton


## AI-Powered Sales & Marketing Intelligence Platform

MarketAI Suite is a production-ready SaaS application that uses explainable AI to help sales and marketing teams generate campaigns, create personalized pitches, and score leads with complete transparency and reasoning.

---

## 🎯 What Problem Does It Solve?

Sales and marketing teams face these challenges daily:
- **Time-consuming campaign planning** - Hours spent brainstorming campaign ideas
- **Generic pitches** - Difficulty personalizing sales pitches at scale
- **Inconsistent lead scoring** - Subjective lead qualification without data backing
- **Black box AI** - Unable to explain AI recommendations to stakeholders

**MarketAI Suite solves these problems** by providing AI-generated insights with full explainability, showing exactly why each recommendation was made.

---

## ✨ Core Features

### 1. Campaign Generator
Generate complete marketing campaigns in seconds:
- **5 Campaign Ideas** - Platform-specific creative concepts
- **5 Call-to-Actions** - Conversion-optimized CTAs with usage tips
- **7-Day Content Calendar** - Daily posting schedule with optimal timing
- **Competitor Analysis** - Market insights and differentiation strategies

**Supports platforms:** LinkedIn, Instagram, Twitter, Facebook, Email, TikTok

### 2. Pitch Generator
Create personalized sales pitches with:
- **Elevator Pitch** - Compelling 1-minute pitch
- **Value Proposition** - Clear benefit statement
- **Key Differentiators** - What makes your product unique
- **Personalized CTA** - Next step tailored to the customer
- **Multi-language Support** - Generate pitches in English, Telugu, Hindi, Tamil, Malayalam, Kannada

### 3. Lead Scoring System
Intelligent lead qualification with:
- **Lead Score (0-100)** - Quantified lead quality
- **Category Classification** - Hot/Warm/Cold categorization
- **Conversion Probability** - Percentage likelihood of closing
- **BANT Analysis** - Budget, Authority, Need, Timeline breakdown
- **Risk Factors** - Potential deal blockers identified
- **Priority Recommendations** - When and how to follow up

---

## 🏗️ Technology Stack

### Backend
- **Python 3.9+** with Flask framework
- **MongoDB Atlas** for cloud database storage
- **Groq API** with LLaMA 3.3 70B model for AI generation
- **JWT** for secure authentication
- **bcrypt** for password encryption

### Frontend
- **HTML5, CSS3, Vanilla JavaScript** - No framework dependencies
- **Responsive Design** - Works on mobile, tablet, and desktop
- **Modern UI** - Gradient-based SaaS aesthetic
- **Tab Navigation** - Clean, organized content display

### Security
- JWT token-based authentication
- Password hashing with bcrypt
- Protected API routes
- User data isolation
- 30-day token expiration

---

## 🚀 Quick Start Guide

### Step 1: Prerequisites
Make sure you have installed:
- Python 3.9 or higher
- pip (Python package manager)
- Internet connection (for MongoDB Atlas and Groq API)

### Step 2: Setup
Navigate to the project folder and run:

**On Windows:**
- Double-click QUICKSTART.bat
- OR manually: activate virtual environment with venv\Scripts\activate
- Then: pip install -r requirements.txt

**On Mac/Linux:**
- Run: bash QUICKSTART.sh
- OR manually: source venv/bin/activate
- Then: pip install -r requirements.txt

### Step 3: Configuration
The .env file is pre-configured with:
- MongoDB connection string
- Groq API key
- Flask secret keys

No additional configuration needed!

### Step 4: Run
Execute: python app.py

The application will start on http://localhost:5000

### Step 5: Use
1. Open browser to http://localhost:5000
2. Register a new account
3. Login with your credentials
4. Start generating campaigns, pitches, or scoring leads!

---

## 📱 How to Use Each Feature

### Campaign Generator
1. Navigate to "Campaigns" from the menu
2. Fill in the form:
   - Product Description (what you're marketing)
   - Target Audience (who you're targeting)
   - Platform (where you'll run the campaign)
   - Industry (your business sector)
3. Click "Generate Campaign"
4. View results in organized tabs:
   - Campaign Ideas tab
   - Call to Actions tab
   - Content Calendar tab
   - Competitor Analysis tab

### Pitch Generator
1. Navigate to "Pitches" from the menu
2. Fill in the form:
   - Product Name
   - Product Description
   - Customer Persona (who you're pitching to)
   - Industry
   - Customer Type (Individual, SMB, Enterprise, etc.)
   - Budget Preference
   - Language (English, Telugu, Hindi, Tamil, Malayalam, Kannada)
3. Click "Generate Pitch"
4. View your personalized pitch with all components

### Lead Scoring
1. Navigate to "Leads" from the menu
2. Enter lead information:
   - Budget (their investment capacity)
   - Business Need (what problem they need solved)
   - Urgency (their timeline)
   - Authority (their decision-making power)
   - Industry
3. Click "Score Lead"
4. View comprehensive scoring with:
   - Overall score and category
   - Detailed BANT breakdown
   - Risk factors
   - Recommended actions

---

## 🎨 User Interface Features

### Modern Design
- Dark theme with gradient accents
- Clean, professional layout
- Intuitive navigation
- Loading states for AI generation
- Error handling with user-friendly messages

### Tab Navigation
Campaign results are organized in tabs for easy access:
- Switch between different sections instantly
- No page reloads
- Smooth animations
- Mobile-responsive

### Feedback System
- Thumbs up/down for AI outputs
- Detailed feedback modal for improvements
- Helps improve AI recommendations over time

---


## 🔒 Security Features

### Authentication
- Secure registration with email validation
- Password hashing (never stored in plain text)
- JWT token-based sessions
- Automatic token expiration
- Protected API endpoints

### Authorization
- User-specific data access
- Route protection with JWT verification
- 401 errors for unauthorized access
- 403 errors for forbidden resources

---

## 📝 Project Structure

**Main Files:**
- app.py - Flask application and API routes
- ai_engine.py - AI generation logic with Groq API
- auth.py - Authentication and user management
- db.py - MongoDB connection and initialization
- utils.py - Helper functions for database operations
- models.py - Data models and schemas

**Frontend:**
- templates/ - HTML pages for each feature
- static/ - CSS styles and JavaScript
- style.css - Global styling
- app.js - Shared JavaScript functions

**Configuration:**
- .env - Environment variables (API keys, database URI)
- requirements.txt - Python dependencies
- QUICKSTART.bat/sh - Setup scripts

---
## 🎬 Next Steps

After setup, try these:
1. Generate a campaign for your product
2. Create a pitch in multiple languages
3. Score a few sample leads
4. Explore the competitor analysis feature
5. Review the content calendar suggestions

---

## 📄 License

Built for educational and commercial use. Feel free to modify and extend.

---

## 🌟 Final Notes

MarketAI Suite demonstrates:
- ✅ Full-stack development with Python and JavaScript
- ✅ AI integration with explainability
- ✅ Production-ready authentication and security
- ✅ Real business value and practical applications
- ✅ Clean, maintainable code architecture
- ✅ Modern, responsive user interface

**Status:** Production-ready. Deploy and use immediately.

---

**Built with ❤️ for sales and marketing teams everywhere.**
