from pydantic import BaseModel

class SourceURL(BaseModel):
    '''Source URL schema'''
    source_url: str
