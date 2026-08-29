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
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
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
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.textEdit = QTextEdit(self.tab)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy1.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.textEdit, 0, 1, 1, 1)

        self.frame_2 = QFrame(self.tab)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_2.setFixedWidth(400)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.CHECKhtfl = QCheckBox(self.frame_2)
        self.CHECKhtfl.setObjectName(u"CHECKhtfl")
        self.CHECKhtfl.setCursor(Qt.CursorShape.PointingHandCursor)

        self.horizontalLayout_4.addWidget(self.CHECKhtfl)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_8.addWidget(self.label_6)

        self.EditPerspectivename = QLineEdit(self.frame_2)
        self.EditPerspectivename.setObjectName(u"EditPerspectivename")

        self.horizontalLayout_8.addWidget(self.EditPerspectivename)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_8.addWidget(self.label)

        self.EDITPerspectiveFile = QLineEdit(self.frame_2)
        self.EDITPerspectiveFile.setObjectName(u"EDITPerspectiveFile")

        self.horizontalLayout_8.addWidget(self.EDITPerspectiveFile)

        self.BTNPerspectiveFile = QPushButton(self.frame_2)
        self.BTNPerspectiveFile.setObjectName(u"BTNPerspectiveFile")
        icon = QIcon()
        icon_path = _resolve_icon(icon_dirs, os.path.join('icons', 'folder', 'default.svg'), theme=theme)
        icon.addFile(icon_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BTNPerspectiveFile.setIcon(icon)
        self.BTNPerspectiveFile.setCursor(Qt.CursorShape.PointingHandCursor)

        self.horizontalLayout_8.addWidget(self.BTNPerspectiveFile)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.line = QFrame(self.frame_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.OPTStandalone = QComboBox(self.frame_2)
        self.OPTStandalone.addItem("")
        self.OPTStandalone.addItem("")
        self.OPTStandalone.addItem("")
        self.OPTStandalone.addItem("")
        self.OPTStandalone.addItem("")
        self.OPTStandalone.addItem("")
        self.OPTStandalone.addItem("")
        self.OPTStandalone.addItem("")
        self.OPTStandalone.addItem("")
        self.OPTStandalone.addItem("")
        self.OPTStandalone.addItem("")
        self.OPTStandalone.addItem("")
        self.OPTStandalone.addItem("")
        self.OPTStandalone.addItem("")
        self.OPTStandalone.setObjectName(u"OPTStandalone")
        self.OPTStandalone.setCursor(Qt.CursorShape.PointingHandCursor)
        arrow_down_icon = _resolve_icon(icon_dirs, os.path.join('arrows', 'down.svg'))
        arrow_up_icon = _resolve_icon(icon_dirs, os.path.join('arrows', 'up.svg'))
        self.OPTStandalone.setStyleSheet(f"""
            QComboBox::down-arrow {{
                image: url({arrow_down_icon});
            }}
            QComboBox::down-arrow:on {{
                image: url({arrow_up_icon});
            }}
        """)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.OPTStandalone.sizePolicy().hasHeightForWidth())
        self.OPTStandalone.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.OPTStandalone)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.BTNConnect = QPushButton(self.frame_2)
        self.BTNConnect.setObjectName(u"BTNConnect")
        icon = QIcon()
        icon_path = _resolve_icon(icon_dirs, os.path.join('icons', 'synchronize', 'default.svg'), theme=theme)
        icon.addFile(icon_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BTNConnect.setIcon(icon)
        self.BTNConnect.setCursor(Qt.CursorShape.PointingHandCursor)

        self.verticalLayout.addWidget(self.BTNConnect)


        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.verticalLayout_3.addWidget(self.frame)

        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"RQTLL IDE", None))
        self.CHECKhtfl.setText(QCoreApplication.translate("Widget", u"Bloquear GUI.", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"Perspectiva:", None))
        self.EditPerspectivename.setPlaceholderText(QCoreApplication.translate("Widget", u"Nombre", None))
        self.label.setText(QCoreApplication.translate("Widget", u"o", None))
        self.EDITPerspectiveFile.setText("")
        self.EDITPerspectiveFile.setPlaceholderText(QCoreApplication.translate("Widget", u"Archivo", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Standalone:", None))
        self.OPTStandalone.setItemText(0, QCoreApplication.translate("Widget", u"No", None))
        self.OPTStandalone.setItemText(1, QCoreApplication.translate("Widget", u"rqt_action.action_plugin", None))
        self.OPTStandalone.setItemText(2, QCoreApplication.translate("Widget", u"rqt_bag.bag", None))
        self.OPTStandalone.setItemText(3, QCoreApplication.translate("Widget", u"rqt_console.console", None))
        self.OPTStandalone.setItemText(4, QCoreApplication.translate("Widget", u"rqt_graph.ros_graph", None))
        self.OPTStandalone.setItemText(5, QCoreApplication.translate("Widget", u"rqt_msg.messages", None))
        self.OPTStandalone.setItemText(6, QCoreApplication.translate("Widget", u"rqt_plot.plot", None))
        self.OPTStandalone.setItemText(7, QCoreApplication.translate("Widget", u"rqt_publisher.publisher", None))
        self.OPTStandalone.setItemText(8, QCoreApplication.translate("Widget", u"rqt_py_console.py_console", None))
        self.OPTStandalone.setItemText(9, QCoreApplication.translate("Widget", u"rqt_reconfigure.param_plugin", None))
        self.OPTStandalone.setItemText(10, QCoreApplication.translate("Widget", u"rqt_service_caller.service_caller", None))
        self.OPTStandalone.setItemText(11, QCoreApplication.translate("Widget", u"rqt_shell.shell", None))
        self.OPTStandalone.setItemText(12, QCoreApplication.translate("Widget", u"rqt_srv.services", None))
        self.OPTStandalone.setItemText(13, QCoreApplication.translate("Widget", u"rqt_topic.topic", None))

        self.BTNConnect.setText(QCoreApplication.translate("Widget", u"Conectar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Widget", u"Tab 1", None))
    # retranslateUi
