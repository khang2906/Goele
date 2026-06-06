from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Event(Base):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    sport: Mapped[str] = mapped_column(String)  # "bike", "motorcycle", or "run"
    title: Mapped[str] = mapped_column(String)
    date: Mapped[datetime] = mapped_column(DateTime)
    meeting_point: Mapped[str] = mapped_column(String)
    route_link: Mapped[str | None] = mapped_column(String, nullable=True)
    description: Mapped[str | None] = mapped_column(String, nullable=True)
    pace: Mapped[str] = mapped_column(String)
    max_participants: Mapped[int | None] = mapped_column(Integer, nullable=True)

    # cascade="all, delete-orphan" means RSVPs are removed when their event is deleted
    rsvps: Mapped[list["RSVP"]] = relationship(
        back_populates="event", cascade="all, delete-orphan"
    )


class RSVP(Base):
    __tablename__ = "rsvps"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    event_id: Mapped[int] = mapped_column(ForeignKey("events.id"))
    name: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    event: Mapped["Event"] = relationship(back_populates="rsvps")
