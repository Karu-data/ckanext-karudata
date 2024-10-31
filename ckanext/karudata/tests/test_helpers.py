"""Tests for helpers.py."""

import ckanext.karudata.helpers as helpers


def test_karudata_hello():
    assert helpers.karudata_hello() == "Hello, karudata!"
