# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import os

try:
    from ..utils.icon_loader import load_qicon, load_qpixmap, _resolve_icon
except (ImportError, ValueError):
    import sys
    _parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if _parent not in sys.path:
        sys.path.insert(0, _parent)
    from utils.icon_loader import load_qicon, load_qpixmap, _resolve_icon

placeholder = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'icons', 'placeholder.svg'))

class Ui_Widget(object):
    def setupUi(self, Widget, icon_dirs=None, theme: str = 'default.qss'):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(455, 200)
        Widget.setMinimumSize(QSize(455, 200))
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(Widget)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 435, 107))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.LABELUri = QLabel(self.scrollAreaWidgetContents)
        self.LABELUri.setObjectName(u"LABELUri")

        self.horizontalLayout_4.addWidget(self.LABELUri)

        self.EDITUri = QLineEdit(self.scrollAreaWidgetContents)
        self.EDITUri.setObjectName(u"EDITUri")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.EDITUri.sizePolicy().hasHeightForWidth())
        self.EDITUri.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.EDITUri)

        """
        self.BTNUri = QPushButton(self.scrollAreaWidgetContents)
        self.BTNUri.setObjectName(u"BTNUri")
        icon = QIcon()
        icon_path = _resolve_icon(icon_dirs, os.path.join('emulator', 'default.svg'), theme=theme)
        icon.addFile(icon_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BTNUri.setIcon(icon)
        self.BTNUri.setCursor(QCursor(Qt.CursorShape.PointingHandCursor)) 

        self.horizontalLayout_4.addWidget(self.BTNUri)
        """


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.LABELDir = QLabel(self.scrollAreaWidgetContents)
        self.LABELDir.setObjectName(u"LABELDir")

        self.horizontalLayout_5.addWidget(self.LABELDir)

        self.EDITDir = QLineEdit(self.scrollAreaWidgetContents)
        self.EDITDir.setObjectName(u"EDITDir")
        sizePolicy1.setHeightForWidth(self.EDITDir.sizePolicy().hasHeightForWidth())
        self.EDITDir.setSizePolicy(sizePolicy1)


        self.horizontalLayout_5.addWidget(self.EDITDir)

        self.BTNDir = QPushButton(self.scrollAreaWidgetContents)
        self.BTNDir.setObjectName(u"BTNDir")
        
        icon1 = QIcon()
        icon1_path = _resolve_icon(icon_dirs, os.path.join('folder', 'default.svg'), theme=theme)
        icon1.addFile(icon1_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        
        self.BTNDir.setIcon(icon1)
        self.BTNDir.setCursor(QCursor(Qt.CursorShape.PointingHandCursor)) 

        self.horizontalLayout_5.addWidget(self.BTNDir)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.LABELName = QLabel(self.scrollAreaWidgetContents)
        self.LABELName.setObjectName(u"LABELName")

        self.horizontalLayout_6.addWidget(self.LABELName)

        self.EDITName = QLineEdit(self.scrollAreaWidgetContents)
        self.EDITName.setObjectName(u"EDITName")
        sizePolicy1.setHeightForWidth(self.EDITName.sizePolicy().hasHeightForWidth())
        self.EDITName.setSizePolicy(sizePolicy1)

        self.horizontalLayout_6.addWidget(self.EDITName)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.BTNClone = QPushButton(Widget)
        self.BTNClone.setObjectName(u"BTNClone")
        self.BTNClone.setCursor(QCursor(Qt.CursorShape.PointingHandCursor)) 

        self.horizontalLayout.addWidget(self.BTNClone)

        self.BTNCancell = QPushButton(Widget)
        self.BTNCancell.setObjectName(u"BTNCancell")
        self.BTNCancell.setCursor(QCursor(Qt.CursorShape.PointingHandCursor)) 

        self.horizontalLayout.addWidget(self.BTNCancell)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"RQTLL IDE / Clonar repositorio", None))
        self.LABELUri.setText(QCoreApplication.translate("Widget", u"URL:", None))
        self.EDITUri.setPlaceholderText(QCoreApplication.translate("Widget", u"https://", None))
        self.LABELDir.setText(QCoreApplication.translate("Widget", u"Destino:", None))
        self.EDITDir.setPlaceholderText(QCoreApplication.translate("Widget", u"~/ros2_ws", None))
        self.LABELName.setText(QCoreApplication.translate("Widget", u"Nombre: ", None))
        self.EDITName.setPlaceholderText(QCoreApplication.translate("Widget", u"cloned_ws", None))
        self.BTNClone.setText(QCoreApplication.translate("Widget", u"Clonar", None))
        self.BTNCancell.setText(QCoreApplication.translate("Widget", u"Cancelar", None))
    # retranslateUi

