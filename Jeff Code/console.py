from listing import Listing
from scrape_craigslist import ListingParser, ListingBuilder, CraigsListScraper
import sqlalchemy
from listing import Base


engine = sqlalchemy.create_engine('sqlite:///craigslist.db', echo=True)

Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
