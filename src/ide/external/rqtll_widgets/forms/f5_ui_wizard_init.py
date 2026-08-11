# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

import os
try:
    from ..utils.icon_loader import load_qicon, load_qpixmap, _resolve_icon
except (ImportError, ValueError):
    import sys
    _parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if _parent not in sys.path:
        sys.path.insert(0, _parent)
    from utils.icon_loader import load_qicon, load_qpixmap, _resolve_icon

class Ui_Widget(object):
    def setupUi(self, Widget, icon_dirs=None, theme: str = "default.qss"):
        self.icon_dirs = icon_dirs
        self.theme = theme
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(630, 393)
        Widget.setMinimumSize(QSize(630, 393))
        Widget.setMaximumSize(QSize(630, 393))
        
        icon = QIcon()
        icon_path = _resolve_icon(self.icon_dirs, os.path.join('logo.svg'))
        icon.addFile(icon_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Widget.setWindowIcon(icon)

        self.verticalLayout_2 = QVBoxLayout(Widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.LABELLogo = QLabel(Widget)
        self.LABELLogo.setObjectName(u"LABELLogo")
        self.LABELLogo.setProperty('role', 'color')
        icon = QIcon()
        logo_path = _resolve_icon(self.icon_dirs, os.path.join("symbolic-color.svg"))
        icon.addFile(logo_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.LABELLogo.setPixmap(icon.pixmap(QSize(256, 256)))
        self.LABELLogo.setFixedSize(QSize(256, 256))
        self.LABELLogo.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.LABELLogo)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.LABELTitle = QLabel(Widget)
        self.LABELTitle.setObjectName(u"LABELTitle")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.LABELTitle.setFont(font)

        self.verticalLayout.addWidget(self.LABELTitle)

        self.LABELText = QLabel(Widget)
        self.LABELText.setObjectName(u"LABELText")
        self.LABELText.setWordWrap(True)

        self.verticalLayout.addWidget(self.LABELText)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.BTNBack = QPushButton(Widget)
        self.BTNBack.setObjectName(u"BTNBack")
        self.BTNBack.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.BTNBack)

        self.BTNNext = QPushButton(Widget)
        self.BTNNext.setObjectName(u"BTNNext")
        self.BTNNext.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.BTNNext)

        self.BTNCancel = QPushButton(Widget)
        self.BTNCancel.setObjectName(u"BTNCancel")
        self.BTNCancel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.BTNCancel)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"RQTLL IDE / Inicializar Instalador", None))
        self.LABELLogo.setText("")
        self.LABELTitle.setText(QCoreApplication.translate("Widget", u"Bienvenido a RQTLL", None))
        self.LABELText.setText(QCoreApplication.translate("Widget", u"Este asistente de configuración lo ayudará a configurar ROS2 en su sistema.", None))
        self.BTNBack.setText(QCoreApplication.translate("Widget", u"Regresar", None))
        self.BTNNext.setText(QCoreApplication.translate("Widget", u"Siguiente", None))
        self.BTNCancel.setText(QCoreApplication.translate("Widget", u"Cancelar", None))
    # retranslateUi

