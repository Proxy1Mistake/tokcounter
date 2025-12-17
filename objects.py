from pydantic import BaseModel
from typing import Any

class Search(BaseModel):
    id: str
    isInvalidID: bool
    userId: int
    username: str
    avatar: str
    verified: bool

class Stats(BaseModel):
    cache: bool
    success: bool
    followerCount: int
    likeCount: int
    followingCount: int
    videoCount: int