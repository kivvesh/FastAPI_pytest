import requests
import pytest
import json

from src.models.models import Name

from http import HTTPStatus


@pytest.mark.asyncio
async def test_get_items_status(
    make_get_request
):
    body, headers, status = await make_get_request(
        'http://127.0.0.1:8000/items'
    )

    assert status == 200
    assert [Name(**i) for i in body]   #body == 1#[Name.parse_raw(**i) for i in body]

@pytest.mark.asyncio
async def test_get_items_data(
    make_get_request
):
    body, headers, status = await make_get_request(
        'http://127.0.0.1:8000/items'
    )

    assert [Name(**i) for i in body]

@pytest.mark.asyncio
async def test_post_add_status(
    make_post_request
):
    for i in range(3):
        status = await make_post_request(
            'http://127.0.0.1:8000/add',
            data = {'name':'1'}
        )
        assert status == 200




# @pytest.mark.asyncio
# async def test_get_items_data(
#     make_get_request
# ):
#     body, headers, status = await make_get_request(
#         'http://127.0.0.1:8000/items'
#     )
#
#     assert body == 1

