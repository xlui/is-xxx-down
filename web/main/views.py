import arrow
from flask import render_template, request, abort, current_app

from db.models import get_core, Notification, db
from job.check_scheduler import check_website
from mail import send_mail
from . import main


@main.route('/', methods=['GET'])
def index():
    core = get_core()
    return render_template(
        'index.html',
        title=core.title,
        url=core.url,
        is_down=core.is_down,
        support_subscribe=core.support_subscribe
    )


@main.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form['email']
    if not email:
        return abort(401, 'Failed to parse email')
    notification = Notification.query.filter_by(email=email).first()
    if notification:
        return abort(400, 'You have already subscribed.')
    else:
        notification = Notification(email=email)
        db.session.add(notification)
        db.session.commit()
        return 'Success', 200


@main.route('/check', methods=['GET', 'POST'])
def check():
    check_website(current_app)
    return 'OK, I have checked the website again.'


@main.route('/send/<email>', methods=['GET'])
def send(email):
    send_mail(
        f'test 123\nnow: {arrow.now().format(arrow.FORMAT_ATOM)} ',
        [email])
