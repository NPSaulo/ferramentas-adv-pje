import requests
import csv
import time
import random
import threading
from bs4 import BeautifulSoup
from funcoes_gerais import MNI_TJMT, dividir_lista_procs



LISTA_PROCS = [] #fornecer lista de processos (por exemplo, extraindo de uma base de dados)
LISTA_USUARIOS = [] #fornecer lista de tuples com (usuario,senha)
LISTA_PROCS_DIV = dividir_lista_procs(LISTA_PROCS,LISTA_USUARIOS)


objs_consulta = []
for usuario, lista_proc in zip (LISTA_USUARIOS,LISTA_PROCS_DIV):
    consulta_tjmt = MNI_TJMT(usuario=usuario[0],senha=usuario[1])
    objs_consulta.append(consulta_tjmt)
threads = []
for obj, lista_proc in zip (objs_consulta, LISTA_PROCS_DIV):
    documentos = False
    movimentos = False
    #mudar caso queira receber documentos e movimentos do proc
    thread = threading.Thread(target=obj.consulta_MNI, args=(lista_proc, documentos, movimentos))
    threads.append(thread)
for thread in threads:
    thread.start()
    time.sleep(1)
for thread in threads:
    thread.join()


        





