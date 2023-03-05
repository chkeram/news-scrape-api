from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True, index=True)
    headline = Column(String)
    author = Column(String)
    body = Column(String)
    url = Column(String)
    genre = Column(String)
    # publishedAt = Column(DateTime)
    # source_id = Column(Integer, ForeignKey("sources.id"))
    # source = relationship("Source")


    # TODO: inspiration to return top5 for all genres
    # @staticmethod
    # @lru_cache
    # def expertise_slugs(session) -> set[str]:
    #     """
    #     Loads all expertise_slugs in all languages into a set
    #     """
    #     slugs = session.query(Expertise).with_entities(distinct(Expertise.expertise_slug)).all()
    #     return set([s[0] for s in slugs])