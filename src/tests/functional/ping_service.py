import time

import requests

from settings import test_settings

while True:
    try:
        requests.get(f'{test_settings.sevice_url}/')
        break
    except:
        time.sleep(1)

