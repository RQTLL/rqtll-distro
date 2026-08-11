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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import os

try:
    from ..utils.icon_loader import load_qicon, load_qpixmap, _resolve_icon
    from ..utils.nav import NavButton
    from ..utils import scaled_icon_label
except (ImportError, ValueError):
    import sys
    _parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if _parent not in sys.path:
        sys.path.insert(0, _parent)
    from utils.icon_loader import load_qicon, load_qpixmap, _resolve_icon
    from utils.nav import NavButton
    from utils import scaled_icon_label

placeholder = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'icons', 'placeholder.svg'))

class Nav(QWidget):
    def __init__(self, Parent, icon_dirs, theme):
        super().__init__(Parent)
        self.icon_dirs = icon_dirs
        self.theme = theme
        self.layout = QVBoxLayout()
        self.layout.setObjectName(u"Nav")
        
        self.code = NavButton(label="", target="code", parent=self)
        self.add(self.code, icon="code")

        self.launch = NavButton(label="", target="launch", parent=self)
        self.add(self.launch, icon="launch")

        self.graph = NavButton(label="", target="nodes", parent=self)
        self.add(self.graph, icon="nodes")

        self.teleop = NavButton(label="", target="teleop", parent=self)
        self.add(self.teleop, icon="teleop")

        self.ssh = NavButton(label="", target="ssh", parent=self)
        self.add(self.ssh, icon="ssh")

        self.spacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.layout.addItem(self.spacer)

        self.viz = NavButton(label="", target="3d", parent=self)
        self.add(self.viz, icon="3d")

        self.sim = NavButton(label="", target="emulator", parent=self)
        self.add(self.sim, icon="emulator")

        self.widgets = NavButton(label="", target="widgets", parent=self)
        self.add(self.widgets, icon="widgets")

        self.packages = NavButton(label="", target="package", parent=self)
        self.add(self.packages, icon="package")

    def add(self, item, icon="close"):
        self.sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.sizePolicy.setHorizontalStretch(0)
        self.sizePolicy.setVerticalStretch(0)
        self.sizePolicy.setHeightForWidth(self.sizePolicy.hasHeightForWidth())
        item.setSizePolicy(self.sizePolicy)
        i = QIcon()
        icon_path = _resolve_icon(self.icon_dirs, os.path.join('icons', icon, 'default.svg'), theme=self.theme)
        i.addFile(icon_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        item.setIcon(i)
        self.layout.addWidget(item)

class Ui_Widget(object):
    def setupUi(self, Widget, icon_dirs=None, theme='default.qss'):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1250, 644)
        Widget.setMinimumSize(QSize(1250, 644))
        icon = QIcon()
        icon_path = _resolve_icon(icon_dirs, os.path.join('logo.svg'))
        icon.addFile(icon_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Widget.setWindowIcon(icon)
        self.horizontalLayout = QHBoxLayout(Widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.nav = Nav(Widget, icon_dirs, theme)
        self.nav.setObjectName(u"nav")
        self.horizontalLayout.addLayout(self.nav.layout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(Widget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.FRAMEImage = QFrame(self.frame)
        self.FRAMEImage.setObjectName(u"FRAMEImage")
        sizePolicy.setHeightForWidth(self.FRAMEImage.sizePolicy().hasHeightForWidth())
        self.FRAMEImage.setSizePolicy(sizePolicy)
        self.FRAMEImage.setFrameShape(QFrame.Shape.StyledPanel)
        self.FRAMEImage.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_3.addWidget(self.FRAMEImage)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.LABELInfo_3 = QLabel(self.frame)
        self.LABELInfo_3.setObjectName(u"LABELInfo_3")

        self.horizontalLayout_5.addWidget(self.LABELInfo_3)

        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_5.addWidget(self.lineEdit_2)

        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.BTNEdit = QPushButton(self.frame)
        self.BTNEdit.setObjectName(u"BTNEdit")
        self.BTNEdit.setCursor(Qt.CursorShape.PointingHandCursor)
        self.BTNEdit.setFixedSize(QSize(200, 32))

        self.horizontalLayout_2.addWidget(self.BTNEdit)

        self.LABELInfo = QLabel(self.frame)
        self.LABELInfo.setObjectName(u"LABELInfo")

        self.horizontalLayout_2.addWidget(self.LABELInfo)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.LABELInfo2 = QLabel(self.frame)
        self.LABELInfo2.setObjectName(u"LABELInfo2")

        self.horizontalLayout_2.addWidget(self.LABELInfo2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setProperty('role', 'control')
        self.horizontalLayout_6.setProperty('variant', 'default')
        self.horizontalLayout_6.setProperty('state', 'normal')
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.BTNFN2 = QPushButton(self.frame)
        self.BTNFN2.setObjectName(u"BTNFN2")
        self.BTNFN2.setFixedSize(QSize(32, 32))
        self.BTNFN2.setCursor(Qt.CursorShape.PointingHandCursor)
        self.BTNFN2.setFont(QFont("Nunito Sans", 8))

        self.gridLayout.addWidget(self.BTNFN2, 2, 0, 1, 1)

        self.BTNFN3 = QPushButton(self.frame)
        self.BTNFN3.setObjectName(u"BTNFN3")
        self.BTNFN3.setFixedSize(QSize(32, 32))
        self.BTNFN3.setCursor(Qt.CursorShape.PointingHandCursor)
        self.BTNFN3.setFont(QFont("Nunito Sans", 8))

        self.gridLayout.addWidget(self.BTNFN3, 3, 1, 1, 1)

        self.BTNFN4 = QPushButton(self.frame)
        self.BTNFN4.setObjectName(u"BTNFN4")
        self.BTNFN4.setFixedSize(QSize(32, 32))
        self.BTNFN4.setCursor(Qt.CursorShape.PointingHandCursor)
        self.BTNFN4.setFont(QFont("Nunito Sans", 8))

        self.gridLayout.addWidget(self.BTNFN4, 2, 2, 1, 1)

        self.BTNFN1 = QPushButton(self.frame)
        self.BTNFN1.setObjectName(u"BTNFN1")
        self.BTNFN1.setFixedSize(QSize(32, 32))
        self.BTNFN1.setCursor(Qt.CursorShape.PointingHandCursor)
        self.BTNFN1.setFont(QFont("Nunito Sans", 8))

        self.gridLayout.addWidget(self.BTNFN1, 0, 1, 1, 1)

        self.BTNFN6 = QPushButton(self.frame)
        self.BTNFN6.setObjectName(u"BTNFN6")
        self.BTNFN6.setFixedSize(QSize(32, 32))
        self.BTNFN6.setCursor(Qt.CursorShape.PointingHandCursor)
        self.BTNFN6.setFont(QFont("Nunito Sans", 8))

        self.gridLayout.addWidget(self.BTNFN6, 3, 3, 1, 1)

        self.BTNFN5 = QPushButton(self.frame)
        self.BTNFN5.setObjectName(u"BTNFN5")
        self.BTNFN5.setFixedSize(QSize(32, 32))
        self.BTNFN5.setCursor(Qt.CursorShape.PointingHandCursor)
        self.BTNFN5.setFont(QFont("Nunito Sans", 8))

        self.gridLayout.addWidget(self.BTNFN5, 0, 3, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)


        self.horizontalLayout_6.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_5)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_3)

        self.BTNFN7 = QPushButton(self.frame)
        self.BTNFN7.setObjectName(u"BTNFN7")
        self.BTNFN7.setFixedSize(QSize(32, 32))
        self.BTNFN7.setCursor(Qt.CursorShape.PointingHandCursor)
        self.BTNFN7.setFont(QFont("Nunito Sans", 8))

        self.verticalLayout_5.addWidget(self.BTNFN7)

        self.BTNFN8 = QPushButton(self.frame)
        self.BTNFN8.setObjectName(u"BTNFN8")
        self.BTNFN8.setFixedSize(QSize(32, 32))
        self.BTNFN8.setCursor(Qt.CursorShape.PointingHandCursor)
        self.BTNFN8.setFont(QFont("Nunito Sans", 8))

        self.verticalLayout_5.addWidget(self.BTNFN8)


        self.horizontalLayout_7.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_4)

        self.BTNFN9 = QPushButton(self.frame)
        self.BTNFN9.setObjectName(u"BTNFN9")
        self.BTNFN9.setFixedSize(QSize(32, 32))
        self.BTNFN9.setCursor(Qt.CursorShape.PointingHandCursor)
        self.BTNFN9.setFont(QFont("Nunito Sans", 8))

        self.verticalLayout_6.addWidget(self.BTNFN9)

        self.BTNFN10 = QPushButton(self.frame)
        self.BTNFN10.setObjectName(u"BTNFN10")
        self.BTNFN10.setFixedSize(QSize(32, 32))
        self.BTNFN10.setCursor(Qt.CursorShape.PointingHandCursor)
        self.BTNFN10.setFont(QFont("Nunito Sans", 8))

        self.verticalLayout_6.addWidget(self.BTNFN10)


        self.horizontalLayout_7.addLayout(self.verticalLayout_6)


        self.verticalLayout_7.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_6.addLayout(self.verticalLayout_7)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_2)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.BTNFN3_2 = QPushButton(self.frame)
        self.BTNFN3_2.setObjectName(u"BTNFN3_2")
        self.BTNFN3_2.setFixedSize(QSize(32, 32))
        self.BTNFN3_2.setCursor(Qt.CursorShape.PointingHandCursor)
        self.BTNFN3_2.setFont(QFont("Nunito Sans", 8))

        self.gridLayout_2.addWidget(self.BTNFN3_2, 3, 2, 1, 1)

        self.BTNFN2_2 = QPushButton(self.frame)
        self.BTNFN2_2.setObjectName(u"BTNFN2_2")
        self.BTNFN2_2.setFixedSize(QSize(32, 32))   
        self.BTNFN2_2.setCursor(Qt.CursorShape.PointingHandCursor)
        self.BTNFN2_2.setFont(QFont("Nunito Sans", 8))

        self.gridLayout_2.addWidget(self.BTNFN2_2, 2, 1, 1, 1)

        self.BTNFN1_2 = QPushButton(self.frame)
        self.BTNFN1_2.setObjectName(u"BTNFN1_2")
        self.BTNFN1_2.setFixedSize(QSize(32, 32))
        self.BTNFN1_2.setCursor(Qt.CursorShape.PointingHandCursor)
        self.BTNFN1_2.setFont(QFont("Nunito Sans", 8))

        self.gridLayout_2.addWidget(self.BTNFN1_2, 0, 2, 1, 1)

        self.BTNFN4_2 = QPushButton(self.frame)
        self.BTNFN4_2.setObjectName(u"BTNFN4_2")
        self.BTNFN4_2.setFixedSize(QSize(32, 32))
        self.BTNFN4_2.setCursor(Qt.CursorShape.PointingHandCursor)
        self.BTNFN4_2.setFont(QFont("Nunito Sans", 8))

        self.gridLayout_2.addWidget(self.BTNFN4_2, 2, 3, 1, 1)

        self.BTNFN5_2 = QPushButton(self.frame)
        self.BTNFN5_2.setObjectName(u"BTNFN5_2")
        self.BTNFN5_2.setFixedSize(QSize(32, 32))
        self.BTNFN5_2.setCursor(Qt.CursorShape.PointingHandCursor)
        self.BTNFN5_2.setFont(QFont("Nunito Sans", 8))

        self.gridLayout_2.addWidget(self.BTNFN5_2, 0, 0, 1, 1)

        self.BTNFN6_2 = QPushButton(self.frame)
        self.BTNFN6_2.setObjectName(u"BTNFN6_2")
        self.BTNFN6_2.setFixedSize(QSize(32, 32))
        self.BTNFN6_2.setCursor(Qt.CursorShape.PointingHandCursor)
        self.BTNFN6_2.setFont(QFont("Nunito Sans", 8))

        self.gridLayout_2.addWidget(self.BTNFN6_2, 3, 0, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_2)


        self.horizontalLayout_6.addLayout(self.verticalLayout_4)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.BTNFN = QPushButton(self.frame)
        self.BTNFN.setObjectName(u"BTNFN")
        self.BTNFN.setCursor(Qt.CursorShape.PointingHandCursor)

        self.verticalLayout.addWidget(self.BTNFN)


        self.verticalLayout_3.addWidget(self.frame)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"RQTLL IDE", None))
        self.LABELInfo_3.setText(QCoreApplication.translate("Widget", u"Tópico:", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Widget", u"cmd_vel", None))
        self.BTNEdit.setText(QCoreApplication.translate("Widget", u"Editar botones", None))
        self.LABELInfo2.setText(QCoreApplication.translate("Widget", u"Vel. lineal: 0. Vel angular: 0.", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Lineal", None))
        self.BTNFN2.setText(QCoreApplication.translate("Widget", u"A", None))
        self.BTNFN3.setText(QCoreApplication.translate("Widget", u"S", None))
        self.BTNFN4.setText(QCoreApplication.translate("Widget", u"D", None))
        self.BTNFN1.setText(QCoreApplication.translate("Widget", u"W", None))
        self.BTNFN6.setText(QCoreApplication.translate("Widget", u"F", None))
        self.BTNFN5.setText(QCoreApplication.translate("Widget", u"R", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"Velocidad", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Lin.", None))
        self.BTNFN7.setText(QCoreApplication.translate("Widget", u"E", None))
        self.BTNFN8.setText(QCoreApplication.translate("Widget", u"Q", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"Ang.", None))
        self.BTNFN9.setText(QCoreApplication.translate("Widget", u"U", None))
        self.BTNFN10.setText(QCoreApplication.translate("Widget", u"O", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Angular", None))
        self.BTNFN3_2.setText(QCoreApplication.translate("Widget", u"K", None))
        self.BTNFN2_2.setText(QCoreApplication.translate("Widget", u"J", None))
        self.BTNFN1_2.setText(QCoreApplication.translate("Widget", u"I", None))
        self.BTNFN4_2.setText(QCoreApplication.translate("Widget", u"L", None))
        self.BTNFN5_2.setText(QCoreApplication.translate("Widget", u"Y", None))
        self.BTNFN6_2.setText(QCoreApplication.translate("Widget", u"H", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"Alto", None))
        self.BTNFN.setText(QCoreApplication.translate("Widget", u"Espacio", None))
    # retranslateUi
