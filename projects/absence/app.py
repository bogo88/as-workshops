import json
from flask import Flask, request
from pymongo import MongoClient
from bson import json_util
from bson.objectid import ObjectId


app = Flask(__name__)

client = MongoClient()
db = client.as_workshops


def to_json(data):
    """Convert Mongo object(s) to JSON"""
    return json.dumps(data, default=json_util.default)


def absence_by_user(user_id):
    results = db.absence.find({'user_id': int(user_id)},
                                 {'user_id': 1, 'absence_start': 1 ,'absence_end': 1, '_id': 0})
    json_results = []
    for result in results:
        json_results.append(result)
    return to_json(json_results)


def absence_by_date(date):
    results = db.absence.find({'absence_start': {'$lte': date}, 'absence_end': {'$gte': date}},
                                 {'user_id': 1, 'absence_start': 1, 'absence_end': 1, '_id': 0})
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

    results = db.absence.find({}, {'user_id': 1, 'absence_start': 1, 'absence_end': 1, '_id': 1})
    json_results = []
    for result in results:
        json_results.append(result)
    return to_json(json_results)


@app.route('/absence/<absence_id>', methods=['get'])
def absence_detail(absence_id):
    results = db.absence.find({'_id': ObjectId(absence_id)})
    json_results = []
    for result in results:
        json_results.append(result)
    return to_json(json_results)


@app.route('/absence', methods=['post'])
def absence_create():
    absence_id = db.absence.insert({
        'user_id': request.values.get('user_id'),
        'absence_start': request.values.get('absence_start'),
        'absence_end': request.values.get('absence_end')})
    return to_json([{'action': 'create', 'status': 'success', 'absence_id': absence_id}])


@app.route('/absence/<absence_id>', methods=['put'])
def absence_edit(absence_id):
    absence_start = request.args.get('absence_start') #OR current value
    absence_end = request.args.get('absence_end') #OR current value
    db.absence.update({'_id': ObjectId(absence_id)}, {'absence_start': absence_start, 'absence_end': absence_end})
    return to_json([{'action': 'edit', 'status': 'success', 'absence_id': absence_id}])


@app.route('/absence/<absence_id>', methods=['delete'])
def absence_delete(absence_id):
    db.absence.remove({'_id': ObjectId(absence_id)})
    return to_json([{'action': 'delete', 'status': 'success', 'absence_id': absence_id}])


if __name__ == '__main__':
    app.run()
