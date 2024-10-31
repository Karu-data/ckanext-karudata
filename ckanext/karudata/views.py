from flask import Blueprint


karudata = Blueprint(
    "karudata", __name__)


def page():
    return "Hello, karudata!"


karudata.add_url_rule(
    "/karudata/page", view_func=page)


def get_blueprints():
    return [karudata]
