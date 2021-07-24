import os
import sys

work_dir = os.path.dirname(os.path.abspath(__file__))
db_dir = os.path.join(os.path.dirname(work_dir), 'db')
db_file = os.path.join(db_dir, 'data.sqlite')
root_key = 'root'

title = os.environ.get('TITLE') or 'Google'
if not title or len(title) == 0:
    print(f'TITLE is invalid. title:{title}')
    sys.exit(1001)

url = os.environ.get('URL') or 'https://google.com'
if not url or len(url) == 0:
    print(f'URL is invalid. url:{url}')
    sys.exit(1002)

support_subscribe = ('FALSE' == os.environ.get('SUPPORT_SUBSCRIBE').upper()) or False


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SCHEDULER_API_ENABLED = True
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{db_file}'

    @staticmethod
    def init_app(app):
        pass
