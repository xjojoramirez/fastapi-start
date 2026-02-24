"""Dependency utilities for API routes.

This module provides FastAPI dependencies used across route handlers,
primarily for authentication and loading the current user from a JWT.
"""

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from sqlalchemy.orm import Session
from app.core.config import SECRET_KEY, ALGORITHM
from app.core.database import get_db
from app.models.user import User

# OAuth2 scheme that looks for a "Authorization: Bearer <token>" header.
# `tokenUrl` is the URL where clients can get a token (used in interactive docs).
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """Resolve and return the currently authenticated user.

    - `token` is extracted from the request by `oauth2_scheme`.
    - The token is decoded using the application's `SECRET_KEY` and `ALGORITHM`.
    - The JWT is expected to include the user's id in the `sub` claim.
    - The user is loaded from the database using the provided `db` session.
    - If no user is found, a 401 is raised to indicate invalid credentials.

    Returns:
        User: The SQLAlchemy `User` model instance for the authenticated user.
    """
    # Decode the JWT to obtain the payload (raises on invalid token).
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

    # The subject ('sub') claim should contain the user id.
    user_id = payload.get("sub")

    # Query the database for the user. `first()` returns None if not found.
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        # If we couldn't find a user for the token's subject, reject the request.
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return user
