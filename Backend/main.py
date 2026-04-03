from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from dotenv import load_dotenv
from groq import Groq
import json
import os

load_dotenv()

app = FastAPI(title="CineMatch API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

class RecommendRequest(BaseModel):
    mood: Optional[str] = ""
    genres: Optional[list[str]] = []
    custom: Optional[str] = ""
    language: Optional[str] = "any"

class WatchlistItem(BaseModel):
    title: str
    year: int
    tags: list[str]

watchlist: list[dict] = []

@app.post("/api/recommend")
async def recommend(req: RecommendRequest):
    parts = []
    if req.mood:
        parts.append(f"mood: {req.mood}")
    if req.genres:
        parts.append(f"genres: {', '.join(req.genres)}")
    if req.custom:
        parts.append(f"extra context: {req.custom}")
    if req.language and req.language != "any":
        parts.append(f"language: {req.language}")

    if not parts:
        raise HTTPException(status_code=400, detail="Provide at least one preference.")

    prompt = f"""Recommend exactly 4 movies for someone with these preferences — {'; '.join(parts)}.

Return ONLY a valid JSON array, no markdown, no explanation:
[
  {{
    "title": "Movie Title",
    "year": 2020,
    "director": "Director Name",
    "rating": 8.2,
    "why": "One warm specific sentence explaining why this fits perfectly.",
    "tags": ["tag1", "tag2", "tag3"],
    "mood_match": 92
  }}
]"""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1024
        )
        text = response.choices[0].message.content
        clean = text.replace("```json", "").replace("```", "").strip()
        movies = json.loads(clean)
        return {"movies": movies}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/watchlist")
async def get_watchlist():
    return {"watchlist": watchlist}

@app.post("/api/watchlist")
async def add_to_watchlist(item: WatchlistItem):
    if any(m["title"] == item.title for m in watchlist):
        return {"message": "Already in watchlist", "watchlist": watchlist}
    watchlist.append(item.dict())
    return {"message": "Added!", "watchlist": watchlist}

@app.delete("/api/watchlist/{title}")
async def remove_from_watchlist(title: str):
    global watchlist
    watchlist = [m for m in watchlist if m["title"] != title]
    return {"message": "Removed", "watchlist": watchlist}

@app.get("/api/health")
async def health():
    return {"status": "ok"}