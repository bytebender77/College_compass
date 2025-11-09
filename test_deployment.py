#!/usr/bin/env python3
"""
Test script to verify the application is ready for Render deployment.
Tests backend API endpoints and configuration.
"""

import sys
import os
from pathlib import Path

def test_imports():
    """Test if all required modules can be imported."""
    print("🔍 Testing imports...")
    try:
        from app import app
        from src.retriever import answer_question
        from fastapi.testclient import TestClient
        print("✅ All imports successful")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_health_endpoint():
    """Test the health check endpoint."""
    print("\n🔍 Testing health endpoint...")
    try:
        from app import app
        from fastapi.testclient import TestClient
        client = TestClient(app)
        response = client.get("/")
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "healthy":
                print("✅ Health endpoint working correctly")
                print(f"   Response: {data}")
                return True
            else:
                print(f"❌ Unexpected response: {data}")
                return False
        else:
            print(f"❌ Health endpoint returned status {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Health endpoint test failed: {e}")
        return False

def test_api_endpoint():
    """Test the API answer endpoint."""
    print("\n🔍 Testing API answer endpoint...")
    try:
        from app import app
        from fastapi.testclient import TestClient
        client = TestClient(app)
        
        # Test with a simple question
        test_question = "What are the hostel rules?"
        response = client.post("/api/answer", json={"question": test_question})
        
        if response.status_code == 200:
            data = response.json()
            if "answer" in data and "sources" in data:
                print("✅ API endpoint working correctly")
                print(f"   Answer length: {len(data['answer'])} characters")
                print(f"   Sources count: {len(data['sources'])}")
                return True
            else:
                print(f"❌ Missing required fields in response: {data.keys()}")
                return False
        else:
            print(f"❌ API endpoint returned status {response.status_code}")
            print(f"   Response: {response.text}")
            return False
    except Exception as e:
        print(f"❌ API endpoint test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_faiss_index():
    """Test if FAISS index exists."""
    print("\n🔍 Testing FAISS index...")
    faiss_dir = Path("faiss_index")
    required_files = ["index.faiss", "index.pkl", "meta.pkl"]
    
    if not faiss_dir.exists():
        print("❌ FAISS index directory not found")
        return False
    
    missing_files = []
    for file in required_files:
        if not (faiss_dir / file).exists():
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Missing FAISS index files: {missing_files}")
        return False
    
    print("✅ FAISS index files present")
    return True

def test_environment_variables():
    """Test if required environment variables are set."""
    print("\n🔍 Testing environment variables...")
    hf_token = os.getenv("HF_TOKEN")
    
    if not hf_token:
        print("⚠️  HF_TOKEN not set (will be required in production)")
        return False
    
    print("✅ HF_TOKEN is set")
    return True

def test_requirements():
    """Test if requirements.txt exists and is readable."""
    print("\n🔍 Testing requirements.txt...")
    req_file = Path("requirements.txt")
    
    if not req_file.exists():
        print("❌ requirements.txt not found")
        return False
    
    with open(req_file) as f:
        lines = f.readlines()
        if len(lines) < 5:
            print("⚠️  requirements.txt seems incomplete")
            return False
    
    print("✅ requirements.txt exists and looks valid")
    return True

def main():
    """Run all tests."""
    print("=" * 60)
    print("🧪 Testing Campus Compass for Render Deployment")
    print("=" * 60)
    
    tests = [
        ("Imports", test_imports),
        ("Requirements", test_requirements),
        ("FAISS Index", test_faiss_index),
        ("Environment Variables", test_environment_variables),
        ("Health Endpoint", test_health_endpoint),
        ("API Endpoint", test_api_endpoint),
    ]
    
    results = []
    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, result))
        except Exception as e:
            print(f"❌ Test '{name}' crashed: {e}")
            results.append((name, False))
    
    print("\n" + "=" * 60)
    print("📊 Test Results Summary")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status}: {name}")
    
    print(f"\nTotal: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 All tests passed! Application is ready for deployment.")
        return 0
    else:
        print(f"\n⚠️  {total - passed} test(s) failed. Please fix issues before deploying.")
        return 1

if __name__ == "__main__":
    sys.exit(main())

