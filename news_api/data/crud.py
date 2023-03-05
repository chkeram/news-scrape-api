import logging
from sqlalchemy.orm import Session
from news_api.data import models, schemas


def get_article_by_id(db: Session, article_id: int):
    return db.query(models.Article).filter(models.Article.id == article_id).first()


def get_all_article(db: Session):
    return db.query(models.Article).all()


def create_article(db: Session, article: schemas.Article):
    db_article = models.Article(**article.dict())
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article
