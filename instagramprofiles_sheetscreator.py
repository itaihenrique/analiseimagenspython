import pytesseract
from PIL import Image
import os
import pandas as pd

caminho_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
caminho_pasta = r"E:\ParaPython\instagram_screenshots"
lista_perfis = list()

def ListCleaner(lista_raiz):
    lista_copia = lista_raiz.copy()
    for elemento in lista_copia:
        if len(elemento) < 3:
            lista_raiz.remove(elemento)
    return

for imagem in os.listdir(caminho_pasta):
    arquivo_png = "E:\\ParaPython\\instagram_screenshots\\" + imagem
    screenshot = Image.open(arquivo_png)
    texto = pytesseract.image_to_string(screenshot).split("\n")
    texto.pop(0)
    ListCleaner(texto)
    lista_perfis.append(texto[0:9])

df = pd.DataFrame(lista_perfis, columns=['Username', 'Seguidores', '-','Nome','Nicho01','Nicho02','Nicho03','Nicho04','Nicho05'])
caminho_saida = 'instagram_profiles.xlsx'
df.to_excel(caminho_saida, index=False)