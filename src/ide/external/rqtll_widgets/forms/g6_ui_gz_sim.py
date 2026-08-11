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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QPushButton, QRadioButton,
    QScrollArea, QSizePolicy, QSpacerItem, QSpinBox,
    QTabWidget, QTextEdit, QToolBox, QVBoxLayout,
    QWidget)
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
        self.verticalLayout_2.setContentsMargins(0,0,0,0)
        self.tabWidget = QTabWidget(self.frame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.South)
        self.tabWidget.setTabBarAutoHide(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0,0,0,0)
        self.textEdit = QTextEdit(self.tab)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.textEdit, 1, 2, 1, 1)

        self.frame_2 = QFrame(self.tab)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_2.setFixedWidth(450)
        self.verticalLayout_10 = QVBoxLayout(self.frame_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0,0,4,0)
        self.scrollArea = QScrollArea(self.frame_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 459, 521))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0,0,4,0)
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.RADIOSIMRun = QRadioButton(self.scrollAreaWidgetContents)
        self.RADIOSIMRun.setObjectName(u"RADIOSIMRun")
        self.RADIOSIMRun.setChecked(True)

        self.verticalLayout_8.addWidget(self.RADIOSIMRun)

        self.RADIOSIMPlay = QRadioButton(self.scrollAreaWidgetContents)
        self.RADIOSIMPlay.setObjectName(u"RADIOSIMPlay")

        self.verticalLayout_8.addWidget(self.RADIOSIMPlay)


        self.horizontalLayout_18.addLayout(self.verticalLayout_8)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_7)


        self.verticalLayout.addLayout(self.horizontalLayout_18)

        self.toolBox = QToolBox(self.scrollAreaWidgetContents)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy1)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 441, 160))
        sizePolicy1.setHeightForWidth(self.page.sizePolicy().hasHeightForWidth())
        self.page.setSizePolicy(sizePolicy1)
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.page)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.EDITSdf = QLineEdit(self.page)
        self.EDITSdf.setObjectName(u"EDITSdf")

        self.horizontalLayout_2.addWidget(self.EDITSdf)

        self.BTNSdf = QPushButton(self.page)
        self.BTNSdf.setObjectName(u"BTNSdf")
        icon = QIcon()
        icon_path = _resolve_icon(icon_dirs, os.path.join('icons', 'folder', 'default.svg'), theme=theme)
        icon.addFile(icon_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BTNSdf.setIcon(icon)
        self.BTNSdf.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.BTNSdf.setFixedSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.BTNSdf)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_12 = QLabel(self.page)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_21.addWidget(self.label_12)

        self.EDITConfig = QLineEdit(self.page)
        self.EDITConfig.setObjectName(u"EDITConfig")

        self.horizontalLayout_21.addWidget(self.EDITConfig)

        self.BTNConfig = QPushButton(self.page)
        self.BTNConfig.setObjectName(u"BTNConfig")
        icon = QIcon()
        icon_path = _resolve_icon(icon_dirs, os.path.join('icons', 'folder', 'default.svg'), theme=theme)
        icon.addFile(icon_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BTNConfig.setIcon(icon)
        self.BTNConfig.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.BTNConfig.setFixedSize(QSize(32, 32))

        self.horizontalLayout_21.addWidget(self.BTNConfig)


        self.verticalLayout_4.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.COMBORunMode = QComboBox(self.page)
        self.COMBORunMode.addItem("")
        self.COMBORunMode.addItem("")
        self.COMBORunMode.addItem("")
        self.COMBORunMode.setObjectName(u"COMBORunMode")
        arrow_down_icon = _resolve_icon(icon_dirs, os.path.join('arrows', 'down.svg'))
        arrow_up_icon = _resolve_icon(icon_dirs, os.path.join('arrows', 'up.svg'))
        self.COMBORunMode.setStyleSheet(f"""
            QComboBox::down-arrow {{
                image: url({arrow_down_icon});
            }}
            QComboBox::down-arrow:on {{
                image: url({arrow_up_icon});
            }}
        """)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.COMBORunMode.sizePolicy().hasHeightForWidth())
        self.COMBORunMode.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.COMBORunMode)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.page, u"Esenciales")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 441, 190))
        self.verticalLayout_5 = QVBoxLayout(self.page_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.SPINHzRate = QDoubleSpinBox(self.page_2)
        self.SPINHzRate.setObjectName(u"SPINHzRate")
        self.SPINHzRate.setStyleSheet(f"""
            QDoubleSpinBox::up-button {{
                image: url({arrow_up_icon});
            }}
            QDoubleSpinBox::down-button {{
                image: url({arrow_down_icon});
            }}
        """)
        sizePolicy2.setHeightForWidth(self.SPINHzRate.sizePolicy().hasHeightForWidth())
        self.SPINHzRate.setSizePolicy(sizePolicy2)
        self.SPINHzRate.setMaximum(1000.000000000000000)
        self.SPINHzRate.setValue(000000000000000)

        self.horizontalLayout_5.addWidget(self.SPINHzRate)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.CHECKhtfl_2 = QCheckBox(self.page_2)
        self.CHECKhtfl_2.setObjectName(u"CHECKhtfl_2")

        self.horizontalLayout_6.addWidget(self.CHECKhtfl_2)

        self.SPINSeed = QSpinBox(self.page_2)
        self.SPINSeed.setObjectName(u"SPINSeed")
        self.SPINSeed.setStyleSheet(f"""
            QSpinBox::up-button {{
                image: url({arrow_up_icon});
            }}
            QSpinBox::down-button {{
                image: url({arrow_down_icon});
            }}
        """)
        sizePolicy2.setHeightForWidth(self.SPINSeed.sizePolicy().hasHeightForWidth())
        self.SPINSeed.setSizePolicy(sizePolicy2)
        self.SPINSeed.setMaximum(9999999)

        self.horizontalLayout_6.addWidget(self.SPINSeed)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.RADIORunAtStart = QRadioButton(self.page_2)
        self.RADIORunAtStart.setObjectName(u"RADIORunAtStart")

        self.horizontalLayout_4.addWidget(self.RADIORunAtStart)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.RADIOWaitAssets = QRadioButton(self.page_2)
        self.RADIOWaitAssets.setObjectName(u"RADIOWaitAssets")

        self.horizontalLayout_17.addWidget(self.RADIOWaitAssets)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_6)


        self.verticalLayout_5.addLayout(self.horizontalLayout_17)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.toolBox.addItem(self.page_2, u"Avanzado")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.page_5.setGeometry(QRect(0, 0, 427, 247))
        self.verticalLayout_9 = QVBoxLayout(self.page_5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_13 = QLabel(self.page_5)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_22.addWidget(self.label_13)

        self.COMBOPysicsEngine = QComboBox(self.page_5)
        self.COMBOPysicsEngine.addItem("")
        self.COMBOPysicsEngine.setObjectName(u"COMBOPysicsEngine")
        self.COMBOPysicsEngine.setStyleSheet(f"""
            QComboBox::down-arrow {{
                image: url({arrow_down_icon});
            }}
            QComboBox::down-arrow:on {{
                image: url({arrow_up_icon});
            }}
        """)
        sizePolicy2.setHeightForWidth(self.COMBOPysicsEngine.sizePolicy().hasHeightForWidth())
        self.COMBOPysicsEngine.setSizePolicy(sizePolicy2)

        self.horizontalLayout_22.addWidget(self.COMBOPysicsEngine)


        self.verticalLayout_9.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_14 = QLabel(self.page_5)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_23.addWidget(self.label_14)

        self.COMBORenderEngine = QComboBox(self.page_5)
        self.COMBORenderEngine.addItem("")
        self.COMBORenderEngine.addItem("")
        self.COMBORenderEngine.setObjectName(u"COMBORenderEngine")
        self.COMBORenderEngine.setStyleSheet(f"""
            QComboBox::down-arrow {{
                image: url({arrow_down_icon});
            }}
            QComboBox::down-arrow:on {{
                image: url({arrow_up_icon});
            }}
        """)
        sizePolicy2.setHeightForWidth(self.COMBORenderEngine.sizePolicy().hasHeightForWidth())
        self.COMBORenderEngine.setSizePolicy(sizePolicy2)

        self.horizontalLayout_23.addWidget(self.COMBORenderEngine)


        self.verticalLayout_9.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_15 = QLabel(self.page_5)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_24.addWidget(self.label_15)

        self.COMBOGUIEngine = QComboBox(self.page_5)
        self.COMBOGUIEngine.addItem("")
        self.COMBOGUIEngine.addItem("")
        self.COMBOGUIEngine.setObjectName(u"COMBOGUIEngine")
        self.COMBOGUIEngine.setStyleSheet(f"""
            QComboBox::down-arrow {{
                image: url({arrow_down_icon});
            }}
            QComboBox::down-arrow:on {{
                image: url({arrow_up_icon});
            }}
        """)
        sizePolicy2.setHeightForWidth(self.COMBOGUIEngine.sizePolicy().hasHeightForWidth())
        self.COMBOGUIEngine.setSizePolicy(sizePolicy2)

        self.horizontalLayout_24.addWidget(self.COMBOGUIEngine)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_10 = QLabel(self.page_5)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_16.addWidget(self.label_10)

        self.COMBOServerEngine = QComboBox(self.page_5)
        self.COMBOServerEngine.addItem("")
        self.COMBOServerEngine.addItem("")
        self.COMBOServerEngine.setObjectName(u"COMBOServerEngine")
        self.COMBOServerEngine.setStyleSheet(f"""
            QComboBox::down-arrow {{
                image: url({arrow_down_icon});
            }}
            QComboBox::down-arrow:on {{
                image: url({arrow_up_icon});
            }}
        """)
        sizePolicy2.setHeightForWidth(self.COMBOServerEngine.sizePolicy().hasHeightForWidth())
        self.COMBOServerEngine.setSizePolicy(sizePolicy2)

        self.horizontalLayout_16.addWidget(self.COMBOServerEngine)

        self.verticalLayout_9.addLayout(self.horizontalLayout_24)
        self.verticalLayout_9.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_16 = QLabel(self.page_5)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_25.addWidget(self.label_16)

        self.COMBOAPI = QComboBox(self.page_5)
        self.COMBOAPI.addItem("")
        self.COMBOAPI.addItem("")
        self.COMBOAPI.addItem("")
        self.COMBOAPI.setObjectName(u"COMBOAPI")
        self.COMBOAPI.setStyleSheet(f"""
            QComboBox::down-arrow {{
                image: url({arrow_down_icon});
            }}
            QComboBox::down-arrow:on {{
                image: url({arrow_up_icon});
            }}
        """)
        sizePolicy2.setHeightForWidth(self.COMBOAPI.sizePolicy().hasHeightForWidth())
        self.COMBOAPI.setSizePolicy(sizePolicy2)

        self.horizontalLayout_25.addWidget(self.COMBOAPI)


        self.verticalLayout_9.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_17 = QLabel(self.page_5)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_26.addWidget(self.label_17)

        self.COMBOAPIGUI = QComboBox(self.page_5)
        self.COMBOAPIGUI.addItem("")
        self.COMBOAPIGUI.addItem("")
        self.COMBOAPIGUI.addItem("")
        self.COMBOAPIGUI.setObjectName(u"COMBOAPIGUI")
        self.COMBOAPIGUI.setStyleSheet(f"""
            QComboBox::down-arrow {{
                image: url({arrow_down_icon});
            }}
            QComboBox::down-arrow:on {{
                image: url({arrow_up_icon});
            }}
        """)
        sizePolicy2.setHeightForWidth(self.COMBOAPIGUI.sizePolicy().hasHeightForWidth())
        self.COMBOAPIGUI.setSizePolicy(sizePolicy2)

        self.horizontalLayout_26.addWidget(self.COMBOAPIGUI)


        self.verticalLayout_9.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_18 = QLabel(self.page_5)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_27.addWidget(self.label_18)

        self.COMBOAPIServer = QComboBox(self.page_5)
        self.COMBOAPIServer.addItem("")
        self.COMBOAPIServer.addItem("")
        self.COMBOAPIServer.addItem("")
        self.COMBOAPIServer.setObjectName(u"COMBOAPIServer")
        self.COMBOAPIServer.setStyleSheet(f"""
            QComboBox::down-arrow {{
                image: url({arrow_down_icon});
            }}
            QComboBox::down-arrow:on {{
                image: url({arrow_up_icon});
            }}
        """)
        sizePolicy2.setHeightForWidth(self.COMBOAPIServer.sizePolicy().hasHeightForWidth())
        self.COMBOAPIServer.setSizePolicy(sizePolicy2)

        self.horizontalLayout_27.addWidget(self.COMBOAPIServer)


        self.verticalLayout_9.addLayout(self.horizontalLayout_27)

        self.toolBox.addItem(self.page_5, u"Motor")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setGeometry(QRect(0, 0, 441, 127))
        self.verticalLayout_7 = QVBoxLayout(self.page_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_8 = QLabel(self.page_4)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_14.addWidget(self.label_8)

        self.SPINSecondaries = QSpinBox(self.page_4)
        self.SPINSecondaries.setObjectName(u"SPINSecondaries")
        self.SPINSecondaries.setStyleSheet(f"""
            QSpinBox::up-button {{
                image: url({arrow_up_icon});
            }}
            QSpinBox::down-button {{
                image: url({arrow_down_icon});
            }}
        """)
        sizePolicy2.setHeightForWidth(self.SPINSecondaries.sizePolicy().hasHeightForWidth())
        self.SPINSecondaries.setSizePolicy(sizePolicy2)

        self.horizontalLayout_14.addWidget(self.SPINSecondaries)


        self.verticalLayout_7.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_9 = QLabel(self.page_4)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_15.addWidget(self.label_9)

        self.COMBOSecondary = QComboBox(self.page_4)
        self.COMBOSecondary.addItem("")
        self.COMBOSecondary.addItem("")
        self.COMBOSecondary.setObjectName(u"COMBOSecondary")
        self.COMBOSecondary.setStyleSheet(f"""
            QComboBox::down-arrow {{
                image: url({arrow_down_icon});
            }}
            QComboBox::down-arrow:on {{
                image: url({arrow_up_icon});
            }}
        """)
        sizePolicy2.setHeightForWidth(self.COMBOSecondary.sizePolicy().hasHeightForWidth())
        self.COMBOSecondary.setSizePolicy(sizePolicy2)

        self.horizontalLayout_15.addWidget(self.COMBOSecondary)


        self.verticalLayout_7.addLayout(self.horizontalLayout_15)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_4)

        self.toolBox.addItem(self.page_4, u"Simulaci\u00f3n distrubuida")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setGeometry(QRect(0, 0, 427, 285))
        self.verticalLayout_6 = QVBoxLayout(self.page_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.CHECKRecord = QCheckBox(self.page_3)
        self.CHECKRecord.setObjectName(u"CHECKRecord")

        self.horizontalLayout_7.addWidget(self.CHECKRecord)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label = QLabel(self.page_3)
        self.label.setObjectName(u"label")

        self.horizontalLayout_8.addWidget(self.label)

        self.EDITRecordDir = QLineEdit(self.page_3)
        self.EDITRecordDir.setObjectName(u"EDITRecordDir")

        self.horizontalLayout_8.addWidget(self.EDITRecordDir)

        self.BTNRecordDir = QPushButton(self.page_3)
        self.BTNRecordDir.setObjectName(u"BTNRecordDir")
        icon = QIcon()
        icon_path = _resolve_icon(icon_dirs, os.path.join('icons', 'folder', 'default.svg'), theme=theme)
        icon.addFile(icon_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BTNRecordDir.setIcon(icon)
        self.BTNRecordDir.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.BTNRecordDir.setFixedSize(QSize(32, 32))

        self.horizontalLayout_8.addWidget(self.BTNRecordDir)


        self.verticalLayout_6.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.CHECKRecordMaterials = QCheckBox(self.page_3)
        self.CHECKRecordMaterials.setObjectName(u"CHECKRecordMaterials")

        self.horizontalLayout_9.addWidget(self.CHECKRecordMaterials)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_3)


        self.verticalLayout_6.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.label_5 = QLabel(self.page_3)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_10.addWidget(self.label_5)

        self.COMBORecordTopics = QComboBox(self.page_3)
        self.COMBORecordTopics.addItem("")
        self.COMBORecordTopics.addItem("")
        self.COMBORecordTopics.setObjectName(u"COMBORecordTopics")
        self.COMBORecordTopics.setStyleSheet(f"""
            QComboBox::down-arrow {{
                image: url({arrow_down_icon});
            }}
            QComboBox::down-arrow:on {{
                image: url({arrow_up_icon});
            }}
        """)
        sizePolicy2.setHeightForWidth(self.COMBORecordTopics.sizePolicy().hasHeightForWidth())
        self.COMBORecordTopics.setSizePolicy(sizePolicy2)

        self.horizontalLayout_10.addWidget(self.COMBORecordTopics)


        self.verticalLayout_6.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.CHECKRecordOverwrite = QCheckBox(self.page_3)
        self.CHECKRecordOverwrite.setObjectName(u"CHECKRecordOverwrite")

        self.horizontalLayout_12.addWidget(self.CHECKRecordOverwrite)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_4)


        self.verticalLayout_6.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_6 = QLabel(self.page_3)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_11.addWidget(self.label_6)

        self.SPINRecordPeriod = QDoubleSpinBox(self.page_3)
        self.SPINRecordPeriod.setObjectName(u"SPINRecordPeriod")
        self.SPINRecordPeriod.setStyleSheet(f"""
            QDoubleSpinBox::up-button {{
                image: url({arrow_up_icon});
            }}
            QDoubleSpinBox::down-button {{
                image: url({arrow_down_icon});
            }}
        """)
        sizePolicy2.setHeightForWidth(self.SPINRecordPeriod.sizePolicy().hasHeightForWidth())
        self.SPINRecordPeriod.setSizePolicy(sizePolicy2)
        self.SPINRecordPeriod.setMaximum(1000.000000000000000)

        self.horizontalLayout_11.addWidget(self.SPINRecordPeriod)

        self.label_7 = QLabel(self.page_3)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_11.addWidget(self.label_7)


        self.verticalLayout_6.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.CHECKRecordZip = QCheckBox(self.page_3)
        self.CHECKRecordZip.setObjectName(u"CHECKRecordZip")

        self.horizontalLayout_13.addWidget(self.CHECKRecordZip)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_5)


        self.verticalLayout_6.addLayout(self.horizontalLayout_13)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)

        self.toolBox.addItem(self.page_3, u"Grabaci\u00f3n")

        self.verticalLayout.addWidget(self.toolBox)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_11 = QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_20.addWidget(self.label_11)

        self.EDITSIMPlay = QLineEdit(self.scrollAreaWidgetContents)
        self.EDITSIMPlay.setObjectName(u"EDITSIMPlay")

        self.horizontalLayout_20.addWidget(self.EDITSIMPlay)

        self.BTNSIMPlay = QPushButton(self.scrollAreaWidgetContents)
        self.BTNSIMPlay.setObjectName(u"BTNSIMPlay")
        icon = QIcon()
        icon_path = _resolve_icon(icon_dirs, os.path.join('icons', 'folder', 'default.svg'), theme=theme)
        icon.addFile(icon_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BTNSIMPlay.setIcon(icon)
        self.BTNSIMPlay.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.BTNSIMPlay.setFixedSize(QSize(32, 32))

        self.horizontalLayout_20.addWidget(self.BTNSIMPlay)


        self.verticalLayout.addLayout(self.horizontalLayout_20)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.BTNConnect = QPushButton(self.scrollAreaWidgetContents)
        self.BTNConnect.setObjectName(u"BTNConnect")
        icon = QIcon()
        icon_path = _resolve_icon(icon_dirs, os.path.join('icons', 'synchronize', 'default.svg'), theme=theme)
        icon.addFile(icon_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BTNConnect.setIcon(icon)
        self.BTNConnect.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.BTNConnect.setFixedHeight(32)

        self.verticalLayout.addWidget(self.BTNConnect)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_10.addWidget(self.scrollArea)


        self.gridLayout.addWidget(self.frame_2, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab, "")

        self.verticalLayout_2.addWidget(self.tabWidget)


        self.verticalLayout_3.addWidget(self.frame)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.retranslateUi(Widget)

        self.tabWidget.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.RADIOSIMRun.setText(QCoreApplication.translate("Widget", u"Simular", None))
        self.RADIOSIMPlay.setText(QCoreApplication.translate("Widget", u"Reproducir simulaci\u00f3n", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"SDF:", None))
        self.EDITSdf.setPlaceholderText(QCoreApplication.translate("Widget", u"Ej. empty.sdf", None))
        self.label_12.setText(QCoreApplication.translate("Widget", u"Configuraci\u00f3n de Gazebo:", None))
        self.EDITConfig.setPlaceholderText(QCoreApplication.translate("Widget", u"Ej. ~/.gz/sim/10/gui.config", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Modo de ejecuci\u00f3n:", None))
        self.COMBORunMode.setItemText(0, QCoreApplication.translate("Widget", u"Completo", None))
        self.COMBORunMode.setItemText(1, QCoreApplication.translate("Widget", u"Solo servidor", None))
        self.COMBORunMode.setItemText(2, QCoreApplication.translate("Widget", u"Solo GUI", None))

        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("Widget", u"Esenciales", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"Frecuencia die actualizaci\u00f3n:", None))
        self.CHECKhtfl_2.setText(QCoreApplication.translate("Widget", u"Semilla aleatoria", None))
        self.RADIORunAtStart.setText(QCoreApplication.translate("Widget", u"Autoreproducir al iniciar", None))
        self.RADIOWaitAssets.setText(QCoreApplication.translate("Widget", u"Esperar recursos antes de simular", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("Widget", u"Avanzado", None))
        self.label_13.setText(QCoreApplication.translate("Widget", u"Motor de fisicas", None))
        self.COMBOPysicsEngine.setItemText(0, QCoreApplication.translate("Widget", u"DART", None))

        self.label_14.setText(QCoreApplication.translate("Widget", u"Motor de randerizado", None))
        self.COMBORenderEngine.setItemText(0, QCoreApplication.translate("Widget", u"OGRE2", None))
        self.COMBORenderEngine.setItemText(1, QCoreApplication.translate("Widget", u"OGRE", None))

        self.label_15.setText(QCoreApplication.translate("Widget", u"Motor de renderizado para la GUI", None))
        self.COMBOGUIEngine.setItemText(0, QCoreApplication.translate("Widget", u"OGRE2", None))
        self.COMBOGUIEngine.setItemText(1, QCoreApplication.translate("Widget", u"OGRE", None))

        self.label_10.setText(QCoreApplication.translate("Widget", u"Motor de renderizado para el servidor", None))
        self.COMBOServerEngine.setItemText(0, QCoreApplication.translate("Widget", u"OGRE2", None))
        self.COMBOServerEngine.setItemText(1, QCoreApplication.translate("Widget", u"OGRE", None))

        self.label_16.setText(QCoreApplication.translate("Widget", u"API", None))
        self.COMBOAPI.setItemText(0, QCoreApplication.translate("Widget", u"Opengl (default)", None))
        self.COMBOAPI.setItemText(1, QCoreApplication.translate("Widget", u"Vulkan (beta)", None))
        self.COMBOAPI.setItemText(2, QCoreApplication.translate("Widget", u"Metal (Apple only)", None))

        self.label_17.setText(QCoreApplication.translate("Widget", u"API para la GUI", None))
        self.COMBOAPIGUI.setItemText(0, QCoreApplication.translate("Widget", u"Opengl (default)", None))
        self.COMBOAPIGUI.setItemText(1, QCoreApplication.translate("Widget", u"Vulkan (beta)", None))
        self.COMBOAPIGUI.setItemText(2, QCoreApplication.translate("Widget", u"Metal (Apple only)", None))

        self.label_18.setText(QCoreApplication.translate("Widget", u"API para el servidor", None))
        self.COMBOAPIServer.setItemText(0, QCoreApplication.translate("Widget", u"Opengl (default)", None))
        self.COMBOAPIServer.setItemText(1, QCoreApplication.translate("Widget", u"Vulkan (beta)", None))
        self.COMBOAPIServer.setItemText(2, QCoreApplication.translate("Widget", u"Metal (Apple only)", None))

        self.toolBox.setItemText(self.toolBox.indexOf(self.page_5), QCoreApplication.translate("Widget", u"Motor", None))
        self.label_8.setText(QCoreApplication.translate("Widget", u"Secundarios esperados:", None))
        self.label_9.setText(QCoreApplication.translate("Widget", u"Rol:", None))
        self.COMBOSecondary.setItemText(0, QCoreApplication.translate("Widget", u"Primario", None))
        self.COMBOSecondary.setItemText(1, QCoreApplication.translate("Widget", u"Secundario", None))

        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), QCoreApplication.translate("Widget", u"Simulaci\u00f3n distrubuida", None))
        self.CHECKRecord.setText(QCoreApplication.translate("Widget", u"Grabar simulaci\u00f3n", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Ruta:", None))
        self.EDITRecordDir.setPlaceholderText(QCoreApplication.translate("Widget", u"Ej. ~/.gz/sim/log", None))
        self.CHECKRecordMaterials.setText(QCoreApplication.translate("Widget", u"Guardar mallas y materiales", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"Grabar t\u00f3pico:", None))
        self.COMBORecordTopics.setItemText(0, QCoreApplication.translate("Widget", u"Ninguno", None))
        self.COMBORecordTopics.setItemText(1, QCoreApplication.translate("Widget", u"Todos", None))

        self.CHECKRecordOverwrite.setText(QCoreApplication.translate("Widget", u"Sobreescribir archivos", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"Intervalo de actualizaci\u00f3n:", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"s", None))
        self.CHECKRecordZip.setText(QCoreApplication.translate("Widget", u"Comprimir al finalizar", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QCoreApplication.translate("Widget", u"Grabaci\u00f3n", None))
        self.label_11.setText(QCoreApplication.translate("Widget", u"Simulaci\u00f3n:", None))
        self.EDITSIMPlay.setPlaceholderText(QCoreApplication.translate("Widget", u"Ej. ~/.gz/sim/log", None))
        self.BTNConnect.setText(QCoreApplication.translate("Widget", u"Conectar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Widget", u"Tab 1", None))
    # retranslateUi
