import requests
import re

def pesquisa_clima(cidade):
    dados = re.sub(r"bot clima ", "", cidade)
    
    content = requests.get('https://api.openweathermap.org/data/2.5/weather?q={0}&appid=d6a6b9bc597f046575f51967bba3b4c5&units=metric&lang=pt_br'.format(dados))

    obj = content.json()

    if (obj['cod'] == 200):
        return("o clima em {1} é {0}°C".format(obj["main"]["temp"], dados))
    else:
        return("Ocorreu um erro e não foi possivel localizar a cidade informada,\n verifique a cidade e tente mais tarde por favor.")
    