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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QTextEdit, QVBoxLayout, QWidget)
import os

try:
    from ..utils.icon_loader import load_qicon, load_qpixmap, _resolve_icon
    from ..utils.nav import NavButton
except (ImportError, ValueError):
    import sys
    _parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if _parent not in sys.path:
        sys.path.insert(0, _parent)
    from utils.icon_loader import load_qicon, load_qpixmap, _resolve_icon
    from utils.nav import NavButton

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
        self.frame.setProperty('role', 'central-shortcuts')
        self.frame.setProperty('variant', 'default')
        self.frame.setProperty('state', 'normal')
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.frame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.South)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setProperty('role', 'central')
        self.tabWidget.setProperty('variant', 'default')
        self.tabWidget.setProperty('state', 'normal')
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        
        self.frame_2 = QFrame(self.tab)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_2.setFixedWidth(400)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_7.addWidget(self.label_5)

        self.EDITServer = QLineEdit(self.frame_2)
        self.EDITServer.setObjectName(u"EDITServer")

        self.horizontalLayout_7.addWidget(self.EDITServer)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_6.addWidget(self.label_4)

        self.EDITUser = QLineEdit(self.frame_2)
        self.EDITUser.setObjectName(u"EDITUser")

        self.horizontalLayout_6.addWidget(self.EDITUser)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.EDITPort = QLineEdit(self.frame_2)
        self.EDITPort.setObjectName(u"EDITPort")

        self.horizontalLayout_3.addWidget(self.EDITPort)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_8.addWidget(self.label_6)

        self.EDITKey = QLineEdit(self.frame_2)
        self.EDITKey.setObjectName(u"EDITKey")

        self.horizontalLayout_8.addWidget(self.EDITKey)

        self.BTNDirKey = QPushButton(self.frame_2)
        self.BTNDirKey.setObjectName(u"BTNDirKey")
        icon = QIcon()
        icon_path = _resolve_icon(icon_dirs, os.path.join('icons', 'folder', 'default.svg'), theme=theme)
        icon.addFile(icon_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BTNDirKey.setIcon(icon)
        self.BTNDirKey.setCursor(Qt.CursorShape.PointingHandCursor)

        self.horizontalLayout_8.addWidget(self.BTNDirKey)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.CHECKVerbose = QCheckBox(self.frame_2)
        self.CHECKVerbose.setObjectName(u"CHECKVerbose")
        self.CHECKVerbose.setCursor(Qt.CursorShape.PointingHandCursor)

        self.horizontalLayout_4.addWidget(self.CHECKVerbose)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.COMBOProtocol = QComboBox(self.frame_2)
        self.COMBOProtocol.addItem("")
        self.COMBOProtocol.addItem("")
        self.COMBOProtocol.addItem("")
        self.COMBOProtocol.setObjectName(u"COMBOProtocol")
        self.COMBOProtocol.setCursor(Qt.CursorShape.PointingHandCursor)
        arrow_down_icon = _resolve_icon(icon_dirs, os.path.join('arrows', 'down.svg'))
        arrow_up_icon = _resolve_icon(icon_dirs, os.path.join('arrows', 'up.svg'))
        self.COMBOProtocol.setStyleSheet(f"""
            QComboBox::down-arrow {{
                image: url({arrow_down_icon});
            }}
            QComboBox::up-arrow {{
                image: url({arrow_up_icon});
            }}
        """)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.COMBOProtocol.sizePolicy().hasHeightForWidth())
        self.COMBOProtocol.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.COMBOProtocol)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.BTNConnect = QPushButton(self.frame_2)
        self.BTNConnect.setObjectName(u"BTNConnect")
        icon = QIcon()
        icon_path = _resolve_icon(icon_dirs, os.path.join('icons', 'synchronize', 'default.svg'), theme=theme)
        icon.addFile(icon_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BTNConnect.setIcon(icon)
        self.BTNConnect.setCursor(Qt.CursorShape.PointingHandCursor)

        self.verticalLayout_4.addWidget(self.BTNConnect)


        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)

        self.textEdit = QTextEdit(self.tab)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.textEdit, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab, "")

        self.verticalLayout_2.addWidget(self.tabWidget)


        self.verticalLayout_3.addWidget(self.frame)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.retranslateUi(Widget)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"Servidor:", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"Usuario:", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Puerto:", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"Llave privada:", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Protocolo:", None))
        self.COMBOProtocol.setItemText(0, QCoreApplication.translate("Widget", u"Todo", None))
        self.COMBOProtocol.setItemText(1, QCoreApplication.translate("Widget", u"IPv4 addresses", None))
        self.COMBOProtocol.setItemText(2, QCoreApplication.translate("Widget", u"IPv6 addresses", None))

        self.CHECKVerbose.setText(QCoreApplication.translate("Widget", u"Salida detallada.", None))
        self.BTNConnect.setText(QCoreApplication.translate("Widget", u"Conectar", None))
        #self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Widget", u"Tab 1", None))
    # retranslateUi
