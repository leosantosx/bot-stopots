from selenium.webdriver import Chrome
from selenium.common.exceptions import (
StaleElementReferenceException, NoSuchElementException, WebDriverException)
from funcoes import *
from configuracao import *
from time import sleep

browser = Chrome()

iniciar_jogo(browser)

while True:

    try:
        limpar_tela()
        letra = pegar_letra_atual(browser)
        pontos = buscar_pontos(browser)
        print(f'Letra atual: {letra}')
        print(f'Seus pontos: {pontos}')

        if escrever_nos_campos:
            escrever_resposta(browser, letra)

        if clica_botao_avaliar_respostas:
            avalia_respostas(browser)

        if modo_de_aprendizado:
            aprende_novas_respostas(browser, letra)

        if clica_botao_estou_pronto:
            clica_estou_pronto(browser)

        sleep(3)

    except (StaleElementReferenceException, NoSuchElementException):
        pass
    except WebDriverException:
        break
