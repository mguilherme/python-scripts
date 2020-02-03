import logging
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

import requests


def log_config():
    filename = f'{splitext(basename(__file__))[0]}.log'
    path: str = dirname(__file__)
    logging.basicConfig(filename=join(path, filename), level=logging.ERROR)


def request_quote() -> str:
    response = requests.get(url='https://api.chucknorris.io/jokes/random')
    content: dict = response.json()
    return content['value']


log_config()
print(request_quote())
