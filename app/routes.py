import codext
from flask import request, redirect
from flask import current_app as app
from .models import Url, db

@app.route('/')
def home():
    return 'Welcome to Shortify! Usage: https://github.com/nikolabogetic/shortify', 200

@app.route('/<short_code>')
def retrieve(short_code):
    """Get full URL from short code and issue redirect"""
    # Decode the base62 short code into numeric index
    try:
        index = int(codext.decode(short_code, 'base62'))
        url = Url.query.filter_by(id=index).first_or_404()
    except ValueError as e:
        app.logger.error(e)
        return 'This value is not supported. Expecting base62-encoded numeric strings.', 400
    return redirect(url.url, code=302)
    

@app.route('/submit', methods=['POST'])
def parse_request():
    """Get URL from request body and create a database record"""
    full_url = request.get_data().decode("utf-8")
    new_url = Url(url=full_url)
    db.session.add(new_url)
    db.session.flush()
    # Get index of newly created row
    index = new_url.id
    db.session.commit()
    # Turn index into short code (int->str->zfill->encode)
    str_index = str(index).zfill(8)
    short_code = codext.encode(str_index, 'base62')
    short_url = request.url_root + short_code
    return short_url