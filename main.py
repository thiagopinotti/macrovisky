import datetime
import sys
import keyboard
import threading
import os
from time import sleep
import pyautogui
from screeninfo import get_monitors
import antibot

START_KEY = 'home'
PAUSE_KEY = 'page up'
KILL_KEY = 'page down'
BOT_KEY = 'delete'
X_CENTER = get_monitors()[0].width/2
Y_CENTER = get_monitors()[0].height/2

#Perceber Antibot
ANTIBOT = 'assets/antibot.png'

#Personagens
CHAPEU_VERDE = 'assets/chapeu_verde.png'
CHAPEU_LARANJA = 'assets/chapeu_laranja.png'
SAPATO_CABELO = 'assets/cabelo_sapato.png'
GRAVATA_CALCA = 'assets/gravata_calca.png'
CAPA_VERMELHA = 'assets/capa_vermelha.png'
CAPA_AZUL = 'assets/capa_azul.png'
ROUPA_AZUL = 'assets/roupa_azul.png'
CABELO_AMARELO = 'assets/cabelo_amarelo.png'
ASA = 'assets/asa.png'

#cores
VERMELHO = 'assets/vermelho.png'
TEXT_VERMELHO = ['[254   0   7]','[240   0   7]'] # OK
AZUL = 'assets/azul.png'
TEXT_AZUL = ['[  0 106 254]','[  0 100 240]'] # ok
AMARELO = 'assets/amarelo.png'
TEXT_AMARELO = ['[180 156   0]',] #ok 
VERDE = 'assets/verde.png'
TEXT_VERDE = ['[ 66 173   0]',] #ok
PRETO = 'assets/preto.png'
TEXT_PRETO = ['[0 0 0]',] # ok
LARANJA = 'assets/laranja.png'
TEXT_LARANJA = ['[254 106   7]',] # ok

atividade_executando = False

def proc_antibot():
    print(f'LOG: INICIO ANTIBOT {datetime.datetime.now().strftime("%H:%M")}')
    pyautogui.press('enter')
    sleep(1)

    if antibot.encontrar_imagem(CHAPEU_VERDE):
        print('Chapeu Verde')
        antibot.select_option(VERDE)

    elif antibot.encontrar_imagem(CAPA_VERMELHA):
        print('Capa Vermelha')
        antibot.select_option(VERMELHO)

    elif antibot.encontrar_imagem(CAPA_AZUL):
        print('Capa Azul')
        antibot.select_option(AZUL)

    elif antibot.encontrar_imagem(CABELO_AMARELO):
        print('CAbelo Amarelo')
        antibot.select_option(AMARELO)

    elif antibot.encontrar_imagem(GRAVATA_CALCA):
        if 'gravata' in antibot.pergunta():
            print('gravata')
            antibot.select_option(VERMELHO)
        else:
            print('calça')
            antibot.select_option(AZUL)

    elif antibot.encontrar_imagem(ROUPA_AZUL):
        print('Roupa Azul')
        antibot.select_option(AZUL)

    elif antibot.encontrar_imagem(CHAPEU_LARANJA):
        print('chapeu laranja')
        antibot.select_option(LARANJA)

    elif antibot.encontrar_imagem(SAPATO_CABELO):
        if 'cabelo' in antibot.pergunta():
            print("cabelo na sorte")
            antibot.select_option(VERDE)
        else:
            print('sapato laranja')
            antibot.select_option(LARANJA)

    elif 'asas' in antibot.pergunta():
        print('Asa')
        antibot.select_option(PRETO)
        #TODO remover imagem asas

    elif 'fala' in antibot.pergunta():
        print('LOG: Entrou no laço de verificação de cor')
        if antibot.cor('color_temp.png') in TEXT_PRETO:
            print('textp preto')
            antibot.select_option(PRETO)
        elif antibot.cor('color_temp.png') in TEXT_AMARELO:
            print('texto amarelo')
            antibot.select_option(AMARELO)
        elif antibot.cor('color_temp.png') in TEXT_VERDE:
            print('textp verde')
            antibot.select_option(VERDE)
        elif antibot.cor('color_temp.png') in TEXT_VERMELHO:
            print('textp vermelho')
            antibot.select_option(VERMELHO)
        elif antibot.cor('color_temp.png') in TEXT_AZUL:
            print('textp azul')
            antibot.select_option(AZUL)
        elif antibot.cor('color_temp.png') in TEXT_LARANJA:
            print('textp laranja')
            antibot.select_option(LARANJA)
    else:
        print(f'LOG: não encontrou {datetime.datetime.now().strftime("%H:%M")}')
        print(datetime.datetime.now())
        while antibot.encontrar_imagem(ANTIBOT):
            sys.stdout.write('\rloading |')
            sleep(0.1)
            sys.stdout.write('\rloading /')
            sleep(0.1)
            sys.stdout.write('\rloading -')
            sleep(0.1)
            sys.stdout.write('\rloading \\')
            sleep(0.1)
    print(f'LOG: Voltando a Iniciar {datetime.datetime.now().strftime("%H:%M")}')
    sleep(1)
    antibot.buff()
    pyautogui.press('home')
       
def farm():
    global atividade_executando
    print("Atividade em andamento...")
    while atividade_executando:
        #690,384 centro tela cheia
        pyautogui.click(X_CENTER+8, Y_CENTER+10)

        pyautogui.keyDown('f2')
        sleep(.1)
        pyautogui.keyUp('f2')
        sleep(1) #.2
        pyautogui.press('f1')
        sleep(.4) #.5

        if antibot.encontrar_imagem(ANTIBOT):
            sleep(.5)
            pyautogui.press('enter')
            sleep(.2)
            proc_antibot()

while True:
    # event = keyboard.read_event(suppress=True) #estudar 873,250
    event = keyboard.read_event() #estudar
    if event.event_type == keyboard.KEY_DOWN:
        if event.name == START_KEY:
            if not atividade_executando:
                print("Atividade iniciada")
                atividade_executando = True
                atividade_thread = threading.Thread(target=farm)
                atividade_thread.start()
        elif event.name == PAUSE_KEY:
            if atividade_executando:
                print("Atividade pausada")
                atividade_executando = False
                atividade_thread.join()
        elif event.name == KILL_KEY:
            if atividade_executando:
                atividade_executando = False
                print("Atividade encerrada")
            print("Programa encerrado")
            os._exit(0)




