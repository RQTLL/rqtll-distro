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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import os

try:
    from ..utils.icon_loader import _resolve_icon
    from ..utils.frame_button import FrameButtonWidget
except (ImportError, ValueError):
    import sys
    _parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if _parent not in sys.path:
        sys.path.insert(0, _parent)
    from utils.icon_loader import _resolve_icon
    from utils.frame_button import FrameButtonWidget


class Ui_Widget(object):
    def setupUi(self, Widget, icon_dirs=None, theme='default.qss'):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1209, 677)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        Widget.resize(880, 550)
        Widget.setMinimumSize(QSize(880, 550))
        Widget.setMaximumSize(QSize(880, 550))
        icon = QIcon()
        icon_path = _resolve_icon(icon_dirs, os.path.join('logo.svg'))
        icon.addFile(icon_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Widget.setWindowIcon(icon)
        self.horizontalLayout = QHBoxLayout(Widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.NAVHome = QPushButton(Widget)
        self.NAVHome.setObjectName(u"NAVHome")
        self.NAVHome.setEnabled(False)

        self.verticalLayout.addWidget(self.NAVHome)

        self.NAVInstall = QPushButton(Widget)
        self.NAVInstall.setObjectName(u"NAVInstall")
        self.NAVInstall.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.NAVInstall)

        self.NAVDocs = QPushButton(Widget)
        self.NAVDocs.setObjectName(u"NAVDocs")
        self.NAVDocs.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.NAVDocs)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.LABELTitleWelcome = QLabel(Widget)
        self.LABELTitleWelcome.setObjectName(u"LABELTitleWelcome")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.LABELTitleWelcome.sizePolicy().hasHeightForWidth())
        self.LABELTitleWelcome.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(64)
        self.LABELTitleWelcome.setFont(font)
        self.LABELTitleWelcome.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.LABELTitleWelcome.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.LABELTitleWelcome)

        self.LABELInfoWelcome = QLabel(Widget)
        self.LABELInfoWelcome.setObjectName(u"LABELInfoWelcome")
        sizePolicy1.setHeightForWidth(self.LABELInfoWelcome.sizePolicy().hasHeightForWidth())
        self.LABELInfoWelcome.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setItalic(True)
        self.LABELInfoWelcome.setFont(font1)
        self.LABELInfoWelcome.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.LABELInfoWelcome.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.LABELInfoWelcome)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        # instantiate reusable FrameButtonWidget

        self.FRAMENew = FrameButtonWidget(
            icon_path=_resolve_icon(icon_dirs, os.path.join('new', 'default.svg')), 
            title="", info="", parent=Widget, theme=theme)
        self.FRAMENew.setObjectName(u"FRAMENew")
        # provide compatibility attributes used elsewhere
        self.ICONNew = self.FRAMENew.icon
        self.LABELTitleNew = self.FRAMENew.title
        self.LABELInfoNew = self.FRAMENew.info
        self.horizontalLayout_2.addWidget(self.FRAMENew)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        # FRAMEOpen -> FrameButtonWidget

        self.FRAMEOpen = FrameButtonWidget(
            icon_path=_resolve_icon(icon_dirs, os.path.join('load', 'default.svg')), 
            title="", info="", parent=Widget, theme=theme)
        self.FRAMEOpen.setObjectName(u"FRAMEOpen")
        self.ICONOpen = self.FRAMEOpen.icon
        self.LABELTitleOpen = self.FRAMEOpen.title
        self.LABELInfoOpen = self.FRAMEOpen.info
        self.horizontalLayout_2.addWidget(self.FRAMEOpen)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        # FRAMEClone -> FrameButtonWidget

        self.FRAMEClone = FrameButtonWidget(
            icon_path=_resolve_icon(icon_dirs, os.path.join('arrows', 'down.svg')), 
            title="", info="", parent=Widget, theme=theme)
        self.FRAMEClone.setObjectName(u"FRAMEClone")
        self.ICONClone = self.FRAMEClone.icon
        self.LABELTitleClone = self.FRAMEClone.title
        self.LABELInfoClone = self.FRAMEClone.info
        self.horizontalLayout_2.addWidget(self.FRAMEClone)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"RQTLL IDE", None))
        self.NAVHome.setText(QCoreApplication.translate("Widget", u"Proyectos", None))
        self.NAVInstall.setText(QCoreApplication.translate("Widget", u"Dependencias", None))
        self.NAVDocs.setText(QCoreApplication.translate("Widget", u"Documentaci\u00f3n", None))
        self.LABELTitleWelcome.setText(QCoreApplication.translate("Widget", u"Bienvenido a RQTLL IDE", None))
        self.LABELInfoWelcome.setText(QCoreApplication.translate("Widget", u"Crea un nuevo espacio de trabajo para iniciar desde cero.\n"
"O carga un espacio de trabajo existente en el almacenamiento local", None))
        self.ICONNew.setText("")
        self.LABELTitleNew.setText(QCoreApplication.translate("Widget", u"Nuevo", None))
        self.LABELInfoNew.setText(QCoreApplication.translate("Widget", u"espacio de trabajo", None))
        self.ICONOpen.setText("")
        self.LABELTitleOpen.setText(QCoreApplication.translate("Widget", u"Cargar", None))
        self.LABELInfoOpen.setText(QCoreApplication.translate("Widget", u"espacio de trabajao", None))
        self.ICONClone.setText("")
        self.LABELTitleClone.setText(QCoreApplication.translate("Widget", u"Clonar", None))
        self.LABELInfoClone.setText(QCoreApplication.translate("Widget", u"espacio de trabajo", None))
    # retranslateUi

