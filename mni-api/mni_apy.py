import requests
import csv
import time
import random
import threading
from bs4 import BeautifulSoup
from funcoes_gerais import MNI_TJMT
#LISTA_PROCS = coletar_lista_procs_db()
#LISTA_USUARIOS = []
#DATABASE = ''



consulta_tjmt = MNI_TJMT(usuario="03540868127",senha="b!tsburg0")
lista_procs = ["10549181420248110001"]
consulta_tjmt.consulta_MNI(lista_procs=lista_procs, documentos=True)

        





