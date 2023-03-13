import logging

from pydantic import BaseModel, Field, conint, validator
from fastapi import APIRouter, HTTPException, Depends, Query, Request


from news_api.data.session import get_db
from news_api.data import models, schemas
from sqlalchemy.orm import Session

from sqlalchemy.orm import Session
from news_api.data import crud

from news_api.data.schemas import Article as SchemaArticle


router = APIRouter()

logger = logging.getLogger(__name__)


@router.get("/news")
def get_all_news(db: Session = Depends(get_db), limit=Query(default=7), offset=Query(default=0)):
    return crud.get_all_article(db=db, limit=limit, offset=offset)


@router.post("/", status_code=201, response_model=SchemaArticle)
def save_article(request: Request, payload: SchemaArticle, db: Session = Depends(get_db)):
    return crud.create_article(db=db, article=payload)



