# 🚀 GitHub Deployment Guide

## Step-by-Step Guide to Push to GitHub

### Step 1: Verify Git Status

Check what files will be committed:
```bash
git status
```

### Step 2: Add Files to Staging

Add all modified and new files:
```bash
git add .
```

**Important**: The `.env` file with your API keys is automatically excluded by `.gitignore` and will NOT be committed. This is intentional for security.

### Step 3: Commit Changes

Create a commit with a descriptive message:
```bash
git commit -m "feat: Make all features runnable - Add dependencies, fix encoding, create deployment files"
```

Or for a more detailed commit:
```bash
git commit -m "feat: Complete deployment preparation

- Add missing dependencies (scikit-learn, numpy, reportlab)
- Fix Windows encoding issues in app.py
- Create deployment files (Procfile, runtime.txt)
- Add comprehensive documentation
- Create test suite for feature verification
- Add GitHub Actions CI/CD pipeline
- Update README with deployment instructions"
```

### Step 4: Push to GitHub

If this is your first push to a new repository:
```bash
# Create a new repository on GitHub first, then:
git remote add origin https://github.com/YOUR_USERNAME/ai-career-advisor.git
git branch -M main
git push -u origin main
```

If you already have a remote configured:
```bash
git push origin main
```

Or if your branch is named differently:
```bash
git push origin master
```

### Step 5: Set Up GitHub Secrets (for CI/CD)

1. Go to your GitHub repository
2. Click on **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Add these secrets:
   - Name: `GEMINI_API_KEY`, Value: Your Gemini API key
   - Name: `GEMINI_INTERVIEW_API_KEY`, Value: Your Interview API key

### Step 6: Verify GitHub Actions

After pushing:
1. Go to the **Actions** tab in your repository
2. Check that the CI/CD pipeline runs successfully
3. All tests should pass ✓

## Files Being Committed

### New Files
- ✅ `test_features.py` - Comprehensive test suite
- ✅ `start.ps1` - Windows startup script
- ✅ `start.sh` - Linux/Mac startup script
- ✅ `Procfile` - Heroku deployment config
- ✅ `runtime.txt` - Python version specification
- ✅ `.env.example` - Template for environment variables
- ✅ `DEPLOYMENT_GUIDE.md` - Detailed deployment instructions
- ✅ `FEATURES_STATUS.md` - Feature status documentation
- ✅ `QUICK_START.md` - Quick start guide
- ✅ `ALL_FEATURES_RUNNABLE.md` - Feature summary
- ✅ `GITHUB_DEPLOYMENT.md` - This file
- ✅ `.github/workflows/ci-cd.yml` - CI/CD pipeline

### Modified Files
- ✅ `requirements.txt` - Added missing dependencies
- ✅ `app.py` - Fixed encoding issues
- ✅ `README.md` - Updated with new features and instructions

### Protected Files (NOT committed)
- 🔒 `.env` - Contains your API keys (excluded by .gitignore)
- 🔒 `career_advisor.db` - Database file (excluded by .gitignore)
- 🔒 `.venv/` - Virtual environment (excluded by .gitignore)
- 🔒 `__pycache__/` - Python cache (excluded by .gitignore)
- 🔒 `downloads/` - Generated files (excluded by .gitignore)
- 🔒 `uploads/` - User uploads (excluded by .gitignore)

## Common Git Commands

### Check current status
```bash
git status
```

### View changes
```bash
git diff
```

### View commit history
```bash
git log --oneline
```

### Create a new branch
```bash
git checkout -b feature/new-feature
```

### Switch branches
```bash
git checkout main
```

### Pull latest changes
```bash
git pull origin main
```

### Discard local changes
```bash
git checkout -- filename.py
```

### Undo last commit (keep changes)
```bash
git reset --soft HEAD~1
```

## Deployment After Push

### Option 1: Deploy to Heroku
```bash
# Install Heroku CLI first, then:
heroku login
heroku create your-app-name
heroku config:set GEMINI_API_KEY=your_key
heroku config:set GEMINI_INTERVIEW_API_KEY=your_key
git push heroku main
heroku open
```

### Option 2: Deploy to Render
1. Go to [render.com](https://render.com)
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
5. Add environment variables:
   - `GEMINI_API_KEY`
   - `GEMINI_INTERVIEW_API_KEY`
6. Click "Create Web Service"

### Option 3: Deploy to Railway
1. Go to [railway.app](https://railway.app)
2. Click "New Project" → "Deploy from GitHub repo"
3. Select your repository
4. Add environment variables in Settings
5. Railway auto-deploys!

### Option 4: Deploy to Vercel
```bash
# Install Vercel CLI
npm install -g vercel

# Deploy
vercel --prod
```

Add environment variables in Vercel dashboard.

## Troubleshooting

### Issue: Git push rejected
**Solution**: Pull latest changes first
```bash
git pull origin main --rebase
git push origin main
```

### Issue: Large files rejected
**Solution**: Check .gitignore and remove large files
```bash
git rm --cached large_file.db
git commit -m "Remove large file"
```

### Issue: Merge conflicts
**Solution**: Resolve conflicts manually
```bash
git status  # See conflicting files
# Edit files to resolve conflicts
git add .
git commit -m "Resolve merge conflicts"
```

### Issue: Wrong commit message
**Solution**: Amend the commit
```bash
git commit --amend -m "New commit message"
git push origin main --force  # Only if not pushed yet
```

## Security Checklist

Before pushing, verify:
- ✅ `.env` is in `.gitignore`
- ✅ No API keys in code
- ✅ No sensitive data in repository
- ✅ Database files excluded
- ✅ `.env.example` has placeholder values only

## Post-Deployment

After successful deployment:
1. ✅ Test all API endpoints
2. ✅ Verify database initialization
3. ✅ Check environment variables
4. ✅ Monitor application logs
5. ✅ Test Gemini AI features
6. ✅ Verify file uploads/downloads

## Need Help?

- GitHub: [GitHub Docs](https://docs.github.com)
- Heroku: [Heroku Dev Center](https://devcenter.heroku.com)
- Render: [Render Docs](https://render.com/docs)
- Railway: [Railway Docs](https://docs.railway.app)

---

**Ready to deploy!** 🚀

For detailed deployment instructions, see [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)
