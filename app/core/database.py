"""Database setup and dependency for route-level DB sessions.

This module configures SQLAlchemy's engine, session factory and base
class used by ORM models. It also exposes `get_db`, a generator-style
dependency that yields a database session for use in request handlers
and ensures the session is closed after the request completes.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import DATABASE_URL

# Create the SQLAlchemy engine using the configured DATABASE_URL.
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class. Using `autoflush=False` and
# `autocommit=False` is a common pattern for request-scoped sessions.
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Base class for declarative models to inherit from.
Base = declarative_base()


def get_db():
    """Yield a database session and ensure it's closed afterwards.

    Use this function as a FastAPI dependency (e.g. `db: Session = Depends(get_db)`).
    It yields a `Session` instance for the duration of the request and
    always closes the session in the `finally` block to avoid connection leaks.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

