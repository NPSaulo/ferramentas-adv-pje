import time
from funcoes_gerais2 import Webdriver_PJe
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select



def down_lista_procs():
    pass

teste = Webdriver_PJe()
teste.get("https://pje.tjmt.jus.br/pje/login.seam")
time.sleep(2)
teste.logar('03540868127','242619')
time.sleep(5)