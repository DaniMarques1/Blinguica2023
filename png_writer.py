import os
from PIL import Image, ImageDraw, ImageFont
'''Com a coleção criada, é hora de criar quantas páginas deseja,e o que irá escrever/desenhar nelas.
Neste programa iremos numerar de 1 a "n" todos os cartões criados, em ordem e em todas as páginas criadas'''

#Este bloco corresponde às definições iniciais de desenho do programa.
font = ImageFont.truetype("arial.ttf", size=45)

#X e y representam onde será feito o primeiro desenho.
x, y = 70, 190

#x_axis e y_axis representam a frequência da distância em que os desenhos serão feitos no loop de iteração.
x_axis, y_axis = 810, 690

'''Em num_pages é possível definir quantas páginas você deseja que o console imprima. Em rows e cols_per_page, definimos
as linhas e colunas onde será feito cada desenho. Como o exemplo se trata de uma matriz com 15 figuras retangulares,
definimos então como 5 linhas e 3 colunas.'''
num_pages = 10
rows_per_page, cols_per_row = 5, 3

#O objeto nums_per_page será necessário para calcular o número da primeira iteração após a criação de cada página.
nums_per_page = rows_per_page * cols_per_row

'''Este loop criará uma página para cada uma que você indicou em num_pages. Ele irá escrever na imagem "colection" 
os números de 1 a "n" conforme os parâmetros que você indicou nos blocos acima.'''
for p in range(num_pages):
    img = Image.open("colection.png")
    draw = ImageDraw.Draw(img)
    #Estes dois loops abaixo são responsáveis por escrever os números na ordem correta, independe da página em que se encontram.
    for i in range(rows_per_page):
        num = p * nums_per_page + i * cols_per_row + 1
        y_index = i
        for j in range(cols_per_row):
            #Esta formatação é usada para deixar todos os números com 4 dígitos cada. Irá facilitar a formatação.
            text = "{:04d}".format(num + j)
            x_pos = x + j * x_axis
            y_pos = y + y_index * y_axis
            draw.text((x_pos, y_pos), text, font=font, fill='black')
            #As imagens .png criadas nesse loop serão salvas no diretório "Convites", com a marcação de 1 a "n" iterações.
            file_path = os.path.join("Convites", f"convites_{p + 1}.png")
    img.save(file_path)






