import cv2
import numpy as np
import pyautogui
from PIL import ImageGrab, ImageOps
from time import sleep
import pytesseract
import keyboard
import datetime
import sys

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def select_option(item_list):
    sleep(.5)
    i = 1
    while pyautogui.locateCenterOnScreen(item_list, grayscale=False) is None and i <= 7:
        print("LOG: testando escolha")
        sleep(.2)
        pyautogui.press('down')
        sleep(.2)
        i += 1
    if i != 7:
        sleep(.5)
        pyautogui.press('enter')
        #TODO Verificar Timers no final das funçoes
        sleep(.5)
    else:
        screenshot = ImageGrab.grab()
        screenshot.save('temp_select.png')

def pergunta():
    # Define as coordenadas da área a ser capturada (x1, y1, x2, y2)
    bbox = (5, 5 , 268,172)

    # Captura a área da tela
    screenshot = ImageGrab.grab(bbox)
    screenshot.save('color_temp.png')
    
    screenshot = ImageOps.grayscale(screenshot)
    screenshot.save('temp2.png')
    # screenshot = screenshot.convert('L').point(lambda x: 0 if x < 128 else 255, '1')


    # screenshot.show()
    texto_extraido = pytesseract.image_to_string(screenshot)
    return texto_extraido

def pergunta_quest():
    # Define as coordenadas da área a ser capturada (x1, y1, x2, y2)
    bbox = (1589,138,1721,297)
    screenshot = ImageGrab.grab(bbox)
    
    screenshot = ImageOps.grayscale(screenshot)

    texto_extraido = pytesseract.image_to_string(screenshot)
    return texto_extraido

def encontrar_imagem(imagem_path, limiar_confianca=0.7): #MUDANÇA 0.8 PARA 0.7
    # Aguarde alguns segundos para permitir a transição para a janela desejada
    # time.sleep(5)

    # Capture a tela
    tela = pyautogui.screenshot()
    tela = cv2.cvtColor(np.array(tela), cv2.COLOR_RGB2BGR)

    # Carregue a imagem alvo
    imagem_alvo = cv2.imread(imagem_path)

    # Realize a correspondência de padrões usando a função matchTemplate do OpenCV
    resultado = cv2.matchTemplate(tela, imagem_alvo, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(resultado)

    # Verifique se a confiança da correspondência é maior que o limiar
    if max_val >= limiar_confianca:
        # Exiba as coordenadas do canto superior esquerdo da correspondência
        return max_loc
    else:
        return None
    
def cor(caminho_da_imagem, k=2):
    # Lê a imagem
    imagem = cv2.imread(caminho_da_imagem)
    
    # Converte de BGR para RGB
    imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
    
    # Remodela a imagem para uma lista de pixels
    pixels = imagem_rgb.reshape((-1, 3))

    # Converte os valores de pixel para float
    pixels = np.float32(pixels)

    # Define critérios e aplica o kmeans()
    criterios = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    _, rotulos, centros = cv2.kmeans(pixels, k, None, criterios, 10, cv2.KMEANS_RANDOM_CENTERS)

    # Converte de volta para valores de 8 bits
    centros = np.uint8(centros)

    # Obtém a cor não-dominante (aquela que não é a cor dominante)
    indice_cor_dominante = np.argmax(np.bincount(rotulos.flatten()))
    cor_nao_dominante = centros[1 - indice_cor_dominante]
    print(str(cor_nao_dominante))
    return str(cor_nao_dominante)

def buff():
    pyautogui.keyDown('alt')
    pyautogui.keyDown('0')
    pyautogui.keyUp('0')
    pyautogui.keyUp('alt')




