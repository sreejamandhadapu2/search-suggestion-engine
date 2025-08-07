from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import json
import csv
import os

app = Flask(__name__, static_folder='bookquest')
CORS(app)

# Load book data
with open('bookquest/sample.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Support both formats: {"books": [...]} or just a list
if isinstance(data, dict) and 'books' in data:
    books = data['books']
elif isinstance(data, list):
    books = data
else:
    raise ValueError("sample.json format not recognized.")

book_titles = [book['title'] for book in books if 'title' in book]

# === Suggest API ===
@app.route("/suggest", methods=["GET"])
def suggest():
    query = request.args.get("q", "").strip().lower()
    if not query:
        return jsonify([])

    # Load past user searches
    past_titles = []
    if os.path.exists('search_logs.csv'):
        with open('search_logs.csv', 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if row:
                    past_titles.append(row[0].strip())

    # Filter titles that contain the query substring (case-insensitive)
    matches = [title for title in book_titles if query in title.lower()]

    # Sort matches: previously searched ones first
    seen = set()
    ranked = []

    for past in past_titles[::-1]:  # reverse to prioritize recent
        if past.lower().find(query) != -1 and past not in seen and past in matches:
            ranked.append(past)
            seen.add(past)

    for title in matches:
        if title not in seen:
            ranked.append(title)
            seen.add(title)

    return jsonify(ranked)

# === Logging Searches (optional future feature) ===
@app.route("/log", methods=["POST"])
def log_search():
    data = request.get_json()
    title = data.get("title", "").strip()
    if title:
        with open("search_logs.csv", "a", newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([title])
    return jsonify({"status": "logged"})

# === Serve Frontend ===
@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

if __name__ == "__main__":
    app.run(debug=True)
