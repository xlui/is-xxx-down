from flask import Flask
from flask_bootstrap import Bootstrap

from config.config import Config
from config.config import root_key, title, url
from db.models import db, Core
from job import scheduler


def create_app():
    bootstrap = Bootstrap()
    app = Flask(__name__)
    app.config.from_object(Config)

    bootstrap.init_app(app)
    db.init_app(app)
    scheduler.init_app(app)

    with app.app_context():
        print(f'uri: {app.config["SQLALCHEMY_DATABASE_URI"]}')
        db.create_all()
        print('loading env...')
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
        print('loading env...done')

        print('loading scheduler...')
        from job.check_scheduler import check_website
        scheduler.add_job(
            id='check_website',
            func=check_website,
            trigger='interval',
            seconds=5,
            args=[app])
        scheduler.start()
        print('loading scheduler...done')

    from .main import main
    app.register_blueprint(main)

    return app
