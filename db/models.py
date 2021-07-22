from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

from config.config import root_key

db = SQLAlchemy()


class Notification(db.Model):
    __tablename__ = 'notification'
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    email = db.Column(db.VARCHAR(256), nullable=False)
    create_time = db.Column(db.DATETIME, default=datetime.now)
    update_time = db.Column(db.DATETIME, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return f'Notification[id={self.id}, email={self.email}, create_time={self.create_time}, update_time={self.update_time}]'


class Core(db.Model):
    __tablename__ = 'core'
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    key = db.Column(db.VARCHAR(4), nullable=False, unique=True, index=True)
    title = db.Column(db.VARCHAR(128), nullable=False)
    url = db.Column(db.VARCHAR(256), nullable=False)
    is_down = db.Column(db.BOOLEAN, default=False, nullable=False)
    create_time = db.Column(db.DATETIME, default=datetime.now)
    update_time = db.Column(db.DATETIME, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return f'Core[id={self.id}, key={self.key}, title={self.title}, ' \
               f'url={self.url}, is_down={self.is_down}, ' \
               f'create_time={self.create_time}, update_time={self.update_time}]'


def get_core():
    core = Core.query.filter_by(key=root_key).first()
    if not core:
        raise RuntimeError('Failed to load core config!')
    return core
