import pytest
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from news_api.data.models import Base, Article
from news_api.data.session import engine, get_db
from news_api.dependencies import get_settings

# def get_test_session():
#     # Create a new engine object with a custom connection URL
#     test_engine = create_engine("postgresql://localhost/mydatabase_test")
#
#     # Create a new session factory using the test engine
#     TestSession = sessionmaker(bind=test_engine)
#
#     # Return a new session object
#     return TestSession()



@pytest.fixture(scope="module")
def db_session():
    settings = get_settings()
    # test_engine = create_engine("postgresql://localhost/mydatabase_test")
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
    # print('--------------- ', get_settings().)
    def test_article_valid(self, db_session, valid_article):
        db_session.add(valid_article)
        db_session.commit()
        article = db_session.query(Article).first()
        assert article.body == "body"
        assert article.headline == "headline"
        assert article.url == "url"
        assert article.author == "author"
        assert article.genre == "genre"


#
# class TestBlog:
#     def setup_class(self):
#         Base.metadata.create_all(engine)
#         Session = sessionmaker(bind=engine)
#         self.session = Session()
#         self.valid_article = Article(
#             headline="headline",
#             body="body",
#             url="url",
#             author="author",
#             genre="genre"
#         )
#
#     def teardown_class(self):
#         self.session.rollback()
#         self.session.close()
#
#     def test_valid_article(self):
#         assert self.valid_article.headline == "headline"
#         assert self.valid_article.body == "body"
#         assert self.valid_article.url == "url"
#         assert self.valid_article.author == "author"
#         assert self.valid_article.genre == "genre"
