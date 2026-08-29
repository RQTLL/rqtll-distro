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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

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
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(630, 393)
        Widget.setMinimumSize(QSize(630, 393))
        Widget.setMaximumSize(QSize(630, 393))

        icon = QIcon()
        icon_path = _resolve_icon(icon_dirs, os.path.join('logo.svg'))
        icon.addFile(icon_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Widget.setWindowIcon(icon)

        self.verticalLayout_2 = QVBoxLayout(Widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.LABELTitle = QLabel(Widget)
        self.LABELTitle.setObjectName(u"LABELTitle")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.LABELTitle.setFont(font)

        self.verticalLayout_2.addWidget(self.LABELTitle)

        self.CBInstallRos = QCheckBox(Widget)
        self.CBInstallRos.setObjectName(u"CBInstallRos")

        self.verticalLayout_2.addWidget(self.CBInstallRos)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

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
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"RQTLL IDE / Opciones de Instalación", None))
        self.LABELTitle.setText(QCoreApplication.translate("Widget", u"Reinstalación", None))
        self.CBInstallRos.setText(QCoreApplication.translate("Widget", u"Deseo instalar o reconfigurar ROS2 en mi sistema.", None))
        self.BTNBack.setText(QCoreApplication.translate("Widget", u"Regresar", None))
        self.BTNNext.setText(QCoreApplication.translate("Widget", u"Siguiente", None))
        self.BTNCancel.setText(QCoreApplication.translate("Widget", u"Cancelar", None))
    # retranslateUi

