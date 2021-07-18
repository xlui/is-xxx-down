from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Notification(db.Model):
    __tablename__ = 'notification'
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    email = db.Column(db.VARCHAR(256), nullable=False)
    create_time = db.Column(db.DATETIME, default=datetime.now)
    update_time = db.Column(db.DATETIME, default=datetime.now, onupdate=datetime.now)


class Core(db.Model):
    __tablename__ = 'core'
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    key = db.Column(db.VARCHAR(4), nullable=False, unique=True, index=True)
    title = db.Column(db.VARCHAR(128), nullable=False)
    url = db.Column(db.VARCHAR(256), nullable=False)
    is_down = db.Column(db.BOOLEAN, default=False, nullable=False)
    create_time = db.Column(db.DATETIME, default=datetime.now)
    update_time = db.Column(db.DATETIME, default=datetime.now, onupdate=datetime.now)
