# app/main.py
from fastapi import FastAPI

from api.core.config import engine
from api.models.models import Base
from api.v1.routes import routes

app = FastAPI()

# Include the routes from the api/v1/routes/routes.py file
app.include_router(routes.router, prefix="/api/v1")

# Create tables
@app.on_event("startup")
def on_startup() -> None:
    Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root() -> dict[str, str]:
    return {"Hello": "World"}

# Run the application using 'uvicorn' if this script is run directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000) # uvicorn api.main:app --reload
