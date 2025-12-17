from requests import Session
from pydantic import parse_obj_as

from .objects import *

class TokCounter:
    headers = {
        'origin': 'https://tokcounter.com',
        'referer': 'https://tokcounter.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
    }
    url = 'https://tiktok.livecounts.io/user/{}'.format
    session = Session()

    @classmethod
    def search(cls, username : str):
        _req = cls.session.get(cls.url(f'search/{username}'), headers = cls.headers)
        return parse_obj_as(list[Search], _req.json()['userData'])


    @classmethod
    def stats(cls, id: str):
        _req = cls.session.get(cls.url(f'stats/{id}'), headers = cls.headers)
        return Stats(**_req.json())