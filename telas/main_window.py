from PySide6.QtCore import QRect, Qt
from PySide6.QtWidgets import *

from py_push_button import PyPushButton
from telas.main_window import *
from telas.telas_swap import Ui_StackedWidget


class UI_MainWindow(object):
    def init_window(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")

        parent.resize(1280, 720)
        parent.setMinimumSize(1280, 720)
        parent.setMaximumSize(1920, 1080)

        # /////////////////////////
        # background
        self.background = QFrame()

        parent.setCentralWidget(self.background)

        # /////////////////////////////////////////////
        # layout principal com sua respectiva tela
        self.main_layout = QHBoxLayout(self.background)
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.setSpacing(0)

        self.main_screen = QFrame()
        self.main_screen.setStyleSheet("background-color: #B93E3E")

        # ///////
        # teste
        self.pages = QStackedWidget()
        self.pages.setStyleSheet("font-size: 12pt; color: #0000ff;")
        self.ui_pages = Ui_StackedWidget()
        self.ui_pages.setupUi(self.pages)
        self.pages.setCurrentWidget(self.ui_pages.home)

        # ////////////////////////
        # barra lateral esquerda
        self.access_bar = QFrame()
        self.access_bar.setStyleSheet("background-color: #0C0C0C")
        self.access_bar.setMaximumWidth(295)
        self.access_bar.setMinimumWidth(295)

        # ///////////////////////////////////////////////////
        # layout barra lateral esquerda
        self.access_bar_layout = QVBoxLayout(self.access_bar)
        self.access_bar_layout.setContentsMargins(0,0,0,0)
        self.access_bar_layout.setSpacing(0)

        #//////////////////////////////////////////////////////////////////////////////
        # espaçador para deixar todos os botoes juntos
        self.espacador = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        #//////////////////////////////////////////////////////////////////////////////
        # titulo da barra lateral
        self.titulo_lateral = QLabel()
        self.titulo_lateral.setMaximumSize(295, 200)
        self.titulo_lateral.setMinimumSize(295, 200)
        self.titulo_lateral.setAlignment(Qt.AlignCenter)
        self.titulo_lateral.setText("Tweet Utils UI")
        self.titulo_lateral.setStyleSheet("color: white; font-family: 'Montserrat'; font-style: normal; font-weight: 700; font-size: 32px; line-height: 39px;")

        self.titulo_lateral2 = QLabel(self.titulo_lateral)
        self.titulo_lateral2.setText("Utils")
        self.titulo_lateral2.setGeometry(QRect(145, 80, 85, 39))
        self.titulo_lateral2.setStyleSheet("color: #7C21F0; font-family: 'Montserrat'; font-style: normal; font-weight: 700; font-size: 32px; line-height: 39px;")

        #///////////////////////////////////
        # criação de botoes
        self.botao_home = PyPushButton(text="Menu", text_color="#ffffff", btn_pressed="#0C0C0C", btn_color="#0C0C0C", )
        self.botaoMenu_Rest_gathering = PyPushButton(text="Rest Gathering", text_color="#ffffff", btn_pressed="#0C0C0C", btn_color="#0C0C0C")
        self.botaoMenu_Gather_profile = PyPushButton(text="Gather Profile", text_color="#ffffff", btn_pressed="#0C0C0C", btn_color="#0C0C0C")
        self.botaoMenu_Sanitize_tweets = PyPushButton(text="Sanitize Tweets", text_color="#ffffff", btn_pressed="#0C0C0C", btn_color="#0C0C0C")
        self.botaoMenu_Quick_report = PyPushButton(text="Quick Report", text_color="#ffffff", btn_pressed="#0C0C0C", btn_color="#0C0C0C")
        self.botaoMenu_Sentiment_Analysis = PyPushButton(text="Sentiments", text_color="#ffffff", btn_pressed="#0C0C0C", btn_color="#0C0C0C")
        self.botaoMenu_newVisualizacao = PyPushButton(text="Visualizations", text_color="#ffffff", btn_pressed="#0C0C0C", btn_color="#0C0C0C")
        self.botaoMenu_dashboard = PyPushButton(text="Dashboard", text_color="#ffffff", btn_pressed="#0C0C0C", btn_color="#0C0C0C")

        #////////////////////////////////////////////
        # inserção dos elementos no layout da barra lateral
        self.access_bar_layout.addWidget(self.titulo_lateral)
        #self.access_bar_layout.addItem(self.espacador)
        self.access_bar_layout.addWidget(self.botao_home)
        self.access_bar_layout.addWidget(self.botaoMenu_Rest_gathering)
        self.access_bar_layout.addWidget(self.botaoMenu_Gather_profile)
        self.access_bar_layout.addWidget(self.botaoMenu_Sanitize_tweets)
        self.access_bar_layout.addWidget(self.botaoMenu_Quick_report)
        self.access_bar_layout.addWidget(self.botaoMenu_Sentiment_Analysis)
        self.access_bar_layout.addWidget(self.botaoMenu_newVisualizacao)
        self.access_bar_layout.addWidget(self.botaoMenu_dashboard)

        self.access_bar_layout.addItem(self.espacador)
        self.main_layout.addWidget(self.access_bar)
        self.main_layout.addWidget(self.pages)
