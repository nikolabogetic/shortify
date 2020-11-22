from flask import current_app as app
from . import db


@app.errorhandler(404)
def not_found_error(error):
    return '404', 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return '500', 500
