from pydantic import BaseModel


class Article(BaseModel):
    body: str
    author: str
    headline: str
    url: str
    genre: str

    class Config:
        orm_mode = True
