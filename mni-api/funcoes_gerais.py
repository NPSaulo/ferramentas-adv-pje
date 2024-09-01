import time
import random
import requests
from bs4 import BeautifulSoup


def dividir_lista_procs(lista_procs,lista_usuarios):
    """
    Função para dividir os processos em partes iguais entre os usuários.
    """
    num_partes = len(lista_usuarios)
    partes_lista = len(lista_procs) // num_partes
    sobra = len(lista_procs) % num_partes
    partes = []
    for i in range(num_partes):
        start_index = i * partes_lista
        end_index = start_index + partes_lista
        if i < sobra:
            end_index += 1
        partes.append(lista_procs[start_index:end_index])
    return partes

class MNI_TJMT():
    def __init__(self, usuario, senha):
        self.dict_assuntos = self.get_dict_assuntos
        self.dict_classes = self.get_dict_classes
        self.usuario = usuario
        self.senha = senha
    x = y = 'false'
    URL = 'https://pje.tjmt.jus.br/pje/intercomunicacao' #conferir se funciona para segundo grau
    
   
    def get_dict_assuntos():
        DICT_CNJ_ASSUNTOS = {}
        with open(r"codigos_cnj/Códigos Assuntos CNJ.csv", mode='r') as f: #csv com os códigos de assuntos e seus significados
            csv_reader = csv.reader(f, delimiter=',')
            for row in csv_reader:
                row_split = row[0].split(";")
                DICT_CNJ_ASSUNTOS[row_split[0]] = row_split[1]
        return DICT_CNJ_ASSUNTOS
    
    def get_dict_classes():
        DICT_CNJ_CLASSES = {}
        with open(r"codigos_cnj/Códigos Classes CNJ.csv", mode='r') as f: #csv com os códigos de classes e seus significados
            csv_reader = csv.reader(f, delimiter=',')
            for row in csv_reader:
                row_split = row[0].split(";")
                DICT_CNJ_CLASSES[row_split[0]] = row_split[1]

    def consulta_MNI(self, lista_procs, movimentos = False,documentos = False, delay=None):
        usuario = self.usuario
        senha = self.senha
        x = y = 'false'
        if movimentos:
            x = 'true'
        if documentos: 
            y = 'true'
        SOAPEnvelope_CONSULTAR_PROCESSO = f"""
                                                <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ser="http://www.cnj.jus.br/servico-intercomunicacao-2.2.2/" xmlns:tip="http://www.cnj.jus.br/tipos-servico-intercomunicacao-2.2.2">
                                                <soapenv:Header/>
                                                <soapenv:Body>
                                                <ser:consultarProcesso>
                                                <tip:idConsultante>[USUARIO]</tip:idConsultante>
                                                <tip:senhaConsultante>[SENHA]</tip:senhaConsultante>
                                                <tip:numeroProcesso>[PROCESSO]</tip:numeroProcesso>
                                                <tip:movimentos>{x}</tip:movimentos>
                                                <tip:incluirDocumentos>{y}</tip:incluirDocumentos>
                                                </ser:consultarProcesso>
                                                </soapenv:Body>
                                                </soapenv:Envelope>
                                                """
        self.SOAPEnvelope_CONSULTAR_PROCESSO= SOAPEnvelope_CONSULTAR_PROCESSO.replace("[USUARIO]",usuario).replace("[SENHA]",senha)
        try:
            for proc in lista_procs:
            #valores de interesse
            #há muitos outros, por ora extraindo apenas os abaixo
                    valor_causa = None
                    codigo_localidade = None
                    classe = None
                    # não extraio data pois já vem de outro roteiro
                    # data_autuacao = None
                    lista_assuntos = []
                    orgao_julgador = None
                    lista_partes_at = []
                    lista_adv_at = []
                    lista_partes_pa = []
                    lista_adv_pa = []
                    x = self.SOAPEnvelope_CONSULTAR_PROCESSO.replace("[PROCESSO]",proc)
                    response = requests.post(self.URL, data=x)
                    xml_content = response.text
                    start_marker = '<soap:Envelope'
                    end_marker = '</soap:Envelope>'
                    start_pos = xml_content.find(start_marker)
                    end_pos = xml_content.find(end_marker) + len(end_marker)
                    body_content = xml_content[start_pos:end_pos]
                    #print(body_content)
                    soup = BeautifulSoup(body_content, 'xml')
                    dados_basicos = soup.find("dadosBasicos")
                    dataAjuizamento = dados_basicos['dataAjuizamento']
                    #os elementos abaixo nem sempre estão presentes
                    try:
                        classe = self.dict_classes[dados_basicos['classeProcessual']]
                    except:
                        pass
                    try:
                        codigo_localidade = dados_basicos['codigoLocalidade']
                    except:
                        pass
                    try:
                        valor_causa = dados_basicos.find('valorCausa').getText()
                    except:
                        pass
                    try:
                        orgao_julgador = dados_basicos.find('orgaoJulgador')['nomeOrgao']
                    except:
                        pass
                    try:
                        assuntos = dados_basicos.find_all('assunto')
                        for assunto in assuntos:
                            lista_assuntos.append(self.dict_assuntos[assunto.getText()])
                    except:
                        pass
                    polos = dados_basicos.find_all('polo')
                    for polo in polos:
                        if polo['polo'] == 'AT':
                            partes_at = polo.find_all('ns2:parte')
                            for parte in partes_at:
                                pessoa = parte.find('ns2:pessoa')
                                # extraindo apenas o nome, sem interesse nos outros atributos
                                pessoa_atributos = {
                                    'nome': pessoa['nome']
                                }
                                lista_partes_at.append(pessoa_atributos['nome'])
                                advogados = parte.find_all('ns2:advogado')
                                for advogado in advogados:
                                    #extraindo apenas o nome
                                    advogado_atributos = {
                                        'nome': advogado['nome']
                                        }
                                    lista_adv_at.append(advogado_atributos['nome'])
                        elif polo['polo'] == 'PA':
                            partes_pa = polo.find_all('ns2:parte')
                            for parte in partes_pa:
                                pessoa = parte.find('ns2:pessoa')
                                # extraindo apenas o nome
                                pessoa_atributos = {
                                    'nome': pessoa['nome']
                                }
                                lista_partes_pa.append(pessoa_atributos['nome'])
                                advogados = parte.find_all('ns2:advogado')
                                for advogado in advogados:
                                    advogado_atributos = {
                                        'nome': advogado['nome']
                                    }
                                    lista_adv_pa.append(advogado_atributos['nome'])
                    valores = [proc[0], orgao_julgador, valor_causa, codigo_localidade, classe, str(lista_assuntos),
                            str(lista_partes_at), str(lista_adv_at), str(lista_partes_pa), str(lista_adv_pa)]
                    print(valores) #colocar aqui o que fazer com os valores
                    #atraso randomizado
                    if delay:
                        r = random.uniform(0.2,1)
                        time.sleep(r + delay)
        except Exception as e:
            print(e)
            print(f"Erro no processo {proc}")
            
    



