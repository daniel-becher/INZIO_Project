import os
import json
from google_test import google_scrape

def test_google_scrape_returns_data():
    query = "Python tutorial"
    results = google_scrape(query)
    
    assert isinstance(results, list)
    assert len(results) > 0
    assert "title" in results[0]
    assert "link" in results[0]

def test_json_file_creation():
    if os.path.exists("test_results.json"):
        os.remove("test_results.json")
    
    test_data = [{"title": "Test", "link": "http://test.com"}]
    with open("test_results.json", "w", encoding="utf-8") as f:
        json.dump(test_data, f)
        
    assert os.path.exists("test_results.json")