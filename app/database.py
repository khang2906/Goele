from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

SQLITE_URL = "sqlite:///groupride.db"

# check_same_thread=False is required for SQLite because FastAPI uses a
# thread pool — without this, SQLite would reject connections from non-creator threads
engine = create_engine(SQLITE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


def get_db():
    """Yield a database session and guarantee it closes after the request."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
