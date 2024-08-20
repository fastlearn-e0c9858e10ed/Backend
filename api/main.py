# app/main.py
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from api.constants.directory import Directory
from api.core.config import engine
from api.models.models import Base
from api.v1.routes import routes

app = FastAPI()

# Serve static files from the "media" directory
app.mount("/uploads", StaticFiles(directory=Directory.UPLOADS_DIR), name="uploads")

# Include the routes from the api/v1/routes/routes.py file
app.include_router(routes.router, prefix="/api/v1")

# Create tables
@app.on_event("startup")
def on_startup() -> None:
    Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root() -> dict[str, str]:
    return {"Hello": "World"}

@app.get("/uploads/pastpapers/{pastpaper_id}.pdf")
async def get_song(pastpaper_id: str) -> FileResponse:
    file_path = Directory.PASTPAPERS_DIR / f"{pastpaper_id}.pdf"

    if not file_path.is_file():
        raise HTTPException(status_code=404, detail="File not found")

    return FileResponse(file_path)

# Run the application using 'uvicorn' if this script is run directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000) # uvicorn api.main:app --reload
