from flask import Flask
from flask_bootstrap import Bootstrap

from config.config import Config
from config.config import root_key, title, url
from db.models import db, Core


def create_app():
    bootstrap = Bootstrap()
    app = Flask(__name__)
    app.config.from_object(Config)

    bootstrap.init_app(app)
    db.init_app(app)

    with app.app_context():
        print(f'uri: {app.config["SQLALCHEMY_DATABASE_URI"]}')
        db.create_all()
        print('load env...')
        core = Core.query.filter_by(key=root_key).first()
        print(f'exist core config: {core}')
        if not core:
            core = Core(
                key=root_key,
                title=title,
                url=url,
                is_down=False
            )
            db.session.add(core)
            db.session.commit()
        else:
            core.title = title
            core.url = url
            core.is_down = False
            db.session.add(core)
            db.session.commit()
        print('load env...done')

    from .main import main
    app.register_blueprint(main)

    return app
