import requests
import json


url = "https://api-publica.datajud.cnj.jus.br/api_publica_tjmt/_search" 
headers = {
    "Authorization" : "APIKey cDZHYzlZa0JadVREZDJCendQbXY6SkJlTzNjLV9TRENyQk1RdnFKZGRQdw==", 
    "Content-Type" : "application/json"
}

body = {
    "size": 100,
    "query": {
        "bool": {
            "must": [
                #{"match": {"classe.codigo": 1116}},
                {"match": {"tribunal": "TJMT"}},
                {"match": {"orgaoJulgador.nome": "Juizado Especial da Fazenda Pública de Cuiabá"}}
                
                
            ]
        }
    },
    "sort": [
        {
            "@timestamp": {
                "order": "asc"
            }
        }
    ]
}

json_body = json.dumps(body)


response = requests.post(url=url,headers=headers,data=json_body)
if response.status_code == 200:
    print("Request successful!")
    response_json = response.json()
    #print(response_json)
    for hit in (response_json['hits']['hits'][:2]):
        print(hit)
        
    



else:
    print(f"Request failed with status code: {response.status_code}")
    print("Response text:", response.text)