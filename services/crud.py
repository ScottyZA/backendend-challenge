from sqlalchemy.orm import Session
from url_shortener import models, schemas, utils


def get_url_data_by_key(database: Session, short_url_key: str) -> models.URL:
    ''''Get source URL via short URL key lookup'''
    return (
        database.query(models.URL)
        .filter(models.URL.short_url_key == short_url_key)
        .first()
    )


def create_short_url(database: Session, source_url: schemas.SourceURL):
    ''''Create a database entry creating a short URL key'''
    short_url_key = utils.generate_short_url_key()

    while get_url_data_by_key(database, short_url_key):
        short_url_key = utils.generate_short_url_key()

    database_url = models.URL(
        source_url=source_url.source_url,
        short_url_key=short_url_key
    )
    database.add(database_url)
    database.commit()
    database.refresh(database_url)
    return database_url
