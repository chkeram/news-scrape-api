from pydantic import BaseModel
from typing import List


class Article(BaseModel):
    body: str
    author: List[str]
    headline: str
    url: str
    genre: str
    source: str

