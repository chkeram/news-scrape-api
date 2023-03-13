import logging
from sqlalchemy.orm import Session
from news_api.data import models, schemas


def get_article_by_url(db: Session, url: int):
    return db.query(models.Article).filter(models.Article.url == url).first()


def get_all_article(db: Session, limit: int, offset: int):
    return db.query(models.Article).offset(offset).limit(limit).all()


def create_article(db: Session, article: schemas.Article):
    db_article = models.Article(**article.dict())
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article
