from flask import Flask, render_template, jsonify
import json
import os

from datetime import datetime
import threading
import time
from news_scraper import NewsAggregator

app = Flask(__name__)

# Global variable to store news data
news_cache = {}
last_update = None
is_scraping = False

def scrape_news_background():
    """Background task to scrape news"""
    global news_cache, last_update, is_scraping
    
    is_scraping = True
    print("🔄 Background scraping started...")
    
    try:
        aggregator = NewsAggregator()
        news_data = aggregator.scrape_all()
        aggregator.save_to_json()
        aggregator.close()
        
        news_cache = news_data
        last_update = datetime.now()
        print("✅ Background scraping completed!")
        
    except Exception as e:
        print(f"❌ Background scraping failed: {str(e)}")
    finally:
        is_scraping = False

def load_cached_data():
    """Load cached news data from JSON file"""
    global news_cache, last_update
    
    if os.path.exists('news_data.json'):
        try:
            with open('news_data.json', 'r', encoding='utf-8') as f:
                news_cache = json.load(f)
            # Get file modification time
            last_update = datetime.fromtimestamp(os.path.getmtime('news_data.json'))
            print("✅ Loaded cached news data")
        except Exception as e:
            print(f"⚠️ Could not load cached data: {e}")

@app.route('/')
def index():
    """Serve the main page"""
    return render_template('index.html')

@app.route('/api/news')
def get_news():
    """API endpoint to get news data"""
    return jsonify({
        'data': news_cache,
        'last_update': last_update.strftime('%Y-%m-%d %H:%M:%S') if last_update else None,
        'is_scraping': is_scraping
    })

@app.route('/api/refresh')
def refresh_news():
    """API endpoint to trigger news refresh"""
    global is_scraping
    
    if is_scraping:
        return jsonify({'status': 'already_scraping'})
    
    # Start scraping in background thread
    thread = threading.Thread(target=scrape_news_background)
    thread.daemon = True
    thread.start()
    
    return jsonify({'status': 'scraping_started'})
