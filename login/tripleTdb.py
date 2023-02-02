from tinydb import TinyDB , Query
from models import login_model


db = TinyDB('database.json')


class Db_Methods (db.model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome : db.Column(db.String(100))
    senha : db.Column(db.String(15))