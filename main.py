from fastapi import FastAPI


app = FastAPI()

@app.post("/url")
async def post_url():
    '''Receive a URL and return a unique short-form URL'''
    return {"short_url": "https://tier.app/abcd1234"}


@app.get("/{short_url_key}")
async def get_url():
    '''Receive a short URL and return the original long URL'''
    return {"source_url": "https://example.com"}
