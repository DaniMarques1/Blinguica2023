import os
from PIL import Image
'''Neste programa, iremos criar a coleção de figuras numa folha A4 em branco.'''

#Modelo A4 da página em branco.
PAGE_WIDTH, PAGE_HEIGHT = 2480, 3508

#Criando o objeto da imagem a ser utilizada na confeccção da coleção.
image = Image.new("RGB", (PAGE_WIDTH, PAGE_HEIGHT), "white")
image_filenames = ["card_linguica.png"]

#Definindo o tamanho padrão das imagens para a coleção.
x1 = 810
y1 = 690

#Neste loop, cada imagem é colocada do lado da outra, até o espaço da folha acabar. Note o primeiro parâmetro do range é a margem utilizada,
#e os outros dois parâmetros definem o tamanho de cada retângulo no tamanho da página, seguindo o que foi definido em x1 e y1.
for x in range(25, PAGE_WIDTH, x1):
    for y in range(25, PAGE_HEIGHT, y1):
        for image_filename in image_filenames:
            image_to_paste = Image.open(os.path.join(image_filename))
            image_to_paste = image_to_paste.resize((x1, y1))
            image.paste(image_to_paste, (x, y))

#A imagem será salva no diretório do arquivo.
image.save("colection.png")
