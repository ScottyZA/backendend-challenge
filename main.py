import validators
from fastapi import FastAPI, HTTPException
from url_shortener.schemas import SourceURL


app = FastAPI()

@app.post("/url")
async def post_url(url: SourceURL):
    '''Receive a URL and return a unique short-form URL'''
    if not validators.url(url.source_url):
        raise HTTPException(status_code=400, detail="Provided URL is not valid")
    return {"short_url": "https://tier.app/abcd1234"}


@app.get("/{short_url_key}")
async def get_url():
    '''Receive a short URL and return the original long URL'''
    return {"source_url": "https://example.com"}
