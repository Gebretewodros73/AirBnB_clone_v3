#!/usr/bin/python3
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

# Wildcard import for PEP8, ignore the warning
from api.v1.views.index import *

