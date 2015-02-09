from contextlib import closing
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash

# configuration
DATABASE = '/tmp/app.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('APP_SETTINGS', silent=True)


def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


@app.route('/absence', methods=['get'])
def absence_list():
    cur = g.db.execute('select * from absence')
    absence = cur.fetchall()
    return str(absence)


@app.route('/absence/<int:absence_id>', methods=['get'])
def absence_detail(absence_id):
    return 'Absence detail {}'.format(absence_id)


@app.route('/absence', methods=['post'])
def absence_create():
    g.db.execute(
        'insert into absence (user_id, absence_status, absence_type, absence_start, absence_end) values (?, ?, ?, ?, ?)',
        [requests.post['user_id'],
         requests.post['absence_status'],
         requests.post['absence_type'],
         requests.post['absence_start'],
         requests.post['absence_end']]
    )
    g.db.commit()
    return 'Absence create'


@app.route('/absence/<int:absence_id>', methods=['put'])
def absence_edit(absence_id):
    return 'Absence edit {}'.format(absence_id)


@app.route('/absence/<int:absence_id>', methods=['delete'])
def absence_delete(absence_id):
    return 'Absence delete {}'.format(absence_id)


if __name__ == '__main__':
    app.run()
