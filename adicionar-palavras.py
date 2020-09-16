from controler_palavras import carregar_palavras
import os
from time import sleep

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    limpar_tela()
    file = carregar_palavras()
    n = False
    while not n:
        print('0 - Para sair')
        print('1 - Adicionar Resposta')
        print('2 - Adicionar categoria')
        print('3 - Listar uma categoria')
        n = int(input('==> '))
        limpar_tela()

        if n == 0:
            exit()

        elif n == 1:

            categoria = input('Digite a categoria: ').upper()
            categoria_valida = categoria in file.keys()

            if categoria_valida:
                resposta = input(f'Digite uma resposta pra categoria {categoria}: ')
                if resposta not in file[categoria]:
                    file[categoria].append(resposta)
                    ap = open('base.json', 'w', encoding='utf-8')
                    ap.write(f'{file}')
                    ap.close()
                    print('Resposta adicionadas com sucesso!')
                    sleep(1)
                else:
                    print('Resposta já existe.')
            else:
                print('Essa categoria não existe.')

        elif n == 2:
            categoria = input('Digite a categoria: ').upper()

            if categoria not in file.keys():
                file[categoria] = []
                ap = open('base.json', 'w', encoding='utf-8')
                ap.write(f'{file}')
                ap.close()
                print(f'Categoria {categoria} adicionada com sucesso!')
            else:
                print('Essa categoria já existe.')

        elif n == 3:
            nome_categoria = input('Digite o nome da categoria: ').upper()

            if nome_categoria in file.keys():
                print(f'Categoria "{nome_categoria}": ')
                for i in file[nome_categoria]:
                    print(f"{' '*7}=> {i}")
            else:
                print('Categoria não encontrada.')

        else:
            n = False

menu()