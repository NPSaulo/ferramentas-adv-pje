"""
Se for possível extrair uma lista de processos do tipo pela API do Datajud,
não haverá motivos para fazê-lo via Selenium.
"""


import time
from funcoes_gerais import Webdriver_PJe_TJMT_1
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select


def down_lista_procs(nome_parte="", outros_nomes="",
                        nome_rep="", cpf="", cnpj="", assunto="", classe="", num_doc="", oab="", jurisd="", orgao="",
                        data_inicial="",data_final="", valor_ini="", valor_fim="", usuario="", senha="",delay=3):
    driver = Webdriver_PJe_TJMT_1()
    driver.logar(usuario,senha)
    driver.ir_consulta()
    driver.inserir_dados(nome_parte, outros_nomes,
                        nome_rep, cpf, cnpj, assunto, classe, num_doc, oab, jurisd, orgao,
                        data_inicial,data_final, valor_ini, valor_fim)
    driver.pesquisar()
    #a seção abaixo serve para definir a quantidade de página - o que é necessário para usar for ao invés de while
    #vai-se para a ultima pagina, e coleta-se o texto do elemento que marca a página atual
    #o try/except é para lidar com quando só há uma página, pois a rotina pressupõe
    #que haja uma página diferente da atual após pesquisar pelos processos
    cont_pags = 0
    botao_ultima_pag = driver.find_elements(By.CSS_SELECTOR, ".rich-datascr-button")[-1]
    botao_ultima_pag.click()
    time.sleep(5)
    try:
        pagina_atual = driver.find_element(By.CSS_SELECTOR, ".rich-datascr-act")
        ultima_pag = int(pagina_atual.text)
        botao_primeira_pag = driver.find_elements(By.CSS_SELECTOR, ".rich-datascr-button")[0]
        botao_primeira_pag.click()
        time.sleep(8)
    except:
        ultima_pag = 1
    #início do loop, visitará todas as páginas e salvará os dados de todos os processos.
    while cont_pags < ultima_pag:
        tabela_procs = driver.find_element(By.ID, "fPP:processosTable:tb")
        for row in tabela_procs.find_elements(By.TAG_NAME, "tr"):
            proc = row.find_elements(By.TAG_NAME, "td")
            proc_cell = proc[1]
            orgao_cell = proc[3]
            data_autuacao_cell = proc[4]
            classe_cell = proc[5]
            # as outras info (polo ativo, polo passivo e última moviment. são melhor capturadas pela API MNI do PJe)
            nmr_proc = proc_cell.text
            orgao_txt = orgao_cell.text
            classe_jud = classe_cell.text
            dia, mes, ano = data_autuacao_cell.text.split("/")
            values = [nmr_proc, orgao_txt, dia, mes, ano, classe_jud]
            print(values) #colocar aqui o que fazer com os dados
        cont_pags += 1
        botao_proxima_pag = driver.find_elements(By.CSS_SELECTOR, ".rich-datascr-button")[-2]
        botao_proxima_pag.click()
        time.sleep(delay)
    driver.quit()


#alterar delay conforme desejado
down_lista_procs(nome_parte="", outros_nomes="",
                        nome_rep="saulo niederle pereira", cpf="", cnpj="", assunto="", classe="", num_doc="", oab="", jurisd="", orgao="",
                        data_inicial="",data_final="", valor_ini="", valor_fim="", usuario="", senha="")
    


