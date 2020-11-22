import codext
from flask import request, redirect
from flask import current_app as app
from .models import Url, db

@app.route('/')
def home():
    return 'ok', 200

@app.route('/<short_code>')
def retrieve(short_code):
    # Decode the base62 short code into numeric index
    index = int(codext.decode(short_code, 'base62'))
    url = Url.query.filter_by(id=index).first_or_404()
    return redirect(url.url, code=302)

@app.route('/submit', methods=['POST'])
def parse_request():
    full_url = request.get_data().decode("utf-8")
    new_url = Url(url=full_url)
    db.session.add(new_url)
    db.session.flush()
    # Get index of newly created row
    index = new_url.id
    # Turn index into short code (int->str->zfill->encode)
    str_index = str(index).zfill(8)
    short_code = codext.encode(str_index, 'base62')
    db.session.commit()

    return short_code