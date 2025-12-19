# Quick Start Guide

## All Features Are Now Runnable! ✓

All dependencies have been installed and configured. The application is ready to run.

## Start the Application

### Option 1: Use the Start Script (Recommended)
```powershell
.\start.ps1
```

### Option 2: Direct Python Command
```powershell
python app.py
```

### Option 3: Using Flask
```powershell
flask run
```

## Once Running

The server will start at: **http://localhost:5000**

You'll see:
```
======================================================================
AI Career Advisor - Hackathon Edition
======================================================================
Features:
   * ATS-Optimized Resume Generation
   * Personalized Cover Letters
   * LinkedIn Profile Optimization
   * AI Mock Interviews with Real-time Feedback
   * 5-Year Career Trajectory Prediction
   * Skill Gap Analysis & Learning Paths
   * Salary Negotiation Strategies
   * Job Description Deep Analysis
   * Industry Insights & Trends
======================================================================
Server running at: http://localhost:5000
Powered by: Gemini AI 1.5 Pro
======================================================================
```

## Access the Application

Open your browser and navigate to:
- **Main App**: http://localhost:5000/
- **Gemini Features**: http://localhost:5000/gemini
- **Mock Interview**: http://localhost:5000/mock-interview
- **Legacy Interface**: http://localhost:5000/old

## Test the Features

Run the test suite to verify everything works:
```powershell
python test_features.py
```

Expected output: All tests should PASS ✓

## What Was Fixed

1. ✓ Added missing dependencies (scikit-learn, numpy, reportlab)
2. ✓ Fixed Windows encoding issues
3. ✓ Verified all directories exist
4. ✓ Database initializes correctly
5. ✓ All modules load successfully
6. ✓ API keys configured

## Available Features

### Core Features
- Student profile analysis
- Skill mapping and assessment
- Job market analysis
- Career recommendations
- Learning path generation
- Resume preparation and PDF generation

### AI-Powered Features (Gemini AI)
- ATS-optimized resume generation
- Personalized cover letters
- LinkedIn profile optimization
- Mock interviews with real-time feedback
- Interview answer evaluation
- Career trajectory prediction (5-year)
- Skill gap analysis
- Salary negotiation strategies
- Job description deep analysis
- Industry insights and trends

### Advanced Mock Interview
- Multi-round interview sessions
- Real-time AI evaluation
- Performance tracking
- Interview history
- Customizable difficulty levels

## API Endpoints

All endpoints are ready and functional:
- GET `/api/skills` - Get available skills
- GET `/api/industries` - Get industries
- POST `/api/analyze` - Analyze student profile
- POST `/api/gemini/*` - 11 Gemini AI endpoints
- POST `/api/interview/*` - Mock interview endpoints
- POST `/api/generate-resume` - Generate PDF resume

## Troubleshooting

If you encounter any issues:

1. **Import errors**: Run `pip install -r requirements.txt`
2. **API errors**: Check `.env` file has valid API keys
3. **Database errors**: Delete `career_advisor.db` and restart
4. **Port in use**: Change port in app.py or kill process on port 5000

## Need Help?

Check [FEATURES_STATUS.md](FEATURES_STATUS.md) for detailed status of all features.

---

**Ready to demo!** 🚀
