from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.dev import devModeRouter
from routes.videoAsk import videoAskRouter

app = FastAPI()
app.include_router(videoAskRouter)
app.include_router(devModeRouter)

origins = [
    "http://localhost:3000",
    "https://interactive-videos-prod.vercel.app/",
    "https://videoask-fawn.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Python version : 3.8.10

# pre-commit run --all-files
