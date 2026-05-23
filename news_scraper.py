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
    def scrape_aljazeera(self):
        print("Scraping Al Jazeera...")
        try:
            self.driver.get("https://www.aljazeera.com")
            time.sleep(3)

            articles = []
            elements = self.driver.find_elements(
                By.CSS_SELECTOR, 'article h3 a'
            )[:10]

            for el in elements:
                try:
                    title = el.text.strip()
                    link = el.get_attribute('href')
                    if title and link:
                        if not link.startswith('http'):
                            link = 'https://www.aljazeera.com' + link
                        articles.append({'title': title, 'link': link, 'summary': ''})
                        if len(articles) >= 5:
                            break
                except Exception:
                    continue

            self.all_news['Al Jazeera'] = articles
            print(f"  Al Jazeera: Found {len(articles)} articles")
        except Exception as e:
            print(f"  Al Jazeera failed: {e}")
            self.all_news['Al Jazeera'] = []

    # ------------------------------------------------------------------
    # AP News
    # ------------------------------------------------------------------
    def scrape_apnews(self):
        print("Scraping AP News...")
        try:
            self.driver.get("https://apnews.com")
            time.sleep(3)

            articles = []
            selectors = [
                'div.PagePromo-content a.Link',
                'div.FeedCard a.Link',
                'h2 a.Link',
                'h3 a.Link',
            ]
            elements = []
            for sel in selectors:
                elements.extend(self.driver.find_elements(By.CSS_SELECTOR, sel))
                if len(elements) >= 20:
                    break

            seen = set()
            for el in elements:
                try:
                    title = el.text.strip()
                    link = el.get_attribute('href')
                    if title and link and title not in seen and len(title) > 20:
                        seen.add(title)
                        if not link.startswith('http'):
                            link = 'https://apnews.com' + link
                        articles.append({'title': title, 'link': link, 'summary': ''})
                        if len(articles) >= 5:
                            break
                except Exception:
                    continue

            self.all_news['AP News'] = articles
            print(f"  AP News: Found {len(articles)} articles")
        except Exception as e:
            print(f"  AP News failed: {e}")
            self.all_news['AP News'] = []

    # ------------------------------------------------------------------
    # The Express Tribune (Pakistan)
    # ------------------------------------------------------------------
    def scrape_express_tribune(self):
        print("Scraping The Express Tribune...")
        try:
            self.driver.get("https://tribune.com.pk")
            time.sleep(3)

            articles = []
            selectors = [
                'h2 a',
                'h3 a',
                '.story-title a',
                '.card-title a',
                'article h2 a',
                'article h3 a'
            ]
            elements = []
            for sel in selectors:
                elements.extend(self.driver.find_elements(By.CSS_SELECTOR, sel))
                if len(elements) >= 20:
                    break

            seen = set()
            for el in elements:
                try:
                    title = el.text.strip()
                    link = el.get_attribute('href')
                    if title and link and title not in seen and len(title) > 20:
                        seen.add(title)
                        if not link.startswith('http'):
                            link = 'https://tribune.com.pk' + link
                        articles.append({'title': title, 'link': link, 'summary': ''})
                        if len(articles) >= 5:
                            break
                except Exception:
                    continue

            self.all_news['The Express Tribune'] = articles
            print(f"  The Express Tribune: Found {len(articles)} articles")
        except Exception as e:
            print(f"  The Express Tribune failed: {e}")
            self.all_news['The Express Tribune'] = []

    # ------------------------------------------------------------------
    # Dawn (Pakistan)
    # ------------------------------------------------------------------
    def scrape_dawn(self):
        print("Scraping Dawn...")
        try:
            self.driver.get("https://www.dawn.com")
            time.sleep(3)

            articles = []
            selectors = [
                'h2 a',
                'h3 a',
                '.story__title a',
                '.media__title a',
                'article h2 a',
                'article h3 a'
            ]
            elements = []
            for sel in selectors:
                elements.extend(self.driver.find_elements(By.CSS_SELECTOR, sel))
                if len(elements) >= 20:
                    break

            seen = set()
            for el in elements:
                try:
                    title = el.text.strip()
                    link = el.get_attribute('href')
                    if title and link and title not in seen and len(title) > 20:
                        seen.add(title)
                        if not link.startswith('http'):
                            link = 'https://www.dawn.com' + link
                        articles.append({'title': title, 'link': link, 'summary': ''})
                        if len(articles) >= 5:
                            break
                except Exception:
                    continue

            self.all_news['Dawn'] = articles
            print(f"  Dawn: Found {len(articles)} articles")
        except Exception as e:
            print(f"  Dawn failed: {e}")
            self.all_news['Dawn'] = []

    # ------------------------------------------------------------------
    # NPR News
    # ------------------------------------------------------------------
    def scrape_npr(self):
        print("Scraping NPR News...")
        try:
            self.driver.get("https://www.npr.org/sections/news/")
            time.sleep(3)

            articles = []
            selectors = [
                'h2.title a',
                'h3.title a',
                'article h2 a',
                'article h3 a',
            ]
            elements = []
            for sel in selectors:
                elements.extend(self.driver.find_elements(By.CSS_SELECTOR, sel))
                if len(elements) >= 20:
                    break

            seen = set()
            for el in elements:
                try:
                    title = el.text.strip()
                    link = el.get_attribute('href')
                    if title and link and title not in seen and len(title) > 20:
                        seen.add(title)
                        articles.append({'title': title, 'link': link, 'summary': ''})
                        if len(articles) >= 5:
                            break
                except Exception:
                    continue

            self.all_news['NPR News'] = articles
            print(f"  NPR News: Found {len(articles)} articles")
        except Exception as e:
            print(f"  NPR News failed: {e}")
            self.all_news['NPR News'] = []

    # ------------------------------------------------------------------
    # Orchestration
    # ------------------------------------------------------------------
    def scrape_all(self):
        print("\n  Starting Global News Aggregation...\n")

        self.scrape_bbc()
        self.scrape_cnn()
        self.scrape_aljazeera()
        self.scrape_apnews()
        self.scrape_express_tribune()  # Replaced France 24
        self.scrape_dawn()              # Replaced DW News
        self.scrape_npr()

        print("\n  Scraping Complete!\n")
        return self.all_news

    def save_to_json(self, filename='news_data.json'):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.all_news, f, indent=2, ensure_ascii=False)
        print(f"  Data saved to {filename}")

    def close(self):
        self.driver.quit()


# ------------------------------------------------------------------
# Standalone run
# ------------------------------------------------------------------
