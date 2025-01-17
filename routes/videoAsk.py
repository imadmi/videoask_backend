from typing import List

from fastapi import APIRouter, File, UploadFile

from models.videoAsk import VideoAsk
from schemas.videoAsk import (
    get_video_from_db,
    get_videos_from_db,
    save_VideoAsk_in_db,
    upload_blob,
)

videoAskRouter = APIRouter(tags=["videoAsk"])


@videoAskRouter.post("/saveVideoAsk")
async def save_VideoAsk(videoAsks: List[VideoAsk]):
    try:
        await save_VideoAsk_in_db(videoAsks)
        return {"success": "true"}
    except Exception as e:
        return {"success": "false", "error": str(e)}


@videoAskRouter.get("/getVideoAsks")
async def get_VideoAsk():
    try:
        videoAsk_list = await get_videos_from_db()
        return {"success": True, "videoAsks": videoAsk_list}
    except Exception as e:
        return {"success": False, "error": str(e)}


@videoAskRouter.get("/getVideoAsk/{id}")
async def get_VideoAsk_by_id(id: str):
    try:
        videoAsk = await get_video_from_db(id)
        return {"success": True, "videoAsk": videoAsk}
    except Exception as e:
        return {"success": False, "error": str(e)}


@videoAskRouter.post("/uploadfile")
async def upload_file(file: UploadFile = File(...)):
    try:
        url = await upload_blob(file)
        return {"success": True, "url": url}
    except Exception as e:
        return {"success": False, "error": str(e)}
