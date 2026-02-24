"""Application configuration values loaded from environment.

This module loads environment variables (via a .env file when present)
and exposes configuration constants used across the application. Default
values are provided for development convenience but should be overridden
in production via environment variables or Docker secrets.
"""

import os
from dotenv import load_dotenv

# Load variables from a .env file into the environment (no-op if none).
load_dotenv()

# Database connection URL (e.g. postgres://user:pass@host/dbname)
DATABASE_URL = os.getenv("DATABASE_URL")

# Secret key used to sign JWTs. Provide a secure random value in production.
SECRET_KEY = os.getenv("SECRET_KEY", "supersecret")

# Algorithm used to sign JWTs.
ALGORITHM = "HS256"

# Access token expiry in minutes.
ACCESS_TOKEN_EXPIRE_MINUTES = 15

# Refresh token expiry in days.
REFRESH_TOKEN_EXPIRE_DAYS = 7
