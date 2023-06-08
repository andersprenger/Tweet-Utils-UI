################################################################################
# Form generated from reading UI file 'untitledowgQMA.ui'
##
# Created by: Qt User Interface Compiler version 6.1.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import os

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWebEngineWidgets import *
from PySide6.QtWidgets import *

from main import MainWindow


class Ui_StackedWidget(object):
    def languageFilter(self):
        return ['None', 'pt', 'es', 'en', 'pt and en']

    def showFilesInput(self, hasTxt = False):
        if not hasTxt:
            return [file for file in os.listdir(MainWindow.getPath(self, "gathering")) if ".json" in file]

        return [file for file in os.listdir(MainWindow.getPath(self, "gathering")) if ".txt" in file or ".json" in file]

    def setupUi(self, StackedWidget):
        if not StackedWidget.objectName():
            StackedWidget.setObjectName(u"StackedWidget")
        StackedWidget.resize(935, 720)

        ###############################################################
        ##                                                           ##
        ##  HOME                                                     ##
        ##                                                           ##
        ###############################################################
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet("background-color: #1B2542")
        self.home_title = QLabel(self.home)
        self.home_title.setObjectName(u"home_title")
        self.home_title.setStyleSheet("""
            color: white;
            font-family: 'Montserrat';
            font-weight: 700;
            font-size: 96px;
            line-height: 117px;""")
        self.home_title.setGeometry(QRect(134, 128, 718, 93))

        self.home_title2 = QLabel(self.home)
        self.home_title2.setObjectName(u"home_title")
        self.home_title2.setStyleSheet("""
            color: #7C21F0;
            font-family: 'Montserrat';
            font-weight: 700;
            font-size: 96px;
            line-height: 117px;""")
        self.home_title2.setGeometry(QRect(476, 128, 230, 93))

        self.home_key = QLineEdit(self.home)
        self.home_key.setObjectName(u"home_key")
        self.home_key.setStyleSheet("""
            background-color: white;
            color: white;
            font-family: Montserrat;""")
        self.home_key.setGeometry(QRect(123, 336, 764, 48))

        self.home_saveButton = QPushButton(self.home)
        self.home_saveButton.setObjectName(u"home_saveButton")
        self.home_saveButton.setStyleSheet("""
            border-radius: 10px;
            background-color: #8321FF;
            color: white;
            font-weight: 700;
            font-family: 'Montserrat';
            font-size: 24px;""")
        self.home_saveButton.setGeometry(QRect(426, 535, 131, 55))

        self.home_label_key = QLabel(self.home)
        self.home_label_key.setObjectName(u"home_label_key")
        self.home_label_key.setStyleSheet("""
            color: white;
            font-family: 'Montserrat';
            font-size: 24px;""")
        self.home_label_key.setGeometry(QRect(123, 305, 220, 29))

        self.home_helpButton = QPushButton(self.home)
        self.home_helpButton.setObjectName(u"home_helpButton")
        self.home_helpButton.setGeometry(QRect(911, 646, 60, 60))
        self.home_helpButton.setMask(QRegion(QRect(0,0,58,58), QRegion.Ellipse))
        self.home_helpButton.setStyleSheet("""
            border-radius: 1px;
            background-color: #8321FF;
            font-weight: 700;
            font-family: 'Montserrat';
            color: white;
            font-size: 24px;
        """)

        self.home_infoboard = QTextBrowser(self.home)
        self.home_infoboard.setObjectName(u"home_infoboard")
        self.home_infoboard.setGeometry(QRect(123, 230, 764, 520))
        self.home_infoboard.setStyleSheet("""
            border-style: solid;
            background-color: #1B2542;
            border-color: #1B2542;
            color: white;
            font-family: 'Montserrat'
        """)

        self.home_infoboard.setText("""
        Welcome to Tweet Utils UI.
        With this application, you can extract, sanitize and make visualizations from Twitter data.
        To collect data, you will need to request permission to Twitter on your site to developers.
        If you have been accepted, so you have access to keys and can extract data!
        You just need to paste the bearer key given on this page.

        With this you can extract Twitter data with these modules:
            * Rest Gathering
            * Gather Profile

        You can sanitize this data collected with:
            * Quick Report
            * Sanitize Tweets

        And you can make visualizations and show them with:
            * Visualizations
            * Dashboard
        """)

        self.home_infoboard.setHidden(True)
        self.home_helpButton.clicked.connect(lambda: self.home_infoboard.setHidden(not self.home_infoboard.isHidden()))

        StackedWidget.addWidget(self.home)

        ###############################################################
        ##                                                           ##
        ##  QUICK REPORT                                             ##
        ##                                                           ##
        ###############################################################
        self.quick_report = QWidget()
        self.quick_report.setObjectName(u"quick_report")
        self.quick_report.setStyleSheet("background-color: #1B2542")

        self.quick_report_runButton = QPushButton(self.quick_report)
        self.quick_report_runButton.setObjectName(u"quick_report_runButton")
        self.quick_report_runButton.setStyleSheet("""
            border-radius: 10px;
            background-color: #8321FF;
            color: white;
            font-weight: 700;
            font-family: 'Montserrat';
            font-size: 24px;""")
        self.quick_report_runButton.setGeometry(QRect(687, 299, 131, 55))

        self.quick_report_label_input = QLabel(self.quick_report)
        self.quick_report_label_input.setObjectName(
            u"quick_report_label_input")
        self.quick_report_label_input.setStyleSheet(
            "color: white; font-family: 'Montserrat'; font-size: 24px;")
        self.quick_report_label_input.setGeometry(QRect(168, 198, 78, 29))

        self.quick_report_label_output = QLabel(self.quick_report)
        self.quick_report_label_output.setObjectName(u"quick_report_label_output")
        self.quick_report_label_output.setStyleSheet("""
            color: white;
            font-family: 'Montserrat';
            font-size: 24px;""")
        self.quick_report_label_output.setGeometry(QRect(518, 198, 221, 29))

        self.quick_report_display_count = QSpinBox(self.quick_report)
        self.quick_report_display_count.setObjectName(
            u"quick_report_display_count")
        self.quick_report_display_count.setGeometry(QRect(168, 312, 63, 39))
        self.quick_report_display_count.setStyleSheet(u"""
            QSpinBox{
                background-color: #ffffff;
                border-style: solid;
                border-color: #ffffff;
                border-radius: 10px;
                color: black;
                font-family: 'Montserrat';
                font-size: 24px;
            }

            QSpinBox::up-button{
                background-color: #10121A;
                border-top-right-radius: 8px;
                width: 24px;
                height: 20px;
            }

            QSpinBox::up-arrow{
                image: url(./icones/arrow_up.png);
                width: 10px;
                height: 12px;
            }

            QSpinBox::down-button{
                background-color: #10121A;
                border-bottom-right-radius: 8px;
                width: 24px;
                height: 20px;
            }

            QSpinBox::down-arrow{
                image: url(./icones/arrow_down.png);
                width: 10px;
                height: 12px;
            }""")
        self.quick_report_display_count.setValue(10)

        self.quick_report_title = QLabel(self.quick_report)
        self.quick_report_title.setObjectName(u"quick_report_title")
        self.quick_report_title.setStyleSheet(
            "color: white; font-family: 'Montserrat'; font-weight: 700; font-size: 36px; line-height: 44px;")
        self.quick_report_title.setGeometry(QRect(346, 100, 293, 45))

        self.quick_report_input = QComboBox(self.quick_report)
        self.quick_report_input.setObjectName(u"quick_report_input")
        self.quick_report_input.setStyleSheet(u"""
            QComboBox {
                background-color: #ffffff;
                border-style: solid;
                border-color: #ffffff;
                color: black;
                font-family: 'Montserrat';
            }

            QComboBox QAbstractItemView {
                background-color: white;
                color: black;
                font-family: 'Montserrat';
            }

            QComboBox::drop-down {
                background-color: #10121A;
                width: 24px;
                height: 54px;
            }

            QComboBox::down-arrow {
                image: url(./icones/arrow_down.png);
            }
            """)
        self.quick_report_input.setGeometry(QRect(168, 227, 300, 48))

        self.quick_report_output = QLineEdit(self.quick_report)
        self.quick_report_output.setObjectName(u"quick_report_output")
        self.quick_report_output.setStyleSheet(
            "background-color: #ffffff; border-style: solid; color: black; font-family: 'Montserrat';")
        self.quick_report_output.setGeometry(QRect(518, 227, 300, 48))

        self.quick_report_displayOutput = QTextBrowser(self.quick_report)
        self.quick_report_displayOutput.setStyleSheet(
            "background-color: #10121A; border-style: solid; border-color: #10121A; border-radius: 10px; color: white; font-family: 'Montserrat'")
        self.quick_report_displayOutput.setObjectName(
            u"quick_report_displayOutput")
        self.quick_report_displayOutput.setGeometry(QRect(168, 378, 650, 281))

        self.quick_report_display_count_label = QLabel(self.quick_report)
        self.quick_report_display_count_label.setObjectName(
            u"quick_report_display_count_label")
        self.quick_report_display_count_label.setGeometry(
            QRect(240, 317, 186, 29))
        self.quick_report_display_count_label.setStyleSheet(
            "color: white; font-family: 'Montserrat'; font-size: 24px;")

        self.quick_report_helpButton = QPushButton(self.quick_report)
        self.quick_report_helpButton.setObjectName(u"quick_report_helpButton")
        self.quick_report_helpButton.setGeometry(QRect(911, 646, 60, 60))
        self.quick_report_helpButton.setMask(QRegion(QRect(0,0,58,58), QRegion.Ellipse))
        self.quick_report_helpButton.setStyleSheet("""
            border-radius: 1px;
            background-color: #8321FF;
            font-weight: 700;
            font-family: 'Montserrat';
            color: white;
            font-size: 24px;
        """)

        self.quick_report_infoboard = QTextBrowser(self.quick_report)
        self.quick_report_infoboard.setObjectName(u"quick_report_infoboard")
        self.quick_report_infoboard.setGeometry(QRect(160, 150, 665, 520))
        self.quick_report_infoboard.setStyleSheet("""
            border-style: solid;
            background-color: #1B2542;
            border-color: #1B2542;
            color: white;
            font-family: 'Montserrat'
        """)

        self.quick_report_infoboard.setText("""
        Generates a summary of the data contained in a Tweet dataset

            * Input: Filename for the input JSON.

            * Display Counts: Display limit for most mentioned words, users,
            and hashtags.

            * Output: Filename for the resulting output. The default is "report.txt".
        """)

        self.quick_report_input.addItems(self.showFilesInput())
        self.quick_report_infoboard.setHidden(True)
        self.quick_report_helpButton.clicked.connect(lambda: self.quick_report_infoboard.setHidden(not self.quick_report_infoboard.isHidden()))

        StackedWidget.addWidget(self.quick_report)

        ###############################################################
        ##                                                           ##
        ##  REST GATHERING                                           ##
        ##                                                           ##
        ###############################################################
        self.rest_gathering = QWidget()
        self.rest_gathering.setStyleSheet("background-color: #1B2542")
        self.rest_gathering.setObjectName(u"rest_gathering")

        self.rest_gathering_title = QLabel(self.rest_gathering)
        self.rest_gathering_title.setObjectName(u"rest_gathering_title")
        self.rest_gathering_title.setStyleSheet("""
            color: white;
            font-weight: 700;
            font-family: 'Montserrat';
            font-size: 36px;""")
        self.rest_gathering_title.setGeometry(QRect(326, 100, 332, 45))

        self.rest_gathering_input = QLineEdit(self.rest_gathering)
        self.rest_gathering_input.setObjectName(u"rest_gathering_input")
        self.rest_gathering_input.setStyleSheet("""
            background-color: #ffffff;
            color: black;
            font-family: 'Montserrat';""")
        self.rest_gathering_input.setGeometry(QRect(165, 200, 650, 48))

        self.rest_gathering_label_input = QLabel(self.rest_gathering)
        self.rest_gathering_label_input.setObjectName(
            u"rest_gathering_label_input")
        self.rest_gathering_label_input.setStyleSheet("""
            color: white;
            font-family: 'Montserrat';
            font-size: 24px;""")
        self.rest_gathering_label_input.setGeometry(QRect(165, 169, 77, 29))

        self.rest_gathering_dateInicio = QDateTimeEdit(self.rest_gathering)
        self.rest_gathering_dateInicio.setObjectName(
            u"rest_gathering_dateInicio")
        self.rest_gathering_dateInicio.setStyleSheet(u"""
            QDateTimeEdit{
                background-color: #ffffff;
                color: black;
                font-family: 'Montserrat';
            }

            QDateTimeEdit::up-button{
                background-color: #10121A;
                width: 28px;
                height: 28px;
            }

            QDateTimeEdit::up-arrow{
                image: url(./icones/arrow_up.png);
                width: 10px;
                height: 12px;
            }

            QDateTimeEdit::down-button{
                background-color: #10121A;
                width: 28px;
                height: 28px;
            }

            QDateTimeEdit::down-arrow{
                image: url(./icones/arrow_down.png);
                width: 10px;
                height: 12px;
            }""")
        self.rest_gathering_dateInicio.setGeometry(QRect(165, 292, 204, 48))

        self.rest_gathering_dateInicio_label = QLabel(self.rest_gathering)
        self.rest_gathering_dateInicio_label.setObjectName(
            u"rest_gathering_dateInicio_label")
        self.rest_gathering_dateInicio_label.setStyleSheet("""
            color: white;
            font-family: 'Montserrat';
            font-size: 24px;""")
        self.rest_gathering_dateInicio_label.setGeometry(
            QRect(165, 261, 130, 29))
        
        # Definindo o formato de exibição como "DD/MM/YYYY HH:MM", para corrigir incompatibilidade com macOS
        self.rest_gathering_dateInicio.setDisplayFormat("dd/MM/yyyy HH:mm")

        self.rest_gathering_dateFim = QDateTimeEdit(self.rest_gathering)
        self.rest_gathering_dateFim.setObjectName(u"rest_gathering_dateFim")
        self.rest_gathering_dateFim.setStyleSheet(u"""
            QDateTimeEdit{
                background-color: #ffffff;
                color: black;
                font-family: 'Montserrat';
            }

            QDateTimeEdit::up-button{
                background-color: #10121A;
                width: 28px;
                height: 28px;
            }

            QDateTimeEdit::up-arrow{
                image: url(./icones/arrow_up.png);
                width: 10px;
                height: 12px;
            }

            QDateTimeEdit::down-button{
                background-color: #10121A;
                width: 28px;
                height: 28px;
            }

            QDateTimeEdit::down-arrow{
                image: url(./icones/arrow_down.png);
                width: 10px;
                height: 12px;
            }""")
        self.rest_gathering_dateFim.setGeometry(QRect(384, 292, 204, 48))

        # Definindo o formato de exibição como "DD/MM/YYYY HH:MM", para corrigir incompatibilidade com macOS
        self.rest_gathering_dateFim.setDisplayFormat("dd/MM/yyyy HH:mm")

        self.rest_gathering_dateFim_label = QLabel(self.rest_gathering)
        self.rest_gathering_dateFim_label.setObjectName(
            u"rest_gathering_dateFim_label")
        self.rest_gathering_dateFim_label.setStyleSheet("""
            color: white;
            font-family: 'Montserrat';
            font-size: 24px;""")
        self.rest_gathering_dateFim_label.setGeometry(QRect(384, 261, 120, 29))

        self.rest_gathering_lingua = QComboBox(self.rest_gathering)
        self.rest_gathering_lingua.setObjectName(u"rest_gathering_lingua")
        self.rest_gathering_lingua.setStyleSheet(u"""
            QComboBox {
                background-color: #ffffff;
                border-style: solid;
                border-color: #ffffff;
                color: black;
                font-family: 'Montserrat';
            }

            QComboBox QAbstractItemView {
                background-color: white;
                color: black;
                font-family: 'Montserrat';
            }

            QComboBox::drop-down {
                background-color: #10121A;
                width: 24px;
                height: 54px;
            }

            QComboBox::down-arrow {
                image: url(./icones/arrow_down.png);
            }
            """)
        self.rest_gathering_lingua.setGeometry(QRect(604, 292, 204, 48))

        self.rest_gathering_lingua_label = QLabel(self.rest_gathering)
        self.rest_gathering_lingua_label.setObjectName(
            u"rest_gathering_lingua_label")
        self.rest_gathering_lingua_label.setStyleSheet("""
            color: white;
            font-family: 'Montserrat';
            font-size: 24px;""")
        self.rest_gathering_lingua_label.setGeometry(QRect(604, 261, 120, 29))

        self.rest_gathering_limite = QSpinBox(self.rest_gathering)
        self.rest_gathering_limite.setObjectName(u"rest_gathering_limite")
        self.rest_gathering_limite.setStyleSheet(u"""
            QSpinBox{
                background-color: #ffffff;
                border-style: solid;
                border-color: #ffffff;
                border-radius: 10px;
                color: black;
                font-family: 'Montserrat';
                font-size: 24px;
            }

            QSpinBox::up-button{
                background-color: #10121A;
                border-top-right-radius: 8px;
                width: 24px;
                height: 20px;
            }

            QSpinBox::up-arrow{
                image: url(./icones/arrow_up.png);
                width: 10px;
                height: 12px;
            }

            QSpinBox::down-button{
                background-color: #10121A;
                border-bottom-right-radius: 8px;
                width: 24px;
                height: 20px;
            }

            QSpinBox::down-arrow{
                image: url(./icones/arrow_down.png);
                width: 10px;
                height: 12px;
            }""")
        self.rest_gathering_limite.setGeometry(QRect(283, 392, 80, 39))
        self.rest_gathering_limite.setMaximum(100000000)

        self.rest_gathering_limite_label = QLabel(self.rest_gathering)
        self.rest_gathering_limite_label.setObjectName(u"rest_gathering_limite_label")
        self.rest_gathering_limite_label.setStyleSheet("""
            color: white;
            font-family: 'Montserrat';
            font-size: 24px;""")
        self.rest_gathering_limite_label.setGeometry(QRect(193, 398, 76, 29))

        self.rest_gathering_checkbox_limite = QCheckBox(self.rest_gathering)
        self.rest_gathering_checkbox_limite.setObjectName(
            u"rest_gathering_checkbox_limite")
        self.rest_gathering_checkbox_limite.setStyleSheet(u"""
            QCheckBox::indicator{
                background-color: #ffffff;
                border-style: solid;
                border-color: #ffffff;
                border-radius: 4px;
                width: 20px;
                height: 16px;
            }

            QCheckBox::indicator:checked {
                image: url(./icones/check.png);
            }""")
        self.rest_gathering_checkbox_limite.setGeometry(QRect(165, 404, 20, 16))

        self.rest_gathering_output = QLineEdit(self.rest_gathering)
        self.rest_gathering_output.setObjectName(u"rest_gathering_output")
        self.rest_gathering_output.setStyleSheet("""
            background-color: #ffffff;
            color: black;
            font-family: 'Montserrat';""")
        self.rest_gathering_output.setGeometry(QRect(398, 383, 189, 48))

        self.rest_gathering_output_label = QLabel(self.rest_gathering)
        self.rest_gathering_output_label.setObjectName(
            u"rest_gathering_output_label")
        self.rest_gathering_output_label.setStyleSheet("""
            color: white;
            font-family: 'Montserrat';
            font-size: 24px;""")
        self.rest_gathering_output_label.setGeometry(QRect(382, 353, 221, 29))

        self.rest_gathering_runButton = QPushButton(self.rest_gathering)
        self.rest_gathering_runButton.setObjectName(u"rest_gathering_runButton")
        self.rest_gathering_runButton.setStyleSheet("""
            border-radius: 10px;
            background-color: #8321FF;
            font-weight: 700;
            font-family: 'Montserrat';
            font-size: 24px;
            color: white;""")
        self.rest_gathering_runButton.setGeometry(QRect(684, 376, 131, 55))

        self.rest_gathering_displayOutput = QTextBrowser(self.rest_gathering)
        self.rest_gathering_displayOutput.setObjectName(u"rest_gathering_displayOutput")
        self.rest_gathering_displayOutput.setStyleSheet("""
            background-color: #10121A;
            border-radius: 10px;
            color: white;
            font-family: 'Montserrat'""")
        self.rest_gathering_displayOutput.setGeometry(
            QRect(165, 445, 650, 235))

        self.rest_gathering_helpButton = QPushButton(self.rest_gathering)
        self.rest_gathering_helpButton.setObjectName(u"rest_gathering_helpButton")
        self.rest_gathering_helpButton.setGeometry(QRect(911, 646, 60, 60))
        self.rest_gathering_helpButton.setMask(QRegion(QRect(0,0,58,58), QRegion.Ellipse))
        self.rest_gathering_helpButton.setStyleSheet("""
            border-radius: 1px;
            background-color: #8321FF;
            font-weight: 700;
            font-family: 'Montserrat';
            color: white;
            font-size: 24px;
        """)

        self.rest_gathering_infoboard = QTextBrowser(self.rest_gathering)
        self.rest_gathering_infoboard.setObjectName(u"rest_gathering_infoboard")
        self.rest_gathering_infoboard.setGeometry(QRect(160, 150, 665, 540))
        self.rest_gathering_infoboard.setStyleSheet("""
            border-style: solid;
            background-color: #1B2542;
            border-color: #1B2542;
            color: white;
            font-family: 'Montserrat'
        """)

        self.rest_gathering_infoboard.setText("""
        Collects tweets from keywords in a date range, or the maximum limit allowed at the moment.

        Parameters:
        * Query: A UTF-8 encoded search query of 500 characters maximum.
        For operator's reference, please refer to
        https://developer.twitter.com/en/docs/tweets/rules-and-filtering/overview/standard-operators.html
        
        * Start Time: Returns results that are more recent than the specified date (UTC).
        
        * End Time: Returns results that are older than the specified date (UTC).

        * Language: Returns results that are in the specified language (None will return all of tweets independent of language).
        
        * Limit: Stops the gathering when the max specified number is reached.
        
        * Output: Filename for the resulting output.
        """)

        self.rest_gathering_infoboard.setHidden(True)
        self.rest_gathering_lingua.addItems(self.languageFilter())
        self.rest_gathering_helpButton.clicked.connect(lambda: self.rest_gathering_infoboard.setHidden(not self.rest_gathering_infoboard.isHidden()))

        StackedWidget.addWidget(self.rest_gathering)

        ###############################################################
        ##                                                           ##
        ##  SENTIMENT ANALYSIS                                       ##
        ##                                                           ##
        ###############################################################
        self.sentiment_analysis = QWidget()
        self.sentiment_analysis.setObjectName(u"sentiment_analysis")
        self.sentiment_analysis.setStyleSheet("background-color: #1B2542")

        self.sentiment_analysis_runButton = QPushButton(self.sentiment_analysis)
        self.sentiment_analysis_runButton.setObjectName(u"sentiment_analysis_runButton")
        self.sentiment_analysis_runButton.setStyleSheet("""
            border-radius: 10px;
            background-color: #8321FF;
            color: white;
            font-weight: 700;
            font-family: 'Montserrat';
            font-size: 24px;""")
        self.sentiment_analysis_runButton.setGeometry(QRect(687, 299, 131, 55))

        self.sentiment_analysis_label_input = QLabel(self.sentiment_analysis)
        self.sentiment_analysis_label_input.setObjectName(
            u"sentiment_analysis_label_input")
        self.sentiment_analysis_label_input.setStyleSheet(
            "color: white; font-family: 'Montserrat'; font-size: 24px;")
        self.sentiment_analysis_label_input.setGeometry(QRect(168, 198, 78, 29))

        self.sentiment_analysis_label_output = QLabel(self.sentiment_analysis)
        self.sentiment_analysis_label_output.setObjectName(u"sentiment_analysis_label_output")
        self.sentiment_analysis_label_output.setStyleSheet("""
            color: white;
            font-family: 'Montserrat';
            font-size: 24px;""")
        self.sentiment_analysis_label_output.setGeometry(QRect(518, 198, 221, 29))

        self.sentiment_analysis_title = QLabel(self.sentiment_analysis)
        self.sentiment_analysis_title.setObjectName(u"sentiment_analysis_title")
        self.sentiment_analysis_title.setStyleSheet(
            "color: white; font-family: 'Montserrat'; font-weight: 700; font-size: 36px; line-height: 44px;")
        self.sentiment_analysis_title.setGeometry(QRect(285, 100, 415, 45))

        self.sentiment_analysis_input = QComboBox(self.sentiment_analysis)
        self.sentiment_analysis_input.setObjectName(u"sentiment_analysis_input")
        self.sentiment_analysis_input.setStyleSheet(u"""
            QComboBox {
                background-color: #ffffff;
                border-style: solid;
                border-color: #ffffff;
                color: black;
                font-family: 'Montserrat';
            }

            QComboBox QAbstractItemView {
                background-color: white;
                color: black;
                font-family: 'Montserrat';
            }

            QComboBox::drop-down {
                background-color: #10121A;
                width: 24px;
                height: 54px;
            }

            QComboBox::down-arrow {
                image: url(./icones/arrow_down.png);
            }
            """)
        self.sentiment_analysis_input.setGeometry(QRect(168, 227, 300, 48))

        self.sentiment_analysis_output = QLineEdit(self.sentiment_analysis)
        self.sentiment_analysis_output.setObjectName(u"sentiment_analysis_output")
        self.sentiment_analysis_output.setStyleSheet(
            "background-color: #ffffff; border-style: solid; color: black; font-family: 'Montserrat';")
        self.sentiment_analysis_output.setGeometry(QRect(518, 227, 300, 48))

        self.sentiment_analysis_displayOutput = QTextBrowser(self.sentiment_analysis)
        self.sentiment_analysis_displayOutput.setStyleSheet(
            "background-color: #10121A; border-style: solid; border-color: #10121A; border-radius: 10px; color: white; font-family: 'Montserrat'")
        self.sentiment_analysis_displayOutput.setObjectName(
            u"sentiment_analysis_displayOutput")
        self.sentiment_analysis_displayOutput.setGeometry(QRect(168, 378, 650, 281))

        self.sentiment_analysis_helpButton = QPushButton(self.sentiment_analysis)
        self.sentiment_analysis_helpButton.setObjectName(u"sentiment_analysis_helpButton")
        self.sentiment_analysis_helpButton.setGeometry(QRect(911, 646, 60, 60))
        self.sentiment_analysis_helpButton.setMask(QRegion(QRect(0,0,58,58), QRegion.Ellipse))
        self.sentiment_analysis_helpButton.setStyleSheet("""
            border-radius: 1px;
            background-color: #8321FF;
            font-weight: 700;
            font-family: 'Montserrat';
            color: white;
            font-size: 24px;
        """)

        self.sentiment_analysis_infoboard = QTextBrowser(self.sentiment_analysis)
        self.sentiment_analysis_infoboard.setObjectName(u"sentiment_analysis_infoboard")
        self.sentiment_analysis_infoboard.setGeometry(QRect(160, 150, 665, 520))
        self.sentiment_analysis_infoboard.setStyleSheet("""
            border-style: solid;
            background-color: #1B2542;
            border-color: #1B2542;
            color: white;
            font-family: 'Montserrat'
        """)

        self.sentiment_analysis_infoboard.setText("""
        Generates a summary of the data contained in a Tweet dataset

            * Input: Filename for the input JSON.

            * Output: Filename for the resulting output. The default is "output_sentiments.json".
        """)

        self.sentiment_analysis_input.addItems(self.showFilesInput())
        self.sentiment_analysis_infoboard.setHidden(True)
        self.sentiment_analysis_helpButton.clicked.connect(lambda: self.sentiment_analysis_infoboard.setHidden(not self.sentiment_analysis_infoboard.isHidden()))

        StackedWidget.addWidget(self.sentiment_analysis)

        ###############################################################
        ##                                                           ##
        ##  SANITIZE TWEETS                                          ##
        ##                                                           ##
        ###############################################################
        self.sanitize_tweets = QWidget()
        self.sanitize_tweets.setObjectName(u"sanitize_tweets")
        self.sanitize_tweets.setStyleSheet("background-color: #1B2542")

        self.sanitize_tweets_title = QLabel(self.sanitize_tweets)
        self.sanitize_tweets_title.setObjectName(u"sanitize_tweets_title")
        self.sanitize_tweets_title.setStyleSheet("""
            color: white;
            font-family: 'Montserrat';
            font-weight: 700;
            font-size: 36px;""")
        self.sanitize_tweets_title.setGeometry(QRect(315, 100, 355, 45))

        self.sanitize_tweets_input_label = QLabel(self.sanitize_tweets)
        self.sanitize_tweets_input_label.setObjectName(u"sanitize_tweets_input_label")
        self.sanitize_tweets_input_label.setStyleSheet("""
            color: white;
            font-family: 'Montserrat';
            font-size: 24px;""")
        self.sanitize_tweets_input_label.setGeometry(QRect(168, 198, 78, 29))

        self.sanitize_tweets_output_label = QLabel(self.sanitize_tweets)
        self.sanitize_tweets_output_label.setObjectName(u"sanitize_tweets_output_label")
        self.sanitize_tweets_output_label.setStyleSheet("""
            color: white;
            font-family: 'Montserrat';
            font-size: 24px;""")
        self.sanitize_tweets_output_label.setGeometry(QRect(518, 198, 221, 29))

        self.sanitize_tweets_input = QComboBox(self.sanitize_tweets)
        self.sanitize_tweets_input.setObjectName(u"sanitize_tweets_input")
        self.sanitize_tweets_input.setStyleSheet(u"""
            QComboBox {
                background-color: #ffffff;
                border-style: solid;
                border-color: #ffffff;
                color: black;
                font-family: 'Montserrat';
            }

            QComboBox QAbstractItemView {
                background-color: white;
                color: black;
                font-family: 'Montserrat';
            }

            QComboBox::drop-down {
                background-color: #10121A;
                width: 24px;
                height: 54px;
            }

            QComboBox::down-arrow {
                image: url(./icones/arrow_down.png);
            }
            """)
        self.sanitize_tweets_input.setGeometry(QRect(168, 227, 300, 48))

        self.sanitize_tweets_output = QLineEdit(self.sanitize_tweets)
        self.sanitize_tweets_output.setObjectName(u"sanitize_tweets_output")
        self.sanitize_tweets_output.setStyleSheet("""
            background-color: #ffffff;
            color: black;
            font-family: 'Montserrat';""")
        self.sanitize_tweets_output.setGeometry(QRect(518, 227, 300, 48))

        self.sanitize_tweets_runButton = QPushButton(self.sanitize_tweets)
        self.sanitize_tweets_runButton.setObjectName(u"sanitize_tweets_runButton")
        self.sanitize_tweets_runButton.setStyleSheet("""
            border-radius: 10px;
            background-color: #8321FF;
            font-weight: 700;
            font-family: 'Montserrat';
            color: white;
            font-size: 24px;""")
        self.sanitize_tweets_runButton.setGeometry(QRect(683, 313, 131, 55))

        self.sanitize_tweets_displayOutput = QTextBrowser(self.sanitize_tweets)
        self.sanitize_tweets_displayOutput.setObjectName(u"sanitize_tweets_displayOutput")
        self.sanitize_tweets_displayOutput.setStyleSheet("""
            background-color: #10121A;
            border-radius: 10px;
            color: white;
            font-family: 'Montserrat'""")
        self.sanitize_tweets_displayOutput.setGeometry(QRect(168, 388, 650, 264))

        self.sanitize_tweets_cleanEmoji = QCheckBox(self.sanitize_tweets)
        self.sanitize_tweets_cleanEmoji.setObjectName(u"sanitize_tweets_cleanEmoji")
        self.sanitize_tweets_cleanEmoji.setStyleSheet(u"""
            QCheckBox {
                color: white;
                font-family: 'Montserrat';
                font-size: 24px;
            }

            QCheckBox::indicator{
                background-color: #ffffff;
                border-style: solid;
                border-color: #ffffff;
                border-radius: 4px;
                width: 20px;
                height: 16px;
            }

            QCheckBox::indicator:checked {
                image: url(./icones/check.png);
            }""")
        self.sanitize_tweets_cleanEmoji.setGeometry(QRect(165, 338, 180, 29))

        self.sanitize_tweets_removeRT = QCheckBox(self.sanitize_tweets)
        self.sanitize_tweets_removeRT.setObjectName(u"sanitize_tweets_removeRT")
        self.sanitize_tweets_removeRT.setStyleSheet(u"""
            QCheckBox {
                color: white;
                font-family: 'Montserrat';
                font-size: 24px;
            }

            QCheckBox::indicator{
                background-color: #ffffff;
                border-style: solid;
                border-color: #ffffff;
                border-radius: 4px;
                width: 20px;
                height: 16px;
            }

            QCheckBox::indicator:checked {
                image: url(./icones/check.png);
            }""")
        self.sanitize_tweets_removeRT.setGeometry(QRect(391, 338, 160, 29))

        self.sanitize_tweets_helpButton = QPushButton(self.sanitize_tweets)
        self.sanitize_tweets_helpButton.setObjectName(u"sanitize_tweets_helpButton")
        self.sanitize_tweets_helpButton.setGeometry(QRect(911, 646, 60, 60))
        self.sanitize_tweets_helpButton.setMask(QRegion(QRect(0,0,58,58), QRegion.Ellipse))
        self.sanitize_tweets_helpButton.setStyleSheet("""
            border-radius: 1px;
            background-color: #8321FF;
            font-weight: 700;
            font-family: 'Montserrat';
            color: white;
            font-size: 24px;
        """)

        self.sanitize_tweets_infoboard = QTextBrowser(self.sanitize_tweets)
        self.sanitize_tweets_infoboard.setObjectName(u"sanitize_tweets_infoboard")
        self.sanitize_tweets_infoboard.setGeometry(QRect(160, 150, 665, 520))
        self.sanitize_tweets_infoboard.setStyleSheet("""
            border-style: solid;
            background-color: #1B2542;
            border-color: #1B2542;
            color: white;
            font-family: 'Montserrat'
        """)

        self.sanitize_tweets_infoboard.setText("""
        This module can remove stopwords, non-twitter symbols, URLs,
        and emoji from JSON datasets.

        Parameters:
            * Input: JSON file to be cleaned. Has to contain a key named text.
            
            * Output: Filename for the resulting output.
            The default is "output_clean" in the input file extension format.
            
            * Clean Emoji: Remove emoji contained in the input file.
            
            * Remove RT: Exclude tweets deemed as retweets from the input file
            (e.g tweets starting with \"RT @\").
        """)

        self.sanitize_tweets_input.addItems(self.showFilesInput())
        self.sanitize_tweets_infoboard.setHidden(True)
        self.sanitize_tweets_helpButton.clicked.connect(lambda: self.sanitize_tweets_infoboard.setHidden(not self.sanitize_tweets_infoboard.isHidden()))

        StackedWidget.addWidget(self.sanitize_tweets)

        ###############################################################
        ##                                                           ##
        ##  GATHER PROFILE                                           ##
        ##                                                           ##
        ###############################################################
        self.gather_profile = QWidget()
        self.gather_profile.setObjectName(u"gather_profile")
        self.gather_profile.setStyleSheet("background-color: #1B2542")

        self.gather_profile_title = QLabel(self.gather_profile)
        self.gather_profile_title.setObjectName(u"gather_profile_title")
        self.gather_profile_title.setStyleSheet("""
            color: white;
            font-family: 'Montserrat';
            font-size: 36px;
            font-weight: 700;""")
        self.gather_profile_title.setGeometry(QRect(326, 101, 333, 45))

        self.gather_profile_displayOutput = QTextBrowser(self.gather_profile)
        self.gather_profile_displayOutput.setObjectName(u"gather_profile_displayOutput")
        self.gather_profile_displayOutput.setStyleSheet("""
            background-color: #10121A;
            border-radius: 10px;
            color: white;
            font-family: 'Montserrat'""")
        self.gather_profile_displayOutput.setGeometry(QRect(167, 389, 650, 264))

        self.gather_profile_input = QLineEdit(self.gather_profile)
        self.gather_profile_input.setObjectName(u"gather_profile_input")
        self.gather_profile_input.setStyleSheet("""
            background-color: #ffffff;
            color: black;
            font-family: 'Montserrat';""")
        self.gather_profile_input.setGeometry(QRect(168, 228, 300, 48))

        self.gather_profile_output = QLineEdit(self.gather_profile)
        self.gather_profile_output.setObjectName(u"gather_profile_output")
        self.gather_profile_output.setStyleSheet("""
            background-color: #ffffff;
            color: black;
            font-family: 'Montserrat';""")
        self.gather_profile_output.setGeometry(QRect(518, 228, 300, 48))

        self.gather_profile_input_label = QLabel(self.gather_profile)
        self.gather_profile_input_label.setObjectName(u"gather_profile_input_label")
        self.gather_profile_input_label.setStyleSheet("""
            color: white;
            font-family: 'Montserrat';
            font-size: 24px;""")
        self.gather_profile_input_label.setGeometry(QRect(168, 199, 128, 29))

        self.gather_profile_output_label = QLabel(self.gather_profile)
        self.gather_profile_output_label.setObjectName(u"gather_profile_output_label")
        self.gather_profile_output_label.setStyleSheet("""
            color: white;
            font-family: 'Montserrat';
            font-size: 24px;""")
        self.gather_profile_output_label.setGeometry(QRect(518, 199, 221, 29))

        self.gather_profile_runButton = QPushButton(self.gather_profile)
        self.gather_profile_runButton.setObjectName(u"gather_profile_runButton")
        self.gather_profile_runButton.setStyleSheet("""
            border-radius: 10px;
            background-color: #8321FF;
            color: white;
            font-weight: 700;
            font-size: 24px;""")
        self.gather_profile_runButton.setGeometry(QRect(420, 301, 131, 55))

        self.gather_profile_helpButton = QPushButton(self.gather_profile)
        self.gather_profile_helpButton.setObjectName(u"gather_profile_helpButton")
        self.gather_profile_helpButton.setGeometry(QRect(911, 646, 60, 60))
        self.gather_profile_helpButton.setMask(QRegion(QRect(0,0,58,58), QRegion.Ellipse))
        self.gather_profile_helpButton.setStyleSheet("""
            border-radius: 1px;
            background-color: #8321FF;
            font-weight: 700;
            font-family: 'Montserrat';
            color: white;
            font-size: 24px;
        """)

        self.gather_profile_infoboard = QTextBrowser(self.gather_profile)
        self.gather_profile_infoboard.setObjectName(u"gather_profile_infoboard")
        self.gather_profile_infoboard.setGeometry(QRect(160, 150, 665, 520))
        self.gather_profile_infoboard.setStyleSheet("""
            border-style: solid;
            background-color: #1B2542;
            border-color: #1B2542;
            color: white;
            font-family: 'Montserrat'
        """)

        self.gather_profile_infoboard.setText("""
        Collects tweets from a username (@) in a date range,
        or the maximum limit allowed at the moment.

        * Username: Username to collects.

        * Output: Filename for the resulting output. The default is "output_profile.json"
        """)

        self.gather_profile_infoboard.setHidden(True)
        self.gather_profile_helpButton.clicked.connect(lambda: self.gather_profile_infoboard.setHidden(not self.gather_profile_infoboard.isHidden()))

        StackedWidget.addWidget(self.gather_profile)


        ###############################################################
        ##                                                           ##
        ##  VISUALIZAÇÕES                                            ##
        ##                                                           ##
        ###############################################################
        self.newViz = QWidget()
        self.newViz.setObjectName(u"newViz")
        self.newViz.setStyleSheet("background-color: #1B2542")

        self.newViz_title = QLabel(self.newViz)
        self.newViz_title.setObjectName(u"newViz_title")
        self.newViz_title.setGeometry(QRect(335, 99, 320, 45))
        self.newViz_title.setStyleSheet("""
            color: white;
            font-family: 'Montserrat';
            font-size: 36px;
            font-weight: 700;""")
      
        self.newViz_lineplot_checkbox = QCheckBox(self.newViz)
        self.newViz_lineplot_checkbox.setObjectName(u"newViz_lineplot_checkbox")
        self.newViz_lineplot_checkbox.setGeometry(QRect(160, 177, 120, 29))
        self.newViz_lineplot_checkbox.setStyleSheet(u"""
            QCheckBox {
                color: white;
                font-family: 'Montserrat';
                font-size: 24px;
            }

            QCheckBox::indicator{
                background-color: #ffffff;
                border-style: solid;
                border-color: #ffffff;
                border-radius: 4px;
                width: 20px;
                height: 16px;
            }

            QCheckBox::indicator:checked {
                image: url(./icones/check.png);
            }""")

        self.newViz_heatmap_checkbox = QCheckBox(self.newViz)
        self.newViz_heatmap_checkbox.setObjectName(u"newViz_heatmap_checkbox")
        self.newViz_heatmap_checkbox.setGeometry(QRect(160, 289, 210, 29))
        self.newViz_heatmap_checkbox.setStyleSheet(u"""
            QCheckBox {
                color: white;
                font-family: 'Montserrat';
                font-size: 24px;
            }

            QCheckBox::indicator{
                background-color: #ffffff;
                border-style: solid;
                border-color: #ffffff;
                border-radius: 4px;
                width: 20px;
                height: 16px;
            }

            QCheckBox::indicator:checked {
                image: url(./icones/check.png);
            }""")

        self.newViz_wordcloud_checkbox = QCheckBox(self.newViz)
        self.newViz_wordcloud_checkbox.setObjectName(u"newViz_wordcloud_checkbox")
        self.newViz_wordcloud_checkbox.setGeometry(QRect(557, 177, 160, 29))
        self.newViz_wordcloud_checkbox.setStyleSheet(u"""
            QCheckBox {
                color: white;
                font-family: 'Montserrat';
                font-size: 24px;
            }

            QCheckBox::indicator{
                background-color: #ffffff;
                border-style: solid;
                border-color: #ffffff;
                border-radius: 4px;
                width: 20px;
                height: 16px;
            }

            QCheckBox::indicator:checked {
                image: url(./icones/check.png);
            }""")

        self.newViz_runButton = QPushButton(self.newViz)
        self.newViz_runButton.setObjectName(u"newViz_runButton")
        self.newViz_runButton.setGeometry(QRect(655, 427, 131, 55))
        self.newViz_runButton.setStyleSheet("""
            border-radius: 10px;
            background-color: #8321FF;
            font-weight: 700;
            font-family: 'Montserrat';
            color: white;
            font-size: 24px;""")

        self.newViz_lineplot_input = QComboBox(self.newViz)
        self.newViz_lineplot_input.setObjectName(u"newViz_lineplot_input")
        self.newViz_lineplot_input.setEnabled(True)
        self.newViz_lineplot_input.setGeometry(QRect(160, 208, 268, 48))
        self.newViz_lineplot_input.setStyleSheet(u"""
            QComboBox {
                background-color: #ffffff;
                border-style: solid;
                border-color: #ffffff;
                color: black;
                font-family: 'Montserrat';
            }

            QComboBox QAbstractItemView {
                background-color: white;
                color: black;
                font-family: 'Montserrat';
            }

            QComboBox::drop-down {
                background-color: #10121A;
                width: 24px;
                height: 54px;
            }

            QComboBox::down-arrow {
                image: url(./icones/arrow_down.png);
            }
            """)

        self.newViz_displayDebug = QTextBrowser(self.newViz)
        self.newViz_displayDebug.setObjectName(u"newViz_displayDebug")
        self.newViz_displayDebug.setGeometry(QRect(160, 500, 665, 164))
        self.newViz_displayDebug.setStyleSheet("""
            background-color: #10121A;
            border-radius: 10px;
            color: white;
            font-family: 'Montserrat'""")

        self.newViz_heatmap_input = QComboBox(self.newViz)
        self.newViz_heatmap_input.setObjectName(u"newViz_heatmap_input")
        self.newViz_heatmap_input.setGeometry(QRect(160, 320, 268, 48))
        self.newViz_heatmap_input.setStyleSheet(u"""
            QComboBox {
                background-color: #ffffff;
                border-style: solid;
                border-color: #ffffff;
                color: black;
                font-family: 'Montserrat';
            }

            QComboBox QAbstractItemView {
                background-color: white;
                color: black;
                font-family: 'Montserrat';
            }

            QComboBox::drop-down {
                background-color: #10121A;
                width: 24px;
                height: 54px;
            }

            QComboBox::down-arrow {
                image: url(./icones/arrow_down.png);
            }
            """)

        self.newViz_wordcloud_input = QComboBox(self.newViz)
        self.newViz_wordcloud_input.setObjectName(u"newViz_wordcloud_input")
        self.newViz_wordcloud_input.setGeometry(QRect(557, 208, 268, 48))
        self.newViz_wordcloud_input.setStyleSheet(u"""
            QComboBox {
                background-color: #ffffff;
                border-style: solid;
                border-color: #ffffff;
                color: black;
                font-family: 'Montserrat';
            }

            QComboBox QAbstractItemView {
                background-color: white;
                color: black;
                font-family: 'Montserrat';
            }

            QComboBox::drop-down {
                background-color: #10121A;
                width: 24px;
                height: 54px;
            }

            QComboBox::down-arrow {
                image: url(./icones/arrow_down.png);
            }
            """)

        self.newViz_topretweets_checkbox = QCheckBox(self.newViz)
        self.newViz_topretweets_checkbox.setObjectName(u"newViz_topretweets_checkbox")
        self.newViz_topretweets_checkbox.setGeometry(QRect(160, 399, 230, 29))
        self.newViz_topretweets_checkbox.setStyleSheet(u"""
            QCheckBox {
                color: white;
                font-family: 'Montserrat';
                font-size: 24px;
            }

            QCheckBox::indicator{
                background-color: #ffffff;
                border-style: solid;
                border-color: #ffffff;
                border-radius: 4px;
                width: 20px;
                height: 16px;
            }

            QCheckBox::indicator:checked {
                image: url(./icones/check.png);
            }""")

        self.newViz_topretweets_input = QComboBox(self.newViz)
        self.newViz_topretweets_input.setObjectName(u"newViz_topretweets_input")
        self.newViz_topretweets_input.setGeometry(QRect(160, 427, 268, 48))
        self.newViz_topretweets_input.setStyleSheet(u"""
            QComboBox {
                background-color: #ffffff;
                border-style: solid;
                border-color: #ffffff;
                color: black;
                font-family: 'Montserrat';
            }

            QComboBox QAbstractItemView {
                background-color: white;
                color: black;
                font-family: 'Montserrat';
            }

            QComboBox::drop-down {
                background-color: #10121A;
                width: 24px;
                height: 54px;
            }

            QComboBox::down-arrow {
                image: url(./icones/arrow_down.png);
            }
            """)

        self.newViz_topretweets_limite = QSpinBox(self.newViz)
        self.newViz_topretweets_limite.setObjectName(u"newViz_topretweets_limite")
        self.newViz_topretweets_limite.setStyleSheet(u"""
            QSpinBox{
                background-color: #ffffff;
                border-style: solid;
                border-color: #ffffff;
                border-radius: 10px;
                color: black;
                font-family: 'Montserrat';
                font-size: 24px;
            }

            QSpinBox::up-button{
                background-color: #10121A;
                border-top-right-radius: 8px;
                width: 24px;
                height: 20px;
            }

            QSpinBox::up-arrow{
                image: url(./icones/arrow_up.png);
                width: 10px;
                height: 12px;
            }

            QSpinBox::down-button{
                background-color: #10121A;
                border-bottom-right-radius: 8px;
                width: 24px;
                height: 20px;
            }

            QSpinBox::down-arrow{
                image: url(./icones/arrow_down.png);
                width: 10px;
                height: 12px;
            }""")
        self.newViz_topretweets_limite.setGeometry(QRect(440, 432, 80, 39))
        self.newViz_topretweets_limite.setValue(10)
        self.newViz_topretweets_limite.setMaximum(100000000)

        self.newViz_topretweets_limite_label = QLabel(self.newViz)
        self.newViz_topretweets_limite_label.setObjectName(u"newViz_topretweets_limite_label")
        self.newViz_topretweets_limite_label.setStyleSheet("""
            color: white;
            font-family: 'Montserrat';
            font-size: 24px;""")
        self.newViz_topretweets_limite_label.setGeometry(QRect(440, 400, 150, 29))

        self.newVizheatmapminute_checkbox = QCheckBox(self.newViz)
        self.newVizheatmapminute_checkbox.setObjectName(u"newVizheatmapminute_checkbox")
        self.newVizheatmapminute_checkbox.setGeometry(QRect(557, 289, 245, 29))
        self.newVizheatmapminute_checkbox.setStyleSheet(u"""
            QCheckBox {
                color: white;
                font-family: 'Montserrat';
                font-size: 24px;
            }

            QCheckBox::indicator{
                background-color: #ffffff;
                border-style: solid;
                border-color: #ffffff;
                border-radius: 4px;
                width: 20px;
                height: 16px;
            }

            QCheckBox::indicator:checked {
                image: url(./icones/check.png);
            }""")

        self.newViz_heatmapminute_input = QComboBox(self.newViz)
        self.newViz_heatmapminute_input.setObjectName(u"newViz_heatmapminute_input")
        self.newViz_heatmapminute_input.setGeometry(QRect(557, 320, 268, 48))
        self.newViz_heatmapminute_input.setStyleSheet(u"""
            QComboBox {
                background-color: #ffffff;
                border-style: solid;
                border-color: #ffffff;
                color: black;
                font-family: 'Montserrat';
            }

            QComboBox QAbstractItemView {
                background-color: white;
                color: black;
                font-family: 'Montserrat';
            }

            QComboBox::drop-down {
                background-color: #10121A;
                width: 24px;
                height: 54px;
            }

            QComboBox::down-arrow {
                image: url(./icones/arrow_down.png);
            }
            """)

        self.newViz_helpButton = QPushButton(self.newViz)
        self.newViz_helpButton.setObjectName(u"newViz_helpButton")
        self.newViz_helpButton.setGeometry(QRect(911, 646, 60, 60))
        self.newViz_helpButton.setMask(QRegion(QRect(0,0,58,58), QRegion.Ellipse))
        self.newViz_helpButton.setStyleSheet("""
            border-radius: 1px;
            background-color: #8321FF;
            font-weight: 700;
            font-family: 'Montserrat';
            color: white;
            font-size: 24px;
        """)

        self.newViz_infoboard = QTextBrowser(self.newViz)
        self.newViz_infoboard.setObjectName(u"newViz_infoboard")
        self.newViz_infoboard.setGeometry(QRect(160, 150, 665, 520))
        self.newViz_infoboard.setStyleSheet("""
            border-style: solid;
            background-color: #1B2542;
            border-color: #1B2542;
            color: white;
            font-family: 'Montserrat'
        """)

        self.newViz_infoboard.setText("""
        In this module is possible make visualizations to show in "Dashboard" module.
        Select desired visualizations just clicking in checkox and select file to create
        the graphic.
        """)
        self.newViz_infoboard.setHidden(True)
        self.newViz_helpButton.clicked.connect(lambda: self.newViz_infoboard.setHidden(not self.newViz_infoboard.isHidden()))

        self.newViz_lineplot_input.clear()
        self.newViz_lineplot_input.addItems(self.showFilesInput())
        self.newViz_heatmap_input.addItems(self.showFilesInput())
        self.newViz_wordcloud_input.addItems(self.showFilesInput(True))
        self.newViz_topretweets_input.addItems(self.showFilesInput())
        self.newViz_heatmapminute_input.addItems(self.showFilesInput())
        StackedWidget.addWidget(self.newViz)

        ###############################################################
        ##                                                           ##
        ##  DASHBOARD                                                ##
        ##                                                           ##
        ###############################################################
        self.dashboard = QWidget()
        self.dashboard.setObjectName(u"dashboard")
        self.view = QWebEngineView(self.dashboard)
        self.view.load(QUrl.fromLocalFile(MainWindow.getPath(self, "root")+os.sep+"teste_viz.html"))
        self.view.resize(1045, 720)
        self.view.show()
        self.dashboard_refreshButton = QPushButton(self.dashboard)
        self.dashboard_refreshButton.setObjectName(
            u"dashboard_refreshButton")
        self.dashboard_refreshButton.setStyleSheet(
            "border-radius: 5px; background-color: #F18303; color: white;")
        self.dashboard_refreshButton.setGeometry(QRect(0, 0, 60, 20))
        StackedWidget.addWidget(self.dashboard)

        self.retranslateUi(StackedWidget)
        QMetaObject.connectSlotsByName(StackedWidget)

    def retranslateUi(self, StackedWidget):
        StackedWidget.setWindowTitle(QCoreApplication.translate(
            "StackedWidget", u"StackedWidget", None))
        self.quick_report_runButton.setText(
            QCoreApplication.translate("StackedWidget", u"RUN", None))
        self.quick_report_label_input.setText(
            QCoreApplication.translate("StackedWidget", u"Input", None))
        self.quick_report_label_output.setText(
            QCoreApplication.translate("StackedWidget", u"Output (optional)", None))
        self.quick_report_title.setText(QCoreApplication.translate(
            "StackedWidget", u"QUICK REPORT", None))
        self.quick_report_display_count_label.setText(
            QCoreApplication.translate("StackedWidget", u"Display Counts", None))
        self.sentiment_analysis_runButton.setText(
            QCoreApplication.translate("StackedWidget", u"RUN", None))
        self.sentiment_analysis_label_input.setText(
            QCoreApplication.translate("StackedWidget", u"Input", None))
        self.sentiment_analysis_label_output.setText(
            QCoreApplication.translate("StackedWidget", u"Output", None))
        self.sentiment_analysis_title.setText(QCoreApplication.translate(
            "StackedWidget", u"SENTIMENT ANALYSIS", None))
        self.sanitize_tweets_title.setText(QCoreApplication.translate(
            "StackedWidget", u"SANITIZE TWEETS", None))
        self.sanitize_tweets_input_label.setText(
            QCoreApplication.translate("StackedWidget", u"Input", None))
        self.sanitize_tweets_output_label.setText(
            QCoreApplication.translate("StackedWidget", u"Output (optional)", None))
        self.sanitize_tweets_runButton.setText(
            QCoreApplication.translate("StackedWidget", u"RUN", None))
        self.sanitize_tweets_cleanEmoji.setText(
            QCoreApplication.translate("StackedWidget", u"Clean Emoji", None))
        self.sanitize_tweets_removeRT.setText(
            QCoreApplication.translate("StackedWidget", u"Remove RT", None))
        self.gather_profile_title.setText(QCoreApplication.translate(
            "StackedWidget", u"GATHER PROFILE", None))
        self.gather_profile_input_label.setText(
            QCoreApplication.translate("StackedWidget", u"Username", None))
        self.gather_profile_output_label.setText(
            QCoreApplication.translate("StackedWidget", u"Output (optional)", None))
        self.gather_profile_runButton.setText(
            QCoreApplication.translate("StackedWidget", u"RUN", None))
        self.rest_gathering_title.setText(QCoreApplication.translate(
            "StackedWidget", u"REST GATHERING", None))
        self.rest_gathering_label_input.setText(
            QCoreApplication.translate("StackedWidget", u"Query", None))
        self.rest_gathering_dateInicio_label.setText(
            QCoreApplication.translate("StackedWidget", u"Start Time", None))
        self.rest_gathering_dateFim_label.setText(
            QCoreApplication.translate("StackedWidget", u"End Time", None))
        self.rest_gathering_lingua_label.setText(
            QCoreApplication.translate("StackedWidget", u"Language", None))
        self.rest_gathering_limite_label.setText(
            QCoreApplication.translate("StackedWidget", u"Limit", None))
        self.rest_gathering_output_label.setText(
            QCoreApplication.translate("StackedWidget", u"Output (optional)", None))
        self.rest_gathering_runButton.setText(
            QCoreApplication.translate("StackedWidget", u"RUN", None))
        self.rest_gathering_checkbox_limite.setText("")
        self.home_title.setText(QCoreApplication.translate(
            "StackedWidget", u"Tweet Utils UI", None))
        self.home_title2.setText(QCoreApplication.translate(
            "StackedWidget", u"Utils", None))
        self.home_saveButton.setText(
            QCoreApplication.translate("StackedWidget", u"SAVE", None))
        self.home_label_key.setText(QCoreApplication.translate(
            "StackedWidget", u"Bearer Token Key", None))
        self.newViz_title.setText(QCoreApplication.translate(
            "StackedWidget", u"VISUALIZATIONS", None))
        self.newViz_lineplot_checkbox.setText(
            QCoreApplication.translate("StackedWidget", u"Lineplot", None))
        self.newViz_heatmap_checkbox.setText(
            QCoreApplication.translate("StackedWidget", u"Heatmap Hour", None))
        self.newViz_wordcloud_checkbox.setText(
            QCoreApplication.translate("StackedWidget", u"Wordcloud", None))
        self.newViz_topretweets_limite_label.setText(
            QCoreApplication.translate("StackedWidget", u"N", None))
        self.newViz_runButton.setText(QCoreApplication.translate(
            "StackedWidget", u"RUN", None))
        self.newViz_topretweets_checkbox.setText(
            QCoreApplication.translate("StackedWidget", u"Top N Retweets", None))
        self.newVizheatmapminute_checkbox.setText(
            QCoreApplication.translate("StackedWidget", u"Heatmap Minutes", None))
        self.dashboard_refreshButton.setText(
            QCoreApplication.translate("StackedWidget", u"Refresh", None))
        self.newViz_helpButton.setText(QCoreApplication.translate("StackedWidget", u"?", None))
        self.gather_profile_helpButton.setText(QCoreApplication.translate("StackedWidget", u"?", None))
        self.sanitize_tweets_helpButton.setText(QCoreApplication.translate("StackedWidget", u"?", None))
        self.rest_gathering_helpButton.setText(QCoreApplication.translate("StackedWidget", u"?", None))
        self.quick_report_helpButton.setText(QCoreApplication.translate("StackedWidget", u"?", None))
        self.sentiment_analysis_helpButton.setText(QCoreApplication.translate("StackedWidget", u"?", None))
        self.home_helpButton.setText(QCoreApplication.translate("StackedWidget", u"?", None))
    # retranslateUi
