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

support_subscribe = os.environ.get('SUPPORT_SUBSCRIBE') or False

mail_server = os.environ.get('MAIL_SERVER')
if not mail_server or len(mail_server) == 0:
    print(f'Mail server is invalid. mail_server:{mail_server}')
    sys.exit(1003)

mail_port = os.environ.get('MAIL_PORT')
if not mail_port or len(mail_port) == 0:
    print(f'Mail port is invalid. mail_port:{mail_port}')
    sys.exit(1004)

mail_username = os.environ.get('MAIL_USERNAME')
if not mail_username or len(mail_username) == 0:
    print(f'Mail username is invalid. mail_username:{mail_username}')
    sys.exit(1005)

mail_password = os.environ.get('MAIL_PASSWORD')
if not mail_password or len(mail_password) == 0:
    print(f'Mail password is invalid. mail_password:{mail_password}')
    sys.exit(1006)


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SCHEDULER_API_ENABLED = True
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{db_file}'
    MAIL_SERVER = mail_server
    MAIL_PORT = mail_port
    MAIL_USE_TLS = True
    MAIL_USERNAME = mail_username
    MAIL_PASSWORD = mail_password
    MAIL_DEFAULT_SENDER = mail_username

    @staticmethod
    def init_app(app):
        pass
