import json
import os
from pprint import pprint
from typing import TypedDict

class Movie(TypedDict):
    title: str
    year: int
    rating: float
    characters: list[str]


string_filme = '{"title": "The Matrix", "year": 1999, "rating": 8.7, "characters": ["Neo", "Morpheus"]}'
string_json = '{"nome": "Luiz", "sobrenome": "Miranda", "idade": 32, "endereço": {"rua": "rua vergueiro", "numero": 123}}'

filme: Movie = json.loads(string_filme)
pprint(filme) 
nome = json.loads(string_json)
pprint(nome)
os.system('clear')

print(json.dumps(filme, indent=2, ensure_ascii=False))