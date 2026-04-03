# 🎬 CineMatch — AI Movie Recommender

CineMatch is an AI-powered movie recommendation web application that suggests movies based on mood, genre, language, and custom preferences. It uses LLMs via the Groq API to generate structured, high-quality recommendations.

---

## 🚀 Features

* 🎭 Mood-based recommendations
* 🎬 Genre filtering
* 🌍 Language selection
* ✍️ Custom input support
* ⭐ AI-generated movie insights
* 📌 Watchlist (add/remove movies)

---

## 🧠 Tech Stack

* **Backend:** FastAPI, Python
* **AI:** Groq API (LLaMA models)
* **Frontend:** HTML, CSS, JavaScript
* **Server:** Uvicorn

---

## 📁 Project Structure

```
cinematch/
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── .env.example
└── frontend/
    └── index.html
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/your-username/cinematch.git
cd cinematch/backend
```

---

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

### 3. Configure environment variables

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

### 4. Run backend

```
uvicorn main:app --reload
```

Server runs at: http://localhost:8000

---

### 5. Run frontend

Open `frontend/index.html` in your browser.

---

## 🔗 API Endpoints

* `POST /api/recommend` → Get movie recommendations
* `GET /api/watchlist` → Get saved movies
* `POST /api/watchlist` → Add movie
* `DELETE /api/watchlist/{title}` → Remove movie
* `GET /api/health` → Health check

---

## 🌐 Deployment (optional)

* Backend → Render / Railway
* Frontend → GitHub Pages / Vercel

---

## 💡 Notes

* Uses in-memory storage for watchlist (can be extended to database)
* Requires valid Groq API key
