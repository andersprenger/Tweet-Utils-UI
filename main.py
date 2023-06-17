import os
import platform
import sys

from PySide6.QtCore import QCoreApplication, QUrl, QProcess

from telas.main_window import *

if platform.system() == 'Windows':
    NAME_PYTHON = "python"

else:
    NAME_PYTHON = "python3"


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.show()

        # nome da janela da aplicação
        self.setWindowTitle("Tweet Utils UI")

        self.ui = UI_MainWindow()
        self.ui.init_window(self)
        self.ui.botao_home.clicked.connect(lambda: self.changeScreen(self.ui.ui_pages.home, self.ui.botao_home))
        self.ui.botaoMenu_Quick_report.clicked.connect(
            lambda: self.changeScreen(self.ui.ui_pages.quick_report, self.ui.botaoMenu_Quick_report))
        self.ui.botaoMenu_Sentiment_Analysis.clicked.connect(
            lambda: self.changeScreen(self.ui.ui_pages.sentiment_analysis, self.ui.botaoMenu_Sentiment_Analysis))
        self.ui.botaoMenu_Rest_gathering.clicked.connect(
            lambda: self.changeScreen(self.ui.ui_pages.rest_gathering, self.ui.botaoMenu_Rest_gathering))
        self.ui.botaoMenu_Sanitize_tweets.clicked.connect(
            lambda: self.changeScreen(self.ui.ui_pages.sanitize_tweets, self.ui.botaoMenu_Sanitize_tweets))
        self.ui.botaoMenu_Gather_profile.clicked.connect(
            lambda: self.changeScreen(self.ui.ui_pages.gather_profile, self.ui.botaoMenu_Gather_profile))
        self.ui.botaoMenu_newVisualizacao.clicked.connect(
            lambda: self.changeScreen(self.ui.ui_pages.newViz, self.ui.botaoMenu_newVisualizacao))
        self.ui.botaoMenu_dashboard.clicked.connect(
            lambda: self.changeScreen(self.ui.ui_pages.dashboard, self.ui.botaoMenu_dashboard))

        self.ui.botao_home.set_active(True)
        self.buttons = [self.ui.botao_home, self.ui.botaoMenu_Quick_report, self.ui.botaoMenu_Sentiment_Analysis,
                        self.ui.botaoMenu_Rest_gathering, self.ui.botaoMenu_Sanitize_tweets,
                        self.ui.botaoMenu_Gather_profile, self.ui.botaoMenu_newVisualizacao,
                        self.ui.botaoMenu_dashboard]

        # Aqui deve ser ligado todos os botoes de todas as telas. Cada botão deve chamar sua respectiva função (ou
        # seja, a "runScriptModel" com seus parâmetros).
        self.ui.ui_pages.quick_report_runButton.clicked.connect(lambda: self.runScriptModel(
            self.ui.ui_pages.quick_report_displayOutput, "quick_report.py"))
        self.ui.ui_pages.sentiment_analysis_runButton.clicked.connect(lambda: self.runScriptModel(
            self.ui.ui_pages.sentiment_analysis_displayOutput, "sentiment_analysis.py"))
        self.ui.ui_pages.rest_gathering_runButton.clicked.connect(lambda: self.runScriptModel(
            self.ui.ui_pages.rest_gathering_displayOutput, "rest_gathering.py"))
        self.ui.ui_pages.sanitize_tweets_runButton.clicked.connect(lambda: self.runScriptModel(
            self.ui.ui_pages.sanitize_tweets_displayOutput, "sanitize_tweets.py"))
        self.ui.ui_pages.gather_profile_runButton.clicked.connect(lambda: self.runScriptModel(
            self.ui.ui_pages.gather_profile_displayOutput, "gather_profile.py"))
        self.ui.ui_pages.newViz_runButton.clicked.connect(
            lambda: self.runScriptModel(self.ui.ui_pages.newViz_displayDebug, "testeViz"))
        self.ui.ui_pages.home_saveButton.clicked.connect(
            lambda: self.saveKey())
        self.ui.ui_pages.dashboard_refreshButton.clicked.connect(lambda: self.refreshViz())

    # ////////////////////////////////////////////////////////////////////////////////////////////////////
    # funções para imprimir no console da aplicação

    # função que imprime as saidas normais do script
    def handle_stdout(self, console: QTextBrowser):
        data = self.teste.readAllStandardOutput()
        stdout = bytes(data).decode("utf8")
        console.append(stdout)

    # função que imprime os erros do script
    def handle_stderr(self, console: QTextBrowser):
        data = self.teste.readAllStandardError()
        stderr = bytes(data).decode("utf8")
        console.append(stderr)

    # função que imprime quando o script termina
    def process_finished(self, console: QTextBrowser):
        console.append("Process finished.")
        if console == self.ui.ui_pages.newViz_displayDebug:
            self.refreshViz()

        self.teste = None

    # função que dispara o script
    def runScriptModel(self, console: QTextBrowser, script: str):
        console.clear()
        console.append("Executing process.")
        self.teste = QProcess()

        # switch com todos os modulos
        if script == "quick_report.py":
            args = [self.getPath("scripts") + script]
            # if self.ui.ui_pages.quick_report_input.text().strip() != "":
            args.append("-i")
            args.append(self.getPath("gathering") +
                        self.ui.ui_pages.quick_report_input.currentText())

            if self.ui.ui_pages.quick_report_output.text().strip() != "":
                args.append("-o")
                args.append(self.getPath("gathering") +
                            self.ui.ui_pages.quick_report_output.text())

            args.append("-dc")
            args.append(self.ui.ui_pages.quick_report_display_count.text())

            self.teste.start(NAME_PYTHON, args)

        elif script == "sentiment_analysis.py":
            args = [self.getPath("scripts") + script]
            args.append("-i")
            args.append(self.getPath("gathering") +
                        self.ui.ui_pages.sentiment_analysis_input.currentText())

            args.append("-o")
            if self.ui.ui_pages.sentiment_analysis_output.text().strip() != "":
                args.append(self.getPath("gathering") +
                            self.ui.ui_pages.sentiment_analysis_output.text())

            else:
                args.append(self.getPath("gathering") + 'output_sentiments.json')

            self.teste.start(NAME_PYTHON, args)

        elif script == "rest_gathering.py":
            args = [self.getPath("scripts") + script]
            if self.ui.ui_pages.rest_gathering_input.text().strip() != "":
                args.append("-q")
                args.append(self.ui.ui_pages.rest_gathering_input.text())

            args.append("-o")
            if self.ui.ui_pages.rest_gathering_output.text().strip() != "":
                args.append(self.getPath("gathering") +
                            self.ui.ui_pages.rest_gathering_output.text())

            else:
                args.append(self.getPath("gathering") + 'output.json')

            data_inicio = self.ui.ui_pages.rest_gathering_dateInicio.text().split(" ")
            dia = '-'.join(data_inicio[0].split('/')[::-1]) + "T"
            hora = data_inicio[1] + "Z"
            data_inicio = dia + hora
            args.append("-s")
            args.append(data_inicio)

            data_final = self.ui.ui_pages.rest_gathering_dateFim.text().split(" ")
            dia = '-'.join(data_final[0].split('/')[::-1]) + "T"
            hora = data_final[1] + "Z"
            data_final = dia + hora
            args.append("-u")
            args.append(data_final)

            if self.ui.ui_pages.rest_gathering_checkbox_limite.isChecked():
                args.append("-m")
                args.append(self.ui.ui_pages.rest_gathering_limite.text())

            args.append("-l")
            args.append(self.ui.ui_pages.rest_gathering_lingua.currentText())

            self.teste.start(NAME_PYTHON, args)

        elif script == "sanitize_tweets.py":
            args = [self.getPath("scripts") + script]
            # if self.ui.ui_pages.sanitize_tweets_input.text().strip() != "":
            args.append("-i")
            args.append(self.getPath("gathering") +
                        self.ui.ui_pages.sanitize_tweets_input.currentText())

            args.append("-o")
            if self.ui.ui_pages.sanitize_tweets_output.text().strip() != "":
                args.append(self.getPath("gathering") +
                            self.ui.ui_pages.sanitize_tweets_output.text())

            else:
                args.append(self.getPath("gathering") + 'output_clean.json')

            if self.ui.ui_pages.sanitize_tweets_cleanEmoji.isChecked():
                args.append("-e")

            if self.ui.ui_pages.sanitize_tweets_removeRT.isChecked():
                args.append("-rt")

            args.append("-s")
            args.append(self.getPath("stopwords") + 'stopwords_pt-br.txt')

            self.teste.start(NAME_PYTHON, args)

        elif script == "gather_profile.py":
            args = [self.getPath("scripts") + script]
            if self.ui.ui_pages.gather_profile_input.text().strip() != "":
                args.append("-u")
                args.append(self.ui.ui_pages.gather_profile_input.text())

            args.append("-o")
            if self.ui.ui_pages.gather_profile_output.text().strip() != "":
                args.append(self.getPath("gathering") +
                            self.ui.ui_pages.gather_profile_output.text())

            else:
                args.append(self.getPath("gathering") + 'output_profile.json')

            self.teste.start(NAME_PYTHON, args)

        elif script == "testeViz":
            args = [self.getPath("scripts") + "testeHTML.py"]
            input_graphs = []

            if self.ui.ui_pages.newViz_lineplot_checkbox.isChecked():
                input_graphs.append("lineplot/" + self.getPath("gathering") +
                                    self.ui.ui_pages.newViz_lineplot_input.currentText())

                # the presence of sentiments will be checked in the lineplot script
                input_graphs.append("sentiments/" + self.getPath("gathering") +
                                    self.ui.ui_pages.newViz_lineplot_input.currentText())

            if self.ui.ui_pages.newViz_heatmap_checkbox.isChecked():
                input_graphs.append("heatmap/" + self.getPath("gathering") +
                                    self.ui.ui_pages.newViz_heatmap_input.currentText())

            if self.ui.ui_pages.newVizheatmapminute_checkbox.isChecked():
                input_graphs.append("heatmapMinute/" + self.getPath("gathering") +
                                    self.ui.ui_pages.newViz_heatmapminute_input.currentText())

            if self.ui.ui_pages.newViz_wordcloud_checkbox.isChecked():
                input_graphs.append("wordcloud/" + self.getPath("gathering") +
                                    self.ui.ui_pages.newViz_wordcloud_input.currentText())

            if self.ui.ui_pages.newViz_topretweets_checkbox.isChecked():
                input_graphs.append("topretweets/" + self.getPath("gathering") +
                                    self.ui.ui_pages.newViz_topretweets_input.currentText() + "?" +
                                    self.ui.ui_pages.newViz_topretweets_limite.text())

            args.append("-i")
            args.append(';'.join(input_graphs))
            self.teste.start(NAME_PYTHON, args)

        self.teste.readyReadStandardOutput.connect(
            lambda: self.handle_stdout(console))
        self.teste.readyReadStandardError.connect(
            lambda: self.handle_stderr(console))
        self.teste.finished.connect(lambda: self.process_finished(console))

    # ////////////////////////////////////////////////////////////////////////////////////////////////////

    # função para atualizar html de visualização
    def refreshViz(self):
        self.ui.ui_pages.view.load(QUrl.fromLocalFile(MainWindow.getPath(self, "root") + os.sep + "teste_viz.html"))
        self.ui.ui_pages.view.resize(self.width() - 295, self.height())
        self.ui.ui_pages.view.show()

    # função para salvar a key para coleta
    def saveKey(self):
        if self.ui.ui_pages.home_key.text().strip() != "":
            arq = open(
                f'{os.path.dirname(os.path.abspath(__file__))}{os.sep}DATA{os.sep}keys.txt', 'w')
            arq.write(self.ui.ui_pages.home_key.text().strip())
            arq.close()
            self.ui.ui_pages.home_saveButton.setText(
                QCoreApplication.translate("StackedWidget", u"Salvo com sucesso", None))
            self.ui.ui_pages.home_saveButton.setStyleSheet(
                "border-radius: 5px; background-color: #E3BF20; color: white;")

    # função para mudar de tela
    def changeScreen(self, screen: QWidget, button):
        for b in self.buttons:
            b.set_active(False)

        button.set_active(True)
        if screen == self.ui.ui_pages.sanitize_tweets:
            self.ui.ui_pages.sanitize_tweets_input.clear()
            self.ui.ui_pages.sanitize_tweets_input.addItems(self.ui.ui_pages.showFilesInput())

        if screen == self.ui.ui_pages.quick_report:
            self.ui.ui_pages.quick_report_input.clear()
            self.ui.ui_pages.quick_report_input.addItems(self.ui.ui_pages.showFilesInput())

        if screen == self.ui.ui_pages.sentiment_analysis:
            self.ui.ui_pages.sentiment_analysis_input.clear()
            self.ui.ui_pages.sentiment_analysis_input.addItems(self.ui.ui_pages.showFilesInput())

        if screen == self.ui.ui_pages.newViz:
            self.ui.ui_pages.newViz_lineplot_input.clear()
            self.ui.ui_pages.newViz_heatmap_input.clear()
            self.ui.ui_pages.newViz_wordcloud_input.clear()
            self.ui.ui_pages.newViz_topretweets_input.clear()
            self.ui.ui_pages.newViz_heatmapminute_input.clear()

            self.ui.ui_pages.newViz_lineplot_input.addItems(self.ui.ui_pages.showFilesInput())
            self.ui.ui_pages.newViz_heatmap_input.addItems(self.ui.ui_pages.showFilesInput())
            self.ui.ui_pages.newViz_wordcloud_input.addItems(self.ui.ui_pages.showFilesInput(True))
            self.ui.ui_pages.newViz_topretweets_input.addItems(self.ui.ui_pages.showFilesInput())
            self.ui.ui_pages.newViz_heatmapminute_input.addItems(self.ui.ui_pages.showFilesInput())

        if screen == self.ui.ui_pages.dashboard:
            self.refreshViz()

        self.ui.pages.setCurrentWidget(screen)

    # função que retorna path especifico
    def getPath(self, destiny):
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

        if destiny == "root":
            return ROOT_DIR

        elif destiny == "viz":
            return ROOT_DIR + "{}DATA{}viz{}".format(os.sep, os.sep, os.sep)

        elif destiny == "gathering":
            return ROOT_DIR + "{}DATA{}gathering{}".format(os.sep, os.sep, os.sep)

        elif destiny == "scripts":
            return ROOT_DIR + "{}scripts{}".format(os.sep, os.sep)

        elif destiny == "stopwords":
            return ROOT_DIR + "{}scripts{}stopwords{}".format(os.sep, os.sep, os.sep)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
