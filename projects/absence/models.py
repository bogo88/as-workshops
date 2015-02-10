from app import db


class Create(db.Document):
    name = db.StringField(max_length=255, required=True)
    surname = db.StringField(max_length=255, required=True)
    absence_start = db.DateTimeField(required=True)
    absence_end = db.DateTimeField(required=True)