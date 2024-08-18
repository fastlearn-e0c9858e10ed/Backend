from fastapi.responses import JSONResponse


async def get_all_subjects() -> JSONResponse:
    return JSONResponse(content={"message": "get_all_subjects"})


async def get_subject_by_id(subject_id: str) -> JSONResponse:
    return JSONResponse(content={"message": f"get_subject_by_id for {subject_id}"})


async def add_subject() -> JSONResponse:
    return JSONResponse(content={"message": "add_subject"})


async def update_subject(subject_id: str) -> JSONResponse:
    return JSONResponse(content={"message": f"update_subject for {subject_id}"})


async def delete_subject(subject_id: str) -> JSONResponse:
    return JSONResponse(content={"message": f"delete_subject for {subject_id}"})
