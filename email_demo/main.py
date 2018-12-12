# -*- coding:utf-8 -*-
from flask import Flask
import logging
from logging.handlers import TimedRotatingFileHandler
from logging.handlers import SMTPHandler

from views.simple_page import simple_page

app = Flask(__name__)
app.register_blueprint(simple_page, url_prefix="/simple_page")


@app.route('/')
def hello_world():
    app.logger.info("Info message")
    app.logger.warning("Warning msg")
    app.logger.error("Error msg----1")
    app.logger.error("Error msg----2")
    app.logger.error("Error msg----3")
    return 'Hello, World!'


if __name__ == '__main__':
    app.debug = True

    # File and Console handler & formtter
    formatter = logging.Formatter(
        "[%(asctime)s][%(module)s:%(lineno)d][%(levelname)s][%(thread)d] - %(message)s")
    handler = TimedRotatingFileHandler(
        "flask.log", when="D", interval=1, backupCount=15,
        encoding="UTF-8", delay=False, utc=True)
    app.logger.addHandler(handler)
    handler.setFormatter(formatter)

    # Email Handler
    mail_handler = SMTPHandler(
        mailhost='10.64.xxx,yyy',
        fromaddr='flask-admin@abc.com',
        toaddrs=['superman@abc.com'],
        subject='Flask Application Error'
    )
    mail_handler.setLevel(logging.ERROR)
    mail_handler.setFormatter(logging.Formatter(
        "[%(asctime)s][%(module)s:%(lineno)d][%(levelname)s][%(thread)d] - %(message)s"
    ))
    app.logger.addHandler(mail_handler)

    app.run()