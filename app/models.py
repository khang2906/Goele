from datetime import datetime

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

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
