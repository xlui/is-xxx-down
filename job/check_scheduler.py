import arrow
import requests

from db.models import db, get_core


def check_website(app):
    print(f'[Checker] Job start at {arrow.now().format(arrow.FORMAT_ATOM)}')
    with app.app_context():
        core = get_core()
        print(core)
        try:
            resp = requests.get(core.url, timeout=2)
            print(f'[Checker] Successfully ping website {core.url}, resp:{resp}')
            core.is_down = False
            db.session.add(core)
            db.session.commit()
        except Exception as e:
            print(f'[Checker] Failed to ping website {core.url}', e)
            core.is_down = True
            db.session.add(core)
            db.session.commit()
        print(f'[Checker] Job end at {arrow.now().format(arrow.FORMAT_ATOM)}')
