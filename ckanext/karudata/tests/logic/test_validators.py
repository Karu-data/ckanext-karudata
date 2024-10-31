"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.karudata.logic import validators


def test_karudata_reauired_with_valid_value():
    assert validators.karudata_required("value") == "value"


def test_karudata_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.karudata_required(None)
