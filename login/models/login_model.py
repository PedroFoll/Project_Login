from itertools import count
from typing import Optional
from pydantic import BaseModel, Field
from tripleTdb import db

c = count

class login_treino(BaseModel):
    id : db.Column(db.Integer, primary_key=True, autoincrement = True)
    nome : db.Column(db.String(100))
    senha : db.Column(db.String(15))
    class Config:
        exclude = 'id'