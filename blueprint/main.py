# -*- coding:utf-8 -*-
from flask import Flask
import logging
from logging.handlers import TimedRotatingFileHandler

from views.simple_page import simple_page

app = Flask(__name__)
app.register_blueprint(simple_page, url_prefix="/simple_page")


@app.route('/')
def hello_world():
    app.logger.info("Info message")
    app.logger.warning("Warning msg")
    app.logger.error("Error msg!!!")
    return 'Hello, World!'


if __name__ == '__main__':
    app.debug = True
    formatter = logging.Formatter(
        "[%(asctime)s][%(filename)s:%(lineno)d][%(levelname)s][%(thread)d] - %(message)s")
    handler = TimedRotatingFileHandler(
        "flask.log", when="D", interval=1, backupCount=15,
        encoding="UTF-8", delay=False, utc=True)
    app.logger.addHandler(handler)
    handler.setFormatter(formatter)

    app.run()