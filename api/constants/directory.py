from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent  # Base directory of the application
UPLOADS_DIR = BASE_DIR / "uploads"  # Directory for uploaded files
NOTES_DIR = UPLOADS_DIR / "notes"  # Directory for uploaded notes
PASTPAPERS_DIR = UPLOADS_DIR / "pastpapers"  # Directory for uploaded pastpapers

# Create the directories if they don't exist
UPLOADS_DIR.mkdir(parents=True, exist_ok=True)
NOTES_DIR.mkdir(parents=True, exist_ok=True)
PASTPAPERS_DIR.mkdir(parents=True, exist_ok=True)

class Directory:
    UPLOADS_DIR = UPLOADS_DIR
    NOTES_DIR = NOTES_DIR
    PASTPAPERS_DIR = PASTPAPERS_DIR
