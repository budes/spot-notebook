#!/usr/bin/python

import cgi
import os

# O caminho é relativo ao path inicial '/'

args = {'arquivo': 'Roteiro.txt', 'caminho': 'Arquivos/'}# cgi.FieldStorage()

caminho = args['caminho'].value
arq = args['arquivo'].value

os.chdir('..')
os.chdir(caminho)

arquivo = open(arq, 'r')

mostrar = arquivo.read()

print("Content-type: text/html")

print(mostrar)

arquivo.close()




