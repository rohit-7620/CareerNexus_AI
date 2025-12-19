"""
Test script to verify all features are runnable
"""
import sys
import os

def test_imports():
    """Test that all modules can be imported"""
    print("Testing module imports...")
    try:
        from modules.skill_mapping import SkillMappingEngine
        from modules.job_market_analysis import JobMarketAnalyzer
        from modules.career_recommender import CareerRecommender
        from modules.learning_planner import LearningPlanGenerator
        from modules.resume_prep import ResumePreparation
        from modules.ai_skill_assessment import AISkillAssessment
        from modules.ai_interview_prep import AIInterviewPreparation
        from modules.gemini_ai_engine import GeminiAIEngine
        from modules.advanced_mock_interview import AdvancedMockInterview
        print("✓ All modules imported successfully")
        return True
    except Exception as e:
        print(f"✗ Import error: {e}")
        return False

def test_module_initialization():
    """Test that all modules can be initialized"""
    print("\nTesting module initialization...")
    try:
        from modules.skill_mapping import SkillMappingEngine
        from modules.job_market_analysis import JobMarketAnalyzer
        from modules.career_recommender import CareerRecommender
        from modules.learning_planner import LearningPlanGenerator
        from modules.resume_prep import ResumePreparation
        from modules.ai_skill_assessment import AISkillAssessment
        from modules.ai_interview_prep import AIInterviewPreparation
        from modules.gemini_ai_engine import GeminiAIEngine
        from modules.advanced_mock_interview import AdvancedMockInterview
        
        skill_mapper = SkillMappingEngine()
        print("  ✓ SkillMappingEngine initialized")
        
        job_analyzer = JobMarketAnalyzer()
        print("  ✓ JobMarketAnalyzer initialized")
        
        career_recommender = CareerRecommender()
        print("  ✓ CareerRecommender initialized")
        
        learning_planner = LearningPlanGenerator()
        print("  ✓ LearningPlanGenerator initialized")
        
        resume_prep = ResumePreparation()
        print("  ✓ ResumePreparation initialized")
        
        ai_assessment = AISkillAssessment()
        print("  ✓ AISkillAssessment initialized")
        
        ai_interview = AIInterviewPreparation()
        print("  ✓ AIInterviewPreparation initialized")
        
        gemini_engine = GeminiAIEngine()
        print("  ✓ GeminiAIEngine initialized")
        
        mock_interview = AdvancedMockInterview()
        print("  ✓ AdvancedMockInterview initialized")
        
        print("✓ All modules initialized successfully")
        return True
    except Exception as e:
        print(f"✗ Initialization error: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_database():
    """Test database initialization"""
    print("\nTesting database...")
    try:
        from app import init_database
        init_database()
        print("✓ Database initialized successfully")
        
        # Check if tables exist
        import sqlite3
        conn = sqlite3.connect('career_advisor.db')
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cursor.fetchall()
        print(f"  Found {len(tables)} tables: {[t[0] for t in tables]}")
        conn.close()
        return True
    except Exception as e:
        print(f"✗ Database error: {e}")
        return False

def test_api_keys():
    """Test that API keys are loaded"""
    print("\nTesting API keys...")
    try:
        from dotenv import load_dotenv
        load_dotenv()
        
        api_key = os.getenv('GEMINI_API_KEY')
        interview_key = os.getenv('GEMINI_INTERVIEW_API_KEY')
        
        if api_key:
            print(f"  ✓ GEMINI_API_KEY loaded: {api_key[:20]}...")
        else:
            print("  ✗ GEMINI_API_KEY not found")
            
        if interview_key:
            print(f"  ✓ GEMINI_INTERVIEW_API_KEY loaded: {interview_key[:20]}...")
        else:
            print("  ✗ GEMINI_INTERVIEW_API_KEY not found")
            
        return bool(api_key and interview_key)
    except Exception as e:
        print(f"✗ API key error: {e}")
        return False

def test_directories():
    """Test that necessary directories exist"""
    print("\nTesting directories...")
    try:
        dirs = ['downloads', 'uploads', 'modules', 'templates']
        for d in dirs:
            if os.path.exists(d):
                print(f"  ✓ {d}/ exists")
            else:
                print(f"  ✗ {d}/ missing")
                os.makedirs(d, exist_ok=True)
                print(f"    Created {d}/")
        return True
    except Exception as e:
        print(f"✗ Directory error: {e}")
        return False

def main():
    print("="*70)
    print("AI Career Advisor - Feature Test Suite")
    print("="*70)
    
    results = []
    
    results.append(("Imports", test_imports()))
    results.append(("API Keys", test_api_keys()))
    results.append(("Directories", test_directories()))
    results.append(("Database", test_database()))
    results.append(("Module Initialization", test_module_initialization()))
    
    print("\n" + "="*70)
    print("Test Results Summary")
    print("="*70)
    
    for test_name, passed in results:
        status = "PASS" if passed else "FAIL"
        symbol = "✓" if passed else "✗"
        print(f"{symbol} {test_name}: {status}")
    
    all_passed = all(r[1] for r in results)
    
    print("="*70)
    if all_passed:
        print("SUCCESS: All features are runnable!")
        print("\nYou can now start the application with:")
        print("  python app.py")
        print("\nOr run it with:")
        print("  flask run")
    else:
        print("FAILURE: Some features have issues. Please check the errors above.")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
