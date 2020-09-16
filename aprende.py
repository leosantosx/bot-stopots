import json

def carregar_palavras():
    file = open('base.json', 'r', encoding='utf-8').read()
    palavras = json.loads(file.replace("'", '"'))

    return palavras

def conta_vogais(resposta):
    vogais = 'AEIOU'
    return sum([resposta.count(i) for i in vogais])

def adicionar_resposta(categoria, resposta, primeira_letra):
    resposta = resposta.upper()
    categoria = categoria.upper()
    banco = carregar_palavras()
    num_vogais = conta_vogais(resposta)
    if len(resposta) > 2 and num_vogais >= 2 and len(categoria) > 0 and resposta[0] == primeira_letra:
        if categoria in banco.keys():
            if resposta not in banco[categoria]:
                banco[categoria].append(resposta)
        else:
            banco[categoria] = [resposta]

    ap = open('base.json', 'w', encoding='utf-8')
    ap.write(f'{banco}')
    ap.close()

