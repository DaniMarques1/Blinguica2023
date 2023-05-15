import os
from PIL import Image
from PyPDF2 import PdfMerger
'''Agora criaremos os arquivos .pdf de cada bloco de convites gerados no nosso último código. É importante
que o diretório esteja sem outras imagens para evitar problemas nos resultados.'''

#Esta iteração irá converter e salvar cada arquivo .png contido na pasta para .pdf, mantendo os nomes originais.
for file in os.listdir():
    if file.split('.')[-1] in (".png"):
        file_name = os.path.basename(file).split('.')[-2]
        imagem = Image.open(file)
        imagem_convertida = imagem.convert('RGB')
        imagem_convertida.save("{0}.pdf".format(file_name))

#Aqui é inciado o Merge para juntar todos os .pdfs criados em um só. Criaremos uma lista para armazená-los.
merger = PdfMerger()
pdf_files = []

#Este loop identifica os arquivos .pdf da pasta e os coloca na lista pdf_files.
for filename in os.listdir():
    if filename.endswith(".pdf"):
        pdf_files.append(filename)

'''Este algoritmo serve para enfileirar os arquivos pela ordem correta de nomeação. Sem ele, é possível que
todo arquivo que contenha o dígito "1" seja priorizado na fila.'''
pdf_files.sort(key=lambda x: int("".join([i for i in x if i.isdigit()])))

#Agora cada item da lista, devidamente enfileirado, será acrescentado ao arquivo contendo todos os .pdfs.
for filename in pdf_files:
    merger.append(filename)

#Instâncias finais para criação do arquivo e fechamento do Merge.
merger.write("convite_finalizado.pdf")
merger.close()


