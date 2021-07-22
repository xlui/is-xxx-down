from flask import render_template

from db.models import get_core
from . import main


@main.route('/', methods=['GET'])
def index():
    core = get_core()
    return render_template('index.html', title=core.title, url=core.url, is_down=core.is_down)
