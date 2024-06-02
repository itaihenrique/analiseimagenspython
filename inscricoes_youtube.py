import pytesseract
from PIL import Image

caminho_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
caminho_imagem = r"C:\Users\Henrique\Desktop\FireShot Capture 052 - Todas as inscrições - YouTube - www.youtube.com.png"

screenshot = Image.open(caminho_imagem)
texto = pytesseract.image_to_string(screenshot).split("\n")

copia_texto = texto.copy()

for string in copia_texto:
    if not string.startswith('@'):
       texto.remove(string)

for i in range(len(texto)):
    indice_espaco = texto[i].find(' ')
    texto[i] = texto[i][:indice_espaco]

with open("inscricoes.txt", "w") as texto_inscricoes:
    for canal in texto:
        texto_inscricoes.write(f"https://www.youtube.com/{canal}\n")
    texto_inscricoes.close()
