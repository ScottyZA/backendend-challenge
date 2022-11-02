from sqlalchemy import Column, Integer, String
from services.database import Base


class URL(Base):
    '''URL database model'''
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True)
    source_url = Column(String, index=True)
    short_url_key = Column(String, unique=True)
