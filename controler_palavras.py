import json
from random import choice

def carregar_palavras():
    file = open('base.json', 'r', encoding='utf-8').read()
    palavras = json.loads(file.replace("'", '"'))

    return palavras

def buscar_palavra(categoria, letra):
    categoria = categoria.upper()
    palavras = carregar_palavras()
    if categoria in palavras.keys():
        lista_palavras = []
        for palavra in palavras[categoria]:
            if letra.upper() == palavra[0].upper():
                lista_palavras.append(palavra)
        if len(lista_palavras) > 0:
            return choice(lista_palavras)
    return False
