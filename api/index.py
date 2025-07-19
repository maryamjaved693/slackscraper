from flask import Flask, jsonify
from scraper import run_scraper

app = Flask(__name__)

@app.route("/run", methods=["GET"])
def trigger_scraper():
    result = run_scraper()
    return jsonify({"message": "Scraper executed", "summary": result})
@app.route("/", methods=["GET"])
def home():
    return "✅ Replit Bounty Scraper is deployed. Use /run to trigger scraping.", 200
