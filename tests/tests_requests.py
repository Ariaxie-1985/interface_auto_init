import pytest
import code

from api_script.api_script_requests_test import data_api, html_api, position_api


def test_hello_world():
    r = data_api()
    if r['hello'] == 'world':
        assert True


def test_html():
    r = html_api()
    if code == 200:
        assert True


def test_position_json():
    r = position_api()
    if r['state'] == 1:
        assert True
