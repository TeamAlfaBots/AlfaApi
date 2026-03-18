from fastapi import FastAPI
from yt_dlp import YoutubeDL

app = FastAPI()

@app.get("/search")
def search(title: str):
    try:
        ydl_opts = {
            "format": "bestaudio",
            "quiet": True,
            "noplaylist": True,
        }

        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch:{title}", download=False)
            video = info["entries"][0]

            return {
                "link": video["url"],
                "title": video["title"],
                "duration": video["duration"],
                "thumbnail": video["thumbnail"]
            }

    except Exception as e:
        return {"error": str(e)}
