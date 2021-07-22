from flask import render_template

from config.config import root_key
from db.models import Core
from . import main


@main.route('/', methods=['GET'])
def index():
    core = get_core()
    return render_template('index.html', title=core.title, url=core.url, is_down=core.is_down)


def get_core():
    core = Core.query.filter_by(key=root_key).first()
    if not core:
        raise RuntimeError('Failed to load core config!')
    return core
