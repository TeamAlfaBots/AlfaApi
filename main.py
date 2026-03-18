from fastapi import FastAPI
from yt_dlp import YoutubeDL

app = FastAPI()

# ✅ Home route
@app.get("/")
def home():
    return {"status": "AlfaApi running 🚀"}

# ✅ Health check (ALL ROUTES - IMPORTANT)
@app.get("/kaithealthcheck")
@app.get("/health")
@app.get("/healthz")
@app.get("/ping")
def health():
    return {"status": "ok"}

# ✅ Search route
@app.get("/search")
def search(title: str):
    try:
        ydl_opts = {
            "format": "bestaudio/best",
            "quiet": True,
            "noplaylist": True,
            "nocheckcertificate": True,
            "default_search": "ytsearch",
            "source_address": "0.0.0.0",
        }

        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch:{title}", download=False)
            video = info["entries"][0]

            return {
                "link": video.get("url"),
                "title": video.get("title"),
                "duration": video.get("duration"),
                "thumbnail": video.get("thumbnail")
            }

    except Exception as e:
        return {"error": str(e)}
