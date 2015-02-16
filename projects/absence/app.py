import json
from flask import Flask, request, session, redirect, flash, url_for
from pymongo import MongoClient
from bson import json_util
from bson.objectid import ObjectId
from flask_oauth import OAuth


app = Flask(__name__)

client = MongoClient()
app.db = client.as_workshops
oauth = OAuth()
github = oauth.remote_app(
    'github',
    base_url='https://api.github.com',
    request_token_url=None,
    access_token_url='/login/oauth/access_token',
    authorize_url='/login/oauth/authorize',
    consumer_key='89e10c0eddb1abc04c6d',
    consumer_secret='6f7932dce60109dd040acdc15f8b9a1354b18776'

)


def to_json(data):
    """Convert Mongo object(s) to JSON"""
    return json.dumps(data, default=json_util.default)

@github.tokengetter
def get_github_token(token=None):
    return session.get('access_token')

@app.route('/login')
def login():
    return github.authorize(callback=url_for('authorized',
        next=request.args.get('next') or request.referrer or None))

@app.route('/oauth-authorized')
@github.authorized_handler
def oauth_authorized(resp):
    next_url = request.args.get('next') or url_for('index')
    if resp is None:
        flash(u'You denied the request to sign in.')
        return redirect(next_url)

    session['github_token'] = (
        resp['access_token']
    )
    session['github_user'] = resp['user']

    flash('You were signed in as %s' % resp['user'])
    return redirect(next_url)


def absence_by_user(user_id):
    results = app.db.absence.find({'user_id': int(user_id)},
                                 {'id': 1, 'user_id': 1, 'absence_start': 1, 'absence_end': 1, '_id': 0})
    json_results = []
    for result in results:
        json_results.append(result)
    return to_json(json_results)


def absence_by_date(date):
    results = app.db.absence.find({'absence_start': {'$lte': date}, 'absence_end': {'$gte': date}},
                                 {'id': 1, 'user_id': 1, 'absence_start': 1, 'absence_end': 1, '_id': 0})
    json_results = []
    for result in results:
        json_results.append(result)
    return to_json(json_results)

@app.route('/absence', methods=['get'])
def absence_list():
    if request.args.get('date'):
        date = request.args.get('date')
        return absence_by_date(date)

    if request.args.get('user'):
        user_id = request.args.get('user')
        return absence_by_user(user_id)

    results = app.db.absence.find({}, { 'user_id': 1, 'absence_start': 1, 'absence_end': 1, '_id': 1})
    json_results = []
    for result in results:
        json_results.append(result)
    return to_json(json_results)


@app.route('/absence/<absence_id>', methods=['get'])
def absence_detail(absence_id):
    results = app.db.absence.find({'_id': ObjectId(absence_id)})
    json_results = []
    for result in results:
        json_results.append(result)
    return to_json(json_results)


@app.route('/absence', methods=['post'])
def absence_create():
    absence_id = app.db.absence.insert({
        'user_id': request.values.get('user_id'),
        'absence_start': request.values.get('absence_start'),
        'absence_end': request.values.get('absence_end')})
    return to_json([{'action': 'create', 'status': 'success', 'absence_id': absence_id}])


@app.route('/absence/<absence_id>', methods=['put'])
def absence_edit(absence_id):
    absence_start = request.args.get('absence_start') #OR current value
    absence_end = request.args.get('absence_end') #OR current value
    app.db.absence.update({'_id': ObjectId(absence_id)}, {'absence_start': absence_start, 'absence_end': absence_end})
    return to_json([{'action': 'edit', 'status': 'success', 'absence_id': absence_id}])


@app.route('/absence/<absence_id>', methods=['delete'])
def absence_delete(absence_id):
    app.db.absence.remove({'_id': ObjectId(absence_id)})
    return to_json([{'action': 'delete', 'status': 'success', 'absence_id': absence_id}])


if __name__ == '__main__':
    app.run()
