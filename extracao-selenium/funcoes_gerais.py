import time
from selenium.webdriver.chromium.webdriver import ChromiumDriver
import select
from selenium.webdriver.common.by import By
from selenium import webdriver


class Webdriver_PJe_TJMT_1(webdriver.Chrome):
    def __init__():
        super().__init__()
    frame_logar_ID = "ssoFrame"
    username_CSS_SELECTOR = "input#username"
    password_CSS_SELECTOR = "input#password"
    logar_ID = "kc-login"
    nome_parte_ID = "fPP:j_id158:nomeParte"
    outros_nomes_ID = "fPP:j_id167:outrosNomesAlcunha"
    nome_rep_ID = "fPP:j_id176:nomeAdvogado"
    cpf_ID = "fPP:dpDec:documentoParte"
    cnpj_ID = "cnpj"
    assunto_ID = "fPP:j_id244:assunto"
    classe_ID = "fPP:j_id253:classeJudicial"
    num_doc_ID = "fPP:j_id262:numeroDocumento"
    oab_ID = "fPP:decorationDados:numeroOAB"
    jurisd_ID_select = "fPP:jurisdicaoComboDecoration:jurisdicaoCombo"
    orgao_ID_select = "fPP:orgaoJulgadorComboDecoration:orgaoJulgadorCombo"
    data_ini_ID = "fPP:dataAutuacaoDecoration:dataAutuacaoInicioInputDate"
    data_final_ID = "fPP:dataAutuacaoDecoration:dataAutuacaoFimInputDate"
    valor_ini_ID = "fPP:valorDaCausaDecoration:valorCausaInicial"
    valor_fim_ID = "fPP:valorDaCausaDecoration:valorCausaFinal"
    pesquisar_CSS_SELECTOR ="input[id='fPP:searchProcessos']"
    
    
    
    def logar(self, username,password):
        self.get("https://pje.tjmt.jus.br/pje/login.seam")
        time.sleep(2)
        frame_logar = self.find_element(By.ID, self.frame_logar_ID)
        self.switch_to.frame(frame_logar)
        self.find_element(By.CSS_SELECTOR, self.username_CSS_SELECTOR).send_keys(username)
        self.find_element(By.CSS_SELECTOR, self.password_CSS_SELECTOR).send_keys(password)
        time.sleep(0.5)
        self.find_element(By.ID, self.logar_ID).click()
        time.sleep(2)


    def ir_consulta(self):
        self.get("https://pje.tjmt.jus.br/pje/Processo/ConsultaProcesso/listView.seam")
        time.sleep(5)

    def inserir_dados(self, nome_parte="", outros_nomes="",
                        nome_rep="", cpf="", cnpj="", assunto="", classe="", num_doc="", oab="", jurisd="", orgao="",
                        data_inicial="",data_final="", valor_ini="", valor_fim="", usuario="", senha=""):
        parametros_elementos = {
        "nome_parte": self.find_element(By.ID, self.nome_parte_ID),
        "outros_nomes": self.find_element(By.ID,self.outros_nomes_ID),
        "nome_rep": self.find_element(By.ID,self.nome_rep_ID),
        "cpf": self.find_element(By.ID,self.cpf_ID),
        "cnpj": self.find_element(By.ID,self.cnpj_ID),
        "assunto": self.find_element(By.ID,self.assunto_ID),
        "classe": self.find_element(By.ID,self.classe_ID),
        "num_doc": self.find_element(By.ID,self.num_doc_ID),
        "oab": self.find_element(By.ID,self.oab_ID),
        "data_inicial": self.find_element(By.ID,self.data_ini_ID),
        "data_final": self.find_element(By.ID,self.data_final_ID),
        "valor_ini": self.find_element(By.ID,self.valor_ini_ID),
        "valor_fim": self.find_element(By.ID,self.valor_fim_ID)
    }
        for parametro, elemento in parametros_elementos.items():
            if locals()[parametro]:
                elemento.send_keys(locals()[parametro])
                time.sleep(1) #para evitar erros
        if jurisd != "":
            self.jurisd_ID_select.select_by_visible_text(jurisd)
            time.sleep(0.5)
        else:
            pass
        if orgao != "":
            self.orgao_ID_select.select_by_visible_text(orgao)
            time.sleep(0.5)
        else:
            pass


    def pesquisar(self):
        self.find_element(By.CSS_SELECTOR,
                                            self.pesquisar_CSS_SELECTOR).click()
        time.sleep(10)
        
        
    

        

