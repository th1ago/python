import json
import requests

url = 'https://<site>'

files = {'upload':open('file.json','rb')}

resposta = requests.post(url, files=files)
print(resposta.json())
print(resposta.status_code)
