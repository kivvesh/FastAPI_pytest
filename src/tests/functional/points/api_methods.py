import requests
from src.tests.functional.settings import test_settings

def get_items():
    req = requests.get(f'{test_settings.sevice_url}/items')
    return req

def post_items(data):
    req = requests.post(f'{test_settings.sevice_url}/add',json=data)
    return req

def delete_items(data):
    req = requests.post(f'{test_settings.sevice_url}/items',json=data)
    return req
