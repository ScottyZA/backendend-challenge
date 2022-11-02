import secrets
import string
from utils.config import get_settings


def generate_short_url_key(length: int = 8) -> str:
    '''Generate a random short url key'''
    chars = string.ascii_uppercase + string.digits
    return "".join(secrets.choice(chars) for _ in range(length))


def generate_short_url(short_url_key: str = '') -> str:
    base_short_url = get_settings().base_short_url

    return f'{base_short_url}{short_url_key}'
