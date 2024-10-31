"""Tests for views.py."""

import pytest

import ckanext.karudata.validators as validators


import ckan.plugins.toolkit as tk


@pytest.mark.ckan_config("ckan.plugins", "karudata")
@pytest.mark.usefixtures("with_plugins")
def test_karudata_blueprint(app, reset_db):
    resp = app.get(tk.h.url_for("karudata.page"))
    assert resp.status_code == 200
    assert resp.body == "Hello, karudata!"
