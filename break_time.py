import webbrowser # importa o modulo

def hora_descanso(): # declaração da função
    time.sleep(7200) # tempo de suspensão da chamada para o número de segundos 
    url = "https://www.google.com" # declara a url que vai ser chamada 
    webbrowser.open_new(url) # abre a url em uma nova aba

hora_descanso() # chamada a função
