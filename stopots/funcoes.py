from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from functools import partial
from time import sleep
from variaveis import *
from controler_palavras import buscar_palavra
from aprende import adicionar_resposta
import os

def iniciar(browser, botao_entrada, nome=''):
    limpar_tela()
    print('Carregando...')

    wdw = WebDriverWait(browser, 25)

    browser.get(url)
    wdw.until(
        partial(espera_elemento, By.XPATH, botao_entrada),
        '"Botão entrar" não foi encontrado'
    )
    browser.find_element_by_xpath(botao_entrada).click()

    if 'Twitter' in browser.title:
        print('Entrando com o twitter...')
        user = input('Digite o usuário/email: ')
        password = input('Digite a senha: ')
        browser.find_element_by_xpath(input_user_twitter).send_keys(user)
        browser.find_element_by_xpath(input_pass_twitter).send_keys(password)
        browser.find_element_by_xpath(input_submit_twitter).click()
    elif 'Facebook' in browser.title:
        print('Entrando com o Facebook...')
        user = input('Digite o email/telefone: ')
        password = input('Digite a senha: ')
        browser.find_element_by_xpath(input_user_facebook).send_keys(user)
        browser.find_element_by_xpath(input_pass_facebook).send_keys(password)
        browser.find_element_by_xpath(input_submit_facebook).click()
    else:

        if len(nome) > 0:
            wdw.until(
                partial(espera_elemento, By.XPATH, input_nome_jogador),
                '"Botão nome jogador" não foi encontrado'
            )

            input_name = browser.find_element_by_xpath(input_nome_jogador)
            input_name.clear()
            input_name.send_keys(nome)

    wdw.until(
        partial(espera_elemento, By.XPATH, botao_iniciar),
        '"Botão iniciar" não foi encontrado'
    )

    button_jogar = browser.find_element_by_xpath(botao_iniciar)
    button_jogar.click()

def iniciar_jogo(browser):
    limpar_tela()
    print('1 - Entrar com Twitter.')
    print('2 - Entrar com Facebook.')
    print('3 - Entrar com nome.')
    print('4 - Entrar como anônimo')
    tipo_entrada = int(input('=> '))
    if tipo_entrada == 1:
        iniciar(browser, botao_entrar_twitter)
    elif tipo_entrada == 2:
        iniciar(browser, botao_entrar_facebook)
    elif tipo_entrada == 3:
        nome_jogador = input("Digite o nome: ")
        iniciar(browser, botao_entrar, nome_jogador)
    elif tipo_entrada == 4:
        iniciar(browser, botao_entrar)
    else:
        print('Resposta invalida.')
        sleep(2)
        iniciar_jogo(browser)

def espera_elemento(by, elemento, browser):
    el = browser.find_elements(by, elemento)
    return bool(el)

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def pegar_letra_atual(browser):
    letra = browser.find_element_by_xpath(letra_atual).text

    if len(letra) > 0:
        return letra

    return '?'

def escrever_resposta(browser, letra):
    labels = browser.find_elements_by_xpath(label_inputs_palavras)
    if bool(labels):
        for label in labels:
            categoria = label.find_element_by_tag_name('span').text

            input = label.find_element_by_tag_name('input')
            if len(input.get_attribute('value')) == 0:
                resposta = buscar_palavra(categoria, letra)
                if resposta:
                    limpar_tela()
                    print('Preenchendo campos...')
                    input.send_keys(resposta)

def buscar_pontos(browser):
    pontos = browser.find_element_by_xpath(meus_pontos).text
    if len(pontos) > 0:
        return pontos.split(' ')[0]
    return '0'

def clica_button(browser, botao_elemento, msg):
    pode_clicar = browser.find_elements_by_xpath(botao_elemento)

    if bool(pode_clicar):
        button_preparado = browser.find_element_by_xpath(botao_elemento)
        if 'disable' not in button_preparado.get_attribute('class'):
            print(msg)
            button_preparado.click()

def clica_estou_pronto(browser):
    clica_button(browser, botao_estou_pronto, 'Clicando em "Estou pronto"')

def avalia_respostas(browser):
    clica_button(browser, botao_avalia_respostas, 'Clicando em "Avaliar respostas"')

def aprende_novas_respostas(browser, primeira_letra):
    tema = browser.find_elements_by_xpath(div_tema)
    if bool(tema):
        tema_text = browser.find_element_by_xpath(div_tema).text
        if  ':' in tema_text:
            tema_text = tema_text.split(':')[1].strip()
            respostas = browser.find_elements_by_xpath(div_palavras)
            for resposta in respostas:
                adicionar_resposta(tema_text, resposta.text, primeira_letra)
