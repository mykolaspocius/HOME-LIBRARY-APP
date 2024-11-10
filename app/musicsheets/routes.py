from app.musicsheets import bp
from flask import render_template
from flask_login import login_required
from app.db_models.item import *

@bp.route('/')
@login_required
def index():
    return render_template("musicsheets/index.html")


