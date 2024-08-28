# ferramentas_adv_pje
Algumas ferramentas para advogados coletarem dados de processos judiciais em um portal PJe.

## 1 - Extração de Dados do PJe via Selenium

Este projeto oferece ferramentas para extração de dados e documentos do PJe utilizando Selenium. Embora o uso de APIs seja geralmente preferível para essas tarefas, em muitos casos, não há alternativas viáveis, tornando o Selenium uma solução prática e necessária para determinadas tarefas, tais como, por exemplo, o download de documentos de processos judiciais em trâmite em portais PJe.

No momento, estão estabelecidos roteiros para fazer o download de documentos e para extrair lista de processos de determinado local/assunto/pessoa etc.

Em funcoes_gerais.py há uma subclasse de webdriver.Chrome com métodos e atributos próprios para lidar com o PJE do TJMT de 1 grau.

Nos outros roteiros, apenas a cadeia de comando.

2 - Extração de Publicações do Portal Comunica-PJe

(...)
3 - Extração de Dados via MNI-PJe
(...)