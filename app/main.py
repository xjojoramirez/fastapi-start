from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.core.database import Base, engine
from app.api.routes import auth, items

# Initialize FastAPI app
app = FastAPI(
    title="FastAPI Starter",
    description="API with User Authentication, JWT, Refresh Tokens, and CRUD",
    version="1.0.0",
)

# Create database tables (if they don't exist)
Base.metadata.create_all(bind=engine)

# Include routers with prefixes and tags
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(items.router, prefix="/items", tags=["Items"])

# Root path → redirect to docs
@app.get("/")
def root():
    return{"message":"Welcome to FastAPI Starter"}
