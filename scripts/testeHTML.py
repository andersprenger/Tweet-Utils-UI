import os
import sys
import math
import argparse

from elementsHTML import *
from viz_v2_plots import *


def add_args():
    parser = argparse.ArgumentParser(description='teste HTML')
    parser.add_argument('-i', '--input', metavar='', required=True)
    return parser.parse_args()


args = add_args().input.split(';')
list_graphs = []
script_graphs = []
top_rt = False

if args == ['']:
    sys.stdout.write(
        "Nenhuma check box selecionada. Nao ha graficos a serem gerados.")
    sys.stdout.flush()
    exit()

for e in args:
    aux = e.split('/', 1)
    style_graph = aux[0]
    filename = aux[1]

    if style_graph == 'lineplot':
        arr, arr2 = getValuesLineplot(filename)

        script = """
        let trace = {}
            x: {},
            y: {},
            mode: 'lines',
            line: {}
                color: 'rgb(255, 255, 255)',
                width: 1
            {}
        {};

        let layout = {}
            title: {}
                text: '<b>Lineplot ({})</b>',
                font: {}
                    size: 36,
                    color: 'white',
                    family: 'Montserrat'
                {}
            {},

            paper_bgcolor: 'rgb(27, 37, 66)',
            plot_bgcolor: 'rgb(27, 37, 66)',

            xaxis: {}
                gridcolor: 'rgb(47, 64, 115)',
                gridwidth: 1,
                
                zerolinecolor: 'rgb(47, 64, 115)',
                zerolinewidth: 1,

                tickfont : {}
                    size : 12,
                    color : 'white'
                {}
            {},

            yaxis: {}
                gridcolor: 'rgb(47, 64, 115)',
                gridwidth: 1,
                
                zerolinecolor: 'rgb(47, 64, 115)',
                zerolinewidth: 1,

                tickfont : {}
                    size : 12,
                    color : 'white'
                {}
            {}
        {};

        Plotly.newPlot('lineplot', [trace], layout);
        """.format('{', arr, arr2, '{', '}', '}', '{', '{', filename.split(os.sep)[-1], '{', '}', '}', '{', '{', '}', '}', '{', '{', '}', '}', '}')

        script_graphs.append(script)

    if style_graph == 'sentiments':
        with open(filename, 'r', encoding='utf8') as f:
            objects = ijson.items(f, 'item')
            data = list(objects)

        if 'emotion' in data[0]:
            positiveX, positiveY = getValueSentimentLineplot(filename, 'positive')
            negativeX, negativeY = getValueSentimentLineplot(filename, 'negative')
            neutralX, neutralY = getValueSentimentLineplot(filename, 'neutral')

            scriptX = """
            let positive = {}
                x: {},
                y: {},
                mode: 'lines',
                line: {}
                    color: 'rgb(128, 255, 0)',
                    width: 1
                {}
            {};
            
            let negative = {}
                x: {},
                y: {},
                mode: 'lines',
                line: {}
                    color: 'rgb(255, 0, 0)',
                    width: 1
                {}
            {};
            
            let neutral = {}
                x: {},
                y: {},
                mode: 'lines',
                line: {}
                    color: 'rgb(255, 255, 0)',
                    width: 1
                {}
            {};
            
            let tracesX = [positive, negative, neutral];
    
            let layoutX = {}
                title: {}
                    text: '<b>Lineplot Sentiments ({})</b>',
                    font: {}
                        size: 36,
                        color: 'white',
                        family: 'Montserrat'
                    {}
                {},
    
                paper_bgcolor: 'rgb(27, 37, 66)',
                plot_bgcolor: 'rgb(27, 37, 66)',
    
                xaxis: {}
                    gridcolor: 'rgb(47, 64, 115)',
                    gridwidth: 1,
    
                    zerolinecolor: 'rgb(47, 64, 115)',
                    zerolinewidth: 1,
    
                    tickfont : {}
                        size : 12,
                        color : 'white'
                    {}
                {},
    
                yaxis: {}
                    gridcolor: 'rgb(47, 64, 115)',
                    gridwidth: 1,
    
                    zerolinecolor: 'rgb(47, 64, 115)',
                    zerolinewidth: 1,
    
                    tickfont : {}
                        size : 12,
                        color : 'white'
                    {}
                {}
            {};
    
            Plotly.newPlot('sentiments', tracesX, layoutX);
            """.format('{', positiveX, positiveY, '{', '}', '}',
                       '{', negativeX, negativeY, '{', '}', '}',
                       '{', neutralX, neutralY, '{', '}', '}',
                       '{', '{', filename.split(os.sep)[-1], '{', '}', '}', '{', '{', '}', '}', '{', '{', '}', '}', '}')

            script_graphs.append(scriptX)

    if style_graph == 'heatmap':
        matrix, xLabel, yLabel = getValuesHeatmap(filename)

        script2 = """
        let data = [
            {}
                x: {},
                y: {},
                z: {},
                type: 'heatmap',
                xgap: 2,
                ygap: 2,
                showscale: false,
                colorscale: [['0.0', 'rgb(237, 222, 255)'],
                             ['0.111111111111', 'rgb(234, 218, 255)'],
                             ['0.222222222222', 'rgb(216, 200, 236)'],
                             ['0.333333333333', 'rgb(178, 117, 254)'],
                             ['0.444444444444', 'rgb(178, 117, 254)'],
                             ['0.555555555556', 'rgb(171, 104, 255)'],
                             ['0.666666666667', 'rgb(163, 91, 255)'],
                             ['0.777777777778', 'rgb(140, 50, 255)'],
                             ['0.888888888889', 'rgb(131, 33, 255)'],
                             ['1.0', 'rgb(124, 33, 240)']]
            {}
        ];

        let layout2 = {}
            title: {}
                text: '<b>Heatmap Hora ({})</b>',
                font: {}
                    size: 36,
                    color: 'white',
                    family: 'Montserrat'
                {}
            {},

            annotations: [],
            height: 280 * {},
            margin: {}
                t: 100,
                r: 0,
                l: 70,
                b: 140
            {},
            
            paper_bgcolor: 'rgb(27, 37, 66)',
            plot_bgcolor: 'rgb(27, 37, 66)',

            xaxis: {}
                gridcolor: 'rgb(47, 64, 115)',
                gridwidth: 1,
                
                zerolinecolor: 'rgb(47, 64, 115)',
                zerolinewidth: 1,

                tickfont : {}
                    size : 12,
                    color : 'white'
                {}
            {},

            yaxis: {}
                gridcolor: 'rgb(47, 64, 115)',
                gridwidth: 1,
                
                zerolinecolor: 'rgb(47, 64, 115)',
                zerolinewidth: 1,

                tickfont : {}
                    size : 12,
                    color : 'white'
                {}
            {}
        {};

        for (let i = 0; i < {}.length; i++) {}
            for (let j = 0; j < {}.length; j++) {}
                let result = {}
                    x: {}[j],
                    y: {}[i],
                    text: {}[i][j],
                    font: {}color: 'rgb(0, 0, 0)'{},
                    showarrow: false
                {};

                layout2.annotations.push(result);
            {}
        {}

        Plotly.newPlot('heatmap', data, layout2);
        """.format('{', xLabel, yLabel, matrix, '}', '{', '{', filename.split(os.sep)[-1], '{', '}', '}', math.ceil(len(matrix)/2),'{', '}', '{', '{', '}', '}', '{', '{', '}', '}', '}', yLabel, '{', xLabel, '{', '{', xLabel, yLabel, matrix, '{', '}', '}', '}', '}')

        script_graphs.append(script2)

    if style_graph == 'heatmapMinute':
        matrix, xLabel, yLabel = getValuesHeatmapMinute(filename)

        script4 = """
        let data2 = [
            {}
                x: {},
                y: {},
                z: {},
                type: 'heatmap',
                xgap: 2,
                ygap: 2,
                showscale: false,
                colorscale: [['0.0', 'rgb(237, 222, 255)'],
                             ['0.111111111111', 'rgb(234, 218, 255)'],
                             ['0.222222222222', 'rgb(216, 200, 236)'],
                             ['0.333333333333', 'rgb(178, 117, 254)'],
                             ['0.444444444444', 'rgb(178, 117, 254)'],
                             ['0.555555555556', 'rgb(171, 104, 255)'],
                             ['0.666666666667', 'rgb(163, 91, 255)'],
                             ['0.777777777778', 'rgb(140, 50, 255)'],
                             ['0.888888888889', 'rgb(131, 33, 255)'],
                             ['1.0', 'rgb(124, 33, 240)']]
            {}
        ];

        let layout4 = {}
            title: {}
                text: '<b>Heatmap Minutos ({})</b>',
                font: {}
                    size: 36,
                    color: 'white',
                    family: 'Montserrat'
                {}
            {},
            annotations: [],
            height: 280 * {},
            margin: {}
                t: 100,
                r: 0,
                l: 70,
                b: 140
            {},

            paper_bgcolor: 'rgb(27, 37, 66)',
            plot_bgcolor: 'rgb(27, 37, 66)',

            xaxis: {}
                gridcolor: 'rgb(47, 64, 115)',
                gridwidth: 1,
                
                zerolinecolor: 'rgb(47, 64, 115)',
                zerolinewidth: 1,

                tickfont : {}
                    size : 12,
                    color : 'white'
                {}
            {},

            yaxis: {}
                gridcolor: 'rgb(47, 64, 115)',
                gridwidth: 1,
                
                zerolinecolor: 'rgb(47, 64, 115)',
                zerolinewidth: 1,

                tickfont : {}
                    size : 12,
                    color : 'white'
                {}
            {}
        {};

        for (let i = 0; i < {}.length; i++) {}
            for (let j = 0; j < {}.length; j++) {}
                let result = {}
                    x: {}[j],
                    y: {}[i],
                    text: {}[i][j],
                    font: {}color: 'rgb(0, 0, 0)'{},
                    showarrow: false
                {};

                layout4.annotations.push(result);
            {}
        {}

        Plotly.newPlot('heatmapMinute', data2, layout4);
        """.format('{', xLabel, yLabel, matrix, '}', '{', '{', filename.split(os.sep)[-1], '{', '}', '}', math.ceil(len(matrix)/2), '{', '}', '{', '{', '}', '}', '{', '{', '}', '}', '}', yLabel, '{', xLabel, '{', '{', xLabel, yLabel, matrix, '{', '}', '}', '}', '}')

        script_graphs.append(script4)

    if style_graph == 'wordcloud':
        dic = getValuesWordcloud(filename)

        script3 = """
        let meio = {}[parseInt({}.length/2)][1];
        let grandes = ['#FF58B2', '#D04AFF', '#0F61FF', '#F96060', '#FFCEFA'];
        let pequenas = ['#AAFF9C', '#A7EEA6', '#87C5FF', '#FFFFFF'];
        WordCloud(document.getElementById('wordcloud'),
        {} 
            list: {},
            gridSize: 18,
            weightFactor: 15,
            fontFamily: 'Times, serif',
            color: function (word, weight) {}
                return (weight > meio) ? grandes[Math.floor(Math.random() * grandes.length)] : pequenas[Math.floor(Math.random() * pequenas.length)];
            {},
            backgroundColor: '#1B2542'
        {});        
        """.format(dic, dic, '{', dic, '{', '}', '}')

        script_graphs.append(script3)

    if style_graph == 'topretweets':
        top_rt = True
        filename_splited, num_rt_str = filename.split('?')
        num_rt = int(num_rt_str)
        top_rt_html = getValuesTopRetweets(filename_splited, num_rt)
        continue

    list_graphs.append(style_graph)

arq = open("teste_viz.html", 'w', encoding='utf-8')
arq.write(getHead())
arq.write(getBody(list_graphs))
if top_rt:
    arq.write(top_rt_html)

arq.write(getScript(script_graphs))
arq.close()
