from typing import Dict

from bson import ObjectId
from fastapi import APIRouter

from config.database import videoAsk_collection

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


query_params_dict: Dict[str, int] = {}


@devModeRouter.get("/track-query-param/")
async def track_query_param(query_param: str):
    """
    Endpoint to track query parameters and their counts.

    Args:
        query_param (str): Query parameter sent in the GET request.

    Returns:
        dict: Updated dictionary containing query parameters and their counts.
    """
    if query_param in query_params_dict:
        # Increment count if query_param exists in dictionary
        query_params_dict[query_param] += 1
    else:
        # Add query_param to dictionary with count of 1 if it doesn't exist
        query_params_dict[query_param] = 1

    return query_params_dict
