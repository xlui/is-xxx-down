import os
import pathlib
import sys

work_dir = os.path.dirname(os.path.abspath(__file__))
db_file = '/data/is-xxx-down/data.sqlite'
root_key = 'root'

secret = os.environ.get('SECRET') or 'gRu4FmQ10xEr2TY5Ko7GZLtsjbfMvCy3ISpBdeNzVU9qaclkJAO8HwhiWD6XnP'
if not secret or len(secret) == 0:
    print(f'SECRET is invalid. secret:{secret}')
    sys.exit(1001)

domain = os.environ.get('DOMAIN') or 'http://127.0.0.1:5000/'
if not domain:
    print(f'DOMAIN is invalid. domain:{domain}')
    sys.exit(1002)

title = os.environ.get('TITLE') or ''
if not title or len(title) == 0:
    print(f'TITLE is invalid. title:{title}')
    sys.exit(1003)

url = os.environ.get('URL') or ''
if not url or len(url) == 0:
    print(f'URL is invalid. url:{url}')
    sys.exit(1004)


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_DATABASE_URI = f'sqlite:///data.sqlite'

    @staticmethod
    def init_app(app):
        pass
