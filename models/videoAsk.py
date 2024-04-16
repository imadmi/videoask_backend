from typing import List, Union

from pydantic import BaseModel


class Question(BaseModel):
    question: str
    audioUrl: str
    next_video_id: Union[str, None]


class VideoAsk(BaseModel):
    id: str
    title: str
    url: str
    questions: List[Question]
