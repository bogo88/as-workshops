import json
import isodate
from flask import Flask
from pymongo import MongoClient
from urllib3 import request
from bson import json_util

app = Flask(__name__)

client = MongoClient()
db = client.as_workshops


def to_json(data):
    """Convert Mongo object(s) to JSON"""
    return json.dumps(data, default=json_util.default)

@app.route('/absence', methods=['get'])
def absence_list():
    results = db['absences'].find()
    json_results = []
    for result in results:
        json_results.append(result)
    return to_json(json_results)


@app.route('/absence/date/<absence_date>', methods=['get'])
def absence_detail(absence_date):
    results = db['absences'].find({'absence_start': {'$lte': absence_date}, 'absence_end': {'$gte': absence_date}})
    json_results = []
    for result in results:
        json_results.append(result)
    return to_json(json_results)


@app.route('/absence', methods=['post'])
def absence_create():
    record = {
        'name': "TestName",
        'surname': "TestSurname",
        'absence_start': "2015-01-02",
        'absence_end': "2015-01-09",
        #'name': request.POST['name'],
        #'surname': request.POST['surname'],
        #'absence_start': request.POST['absence_start'],
        #'absence_end': request.POST['absence_end']
    }
    absences = db.absence
    absence_id = absences.insert(record)
    return 'Absence {} created\n'.format(absence_id)
    #return 'Absence  created\n'


@app.route('/absence/<int:absence_id>', methods=['put'])
def absence_edit(absence_id):
    return 'Absence edit {}\n'.format(absence_id)


@app.route('/absence/<int:absence_id>', methods=['delete'])
def absence_delete(absence_id):
    return 'Absence delete {}\n'.format(absence_id)


if __name__ == '__main__':
    app.run()
