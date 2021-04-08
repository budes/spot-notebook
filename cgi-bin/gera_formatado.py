#!/usr/bin/python

import cgitb; cgitb.enable()
import os

# O caminho é relativo ao path inicial '/'

arg_nav = cgi.FieldStorage()
args = {'arquivo': 'Roteiro.txt', 'caminho': 'Arquivos/'}# cgi.FieldStorage()

caminho = args['caminho']
arq = args['arquivo']

os.chdir('..')
os.chdir(caminho)

arquivo = open(arq, 'r')

mostrar = arquivo.read()

print("Content-type: text/html")

print(mostrar)

arquivo.close()




