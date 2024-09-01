# ferramentas_adv_pje
Algumas ferramentas para advogados coletarem dados de processos judiciais em um portal PJe.

## 1 - Extração de Dados do PJe via Selenium

Este projeto oferece ferramentas para extração de dados e documentos do PJe utilizando Selenium. Embora o uso de APIs seja geralmente preferível para essas tarefas, em muitos casos, não há alternativas viáveis, tornando o Selenium uma solução prática e necessária para determinadas tarefas, tais como, por exemplo, o download de documentos de processos judiciais em trâmite em portais PJe.

No momento, está estabelecido apenas um roteiro para extrair lista de processos de determinado local/assunto/pessoa etc.

Em seguida, planeja-se estabelecer um para baixar documentos dos processos.

Em funcoes_gerais.py há uma subclasse de webdriver.Chrome com métodos e atributos próprios para lidar com o PJE do TJMT de 1 grau.

No(s) outro(s) roteiro(s), apenas a cadeia de comando para a tarefa específica.

## 2 - Extração de Publicações do Portal Comunica-PJe

Roteiro para coleta de publicações de processos judiciais disponibilizadas no portal Comunica-PJE.

Utiliza-se a biblioteca `requests` para realizar as requisições HTTP e processar os dados recebidos em formato JSON.

A ferramenta realiza requisições à API do PJe para buscar comunicações judiciais com base nos parâmetros fornecidos, como tribunal, órgão, data de disponibilização, e outras informações relevantes.

Daí os dados podem ser processados conforme a finalidade desejada (salvar em base dados para posterior análise, por exemplo), bastando encorpar a função `capturar_info_item` com as tarefas.


## 3 - Extração de Dados via MNI-PJe

O MNI - Modelo Nacional de Interoperabilidade - "representa o padrão para troca de informações processuais no âmbito do Poder Judiciário" (https://www.pje.jus.br/wiki/index.php/Tutorial_MNI).

Trata-se de um webservice que pode ser utilizado para extrair informações de processos judiciais em trâmites nos portais PJe.

Aqui, há um roteiro simples para extrair informações, sem definição quanto a como salvar ou processar os dados.

O caminho é estabelecido para trabalho em multithread, para agilizar as consultas.