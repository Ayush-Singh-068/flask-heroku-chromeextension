from flask import Blueprint, request
from app.services.summary_service import get_website_summary
from config.constants import *
# Define a Flask Blueprint for your routes
api = Blueprint('api', __name__)


@api.route('/', methods=['GET', 'POST'])
def handle_request():
    api_key = request.headers.get('apiKey')
    url = request.args.get('input') or DEFAULT_SITE_URL
    points = request.args.get('points') or 'false'
    isPoints = points.lower() == 'true'
    return get_website_summary(url, isPoints, api_key)
