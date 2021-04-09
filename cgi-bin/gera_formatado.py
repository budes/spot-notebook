#!/usr/bin/python

import cgi
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

print("Content-type: text/html \n")

print('<html>')
print(mostrar)
print('</html>')

arquivo.close()




