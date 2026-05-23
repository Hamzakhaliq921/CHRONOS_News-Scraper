# 📰 Chronos News Aggregator

![Python](https://img.shields.io/badge/python-3.8+-blue) ![Flask](https://img.shields.io/badge/flask-2.3.3-lightgrey) ![Selenium](https://img.shields.io/badge/selenium-4.15.0-green) ![License](https://img.shields.io/badge/license-MIT-yellow)

A real-time news aggregation web app that scrapes headlines from 7 global sources using Selenium and serves them through a clean, responsive UI.

---

## Features

- Scrapes live headlines from 7 news sources using Selenium
- Auto-refreshes every 15 minutes in the background
- Responsive UI — works on desktop, tablet, and mobile
- REST API for programmatic access
- Caches data locally to reduce load times
- XSS-safe HTML escaping

---

## News Sources

| Source | Country | Focus |
|--------|---------|-------|
| BBC News | UK | World news, politics |
| CNN | USA | Breaking news, US affairs |
| Al Jazeera | Qatar | Middle East, global |
| AP News | USA | Factual wire reporting |
| The New York Times | USA | In-depth journalism |
| Dawn | Pakistan | Pakistani & regional news |
| NPR News | USA | Public radio, culture |

---

## Quick Start

**Requirements:** Python 3.8+, Google Chrome

```bash
git clone https://github.com/yourusername/chronos-news-aggregator.git
cd chronos-news-aggregator
pip install -r requirements.txt
python app.py
```

Then open `http://127.0.0.1:5000` in your browser.

> **Windows users:** You can also double-click `start.bat` — it handles setup automatically.  
> **Mac/Linux users:** Run `./start.sh`

---

## Project Structure

```
chronos-news-aggregator/
├── app.py               # Flask server & API endpoints
├── news_scraper.py      # Selenium scraping logic
├── requirements.txt
├── start.bat / start.sh
├── templates/
│   └── index.html
├── static/
│   ├── css/style.css
│   └── js/app.js
└── news_data.json       # Auto-generated cache
```

---

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Main UI |
| `/api/news` | GET | Returns current news data |
| `/api/refresh` | GET | Triggers a fresh scrape |

**Example response from `/api/news`:**
```json
{
  "data": {
    "BBC News": [
      { "title": "Article headline", "link": "https://bbc.com/...", "summary": "" }
    ]
  },
  "last_update": "2024-01-15 14:30:00",
  "is_scraping": false
}
```

---

## Customization

**Change refresh interval** — in `static/js/app.js`:
```javascript
setInterval(() => { refreshNews(); }, 15 * 60 * 1000); // change 15 to desired minutes
```

**Change articles per source** — in `news_scraper.py`:
```python
if len(articles) >= 5:  # change 5 to desired number
    break
```

**Change port** — in `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5000)  # change 5000
```

---

## Troubleshooting

**No news showing?** Wait ~60 seconds for the initial scrape to complete. If it still fails, delete `news_data.json` and restart.

**ChromeDriver error?** Selenium 4.x manages ChromeDriver automatically — just make sure Chrome is up to date.

**Port 5000 in use?**
```bash
# Mac/Linux
lsof -i:5000 && kill -9 <PID>

# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

**Python not found?** Use `python3` on macOS/Linux. On Windows, ensure Python is added to PATH during installation.

---

## Tech Stack

**Backend:** Python, Flask, Selenium  
**Frontend:** HTML5, CSS3 (Grid/Flexbox), Vanilla JS  
**Fonts:** Crimson Pro, Darker Grotesque (Google Fonts)

---

## License

MIT — see [LICENSE](LICENSE) for details.

---

> **Note:** This project is for educational purposes. Please respect each website's `robots.txt` and terms of service.