"""Security helpers: password hashing and JWT creation.

This module centralizes password hashing/verification and access token
generation so other parts of the app can depend on a consistent
implementation.
"""

from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
from app.core.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

# Password hashing context configured to use bcrypt.
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto", bcrypt__rounds=12)



def hash_password(password: str):
    """Hash a plain-text password.

    Returns a salted bcrypt hash suitable for storing in the database.
    """
    return pwd_context.hash(password)


def verify_password(password: str, hashed: str):
    """Verify a plain-text password against a stored hash.

    Returns True if the password matches the hash, False otherwise.
    """
    return pwd_context.verify(password, hashed)


def create_access_token(data: dict):
    """Create a JWT access token containing `data` as claims.

    The token will include an `exp` claim set to `ACCESS_TOKEN_EXPIRE_MINUTES`
    minutes from now. `SECRET_KEY` and `ALGORITHM` from config are used to sign
    the token.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
