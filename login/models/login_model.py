from itertools import count
from typing import Optional
from pydantic import BaseModel, Field
from tinydb import TinyDB , Query


db = TinyDB('db.json')
c = count()

class login_treino(BaseModel):

    def db_model(nome,senha):
        db.insert({'nome':nome,'senha':senha} )
        id: Optional[int] = Field(default_factory= lambda: next(c))
        nome : str
        senha: str
    class Config:
        exclude = 'id'