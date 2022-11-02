import validators
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from url_shortener import models, schemas
from url_shortener.utils import generate_short_url
from services.database import SessionLocal, engine
from services import crud


app = FastAPI()
# TODO: lock down CORS policy
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=engine)


def get_db():
    ''''DB Session. Use thoughout the request'''
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()


@app.post("/url", response_model=schemas.URLInfo)
async def post_url(
    url: schemas.SourceURL,
    database: Session = Depends(get_db)
):
    '''Receive a URL and return a unique short-form URL'''
    if not validators.url(url.source_url):
        raise HTTPException(
            status_code=400,
            detail="Provided URL is not valid"
        )

    database_url = crud.create_short_url(database=database, source_url=url)

    database_url.short_url = generate_short_url(database_url.short_url_key)

    return database_url


@app.get("/{short_url_key}", response_model=schemas.SourceURL)
async def get_url(
    short_url_key: str,
    database: Session = Depends(get_db)
):
    '''Receive a short URL and return the original long URL'''

    database_url = crud.get_url_data_by_key(database, short_url_key)

    if database_url:
        return database_url
    else:
        message = f"Source URL for '{short_url_key}' key not found"
        raise HTTPException(status_code=404, detail=message)
