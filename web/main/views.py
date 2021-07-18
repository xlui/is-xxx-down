from flask import render_template

from . import main


@main.route('/', methods=['GET'])
def index():
    return render_template('index.html', title='VCB-S', is_down=False)
