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

