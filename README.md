# 📰 Chronos News Aggregator

A beautiful, Selenium-powered web application that aggregates news from multiple trusted global sources and presents them in an elegant, user-friendly interface.

## ✨ Features

- **Multi-Source Aggregation**: Pulls latest news from 5 major sources:
  - BBC News
  - Reuters
  - CNN
  - The Guardian
  - Al Jazeera

- **Clean, Distinctive UI**: 
  - Custom color palette (Sage Green, Off-White, Deep Charcoal)
  - Sophisticated typography (Darker Grotesque + Crimson Pro)
  - Smooth animations and transitions
  - Responsive design for all devices

- **Real-time Updates**: 
  - Manual refresh button
  - Auto-refresh every 15 minutes
  - Background scraping without blocking UI

- **Smart Caching**: Stores scraped data in JSON for quick loading

## 🎨 Design Philosophy

**Color System:**
- Background: Light Grey-Green (#E8EDE6)
- Cards: Off-White (#F5F5F0)
- Accent: Sage Green (#8A9A7C)
- Text: Deep Charcoal (#2D2D2D)

**Gestalt Principles Applied:**
- **Proximity**: Articles grouped by source
- **Similarity**: Consistent card styling
- **Hierarchy**: Clear visual importance (source > headline)
- **Continuity**: Smooth scrolling and transitions

## 🚀 Installation & Setup

### Prerequisites

1. **Python 3.8+**
2. **Google Chrome** (latest version)
3. **ChromeDriver** (will be auto-installed by webdriver-manager)

### Step 1: Clone or Download the Project

```bash
# If you have the files, navigate to the directory
cd /path/to/news-aggregator
```

### Step 2: Install Python Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- Flask (web framework)
- Selenium (web scraping)
- webdriver-manager (automatic ChromeDriver management)

### Step 3: Run the Application

```bash
python app.py
```

You should see:
```
🌐 Starting News Aggregation...

Scraping BBC News...
✓ BBC: Found 5 articles
Scraping Reuters...
✓ Reuters: Found 5 articles
...

🚀 Starting Flask server...
📱 Open http://127.0.0.1:5000 in your browser
```

### Step 4: Open in Browser

Navigate to: **http://127.0.0.1:5000**

## 📁 Project Structure

```
news-aggregator/
│
├── app.py                    # Flask server & API endpoints
├── news_scraper.py          # Selenium scraping logic
├── requirements.txt         # Python dependencies
├── news_data.json          # Cached news data (auto-generated)
│
├── templates/
│   └── index.html          # Main HTML template
│
└── static/
    ├── css/
    │   └── style.css       # Sophisticated styling
    └── js/
        └── app.js          # Frontend JavaScript
```

## 🔧 How It Works

### Backend (Python + Selenium)

1. **news_scraper.py**: 
   - Opens each news website with Selenium
   - Extracts top 5 articles using CSS selectors
   - Returns structured data (title, link, summary)
   
2. **app.py**:
   - Flask server with API endpoints
   - Background scraping in separate thread
   - Caches results in `news_data.json`

### Frontend (HTML + CSS + JavaScript)

1. **index.html**: Clean semantic structure
2. **style.css**: Custom design system with CSS variables
3. **app.js**: Fetches data from API, renders dynamically

## 🔄 API Endpoints

- `GET /` - Main page
- `GET /api/news` - Get cached news data
- `GET /api/refresh` - Trigger new scraping

## ⚙️ Customization

### Add More News Sources

Edit `news_scraper.py`:

```python
def scrape_your_source(self):
    """Scrape Your News Source"""
    print("Scraping Your Source...")
    try:
        self.driver.get("https://yournewssite.com")
        time.sleep(3)
        
        articles = []
        article_elements = self.driver.find_elements(
            By.CSS_SELECTOR, 
            'your-css-selector'
        )[:10]
        
        # Extract data...
        
        self.all_news['Your Source'] = articles
    except Exception as e:
        print(f"✗ Failed: {str(e)}")
        self.all_news['Your Source'] = []
```

Then add to `scrape_all()`:
```python
def scrape_all(self):
    # ... existing sources ...
    self.scrape_your_source()
```

### Change Color Scheme

Edit `static/css/style.css`:

```css
:root {
    --bg-primary: #YourColor;
    --bg-secondary: #YourColor;
    --accent-primary: #YourColor;
    /* etc... */
}
```

### Adjust Scraping Frequency

Edit `static/js/app.js`:

```javascript
// Auto-refresh every X minutes (default: 15)
setInterval(() => {
    if (!AppState.isScraping) {
        refreshNews();
    }
}, 15 * 60 * 1000);  // Change 15 to your desired minutes
```

## 🐛 Troubleshooting

### "ChromeDriver not found"
- The app uses `webdriver-manager` to auto-install ChromeDriver
- Make sure Chrome browser is installed
- First run may be slower as it downloads ChromeDriver

### "No articles found"
- News websites change their HTML structure
- Check `news_scraper.py` and update CSS selectors
- Some sites may block automated access

### Port 5000 already in use
Change port in `app.py`:
```python
app.run(debug=True, port=5001)  # Use different port
```

## 📝 Notes

- **Rate Limiting**: Be respectful of news sites' servers
- **Legal**: This is for educational purposes only
- **Scraping**: Some sites may block automated access
- **Updates**: News site structures change; selectors may need updates

## 🎯 Future Enhancements

- [ ] Search/filter functionality
- [ ] Category filtering (World, Tech, Sports, etc.)
- [ ] Dark mode toggle
- [ ] Export to PDF
- [ ] Email digest
- [ ] User preferences (favorite sources)
- [ ] RSS feed support
- [ ] Mobile app version

## 📄 License

This project is for educational purposes. Respect the terms of service of all news sources.

## 🙏 Credits

**News Sources:**
- BBC News
- Reuters
- CNN
- The Guardian
