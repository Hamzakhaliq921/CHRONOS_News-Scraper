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
