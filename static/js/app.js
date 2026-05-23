// ==========================================
// App State & Configuration
// ==========================================

const AppState = {
    newsData: null,
    lastUpdate: null,
    isScraping: false
};

// ==========================================
// Utility Functions
// ==========================================

const formatDate = (dateString) => {
    if (!dateString) return '—';

    const date = new Date(dateString);
    const now = new Date();
    const diffMs = now - date;
    const diffMins = Math.floor(diffMs / 60000);
    const diffHours = Math.floor(diffMs / 3600000);

    if (diffMins < 1) return 'Just now';
    if (diffMins < 60) return `${diffMins} min${diffMins > 1 ? 's' : ''} ago`;
    if (diffHours < 24) return `${diffHours} hour${diffHours > 1 ? 's' : ''} ago`;

    return date.toLocaleDateString('en-US', {
        month: 'short',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    });
};

const getDomain = (url) => {
    try {
        return new URL(url).hostname.replace('www.', '');
    } catch {
        return 'news.com';
    }
};

const escapeHtml = (text) => {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
};

// ==========================================
// UI Rendering Functions
// ==========================================

const renderArticleCard = (article, index) => {
    const domain = getDomain(article.link);

    return `
        <div class="article-card" style="animation-delay: ${index * 0.05}s">
            <a href="${article.link}" target="_blank" rel="noopener noreferrer" class="article-link">
                <h3 class="article-title">${escapeHtml(article.title)}</h3>
                <div class="article-meta">
                    <svg class="article-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                              d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/>
                    </svg>
                    <span>${escapeHtml(domain)}</span>
                </div>
            </a>
        </div>
    `;
};

const renderNewsSource = (sourceName, articles) => {
    if (!articles || articles.length === 0) {
        return `
            <div class="news-source">
                <div class="source-header">
                    <h2 class="source-name">${escapeHtml(sourceName)}</h2>
                    <span class="article-count">0 articles</span>
                </div>
                <div class="empty-state">
                    <p>No articles available from this source</p>
                </div>
            </div>
        `;
    }

    const articlesHTML = articles
        .map((article, index) => renderArticleCard(article, index))
        .join('');

    return `
        <div class="news-source">
            <div class="source-header">
                <h2 class="source-name">${escapeHtml(sourceName)}</h2>
                <span class="article-count">${articles.length} article${articles.length !== 1 ? 's' : ''}</span>
            </div>
            <div class="articles-grid">
                ${articlesHTML}
            </div>
        </div>
    `;
};

const renderAllNews = (newsData) => {
    const newsGrid = document.getElementById('newsGrid');

    if (!newsData || Object.keys(newsData).length === 0) {
        newsGrid.innerHTML = `
            <div class="empty-state">
                <p>No news data available. Click refresh to fetch latest news.</p>
            </div>
        `;
        return;
    }

    // FIXED: Match exactly what your scraper produces
    const sourceOrder = [
        'BBC News',
        'CNN',
        'Al Jazeera',
        'AP News',
        'The Express Tribune',
        'Dawn',
        'NPR News'
    ];

    const newsHTML = sourceOrder
        .filter(source => newsData.hasOwnProperty(source))
        .map(source => renderNewsSource(source, newsData[source]))
        .join('');

    newsGrid.innerHTML = newsHTML;
};

// ==========================================
// API Functions
// ==========================================

const fetchNews = async () => {
    try {
        const response = await fetch('/api/news');
        const data = await response.json();

        AppState.newsData = data.data;
        AppState.lastUpdate = data.last_update;
        AppState.isScraping = data.is_scraping;

        updateUI();
    } catch (error) {
        console.error('Error fetching news:', error);
        showError('Failed to load news data');
    }
};

const refreshNews = async () => {
    const refreshBtn = document.getElementById('refreshBtn');
    const loadingState = document.getElementById('loadingState');

    try {
        refreshBtn.classList.add('loading');
        loadingState.classList.add('active');

        const response = await fetch('/api/refresh');
        const data = await response.json();

        if (data.status === 'already_scraping') {
            showNotification('Refresh already in progress...');
            return;
        }

        showNotification('Fetching latest global news...');

        // Poll for updates every 3 seconds
        const pollInterval = setInterval(async () => {
            const newsResponse = await fetch('/api/news');
            const newsData = await newsResponse.json();

            if (!newsData.is_scraping) {
                clearInterval(pollInterval);

                AppState.newsData = newsData.data;
                AppState.lastUpdate = newsData.last_update;
                AppState.isScraping = false;

                updateUI();
                refreshBtn.classList.remove('loading');
                loadingState.classList.remove('active');
                showNotification('Global news updated successfully!');
            }
        }, 3000);

    } catch (error) {
        console.error('Error refreshing news:', error);
        showError('Failed to refresh news');
        refreshBtn.classList.remove('loading');
        loadingState.classList.remove('active');
    }
};

// ==========================================
// UI Update Functions
// ==========================================

const updateUI = () => {
    const lastUpdateElement = document.getElementById('lastUpdate');
    if (lastUpdateElement) {
        lastUpdateElement.textContent = formatDate(AppState.lastUpdate);
    }

    const mainContent = document.getElementById('mainContent');
    const loadingState = document.getElementById('loadingState');

    if (AppState.isScraping) {
        loadingState.classList.add('active');
        mainContent.style.opacity = '0.5';
    } else {
        loadingState.classList.remove('active');
        mainContent.style.opacity = '1';
        renderAllNews(AppState.newsData);
    }
};

// ==========================================
// Notification System
// ==========================================

let notificationTimeout;

const showNotification = (message) => {
    if (notificationTimeout) clearTimeout(notificationTimeout);

    let notification = document.querySelector('.notification');

    if (!notification) {
        notification = document.createElement('div');
        notification.className = 'notification';
        document.body.appendChild(notification);

        const style = document.createElement('style');
        style.textContent = `
            .notification {
                position: fixed;
                top: 100px;
                right: 20px;
                background: #c41e3a;
                color: white;
                padding: 1rem 1.5rem;
                border-radius: 8px;
                font-weight: 600;
                z-index: 1000;
                opacity: 0;
                transform: translateX(400px);
                transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
            }
            .notification.show {
                opacity: 1;
                transform: translateX(0);
            }
        `;
        document.head.appendChild(style);
    }

    notification.textContent = message;
    setTimeout(() => notification.classList.add('show'), 10);

    notificationTimeout = setTimeout(() => {
        notification.classList.remove('show');
    }, 3000);
};

const showError = (message) => showNotification('❌ ' + message);

// ==========================================
// Event Listeners
// ==========================================

const initEventListeners = () => {
    const refreshBtn = document.getElementById('refreshBtn');
    if (refreshBtn) {
        refreshBtn.addEventListener('click', refreshNews);
    }

    // Auto-refresh every 15 minutes
    setInterval(() => {
        if (!AppState.isScraping) refreshNews();
    }, 15 * 60 * 1000);
};

// ==========================================
// App Initialization
// ==========================================

const initApp = async () => {
    console.log('🌐 Initializing Chronos Global News Aggregator...');
    initEventListeners();
    await fetchNews();
    console.log('✅ App initialized successfully!');
};

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initApp);
} else {
    initApp();
}