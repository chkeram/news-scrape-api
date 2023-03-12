from pydantic import BaseModel, validator


class Article(BaseModel):
    body: str
    author: str
    headline: str
    url: str
    genre: str
    source: str

    @validator('author', pre=True, always=True)
    def set_author(cls, v):
        if isinstance(v, list):
            return ', '.join(v)
        return v

    class Config:
        orm_mode = True
