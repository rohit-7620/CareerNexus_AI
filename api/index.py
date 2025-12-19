"""
Vercel Serverless Function for CareerNexus API
This module imports and wraps the Flask app routes for serverless deployment
"""
import os
import sys
from pathlib import Path

# Add parent directory to path to import modules
current_dir = Path(__file__).parent
parent_dir = current_dir.parent
sys.path.insert(0, str(parent_dir))

from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import AI modules
from modules.gemini_ai_engine import GeminiAIEngine

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Initialize Gemini AI Engine
try:
    gemini_engine = GeminiAIEngine()
    print("✓ Gemini AI Engine initialized successfully")
except Exception as e:
    print(f"✗ Failed to initialize Gemini AI Engine: {str(e)}")
    gemini_engine = None

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'gemini_initialized': gemini_engine is not None,
        'api_key_set': bool(os.getenv('GEMINI_API_KEY'))
    })

@app.route('/api/gemini/ats-resume', methods=['POST'])
def ats_resume():
    try:
        if not gemini_engine:
            return jsonify({
                'success': False, 
                'error': 'Gemini AI Engine not initialized. Check API keys in environment variables.'
            }), 500
            
        data = request.json
        if not data:
            return jsonify({'success': False, 'error': 'No data provided'}), 400
            
        user_data = {
            'name': data.get('name'),
            'email': data.get('email'),
            'phone': data.get('phone'),
            'target_role': data.get('target_role'),
            'years_experience': data.get('years_experience'),
            'skills': data.get('skills', []),
            'education': data.get('education'),
            'experience': data.get('experience'),
            'achievements': data.get('achievements')
        }
        result = gemini_engine.generate_ats_optimized_resume(user_data)
        return jsonify(result)
    except Exception as e:
        import traceback
        error_details = traceback.format_exc()
        print(f"Error in ats_resume: {error_details}")
        return jsonify({
            'success': False, 
            'error': str(e),
            'details': 'Check server logs for more information'
        }), 500

@app.route('/api/gemini/cover-letter', methods=['POST'])
def cover_letter():
    try:
        data = request.json
        user_data = data.get('user_profile', {})
        job_description = data.get('job_description', '')
        result = gemini_engine.generate_personalized_cover_letter(user_data, job_description)
        return jsonify({'success': True, 'cover_letter': result})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/gemini/linkedin-optimizer', methods=['POST'])
def linkedin_optimizer():
    try:
        data = request.json
        profile_data = data.get('current_profile', {})
        result = gemini_engine.analyze_linkedin_profile(profile_data)
        return jsonify(result)
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/gemini/mock-interview', methods=['POST'])
def mock_interview():
    try:
        data = request.json
        role = data.get('role', 'Software Engineer')
        difficulty = data.get('difficulty', 'medium')
        question_number = data.get('question_number', 1)
        result = gemini_engine.conduct_mock_interview(role, difficulty, question_number)
        return jsonify(result)
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/gemini/evaluate-answer', methods=['POST'])
def evaluate_answer():
    try:
        data = request.json
        question = data.get('question', '')
        answer = data.get('answer', '')
        role = data.get('role', '')
        result = gemini_engine.evaluate_interview_answer(question, answer, role)
        return jsonify(result)
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/gemini/career-trajectory', methods=['POST'])
def career_trajectory():
    try:
        data = request.json
        user_profile = data.get('user_profile', {})
        result = gemini_engine.predict_career_trajectory(user_profile)
        return jsonify(result)
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/gemini/skill-gap', methods=['POST'])
def skill_gap():
    try:
        data = request.json
        current_skills = data.get('current_skills', [])
        target_role = data.get('target_role', '')
        result = gemini_engine.analyze_skill_gaps(current_skills, target_role)
        return jsonify(result)
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/gemini/salary-negotiation', methods=['POST'])
def salary_negotiation():
    try:
        data = request.json
        user_data = data.get('user_profile', {})
        job_offer = data.get('job_offer', {})
        result = gemini_engine.generate_salary_negotiation_strategy(user_data, job_offer)
        return jsonify(result)
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/gemini/job-analysis', methods=['POST'])
def job_analysis():
    try:
        data = request.json
        job_description = data.get('job_description', '')
        result = gemini_engine.analyze_job_description(job_description)
        return jsonify(result)
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/gemini/learning-path', methods=['POST'])
def learning_path():
    try:
        data = request.json
        user_profile = data.get('user_profile', {})
        goal = data.get('goal', '')
        result = gemini_engine.generate_personalized_learning_path(user_profile, goal)
        return jsonify(result)
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

# Export app for Vercel - this is the WSGI application
application = app
