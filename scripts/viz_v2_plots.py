import ijson
import requests
from operator import itemgetter
from datetime import datetime, timedelta
from sanitize_tweets import sanitize
from quick_report import report
import pandas as pd
import json


# def add_args():
#    parser = argparse.ArgumentParser(description='Lineplot Viz 2.0')
#    parser.add_argument('-i', '--input', metavar='', required=True)
#    return parser.parse_args()

def old_getValuesLineplot(filename):
    # args = add_args()
    # args.input
    with open(filename, 'r', encoding='utf8') as f:
        objects = ijson.items(f, 'item')
        data = list(objects)

    horarios = []
    for i in range(len(data) - 1, -1, -1):
        horarios.append(datetime.strptime(data[i]['created_at'], '%Y-%m-%dT%H:%M:%SZ'))

    ex = []
    ey = []

    count = 0
    started_time = horarios[0]
    started_time += timedelta(seconds=1)
    for i in range(len(horarios)):
        if horarios[i] >= started_time:
            ey.append(count)
            started_time = horarios[i]
            ex.append(datetime.strftime(started_time, '%Y-%m-%dT%H:%M:%SZ'))
            started_time += timedelta(seconds=1)
            count = 1

        else:
            count += 1

    print('Lineplot criado.')
    return ex, ey

def getValuesLineplot(filename):
    data = []
    tempo = []
    contagemPositivo = []
    contagemNeutro = []
    contagemNegativo = []

    with open(filename, encoding='utf-8') as file:
        data = json.load(file)

    for objeto in data:
        tempo.append(objeto['created_at'])

        if objeto['emotion'] == 'positive':
            contagemPositivo.append(1)
            contagemNegativo.append(0)
            contagemNeutro.append(0)
        elif objeto['emotion'] == 'negative':
            contagemPositivo.append(0)
            contagemNegativo.append(1)
            contagemNeutro.append(0)
        elif objeto['emotion'] == 'neutral':
            contagemPositivo.append(0)
            contagemNegativo.append(0)
            contagemNeutro.append(1)

    dfSentimentos = pd.DataFrame({
        'Positive': contagemPositivo,
        'Neutral': contagemNeutro,
        'Negative': contagemNegativo,
        'created_at': tempo
    })

    # print('dfSentimentos_antes', dfSentimentos)
    dfSentimentos['created_at'] = pd.to_datetime(dfSentimentos['created_at'], errors='coerce')
    print('dfSentimentos', dfSentimentos)
    dfAgrupadoSentimentos = dfSentimentos.groupby(['created_at']).sum().reset_index()
    print('dfAgrupadoSentimentos', dfAgrupadoSentimentos)

    ex = dfAgrupadoSentimentos['created_at']
    eyPositive = dfAgrupadoSentimentos['Positive']
    eyNeutral = dfAgrupadoSentimentos['Neutral']
    eyNegative = dfAgrupadoSentimentos['Negative']

    return ex, eyPositive, eyNeutral, eyNegative


def getValuesHeatmap(filename):
    with open(filename, 'r', encoding='utf8') as f:
        objects = ijson.items(f, 'item')
        data = list(objects)

    horarios = []
    for i in range(len(data) - 1, -1, -1):
        horarios.append(datetime.strptime(data[i]['created_at'], '%Y-%m-%dT%H:%M:%SZ'))

    data = []
    dia_atual = [0] * horarios[0].hour
    hora_atual = horarios[0].hour
    hora_inicial = horarios[0].hour

    xLabel = list(range(1, 25))
    yLabel = [f'{horarios[0].day}-{horarios[0].month}-{horarios[0].year}']

    count = 0
    started_time = horarios[0]
    started_time = started_time + timedelta(hours=1) - timedelta(minutes=started_time.minute) - timedelta(
        seconds=started_time.second)
    for i in range(len(horarios)):
        if horarios[i] >= started_time:
            # print('passou uma hora!')
            dia_atual.append(count)
            started_time = horarios[i]
            started_time = started_time + timedelta(hours=1) - timedelta(minutes=started_time.minute) - timedelta(
                seconds=started_time.second)
            count = 1
            hora_atual += 1

            if hora_atual == 24:
                hora_atual = 0
                data.append(dia_atual)
                dia_atual = []
                yLabel.append(f'{horarios[i].day}-{horarios[i].month}-{horarios[i].year}')

        else:
            count += 1

    if hora_atual == hora_inicial:
        dia_atual[-1] = count

    else:
        dia_atual.append(count)

    if hora_atual != 24:
        for i in range(23 - hora_atual):
            dia_atual.append(0)

        data.append(dia_atual)

    print('Heatmap hora criado.')
    return data, xLabel, yLabel


def getValuesHeatmapMinute(filename):
    with open(filename, 'r', encoding='utf8') as f:
        objects = ijson.items(f, 'item')
        data = list(objects)

    horarios = []
    for i in range(len(data) - 1, -1, -1):
        horarios.append(datetime.strptime(data[i]['created_at'], '%Y-%m-%dT%H:%M:%SZ'))

    data = []
    dia_hora_atual = [0] * horarios[0].minute
    minuto_atual = horarios[0].minute
    minuto_inicial = horarios[0].minute

    xLabel = list(range(60))
    yLabel = [f'{horarios[0].day}-{horarios[0].month} {horarios[0].hour}h']

    count = 0
    started_time = horarios[0]
    started_time = started_time + timedelta(minutes=1) - timedelta(seconds=started_time.second)
    for i in range(len(horarios)):
        if horarios[i] >= started_time:
            dia_hora_atual.append(count)
            started_time = horarios[i]
            started_time = started_time + timedelta(minutes=1) - timedelta(seconds=started_time.second)
            count = 1
            minuto_atual += 1

            if minuto_atual == 60:
                minuto_atual = 0
                data.append(dia_hora_atual)
                dia_hora_atual = []
                yLabel.append(f'{horarios[i].day}-{horarios[i].month} {horarios[i].hour}h')

        else:
            count += 1

    if minuto_atual == minuto_inicial:
        dia_hora_atual[-1] = count

    else:
        dia_hora_atual.append(count)

    if minuto_atual != 60:
        for i in range(59 - minuto_atual):
            dia_hora_atual.append(0)

        data.append(dia_hora_atual)

    print('Heatmap minutos criado.')
    return data, xLabel, yLabel


def getValuesWordcloud(filename):
    if ".json" in filename:
        print('JSON passado como parametro. Iniciando sanitize e gerando quick reports automatico...')
        sanitize(filename, 'sanitize_auto_aux.json', ['./scripts/stopwords/stopwords_en.txt'], True, True)
        report('sanitize_auto_aux.json', 'quick_sanitize_auto_aux.txt', 10)
        filename = 'quick_sanitize_auto_aux.txt'

    arq = open(filename, 'r', encoding='utf8')
    linhas = arq.read().splitlines()
    arq.close()

    index_inicio = linhas.index('Word ranking:') + 2
    d = []

    while linhas[index_inicio] != '':
        aux = linhas[index_inicio].split(': ')
        d.append([aux[0].strip(), int(aux[1])])
        index_inicio += 1

    # teste
    for i in range(len(d)):
        d[i][1] = int(d[i][1] / d[-1][1])

    print('Wordcloud criada.')
    return d


def getValuesTopRetweets(filename, user_num_rts):
    with open(filename, 'r', encoding='utf8') as f:
        objects = ijson.items(f, 'item')
        data = list(objects)

    rts_list = []

    for item in data:
        if item['retweet_count'] > 1 and 'RT @' not in item['text']:
            rts_list.append(item)

    rts_list = sorted(rts_list, key=itemgetter('retweet_count'), reverse=True)
    html_string = "<body>\n<h3 style='text-align: center; color: white; font-size: 36px; font-family: Montserrat; font-weight: bold'>Top Retweets</h3>"

    i = 0
    j = 0

    if len(rts_list) < user_num_rts:
        if len(rts_list) == 0:
            print('Não foi encontrado nenhum retweet relevante nesse dataset.')

        else:
            print(f"Foram encontrados apenas {len(rts_list)} tweets com mais de um retweet")

        num_rts = len(rts_list)

    else:
        num_rts = user_num_rts

    while i < num_rts:
        base_url = 'https://twitter.com/bomdia/status/'
        tweet_id = rts_list[j]['id']
        r = requests.get('https://publish.twitter.com/oembed?url=' + base_url + str(tweet_id))

        if r.status_code == 200:
            r_json = r.json()
            html_string += r_json['html'] + '<br>'
            i += 1

        j += 1

    html_string += '</body>'
    print('Top retweets criados.')
    return html_string
