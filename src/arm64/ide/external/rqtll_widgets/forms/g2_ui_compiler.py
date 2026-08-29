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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPlainTextEdit, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QTabWidget, QCompleter,
    QTextEdit, QVBoxLayout, QWidget)
import os

try:
    from ..utils.icon_loader import load_qicon, load_qpixmap, _resolve_icon
    from ..utils.nav import NavButton
    from .g2_ui_compiler_list import message_types
except (ImportError, ValueError):
    import sys
    _parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if _parent not in sys.path:
        sys.path.insert(0, _parent)
    from utils.icon_loader import load_qicon, load_qpixmap, _resolve_icon
    from utils.nav import NavButton
    from g2_ui_compiler_list import message_types

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
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_2.setFixedWidth(350)
        self.verticalLayout_7 = QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_7.addWidget(self.label_4)

        self.BTNROSColcon = QPushButton(self.frame_2)
        self.BTNROSColcon.setObjectName(u"BTNROSColcon")
        icon = QIcon()
        icon_path = _resolve_icon(icon_dirs, os.path.join('icons', 'compile', 'default.svg'), theme=theme)
        icon.addFile(icon_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BTNROSColcon.setIcon(icon)
        self.BTNROSColcon.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.BTNROSColcon.setFixedHeight(32)

        self.verticalLayout_7.addWidget(self.BTNROSColcon)

        self.BTNROSCLean = QPushButton(self.frame_2)
        self.BTNROSCLean.setObjectName(u"BTNROSCLean")
        icon = QIcon()
        icon_path = _resolve_icon(icon_dirs, os.path.join('icons', 'clean', 'click.svg'), theme=theme)
        icon.addFile(icon_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BTNROSCLean.setIcon(icon)
        self.BTNROSCLean.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.BTNROSCLean.setFixedHeight(32)

        self.verticalLayout_7.addWidget(self.BTNROSCLean)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_5)

        self.line_2 = QFrame(self.frame_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_7.addWidget(self.line_2)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_7.addWidget(self.label_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.EDITROSPlay = QLineEdit(self.frame_2)
        self.EDITROSPlay.setObjectName(u"EDITROSPlay")

        self.horizontalLayout_3.addWidget(self.EDITROSPlay)

        self.BTNROSPlayDir = QPushButton(self.frame_2)
        self.BTNROSPlayDir.setObjectName(u"BTNROSPlayDir")
        icon = QIcon()
        icon_path = _resolve_icon(icon_dirs, os.path.join('icons', 'folder', 'default.svg'), theme=theme)
        icon.addFile(icon_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BTNROSPlayDir.setIcon(icon)
        self.BTNROSPlayDir.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.BTNROSPlayDir.setFixedSize(QSize(32, 32))
        self.horizontalLayout_3.addWidget(self.BTNROSPlayDir)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)

        self.BTNROSBag = QPushButton(self.frame_2)
        self.BTNROSBag.setObjectName(u"BTNROSBag")
        icon = QIcon()
        icon_path = _resolve_icon(icon_dirs, os.path.join('icons', 'record', 'default.svg'), theme=theme)
        icon.addFile(icon_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BTNROSBag.setIcon(icon)
        self.BTNROSBag.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.BTNROSBag.setFixedHeight(32)

        self.verticalLayout_7.addWidget(self.BTNROSBag)

        self.BTNROSPlay = QPushButton(self.frame_2)
        self.BTNROSPlay.setObjectName(u"BTNROSPlay")
        icon = QIcon()
        icon_path = _resolve_icon(icon_dirs, os.path.join('icons', 'play', 'default.svg'), theme=theme)
        icon.addFile(icon_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BTNROSPlay.setIcon(icon)
        self.BTNROSPlay.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.BTNROSPlay.setFixedHeight(32)
        self.verticalLayout_7.addWidget(self.BTNROSPlay)

        self.verticalSpacer = QSpacerItem(20, 108, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.line_5 = QFrame(self.frame_2)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_7.addWidget(self.line_5)

        self.scrollArea_4 = QScrollArea(self.frame_2)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 317, 430))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_1 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_1.setObjectName(u"label_1")

        self.verticalLayout_5.addWidget(self.label_1)

        self.LAYOUTNodes = QGridLayout()
        self.LAYOUTNodes.setObjectName(u"LAYOUTNodes")
        self.LABELNode1 = QLabel(self.scrollAreaWidgetContents_4)
        self.LABELNode1.setObjectName(u"LABELNode1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.LABELNode1.sizePolicy().hasHeightForWidth())
        self.LABELNode1.setSizePolicy(sizePolicy1)

        self.LAYOUTNodes.addWidget(self.LABELNode1, 0, 0, 1, 1)

        self.BTNNode_1 = QPushButton(self.scrollAreaWidgetContents_4)
        self.BTNNode_1.setObjectName(u"BTNNode_1")
        icon = QIcon()
        icon_path = _resolve_icon(icon_dirs, os.path.join('icons', 'run', 'default.svg'), theme=theme)
        icon.addFile(icon_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BTNNode_1.setIcon(icon)
        self.BTNNode_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.BTNNode_1.setFixedSize(QSize(32, 32))

        self.LAYOUTNodes.addWidget(self.BTNNode_1, 0, 1, 1, 1)


        self.verticalLayout_5.addLayout(self.LAYOUTNodes)

        self.line = QFrame(self.scrollAreaWidgetContents_4)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_5.addWidget(self.line)

        self.label_2 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_5.addWidget(self.label_2)

        self.LAYOUTLanchers = QGridLayout()
        self.LAYOUTLanchers.setObjectName(u"LAYOUTLanchers")
        self.LABELLaunch1 = QLabel(self.scrollAreaWidgetContents_4)
        self.LABELLaunch1.setObjectName(u"LABELLaunch1")
        sizePolicy1.setHeightForWidth(self.LABELLaunch1.sizePolicy().hasHeightForWidth())
        self.LABELLaunch1.setSizePolicy(sizePolicy1)

        self.LAYOUTLanchers.addWidget(self.LABELLaunch1, 0, 0, 1, 1)

        self.BTNLaunch_1 = QPushButton(self.scrollAreaWidgetContents_4)
        self.BTNLaunch_1.setObjectName(u"BTNLaunch_1")
        icon = QIcon()
        icon_path = _resolve_icon(icon_dirs, os.path.join('icons', 'run', 'default.svg'), theme=theme)
        icon.addFile(icon_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BTNLaunch_1.setIcon(icon)
        self.BTNLaunch_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.BTNLaunch_1.setFixedSize(QSize(32, 32))

        self.LAYOUTLanchers.addWidget(self.BTNLaunch_1, 0, 1, 1, 1)


        self.verticalLayout_5.addLayout(self.LAYOUTLanchers)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_7.addWidget(self.scrollArea_4)


        self.horizontalLayout_4.addWidget(self.frame_2)

        self.line_4 = QFrame(self.frame)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_4.addWidget(self.line_4)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_3.setFixedWidth(425)
        self.verticalLayout_9 = QVBoxLayout(self.frame_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_3 = QScrollArea(self.frame_3)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 383, 818))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.line_3 = QFrame(self.scrollAreaWidgetContents_3)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.LAYOUTTopic1_2 = QHBoxLayout()
        self.LAYOUTTopic1_2.setObjectName(u"LAYOUTTopic1_2")
        self.EDITNEWTopic = QLineEdit(self.scrollAreaWidgetContents_3)
        self.EDITNEWTopic.setObjectName(u"EDITNEWTopic")

        self.LAYOUTTopic1_2.addWidget(self.EDITNEWTopic)

        self.BTNPUBConfig = QPushButton(self.scrollAreaWidgetContents_3)
        self.BTNPUBConfig.setObjectName(u"BTNPUBConfig")
        icon = QIcon()
        icon_path = _resolve_icon(icon_dirs, os.path.join('icons', 'settings', 'default.svg'), theme=theme)
        icon.addFile(icon_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BTNPUBConfig.setIcon(icon)
        self.BTNPUBConfig.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.BTNPUBConfig.setFixedSize(QSize(32, 32))

        self.LAYOUTTopic1_2.addWidget(self.BTNPUBConfig)


        self.verticalLayout.addLayout(self.LAYOUTTopic1_2)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_8 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_5.addWidget(self.label_8)

        self.EDITMSGType = QLineEdit(self.scrollAreaWidgetContents_3)
        self.EDITMSGType.setObjectName(u"EDITMSGType")
        self.completer = QCompleter(message_types)
        self.completer.setFilterMode(Qt.MatchContains)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.EDITMSGType.setCompleter(self.completer)
        self.horizontalLayout_5.addWidget(self.EDITMSGType)


        self.verticalLayout_8.addLayout(self.horizontalLayout_5)

        self.label_10 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_8.addWidget(self.label_10)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_9 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_6.addWidget(self.label_9)

        self.BTNMSGDir = QPushButton(self.scrollAreaWidgetContents_3)
        self.BTNMSGDir.setObjectName(u"BTNMSGDir")
        icon = QIcon()
        icon_path = _resolve_icon(icon_dirs, os.path.join('icons', 'folder', 'default.svg'), theme=theme)
        icon.addFile(icon_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BTNMSGDir.setIcon(icon)
        self.BTNMSGDir.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.BTNMSGDir.setFixedSize(QSize(32, 32))

        self.horizontalLayout_6.addWidget(self.BTNMSGDir)


        self.verticalLayout_8.addLayout(self.horizontalLayout_6)

        self.EDITMSGContent = QPlainTextEdit(self.scrollAreaWidgetContents_3)
        self.EDITMSGContent.setObjectName(u"EDITMSGContent")

        self.verticalLayout_8.addWidget(self.EDITMSGContent)

        self.BTNPUBTopic = QPushButton(self.scrollAreaWidgetContents_3)
        self.BTNPUBTopic.setObjectName(u"BTNPUBTopic")
        icon = QIcon()
        icon_path = _resolve_icon(icon_dirs, os.path.join('icons', 'new', 'default.svg'), theme=theme)
        icon.addFile(icon_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BTNPUBTopic.setIcon(icon)
        self.BTNPUBTopic.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.BTNPUBTopic.setFixedHeight(32)

        self.verticalLayout_8.addWidget(self.BTNPUBTopic)


        self.verticalLayout.addLayout(self.verticalLayout_8)

        self.line_6 = QFrame(self.scrollAreaWidgetContents_3)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_6)

        self.LAYOUTTopic1 = QHBoxLayout()
        self.LAYOUTTopic1.setObjectName(u"LAYOUTTopic1")
        self.LABELTopic_1 = QLabel(self.scrollAreaWidgetContents_3)
        self.LABELTopic_1.setObjectName(u"LABELTopic_1")
        sizePolicy1.setHeightForWidth(self.LABELTopic_1.sizePolicy().hasHeightForWidth())
        self.LABELTopic_1.setSizePolicy(sizePolicy1)

        self.LAYOUTTopic1.addWidget(self.LABELTopic_1)

        self.BTNECHOTopic_1 = QPushButton(self.scrollAreaWidgetContents_3)
        self.BTNECHOTopic_1.setObjectName(u"BTNECHOTopic_1")
        icon1 = QIcon()
        icon1_path = _resolve_icon(icon_dirs, os.path.join('icons', 'arrows', 'down.svg'), theme=theme)
        icon1.addFile(icon1_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BTNECHOTopic_1.setIcon(icon1)
        self.BTNECHOTopic_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.BTNECHOTopic_1.setFixedSize(QSize(32, 32))

        self.LAYOUTTopic1.addWidget(self.BTNECHOTopic_1)

        self.BTNPUBConfig_1 = QPushButton(self.scrollAreaWidgetContents_3)
        self.BTNPUBConfig_1.setObjectName(u"BTNPUBConfig_1")
        icon2 = QIcon()
        icon2_path = _resolve_icon(icon_dirs, os.path.join('icons', 'settings', 'default.svg'), theme=theme)
        icon2.addFile(icon2_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BTNPUBConfig_1.setIcon(icon2)
        self.BTNPUBConfig_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.BTNPUBConfig_1.setFixedSize(QSize(32, 32))

        self.LAYOUTTopic1.addWidget(self.BTNPUBConfig_1)


        self.verticalLayout.addLayout(self.LAYOUTTopic1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.scrollAreaWidgetContents_3)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.EDITMSGType_1 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.EDITMSGType_1.setObjectName(u"EDITMSGType_1")
        self.completer = QCompleter(message_types)
        self.completer.setFilterMode(Qt.MatchContains)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.EDITMSGType_1.setCompleter(self.completer)

        self.horizontalLayout_2.addWidget(self.EDITMSGType_1)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.label_11 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_6.addWidget(self.label_11)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_7 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_8.addWidget(self.label_7)

        self.BTNMSGDir_1 = QPushButton(self.scrollAreaWidgetContents_3)
        self.BTNMSGDir_1.setObjectName(u"BTNMSGDir_1")
        icon3 = QIcon()
        icon3_path = _resolve_icon(icon_dirs, os.path.join('icons', 'folder', 'default.svg'), theme=theme)
        icon3.addFile(icon3_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BTNMSGDir_1.setIcon(icon3)
        self.BTNMSGDir_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.BTNMSGDir_1.setFixedSize(QSize(32, 32))

        self.horizontalLayout_8.addWidget(self.BTNMSGDir_1)


        self.verticalLayout_6.addLayout(self.horizontalLayout_8)

        self.EDITMSGContent_1 = QPlainTextEdit(self.scrollAreaWidgetContents_3)
        self.EDITMSGContent_1.setObjectName(u"EDITMSGContent_1")

        self.verticalLayout_6.addWidget(self.EDITMSGContent_1)

        self.BTNPUBTopic_1 = QPushButton(self.scrollAreaWidgetContents_3)
        self.BTNPUBTopic_1.setObjectName(u"BTNPUBTopic_1")
        icon4 = QIcon()
        icon4_path = _resolve_icon(icon_dirs, os.path.join('icons', 'arrows', 'up.svg'), theme=theme)
        icon4.addFile(icon4_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BTNPUBTopic_1.setIcon(icon4)
        self.BTNPUBTopic_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.BTNPUBTopic_1.setFixedHeight(32)

        self.verticalLayout_6.addWidget(self.BTNPUBTopic_1)


        self.verticalLayout.addLayout(self.verticalLayout_6)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_9.addWidget(self.scrollArea_3)


        self.horizontalLayout_4.addWidget(self.frame_3)

        self.tabWidget = QTabWidget(self.frame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_4 = QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.textEdit = QTextEdit(self.tab)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy2)
        self.textEdit.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)
        self.textEdit.setOverwriteMode(False)

        self.verticalLayout_4.addWidget(self.textEdit)

        self.LABELInfo = QLabel(self.tab)
        self.LABELInfo.setObjectName(u"LABELInfo")

        self.verticalLayout_4.addWidget(self.LABELInfo)

        self.tabWidget.addTab(self.tab, "")

        self.horizontalLayout_4.addWidget(self.tabWidget)

        self.verticalLayout_3.addWidget(self.frame)

        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"RQTLL IDE", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"Colcon", None))
        self.BTNROSColcon.setText(QCoreApplication.translate("Widget", u"Compilar", None))
        self.BTNROSCLean.setText(QCoreApplication.translate("Widget", u"Limpiar", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"Rosbags", None))
        self.BTNROSBag.setText(QCoreApplication.translate("Widget", u"Grabar", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"Ubicaci\u00f3n:", None))
        self.BTNROSPlayDir.setText(QCoreApplication.translate("Widget", u"", None))
        self.BTNROSPlay.setText(QCoreApplication.translate("Widget", u"Reproducir", None))
        self.label_1.setText(QCoreApplication.translate("Widget", u"Nodos", None))
        self.LABELNode1.setText(QCoreApplication.translate("Widget", u"minimal_publisher", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Lanzadores", None))
        self.LABELLaunch1.setText(QCoreApplication.translate("Widget", u"simple_robot_launcher", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"T\u00f3picos", None))
        self.EDITNEWTopic.setPlaceholderText(QCoreApplication.translate("Widget", u"Nuevo t\u00f3pico", None))
        self.label_8.setText(QCoreApplication.translate("Widget", u"Tipo de mensaje:", None))
        self.EDITMSGType.setPlaceholderText(QCoreApplication.translate("Widget", u"Ej. std_msgs/String", None))
        self.label_10.setText(QCoreApplication.translate("Widget", u"Mensaje", None))
        self.label_9.setText(QCoreApplication.translate("Widget", u"Importar archivo (opcional):", None))
        self.BTNPUBTopic.setText(QCoreApplication.translate("Widget", u"Crear t\u00f3pico", None))
        self.LABELTopic_1.setText(QCoreApplication.translate("Widget", u"/topic1", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Tipo de mensaje:", None))
        self.EDITMSGType_1.setPlaceholderText(QCoreApplication.translate("Widget", u"Ej. std_msgs/String", None))
        self.label_11.setText(QCoreApplication.translate("Widget", u"Mensaje", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"Importar archivo (opcional):", None))
        self.BTNPUBTopic_1.setText(QCoreApplication.translate("Widget", u"Publicar mensaje", None))
        self.LABELInfo.setText(QCoreApplication.translate("Widget", u"Bandwidth: 0 B/s \t\tPublicadores: 0\nFrecuencia: 0 hz\t\tSuscriptores: 0\nTipo: none", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Widget", u"Tab 1", None))
    # retranslateUi
