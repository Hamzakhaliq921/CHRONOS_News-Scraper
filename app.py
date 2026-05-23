from flask import Flask, render_template, jsonify
import json
import os

from datetime import datetime
import threading
import time
from news_scraper import NewsAggregator

