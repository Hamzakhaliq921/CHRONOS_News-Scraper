from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import json
import time
import os


class NewsAggregator:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_argument(
            'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        )
        self.driver = webdriver.Chrome(options=chrome_options)
        self.all_news = {}

    # ------------------------------------------------------------------
    # BBC News
    # ------------------------------------------------------------------
    

    # ------------------------------------------------------------------
    # Al Jazeera
    # ------------------------------------------------------------------
   

    # ------------------------------------------------------------------
    # Dawn (Pakistan)
    # ------------------------------------------------------------------
   
    # ------------------------------------------------------------------
    # NPR News
    # ------------------------------------------------------------------
  
# ------------------------------------------------------------------
# Standalone run
# ------------------------------------------------------------------
