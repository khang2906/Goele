from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Serve files from /static (CSS, images, JS) at the URL path /static
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="app/templates")

# Hardcoded placeholder events — will be replaced by DB queries later
FAKE_EVENTS = [
    {
        "title": "Morning Ride to Starnberger See",
        "sport": "bike",
        "date": "2026-05-10 08:00",
        "meeting_point": "Marienplatz, Munich",
        "pace": "moderate",
    },
    {
        "title": "Sunday Motorcycle Tour — Bavarian Alps",
        "sport": "motorcycle",
        "date": "2026-05-12 09:00",
        "meeting_point": "Siegestor, Munich",
        "pace": "relaxed",
    },
    {
        "title": "English Garden 10k Run",
        "sport": "run",
        "date": "2026-05-14 07:00",
        "meeting_point": "Chinesischer Turm, Munich",
        "pace": "fast",
    },
]


@app.get("/")
async def index(request: Request):
    """Render the homepage with a list of upcoming events."""
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "events": FAKE_EVENTS},
    )
