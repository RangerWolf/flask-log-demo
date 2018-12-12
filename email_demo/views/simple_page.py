from flask import Blueprint
from flask import current_app

simple_page = Blueprint('simple_page', __name__)


@simple_page.route('/')
def show():
    current_app.logger.info("simple page info...")
    current_app.logger.warning("warning msg!")
    current_app.logger.error("ERROR!!!!!")
    return "simple page"