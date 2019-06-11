import json
import requests

# leitura do arquivo e trabalhando com ele
file_json = open('file.json').read()
dados = json.loads(file_json)

texto = dados["texto"]
chave = dados["decimais"]
modo = input('Escolha E para encriptar ou D para decriptar o texto: ')
CARACTERES = 'abcdefghijklmnopqrstuvwxyz'

# armazena o texto criptografado
convertido = ''
for caractere in texto:
  if caractere in CARACTERES:
    num = CARACTERES.find(caractere)
    if modo == 'e':
      num = num + chave
    elif modo == 'd':
      num = num - chave
  # for para validar o maior do que o comprimento de CARACTERES ou menor que 0
  if num >= len(CARACTERES):
    num = num - len(CARACTERES)
  elif num < 0:
    num = num + len(CARACTERES)
    convertido = convertido + CARACTERES[num] 
  else:
    convertido = convertido + caractere
if modo == 'e':
  print('O texto criptografado é ', convertido)
if modo == 'd':
  print('O texto decriptado é ', convertido)
  dados["decifrado"] = convertido

#  resumo criptografico usando o algoritmo sha1
texto_to_hash = dados["decifrado"]
hash_object = hashlib.sha256(str(texto_to_hash).encode('utf-8'))
print('Hash', hash_object.hexdigest())
dados["resumo"] = hash_object.hexdigest()
  
# alterando o arquivo .json
with open('answer.json',"w") as fp:
  json.dump(dados, fp)
