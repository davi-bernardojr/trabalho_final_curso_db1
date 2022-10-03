from bs4 import BeautifulSoup as bs
import requests as rq
import re

def buscar_acao(acao):
    dado = re.sub(r"bot acao ", "", acao)
    html = rq.get(f'https://statusinvest.com.br/acoes/{dado}').content

    html_text = bs(html, 'html.parser')

    vlr = html_text.find(title="Valor atual do ativo")
    vlr_min = html_text.find(title="Valor mínimo das últimas 52 semanas")
    vlr_max = html_text.find(title="Valor máximo das últimas 52 semanas")
    vlr_dy = html_text.find(title="Dividend Yield com base nos últimos 12 meses")
    vlr_dmes = html_text.find(title="Valorização no preço do ativo com base nos últimos 12 meses")

    ret = 'Valor da ação: R$' + vlr.strong.string
    ret = ret + '\nValor mínimo das ultimas 52 semanas: R${0}'.format(vlr_min.strong.string)
    ret = ret + '\nValor máximo das ultimas 52 semanas: R${0}'.format(vlr_max.strong.string)
    ret = ret + '\nDividend Yield com base nos últimos 12 meses: {0}%'.format(vlr_dy.strong.string)
    ret = ret + '\nValorização nos últimos 12 meses: {0}'.format(vlr_dmes.strong.string)

    return (ret)

