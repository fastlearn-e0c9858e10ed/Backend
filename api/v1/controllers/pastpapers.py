from fastapi.responses import JSONResponse


async def root() -> JSONResponse:
    return JSONResponse(content={"message": "/api/v1"})


async def get_all_pastpapers_metadata() -> JSONResponse:
    return JSONResponse(content={"message": "get_all_pastpapers"})


async def get_pastpaper_metadata(pastpaper_id: str) -> JSONResponse:
    return JSONResponse(content={"message": f"get_pastpaper_metadata for {pastpaper_id}"})


async def add_pastpaper() -> JSONResponse:
    return JSONResponse(content={"message": "add_pastpaper"})


async def update_pastpaper(pastpaper_id: str) -> JSONResponse:
    return JSONResponse(content={"message": f"update_pastpaper for {pastpaper_id}"})


async def delete_pastpaper(pastpaper_id: str) -> JSONResponse:
    return JSONResponse(content={"message": f"delete_pastpaper for {pastpaper_id}"})


async def get_pastpapers_by_subject(subject: str) -> JSONResponse:
    return JSONResponse(content={"message": f"get_pastpapers_by_subject for {subject}"})
