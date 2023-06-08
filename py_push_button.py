from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *


class PyPushButton(QPushButton):
    def __init__(
            self,
            text="",
            height=50,
            minimum_width=50,
            text_padding=55,
            text_font="Montserrat",
            text_color="#c3ccdf",
            btn_color="#44475a",
            btn_hover="#4f5368",
            btn_pressed="#282a36",
            is_active=False
    ):
        super().__init__()

        # Set default parametros
        self.setText(text)
        self.setMaximumHeight(height)
        self.setMinimumHeight(height)
        self.setCursor(Qt.PointingHandCursor)

        # Custom parameters
        self.minimum_width = minimum_width
        self.text_padding = text_padding
        self.text_color = text_color
        self.text_font = text_font
        self.btn_color = btn_color
        self.btn_hover = btn_hover
        self.btn_pressed = btn_pressed
        self.is_active = is_active

        # Set style
        self.set_style(
            text_padding=self.text_padding,
            text_color=self.text_color,
            text_font=self.text_font,
            btn_color=self.btn_color,
            btn_hover=self.btn_hover,
            btn_pressed=self.btn_pressed,
            is_active=self.is_active
        )

    def set_active(self, is_active_menu):
        self.set_style(
            text_padding=self.text_padding,
            text_color=self.text_color,
            text_font=self.text_font,
            btn_color=self.btn_color,
            btn_hover=self.btn_hover,
            btn_pressed=self.btn_pressed,
            is_active=is_active_menu
        )

    def set_style(
            self,
            text_padding=55,
            text_font="Montserrat",
            text_color="#c3ccdf",
            btn_color="#44475a",
            btn_hover="#4f5368",
            btn_pressed="#282a36",
            is_active=False
    ):
        style = f"""
        QPushButton {{
            font-family: {text_font};
            font-size: 24px;
            color: {text_color};
            background-color: {btn_color};
            padding-left: {text_padding}px;
            text-align: left;
            border: none;
        }}
        QPushButton:hover {{
            background-color: {btn_hover};
        }}
        QPushButton:pressed {{
            background-color: {btn_pressed};
        }}
        """

        active_style = f"""
        QPushButton {{
            border-left: 10px solid #7C21F0;
        }}
        """
        if not is_active:
            self.setStyleSheet(style)
        else:
            self.setStyleSheet(style + active_style)
