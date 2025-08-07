# 🔍 BookQuest – Intelligent Search Suggestion Engine

**BookQuest** is a full-stack search suggestion engine designed to enhance user experience while browsing book titles. It uses a combination of Natural Language Processing (NLP) techniques and user behavior metrics to dynamically suggest the most relevant results as the user types.

This project demonstrates the integration of data science with web development using a layered architecture for intelligent, fast, and context-aware search suggestions.

---

## 🎯 Project Goals

- Simulate a real-world book search platform with smart suggestion features.
- Integrate machine learning & ranking techniques to improve search result relevance.
- Build a maintainable architecture using Flask (backend) and HTML/CSS/JavaScript (frontend).
- Implement learning-to-rank components based on click-through behavior.

---

## 🧠 Features

✅ Real-time search suggestions as user types  
✅ N-gram token matching for partial input recognition  
✅ TF-IDF + Fuzzy matching for typo-tolerant matching  
✅ CTR (Click Through Rate)-based ranking for user-driven optimization  
✅ Interactive frontend with AJAX calls to Flask backend  
✅ Modular backend system with support for easy extension  
✅ Search logs saved for future behavioral analytics  

---

## 🛠️ Tech Stack

| Layer         | Technologies Used                                       |
|---------------|---------------------------------------------------------|
| Frontend      | HTML5, CSS3, JavaScript (vanilla), AJAX                |
| Backend       | Python, Flask                                           |
| NLP Libraries | scikit-learn, fuzzywuzzy, ngram, pandas                 |
| Data Storage  | CSV logs (search_logs.csv)                             |
| Dev Tools     | VS Code, Git, GitHub, Postman                          |

---

## 📁 Project Structure

project_root/
│
├── bookquest/                  # Frontend
│   ├── index.html              # Main UI
│   ├── style.css               # Styling
│   ├── script.js               # AJAX and UI logic
│   └── data/
│       └── books.json          # Static book data source
│
├── search_engine/              # Backend
│   ├── app.py                  # Flask backend with /suggest API
│   ├── ngram.py                # N-gram matching logic
│   ├── tfidf_matcher.py        # TF-IDF and fuzzy search
│   ├── ctr_ranking.py          # CTR-based ranking algorithm
│   └── search_logs.csv         # Click logs for future ranking
│
└── README.md                   # Project documentation

---

## ⚙️ How It Works

### 🔁 Search Flow:

1. User types into the search bar in index.html.
2. script.js sends real-time AJAX requests to the Flask backend (/suggest endpoint).
3. Backend:
   - Tokenizes input using n-grams
   - Finds similar entries with TF-IDF + fuzzy matching
   - Ranks them using CTR-based learning
4. Suggestions are returned and shown under the search bar.
5. User clicks on a suggestion → click data is stored in search_logs.csv.

---

## 🚀 How to Run the Project

### 💻 Backend Setup

# Navigate to backend
cd search_engine

# Install dependencies
pip install flask fuzzywuzzy scikit-learn pandas

# Run Flask server
python app.py

### 🌐 Frontend Setup

- Open bookquest/index.html in your browser
- Start typing in the search bar and observe dynamic suggestions

---

## 📊 Future Improvements

- Store and analyze user click data in a proper database (SQLite/PostgreSQL)
- Integrate spell check correction
- Add personalized recommendations based on user profiles
- Build an admin panel to analyze popular searches and trends
- Train ML models (like XGBoost Ranker) for advanced ranking

---

## 🎥 Demo (Optional)

*Include a video link or GIF here if available.*

---

## 👩‍💻 Author

**Sreeja Mandhadapu**  
3rd Year B.Tech Student | Data Science & Software Development Enthusiast  
📫 GitHub: https://github.com/sreejamandhadapu2

---

