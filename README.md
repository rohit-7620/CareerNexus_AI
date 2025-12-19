# 🚀 AI Career Advisor - Hackathon Edition

A comprehensive AI-driven career advisory system powered by Google Gemini AI that helps students and professionals discover their ideal career paths through personalized skill analysis, market insights, and advanced AI features.

## ✨ Key Features

### 🎯 Core Features
- **Skill Mapping Engine**: ML-based skill analysis identifying strengths, gaps, and improvement areas
- **Job Market Analysis**: Real-time market trends and industry opportunities
- **Career Recommendations**: Personalized career paths based on skills and interests
- **Learning Plan Generator**: Customized learning paths with courses, certifications, and projects
- **Resume Preparation**: PDF generation with ATS optimization

### 🤖 Advanced Gemini AI Features
- **ATS-Optimized Resume Generation**: AI-powered resume creation with industry-specific keywords
- **Personalized Cover Letters**: Tailored cover letters for specific job applications
- **LinkedIn Profile Optimization**: Professional profile analysis and improvement suggestions
- **AI Mock Interviews**: Real-time interview simulation with instant feedback
- **Interview Answer Evaluation**: Detailed assessment of interview responses
- **Career Trajectory Prediction**: 5-year career path forecasting
- **Skill Gap Analysis**: Comprehensive analysis with learning recommendations
- **Salary Negotiation Strategies**: Data-driven negotiation guidance
- **Job Description Analysis**: Deep dive into job requirements and fit analysis
- **Industry Insights**: Real-time trends and market intelligence

### 💼 Interview Preparation
- **Advanced Mock Interviews**: Multi-round interview sessions with difficulty levels
- **Real-time Feedback**: Instant AI evaluation of answers
- **Performance Tracking**: Historical data and improvement metrics
- **Customizable Difficulty**: Easy, Medium, Hard interview levels

## 🏗️ Architecture

### Technology Stack
- **Backend**: Flask 3.0.0 (Python web framework)
- **AI Engine**: Google Gemini 2.5 Flash (generative AI)
- **ML Libraries**: scikit-learn 1.3.2, numpy 1.26.2
- **Database**: SQLite3 (with 7 tables for data management)
- **PDF Generation**: reportlab 4.0.7
- **CORS**: flask-cors 4.0.0

### System Components
1. **Student Inputs**: Skills, interests, educational background, experience, goals
2. **AI Modules**: 9 core modules processing data through ML and AI
3. **Gemini AI Engine**: Advanced features powered by Google's latest AI
4. **Career Recommendations**: Personalized career paths with detailed insights
5. **Output Delivery**: Web interface, PDF downloads, API responses

## 🚀 Quick Start

### Prerequisites
- Python 3.8+ (3.12.8 recommended)
- Git
- Google Gemini API key ([Get one here](https://makersuite.google.com/app/apikey))

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/ai-career-advisor.git
   cd ai-career-advisor
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv .venv
   ```

3. **Activate virtual environment**:
   
   **Windows:**
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```
   
   **Linux/Mac:**
   ```bash
   source .venv/bin/activate
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables**:
   ```bash
   # Copy example file
   cp .env.example .env
   
   # Edit .env and add your API keys
   GEMINI_API_KEY=your_gemini_api_key_here
   GEMINI_INTERVIEW_API_KEY=your_gemini_api_key_here
   ```

6. **Run tests** (optional but recommended):
   ```bash
   python test_features.py
   ```
   
   All tests should pass ✓

7. **Start the application**:
   ```bash
   python app.py
   ```
   
   Or use the startup script:
   ```bash
   .\start.ps1  # Windows
   ./start.sh   # Linux/Mac
   ```

8. **Access the application**:
   Open your browser and go to:
   - Main App: `http://localhost:5000`
   - Gemini Features: `http://localhost:5000/gemini`
   - Mock Interview: `http://localhost:5000/mock-interview`

## Usage

1. **Input Your Information**:
   - Select your skills from the available options
   - Choose your areas of interest
   - Provide your educational background and experience
   - Describe your career goals

2. **Get AI Analysis**:
   - The system analyzes your profile using AI modules
   - Skill mapping identifies your strengths and gaps
   - Market analysis provides industry insights

3. **Receive Recommendations**:
   - Get personalized career path recommendations
   - Access customized learning plans
   - Receive resume and interview preparation guidance

## 📡 API Endpoints

### Core Endpoints
- `GET /` - Main application interface (Gemini features)
- `GET /gemini` - Gemini AI features page
- `GET /old` - Legacy interface
- `GET /mock-interview` - Mock interview demo page
- `POST /api/analyze` - Analyze student profile and get recommendations
- `GET /api/skills` - Get available skills from database
- `GET /api/industries` - Get available industries

### Gemini AI Endpoints
- `POST /api/gemini/ats-resume` - Generate ATS-optimized resume
- `POST /api/gemini/cover-letter` - Generate personalized cover letter
- `POST /api/gemini/linkedin-analysis` - Analyze LinkedIn profile
- `POST /api/gemini/mock-interview` - Generate mock interview questions
- `POST /api/gemini/evaluate-answer` - Evaluate interview answers
- `POST /api/gemini/career-trajectory` - Predict career trajectory
- `POST /api/gemini/skill-gaps` - Analyze skill gaps
- `POST /api/gemini/salary-negotiation` - Salary negotiation strategies
- `POST /api/gemini/job-analysis` - Analyze job descriptions
- `POST /api/gemini/learning-path` - Generate learning roadmap
- `POST /api/gemini/industry-insights` - Get industry insights

### Mock Interview Endpoints
- `GET /api/interview/test-connection` - Test API connection
- `POST /api/interview/start-session` - Start new interview session
- `POST /api/interview/submit-answer` - Submit interview answer
- `GET /api/interview/history/<user_id>` - Get interview history
- `GET /api/interview/session/<session_id>` - Get session details

### Assessment Endpoints
- `POST /api/assessment/start` - Start skill assessment
- `POST /api/assessment/submit` - Submit assessment answer
- `GET /api/assessment/history/<user_id>` - Get assessment history
- `GET /api/assessment/insights/<user_id>` - Get skill insights

### Resume Generation
- `POST /api/generate-resume` - Generate PDF resume
- `GET /downloads/<filename>` - Download generated files

## Database Schema

The system uses SQLite with the following tables:
- `skills`: Available skills with categories and descriptions
- `careers`: Career information with required skills and market data

## Modules

### Skill Mapping Engine (`modules/skill_mapping.py`)
- Analyzes student skills against available skill database
- Identifies skill gaps and strengths
- Recommends skills to develop

### Job Market Analysis (`modules/job_market_analysis.py`)
- Analyzes current job market trends
- Provides industry-specific insights
- Calculates opportunity scores

### Career Recommender (`modules/career_recommender.py`)
- Generates personalized career recommendations
- Calculates compatibility scores
- Suggests career progression paths

### Learning Plan Generator (`modules/learning_planner.py`)
- Creates personalized learning timelines
- Recommends courses and certifications
- Suggests portfolio projects

### Resume Preparation (`modules/resume_prep.py`)
- Provides resume templates and optimization tips
- Generates interview questions
- Offers networking guidance

## Customization

### Adding New Skills
1. Add skills to the database using the SQLite interface
2. Update the skill categories and descriptions
3. Modify the skill mapping logic if needed

### Adding New Careers
1. Insert career data into the `careers` table
2. Update the career recommendation logic
3. Add industry-specific templates

### Customizing Learning Plans
1. Modify the course database in `learning_planner.py`
2. Update certification recommendations
3. Add new project suggestions

## 📦 Deployment

### Deploy to Heroku
```bash
heroku create your-app-name
heroku config:set GEMINI_API_KEY=your_key
heroku config:set GEMINI_INTERVIEW_API_KEY=your_key
git push heroku main
```

### Deploy to Render
1. Connect GitHub repository
2. Set build command: `pip install -r requirements.txt`
3. Set start command: `python app.py`
4. Add environment variables in dashboard

### Deploy to Vercel (Serverless)
```bash
vercel --prod
```
Configure environment variables in Vercel dashboard.

See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for detailed deployment instructions.

## 📚 Documentation

- [QUICK_START.md](QUICK_START.md) - Quick start guide
- [FEATURES_STATUS.md](FEATURES_STATUS.md) - Complete feature list and status
- [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) - Detailed deployment instructions
- [ALL_FEATURES_RUNNABLE.md](ALL_FEATURES_RUNNABLE.md) - Feature verification summary

## 🧪 Testing

Run the comprehensive test suite:
```bash
python test_features.py
```

Expected output:
```
✓ Imports: PASS
✓ API Keys: PASS
✓ Directories: PASS
✓ Database: PASS
✓ Module Initialization: PASS
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 💡 Support

For support and questions:
- Open an issue in the repository
- Check existing documentation
- Review the FAQ section

## 🌟 Acknowledgments

- Powered by Google Gemini AI
- Built with Flask and Python
- Uses scikit-learn for ML features

## 📊 Project Status

✅ All features fully operational
✅ Ready for deployment
✅ Production-ready code
✅ Comprehensive documentation

## 🔮 Future Enhancements

- Multi-language support
- Mobile application
- Advanced analytics dashboard
- Integration with job portals
- Blockchain-based credential verification
- Video interview simulation
- Team collaboration features

- Integration with real job market APIs
- Machine learning model improvements
- Mobile application
- Advanced analytics dashboard
- Integration with learning platforms
- Real-time skill assessment
- Mentorship matching system

