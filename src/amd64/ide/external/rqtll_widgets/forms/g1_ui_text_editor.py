# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

#from utils import scaled_icon_label
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)

from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QSizePolicy, QTabWidget, QTextEdit, QTreeWidget, QPushButton,
    QLabel, QSpacerItem, QTreeWidgetItem, QVBoxLayout, QWidget)
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
        self.theme = theme
        Widget.resize(1250, 644)
        Widget.setMinimumSize(QSize(1250, 644))
        icon = QIcon()
        icon_path = _resolve_icon(icon_dirs, os.path.join('logo.svg'))
        icon.addFile(icon_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Widget.setWindowIcon(icon)
        self.horizontalLayout = QHBoxLayout(Widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(6)

        self.nav = Nav(Widget, icon_dirs, theme)
        self.nav.setObjectName(u"nav")
        self.nav.layout.setContentsMargins(8, 4, 0, 8)
        
        self.horizontalLayout.addLayout(self.nav.layout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.frame = QFrame(Widget)
        self.frame.setObjectName(u"frame")
        self.frame.setProperty('role', 'central')
        self.frame.setProperty('variant', 'default')
        self.frame.setProperty('state', 'normal')
        self.frame.setContentsMargins(0, 0, 0, 0)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.TREEFILEManage = QTreeWidget(self.frame)
        QTreeWidgetItem(self.TREEFILEManage)
        __qtreewidgetitem = QTreeWidgetItem(self.TREEFILEManage)
        QTreeWidgetItem(__qtreewidgetitem)
        self.TREEFILEManage.setObjectName(u"TREEFILEManage")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.TREEFILEManage.sizePolicy().hasHeightForWidth())
        self.TREEFILEManage.setSizePolicy(sizePolicy1)
        self.TREEFILEManage.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_2.addWidget(self.TREEFILEManage)

        self.TABCODETabs = QTabWidget(self.frame)
        self.TABCODETabs.setObjectName(u"TABCODETabs")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.TABCODETabs.sizePolicy().hasHeightForWidth())
        self.TABCODETabs.setSizePolicy(sizePolicy2)
        self.TABCODETabs.setMovable(True)
        self.TABCODETabs.setTabBarAutoHide(True)
        self.widget = QWidget()
        self.widget.setObjectName(u"widget")
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.EDITCODEditor = QTextEdit(self.widget)
        self.EDITCODEditor.setObjectName(u"EDITCODEditor")
        self.EDITCODEditor.setTabStopDistance(32.000000000000000)
        self.EDITCODEditor.setFont(QFont('UbuntuMono Nerd Font Mono'))

        self.verticalLayout_4.addWidget(self.EDITCODEditor)

        self.TABCODETabs.addTab(self.widget, "")

        self.horizontalLayout_2.addWidget(self.TABCODETabs)

        self.TABTERMTabs = QTabWidget(self.frame)
        self.TABTERMTabs.setObjectName(u"TABTERMTabs")
        sizePolicy2.setHeightForWidth(self.TABTERMTabs.sizePolicy().hasHeightForWidth())
        self.TABTERMTabs.setSizePolicy(sizePolicy2)
        self.TABTERMTabs.setDocumentMode(False)
        self.TABTERMTabs.setTabBarAutoHide(True)
        self.widget_2 = QWidget()
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setProperty('role', 'tab')
        self.widget_2.setProperty('variant', 'default')
        self.widget_2.setProperty('state', 'normal')
        self.verticalLayout_6 = QVBoxLayout(self.widget_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.EDITORTERMEditor = QTextEdit(self.widget_2)
        self.EDITORTERMEditor.setObjectName(u"EDITORTERMEditor")
        self.EDITORTERMEditor.setTabStopDistance(32.000000000000000)
        self.EDITORTERMEditor.setFont(QFont('UbuntuMono Nerd Font Mono'))

        self.verticalLayout_6.addWidget(self.EDITORTERMEditor)

        self.TABTERMTabs.addTab(self.widget_2, "")

        self.horizontalLayout_2.addWidget(self.TABTERMTabs)

        self.verticalLayout_3.addWidget(self.frame)

        self.frame_2 = QFrame(Widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setProperty('role', 'status-bar')
        self.frame_2.setProperty('variant', 'default')
        self.frame_2.setProperty('state', 'normal')
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(8, 4, 8, 4)
        self.horizontalLayout_3.setSpacing(6)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)
        i = QIcon()

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        icon_path = _resolve_icon(icon_dirs, os.path.join('icons', 'folder', 'default.svg'), self.theme)
        i.addFile(icon_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.label_2.setPixmap(i.pixmap(QSize(16, 16)))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.statusdir = QLabel(self.frame_2)
        self.statusdir.setObjectName(u"statusdir")
        self.statusdir.setText("./")
        self.statusdir.setStyleSheet("font-size: 12px; font-weight: bold;")
        self.horizontalLayout_3.addWidget(self.statusdir)\

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        icon_path = _resolve_icon(icon_dirs, os.path.join('icons', 'nodes', 'hover.svg'), self.theme)
        i.addFile(icon_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.label_3.setPixmap(i.pixmap(QSize(16, 16)))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.statustopics = QLabel(self.frame_2)
        self.statustopics.setObjectName(u"statustopics")
        self.statustopics.setText("Nodos: 0 / Topics: 0")
        self.statustopics.setStyleSheet("font-size: 12px; font-weight: bold;")
        self.horizontalLayout_3.addWidget(self.statustopics)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addWidget(self.frame_2)
        
        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.retranslateUi(Widget, icon_dirs, theme)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget, icon_dirs, theme):
        new_path = _resolve_icon(icon_dirs, os.path.join('icons', 'new', 'default.svg'), self.theme)
        folder_path = _resolve_icon(icon_dirs, os.path.join('icons', 'folder', 'default.svg'), self.theme)

        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"RQTLL IDE", None))
        ___qtreewidgetitem = self.TREEFILEManage.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Widget", u"Explorador", None))

        __sortingEnabled = self.TREEFILEManage.isSortingEnabled()
        self.TREEFILEManage.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.TREEFILEManage.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("Widget", u"nuevo", None))
        ___qtreewidgetitem1.setIcon(0, QIcon(new_path))
        
        ___qtreewidgetitem2 = self.TREEFILEManage.topLevelItem(1)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("Widget", u"dir", None))
        ___qtreewidgetitem2.setIcon(0, QIcon(folder_path))

        ___qtreewidgetitem3 = ___qtreewidgetitem2.child(0)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("Widget", u"nuevo", None))
        ___qtreewidgetitem3.setIcon(0, QIcon(new_path))
        

        self.TREEFILEManage.setSortingEnabled(__sortingEnabled)

        self.TABCODETabs.setTabText(self.TABCODETabs.indexOf(self.widget), QCoreApplication.translate("Widget", u"archivo", None))
        self.TABTERMTabs.setTabText(self.TABTERMTabs.indexOf(self.widget_2), QCoreApplication.translate("Widget", u"Terminal", None))
    # retranslateUi
