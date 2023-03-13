from typing import List
from functools import lru_cache

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True, index=True)
    headline = Column(String)
    author = Column(String)
    body = Column(String)
    url = Column(String, nullable=False)
    genre = Column(String)
    source = Column(String)
