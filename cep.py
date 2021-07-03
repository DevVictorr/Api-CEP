import requests


def procurar_cep(cep1):

    req = requests.get('https://viacep.com.br/ws/'+cep1+'/json/')
    json = req.json()

    for k, v in json.items():
        print(k," - ",v) 
