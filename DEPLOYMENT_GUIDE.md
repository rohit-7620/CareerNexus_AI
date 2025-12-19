# 🚀 AI Career Advisor - Deployment Guide

## Prerequisites

- Python 3.8+
- Git
- GitHub account
- Google Gemini API keys (get from [Google AI Studio](https://makersuite.google.com/app/apikey))

## Step 1: Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/career-advisor.git
cd career-advisor
```

## Step 2: Set Up Environment

### Create Virtual Environment
```bash
python -m venv .venv
```

### Activate Virtual Environment

**Windows PowerShell:**
```powershell
.\.venv\Scripts\Activate.ps1
```

**Windows CMD:**
```cmd
.venv\Scripts\activate.bat
```

**Linux/Mac:**
```bash
source .venv/bin/activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

## Step 3: Configure Environment Variables

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and add your API keys:
   ```
   GEMINI_API_KEY=your_actual_gemini_api_key
   GEMINI_INTERVIEW_API_KEY=your_actual_interview_api_key
   ```

   Get your API keys from: https://makersuite.google.com/app/apikey

## Step 4: Test Installation

Run the test suite to verify everything is set up correctly:
```bash
python test_features.py
```

All tests should pass ✓

## Step 5: Run the Application

### Development Mode
```bash
python app.py
```

Or use the startup script:
```bash
.\start.ps1  # Windows
./start.sh   # Linux/Mac
```

The server will start at: http://localhost:5000

## Deployment Options

### Option 1: Heroku Deployment

1. Install Heroku CLI
2. Create `Procfile`:
   ```
   web: gunicorn app:app
   ```
3. Add gunicorn to requirements.txt:
   ```bash
   pip install gunicorn
   pip freeze > requirements.txt
   ```
4. Deploy:
   ```bash
   heroku create your-app-name
   heroku config:set GEMINI_API_KEY=your_key
   heroku config:set GEMINI_INTERVIEW_API_KEY=your_key
   git push heroku main
   ```

### Option 2: Render Deployment

1. Go to [Render](https://render.com)
2. Connect your GitHub repository
3. Create a new Web Service
4. Set build command: `pip install -r requirements.txt`
5. Set start command: `gunicorn app:app`
6. Add environment variables in Render dashboard:
   - `GEMINI_API_KEY`
   - `GEMINI_INTERVIEW_API_KEY`
7. Deploy!

### Option 3: Railway Deployment

1. Go to [Railway](https://railway.app)
2. Connect your GitHub repository
3. Add environment variables:
   - `GEMINI_API_KEY`
   - `GEMINI_INTERVIEW_API_KEY`
4. Railway auto-detects Python and deploys

### Option 4: Google Cloud Run

1. Install Google Cloud SDK
2. Create `Dockerfile`:
   ```dockerfile
   FROM python:3.11-slim
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   COPY . .
   CMD ["python", "app.py"]
   ```
3. Deploy:
   ```bash
   gcloud run deploy career-advisor --source .
   ```

### Option 5: Vercel (Serverless)

Already configured! Use existing `vercel.json`:
```bash
vercel --prod
```

Set environment variables in Vercel dashboard.

## Environment Variables Required

All deployment platforms need these environment variables:

- `GEMINI_API_KEY` - Your Google Gemini API key
- `GEMINI_INTERVIEW_API_KEY` - Your Gemini Interview API key

## Production Considerations

### Security
- ✅ API keys are in `.env` (excluded from git)
- ✅ CORS is enabled (configure for production domain)
- ⚠️ Change Flask debug mode to False (already done)
- ⚠️ Use HTTPS in production
- ⚠️ Set up rate limiting for API endpoints

### Database
- Current: SQLite (file-based)
- Production: Consider PostgreSQL or MySQL for better concurrency
- Cloud options: Supabase, PlanetScale, or cloud provider databases

### Performance
- Add caching for API responses (Redis)
- Use a production WSGI server (gunicorn/waitress)
- Set up CDN for static files
- Configure logging and monitoring

### Scaling
- Use environment-based configuration
- Separate database server
- Load balancer for multiple instances
- Queue system for heavy operations (Celery + Redis)

## Troubleshooting

### Import Errors
```bash
pip install -r requirements.txt --upgrade
```

### Database Errors
Delete and recreate database:
```bash
rm career_advisor.db
python app.py  # Will recreate on startup
```

### API Key Errors
- Verify keys are in `.env` file
- Check keys are valid at Google AI Studio
- Ensure `.env` is not in `.gitignore` (it should be!)

### Port Already in Use
Change port in `app.py`:
```python
app.run(debug=False, host='0.0.0.0', port=5001)
```

## Monitoring

### Health Check Endpoint
Add to your deployment:
```python
@app.route('/health')
def health():
    return {'status': 'healthy', 'timestamp': datetime.now().isoformat()}
```

### Logs
- Check application logs in deployment platform
- Set up error tracking (Sentry, Rollbar)
- Monitor API usage and quotas

## Support

For issues or questions:
- Check [FEATURES_STATUS.md](FEATURES_STATUS.md)
- Check [QUICK_START.md](QUICK_START.md)
- Review [README.md](README.md)

## License

[Your License Here]

---

**Happy Deploying!** 🚀
