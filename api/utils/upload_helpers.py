import shutil
from pathlib import Path

from fastapi import UploadFile


def save_pdf_file(file: UploadFile, file_path: Path) -> bool:
    # Check if file already exists
    if not file_path.is_file():
        try:
            with Path.open(file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
        except Exception:
            return False
    return True
