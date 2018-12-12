from sqlalchemy.orm import sessionmaker
from .models import RedditModel, db_connect, create_deals_table


class nlp_data_science_pipeline(object):
    """Livingsocial pipeline for storing scraped items in the database"""
    def __init__(self):
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates deals table.
        """
        engine = db_connect()
        create_deals_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save deals in the database.

        This method is called for every item pipeline component.

        """
        session = self.Session()
        rm = RedditModel(**item)

        try:
            session.add(rm)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item