from src.models.models import Name
from src.tests.functional.points.api_methods import get_items,post_items

def test_get_items_status():
    req = get_items()
    assert req.status_code == 200

def test_get_items_correct_data():
    req = get_items()
    assert [Name(**i) for i in req.json()]

def test_post_add_status():
    data = {'name':'name'}
    for i in range(3):
        req = post_items(data)
        assert req.status_code == 200
