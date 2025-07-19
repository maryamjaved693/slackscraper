import firecrawl
import json
import re
import requests
import time
from getpass import getpass
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Setup Firecrawl API (use env vars in Vercel)
import os
firecrawl_api_key = os.getenv("FIRECRAWL_API_KEY")
slack_webhook_url = os.getenv("SLACK_WEBHOOK_URL")
app = firecrawl.FirecrawlApp(api_key=firecrawl_api_key)

# Include all your scraping logic from the shared code...
# For brevity, the rest of the code is assumed imported here

def run_scraper():
    print("🚀 Running Replit Bounty Scraper")
    recent_bounties = get_recent_bounties(hours_limit=24)
    if not recent_bounties:
        send_to_slack("No recent bounties found", slack_webhook_url)
        return "No bounties found"
    top_bounty = recent_bounties[0]
    message = f"🏆 TOP REPLIT BOUNTY: {top_bounty['title']} - {top_bounty['amount']}"
    send_to_slack(message, slack_webhook_url)
    return {
        "top_amount": top_bounty['amount'],
        "title": top_bounty['title'],
        "posted_hours_ago": top_bounty.get("hours_old", "N/A")
    }
