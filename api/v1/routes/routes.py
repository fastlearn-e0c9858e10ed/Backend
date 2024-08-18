from fastapi import APIRouter

import api.v1.controllers.pastpapers as PastPaperController
import api.v1.controllers.subjects as Subjects

router = APIRouter()

# /api/v1 -> GET
router.get("/")(PastPaperController.root)

# /api/v1/pastpapers -> GET
router.get("/pastpapers")(PastPaperController.get_all_pastpapers_metadata)

# /api/v1/pastpapers/subject/{subject} -> GET
router.get("/pastpapers/subject/{subject}")(PastPaperController.get_pastpapers_by_subject)

# /api/v1/pastpapers/{pastpaper_id} -> GET
router.get("/pastpapers/{pastpaper_id}")(PastPaperController.get_pastpaper_metadata)

# /api/v1/pastpapers -> POST
router.post("/pastpapers")(PastPaperController.add_pastpaper)

# /api/v1/pastpapers/{pastpaper_id} -> PUT
router.put("/pastpapers/{pastpaper_id}")(PastPaperController.update_pastpaper)

# /api/v1/pastpapers/{pastpaper_id} -> DELETE
router.delete("/pastpapers/{pastpaper_id}")(PastPaperController.delete_pastpaper)

# /api/v1/subjects -> GET
router.get("/subjects")(Subjects.get_all_subjects)

# /api/v1/subjects/{subject_id} -> GET
router.get("/subjects/{subject_id}")(Subjects.get_subject_by_id)

# /api/v1/subjects -> POST
router.post("/subjects")(Subjects.add_subject)

# /api/v1/subjects/{subject_id} -> PUT
router.put("/subjects/{subject_id}")(Subjects.update_subject)

# /api/v1/subjects/{subject_id} -> DELETE
router.delete("/subjects/{subject_id}")(Subjects.delete_subject)
