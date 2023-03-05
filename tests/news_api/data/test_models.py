import pytest
import logging

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from news_api.data.models import Base, Article
from news_api.data.session import engine, get_db
from news_api.dependencies import get_settings


@pytest.fixture(scope="module")
def db_session():
    settings = get_settings()
    test_engine = create_engine(f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}/{settings.POSTGRES_DB}")
    Base.metadata.create_all(test_engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.rollback()
    session.close()


@pytest.fixture(scope="module")
def valid_article():
    return Article(
        headline="headline",
        body="body",
        url="url",
        author="author",
        genre="genre"
    )


class TestModels:

    def test_article_valid(self, db_session, valid_article):
        db_session.add(valid_article)
        db_session.commit()
        article = db_session.query(Article).first()
        assert article.body == "body"
        assert article.headline == "headline"
        assert article.url == "url"
        assert article.author == "author"
        assert article.genre == "genre"

    # @pytest.mark.xfail(raises=IntegrityError)
    def test_author_no_url(self, db_session):
        article = Article(
            headline="headline",
            body="body",
            author="author",
            genre="genre"
        )
        db_session.add(article)
        try:
            db_session.commit()
            logging.info("()()()()()()()()()()()() CORRECT")
        except IntegrityError:
            logging.info("()()()()()()()()()()()() Exception")
            db_session.rollback()
