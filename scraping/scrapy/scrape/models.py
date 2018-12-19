from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

from .local import DATABASE

DeclarativeBase = declarative_base()


def db_connect():
    print(URL(**DATABASE))
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(URL(**DATABASE))


def create_reddit_table(engine):
    """"""
    DeclarativeBase.metadata.create_all(engine)


class RedditModel(DeclarativeBase):
    """Sqlalchemy RedditModel model"""
    __tablename__ = "RedditModel"

    id = Column(Integer, primary_key=True)
    title = Column('title', String)
    domain = Column('domain', String, nullable=True)