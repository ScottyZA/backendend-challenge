from pydantic import BaseModel


class SourceURL(BaseModel):
    '''Source URL schema'''
    source_url: str

    class Config:
        orm_mode = True


class URLInfo(SourceURL):
    '''URL Information schema'''
    short_url_key: str
    short_url: str
