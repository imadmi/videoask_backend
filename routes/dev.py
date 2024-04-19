from typing import Dict

from bson import ObjectId
from fastapi import APIRouter

from config.database import videoAsk_collection, stats_collection

devModeRouter = APIRouter(tags=["videoAsk"])


@devModeRouter.delete("/deleteAllVideoAsks")
async def delete_all_files():
    try:
        videoAsk_collection.delete_many({})
        return {"success": True}
    except Exception as e:
        return {"success": False, "error": str(e)}


@devModeRouter.delete("/deleteVideoAsk/{id}")
async def delete_videoAsk_by_id(id: str):
    try:
        videoAsk_collection.delete_one({"_id": ObjectId(id)})
        return {"success": True}
    except Exception as e:
        return {"success": False, "error": str(e)}


@devModeRouter.get("/track-query-param/")
async def track_query_param(query_param: str):
    try:
        db_query_param = await stats_collection.find_one({"query_param": query_param})
        if db_query_param:
            await stats_collection.update_one({"_id": db_query_param["_id"]}, {"$inc": {"count": 1}})
        else:
            await stats_collection.insert_one({"query_param": query_param, "count": 1})
        return {"query_param": query_param, "count": (db_query_param["count"] + 1) if db_query_param else 1}
    except Exception as e:
        return {"error": str(e)}


@devModeRouter.get("/get-all-stats")
async def get_all_stats():
    try:
        all_stats = []
        cursor = await stats_collection.find().to_list(1000)

        for stat in cursor:
            stat["_id"] = str(stat["_id"])
            all_stats.append(stat)

        return all_stats

    except Exception as e:
        return {"error": str(e)}

