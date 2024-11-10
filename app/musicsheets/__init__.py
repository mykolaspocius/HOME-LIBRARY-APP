from flask import Blueprint

bp = Blueprint('musicsheets', __name__)

from app.musicsheets import routes