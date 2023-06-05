def getHead():
    head = """<!DOCTYPE html>
    <head>
    <script src='https://cdn.plot.ly/plotly-2.8.3.min.js'></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjs/6.2.1/math.js"></script>
    <script src='https://cdnjs.cloudflare.com/ajax/libs/wordcloud2.js/1.1.1/wordcloud2.min.js'></script>
</head>

"""

    return head

def getBody(params):
    body = "<body style='background-color: #1B2542'>\n"
    for elem in params:
        if elem == 'wordcloud':
            body += f"<h3 style='text-align: center; color: white; font-size: 36px; font-family: Montserrat; font-weight: bold'>Wordcloud</h3>\n"
            body += f"    <div id='{elem}' style='width:100%;height:250px'>\n"
            body += f"    <canvas></canvas>\n"
            body += "</div>\n"
        
        else:
            body += f"    <div id='{elem}'></div>\n"

    body += "</body>\n\n"

    return body

def getScript(programs):
    script = "<script>\n"
    for elem in programs:
        script += f"{elem}\n"

    script += "</script>"

    return script