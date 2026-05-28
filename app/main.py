from contextlib import asynccontextmanager
from datetime import datetime

from fastapi import Depends, FastAPI, Form, HTTPException, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import Base, SessionLocal, engine, get_db
from app.models import Event


def seed_events() -> None:
    """Add placeholder events if the database is empty."""
    db = SessionLocal()
    try:
        if db.query(Event).count() > 0:
            return
        db.add_all([
            Event(
                sport="bike",
                title="Morning Ride to Starnberger See",
                date=datetime(2026, 5, 10, 8, 0),
                meeting_point="Marienplatz, Munich",
                description="A relaxed morning ride along the Isar to Starnberger See.",
                pace="moderate",
                max_participants=10,
            ),
            Event(
                sport="motorcycle",
                title="Sunday Motorcycle Tour — Bavarian Alps",
                date=datetime(2026, 5, 12, 9, 0),
                meeting_point="Siegestor, Munich",
                description="Scenic tour through the foothills of the Alps.",
                pace="relaxed",
                max_participants=8,
            ),
            Event(
                sport="run",
                title="English Garden 10k Run",
                date=datetime(2026, 5, 14, 7, 0),
                meeting_point="Chinesischer Turm, Munich",
                description="A brisk 10k loop around the English Garden.",
                pace="fast",
                max_participants=15,
            ),
        ])
        db.commit()
    finally:
        db.close()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Runs once on startup: create tables if they don't exist, then seed
    Base.metadata.create_all(bind=engine)
    seed_events()
    yield  # server runs here; anything after yield runs on shutdown


app = FastAPI(lifespan=lifespan)

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="app/templates")


@app.get("/")
async def index(request: Request, db: Session = Depends(get_db)):
    """Render the homepage with upcoming events ordered by date."""
    events = db.query(Event).order_by(Event.date).all()
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "events": events},
    )


@app.get("/events/new")
async def new_event_form(request: Request):
    """Render the empty form for creating a new event."""
    return templates.TemplateResponse("new_event.html", {"request": request})


@app.post("/events/new")
async def create_event(
    db: Session = Depends(get_db),
    sport: str = Form(...),
    title: str = Form(...),
    date: str = Form(...),
    meeting_point: str = Form(...),
    pace: str = Form(...),
    max_participants: str | None = Form(None),
    route_link: str | None = Form(None),
    description: str | None = Form(None),
):
    """Save a new event from submitted form data, then redirect to its detail page."""
    event = Event(
        sport=sport,
        title=title,
        date=datetime.fromisoformat(date),  # datetime-local sends "2026-05-20T08:00"
        meeting_point=meeting_point,
        pace=pace,
        # HTML forms submit empty fields as "" (never null), so coerce blanks to None
        max_participants=int(max_participants) if max_participants else None,
        route_link=route_link or None,
        description=description or None,
    )
    db.add(event)
    db.commit()
    db.refresh(event)  # reloads the row so event.id (assigned by the DB) is available
    return RedirectResponse(url=f"/events/{event.id}", status_code=303)


@app.get("/events/{event_id}")
async def event_detail(event_id: int, request: Request, db: Session = Depends(get_db)):
    """Render the detail page for a single event."""
    event = db.query(Event).filter(Event.id == event_id).first()
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return templates.TemplateResponse(
        "event.html",
        {"request": request, "event": event},
    )
