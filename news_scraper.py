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
    def scrape_bbc(self):
        print("Scraping BBC News...")
        try:
            self.driver.get("https://www.bbc.com/news")
            time.sleep(3)

            articles = []
            elements = self.driver.find_elements(
                By.CSS_SELECTOR, 'a[data-testid="internal-link"]'
            )[:20]

            seen = set()
            for el in elements:
                try:
                    title = (el.get_attribute('aria-label') or el.text).strip()
                    link = el.get_attribute('href')
                    if title and link and title not in seen and len(title) > 20:
                        seen.add(title)
                        articles.append({'title': title, 'link': link, 'summary': ''})
                        if len(articles) >= 5:
                            break
                except Exception:
                    continue

            self.all_news['BBC News'] = articles
            print(f"  BBC: Found {len(articles)} articles")
        except Exception as e:
            print(f"  BBC failed: {e}")
            self.all_news['BBC News'] = []

    # ------------------------------------------------------------------
    # CNN
    # ------------------------------------------------------------------
    def scrape_cnn(self):
        print("Scraping CNN...")
        try:
            self.driver.get("https://www.cnn.com")
            time.sleep(3)

            articles = []
            elements = self.driver.find_elements(
                By.CSS_SELECTOR, 'a.container__link, a.ci-card__link'
            )[:20]

            seen = set()
            for el in elements:
                try:
                    title = el.text.strip()
                    link = el.get_attribute('href')
                    if title and link and title not in seen and len(title) > 15:
                        seen.add(title)
                        articles.append({'title': title, 'link': link, 'summary': ''})
                        if len(articles) >= 5:
                            break
                except Exception:
                    continue

            self.all_news['CNN'] = articles
            print(f"  CNN: Found {len(articles)} articles")
        except Exception as e:
            print(f"  CNN failed: {e}")
            self.all_news['CNN'] = []

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
