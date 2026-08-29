# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame,
    QGroupBox, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)
import os
import re

try:
    from ..utils.icon_loader import load_qicon, load_qpixmap, _resolve_icon
    from ..utils.name_utils import sanitize_item_name
    from ..utils.removable_item import RemovableItemWidget
except (ImportError, ValueError):
    import sys
    _parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if _parent not in sys.path:
        sys.path.insert(0, _parent)
    from utils.icon_loader import load_qicon, load_qpixmap, _resolve_icon
    from utils.name_utils import sanitize_item_name
    from utils.removable_item import RemovableItemWidget

placeholder = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'icons', 'placeholder.svg'))

class Ui_Widget(object):
    def setupUi(self, Widget, icon_dirs=None, theme: str = 'default.qss'):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(810, 870)
        self.theme = theme
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        Widget.setMinimumSize(QSize(810, 870))
        icon = QIcon()
        icon_path = _resolve_icon(icon_dirs, os.path.join('logo.svg'), theme=self.theme)
        icon.addFile(icon_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.verticalLayout_17 = QVBoxLayout(Widget)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.LABELWSNew = QLabel(Widget)
        self.LABELWSNew.setObjectName(u"LABELWSNew")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.LABELWSNew.sizePolicy().hasHeightForWidth())
        self.LABELWSNew.setSizePolicy(sizePolicy1)

        self.horizontalLayout_10.addWidget(self.LABELWSNew)

        self.EDITWSNew = QLineEdit(Widget)
        self.EDITWSNew.setObjectName(u"EDITWSNew")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.EDITWSNew.sizePolicy().hasHeightForWidth())
        self.EDITWSNew.setSizePolicy(sizePolicy2)
        self.EDITWSNew.setClearButtonEnabled(False)

        self.horizontalLayout_10.addWidget(self.EDITWSNew)
        
        self.LABELDir = QLabel(Widget)
        self.LABELDir.setObjectName(u"LABELDir")
        sizePolicy13 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.LABELDir.sizePolicy().hasHeightForWidth())
        self.LABELDir.setSizePolicy(sizePolicy13)

        self.EDITDir = QLineEdit(Widget)
        self.EDITDir.setObjectName(u"EDITDir")
        sizePolicy14 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy14.setHorizontalStretch(0)
        sizePolicy14.setVerticalStretch(0)
        sizePolicy14.setHeightForWidth(self.EDITDir.sizePolicy().hasHeightForWidth())
        self.EDITDir.setSizePolicy(sizePolicy14)

        self.BTNDir = QPushButton(Widget)
        self.BTNDir.setObjectName(u"BTNDir")
        icon1 = QIcon()
        icon1_path = _resolve_icon(icon_dirs, os.path.join('folder', 'default.svg'), theme=theme)
        icon1.addFile(icon1_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BTNDir.setIcon(icon1)
        self.BTNDir.setCursor(QCursor(Qt.CursorShape.PointingHandCursor)) 
        
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.addWidget(self.LABELDir)
        self.horizontalLayout_9.addWidget(self.EDITDir)
        self.horizontalLayout_9.addWidget(self.BTNDir)


        self.verticalLayout_17.addLayout(self.horizontalLayout_9)
        self.verticalLayout_17.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.LABELPKGNew = QLabel(Widget)
        self.LABELPKGNew.setObjectName(u"LABELPKGNew")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.LABELPKGNew.sizePolicy().hasHeightForWidth())
        self.LABELPKGNew.setSizePolicy(sizePolicy3)

        self.horizontalLayout_8.addWidget(self.LABELPKGNew)

        self.EDITPKGNew = QLineEdit(Widget)
        self.EDITPKGNew.setObjectName(u"EDITPKGNew")
        sizePolicy2.setHeightForWidth(self.EDITPKGNew.sizePolicy().hasHeightForWidth())
        self.EDITPKGNew.setSizePolicy(sizePolicy2)

        self.horizontalLayout_8.addWidget(self.EDITPKGNew)

        self.BTNPKGNew = QPushButton(Widget)
        self.BTNPKGNew.setObjectName(u"BTNPKGNew")
        icon1 = QIcon()
        icon1_path = _resolve_icon(icon_dirs, os.path.join('new', 'default.svg'), theme=self.theme)
        icon1.addFile(icon1_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BTNPKGNew.setIcon(icon1)
        self.BTNPKGNew.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_8.addWidget(self.BTNPKGNew)


        self.verticalLayout_17.addLayout(self.horizontalLayout_8)

        self.TABPKGNew = QTabWidget(Widget)
        self.TABPKGNew.setObjectName(u"TABPKGNew")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.TABPKGNew.sizePolicy().hasHeightForWidth())
        self.TABPKGNew.setSizePolicy(sizePolicy4)
        self.TAB_my_pkg = QWidget()
        self.TAB_my_pkg.setProperty('role', 'in-tab')
        self.TAB_my_pkg.setProperty('variant', 'default')
        self.TAB_my_pkg.setProperty('state', 'normal')
        self.TAB_my_pkg.setObjectName(u"TAB_my_pkg")
        self.verticalLayout_4 = QVBoxLayout(self.TAB_my_pkg)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.LABELPKGInfo = QLabel(self.TAB_my_pkg)
        self.LABELPKGInfo.setObjectName(u"LABELPKGInfo")

        self.horizontalLayout.addWidget(self.LABELPKGInfo)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.BTNDel_my_pkg = QPushButton(self.TAB_my_pkg)
        self.BTNDel_my_pkg.setObjectName(u"BTNDel_my_pkg")
        icon_del_pkg = QIcon()
        icon_del_pkg_path = _resolve_icon(icon_dirs, os.path.join('close', 'default.svg'), theme=self.theme)
        icon_del_pkg.addFile(icon_del_pkg_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BTNDel_my_pkg.setIcon(icon_del_pkg)
        self.BTNDel_my_pkg.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.BTNDel_my_pkg.setProperty('role', 'close')
        self.BTNDel_my_pkg.setProperty('variant', 'default')
        self.BTNDel_my_pkg.setProperty('state', 'normal')

        self.horizontalLayout.addWidget(self.BTNDel_my_pkg)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.scrollArea = QScrollArea(self.TAB_my_pkg)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy5)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -68, 725, 486))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.LABELPKGDescription = QLabel(self.scrollAreaWidgetContents)
        self.LABELPKGDescription.setObjectName(u"LABELPKGDescription")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.LABELPKGDescription.sizePolicy().hasHeightForWidth())
        self.LABELPKGDescription.setSizePolicy(sizePolicy6)
        self.LABELPKGDescription.setWordWrap(True)

        self.horizontalLayout_15.addWidget(self.LABELPKGDescription)

        self.EDITPKGDescription = QLineEdit(self.scrollAreaWidgetContents)
        self.EDITPKGDescription.setObjectName(u"EDITPKGDescription")

        self.horizontalLayout_15.addWidget(self.EDITPKGDescription)

        self.LABELPKGLicense = QLabel(self.scrollAreaWidgetContents)
        self.LABELPKGLicense.setObjectName(u"LABELPKGLicense")
        sizePolicy6.setHeightForWidth(self.LABELPKGLicense.sizePolicy().hasHeightForWidth())
        self.LABELPKGLicense.setSizePolicy(sizePolicy6)
        self.LABELPKGLicense.setWordWrap(True)

        self.horizontalLayout_15.addWidget(self.LABELPKGLicense)

        self.CBPKGLicense = QComboBox(self.scrollAreaWidgetContents)
        self.CBPKGLicense.addItem("")
        self.CBPKGLicense.addItem("")
        self.CBPKGLicense.addItem("")
        self.CBPKGLicense.addItem("")
        self.CBPKGLicense.addItem("")
        self.CBPKGLicense.addItem("")
        self.CBPKGLicense.addItem("")
        self.CBPKGLicense.addItem("")
        self.CBPKGLicense.addItem("")
        self.CBPKGLicense.setObjectName(u"CBPKGLicense")
        self.CBPKGLicense.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        arrow_down_icon = load_qicon(os.path.join('arrows', 'down.svg'), icon_dirs)
        arrow_up_icon = load_qicon(os.path.join('arrows', 'up.svg'), icon_dirs)
        if not arrow_down_icon.isNull() and not arrow_up_icon.isNull():
            self.CBPKGLicense.setStyleSheet(f"""
                QComboBox::down-arrow {{ image: url({_resolve_icon(icon_dirs, os.path.join('arrows', 'down.svg'))}); }}
                QComboBox::up-arrow {{ image: url({_resolve_icon(icon_dirs, os.path.join('arrows', 'up.svg'))}); }}
            """)
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.CBPKGLicense.sizePolicy().hasHeightForWidth())
        self.CBPKGLicense.setSizePolicy(sizePolicy7)

        self.horizontalLayout_15.addWidget(self.CBPKGLicense)


        self.verticalLayout_2.addLayout(self.horizontalLayout_15)

        self.GROUPPKGConf = QGroupBox(self.scrollAreaWidgetContents)
        self.GROUPPKGConf.setObjectName(u"GROUPPKGConf")
        sizePolicy6.setHeightForWidth(self.GROUPPKGConf.sizePolicy().hasHeightForWidth())
        self.GROUPPKGConf.setSizePolicy(sizePolicy6)
        self.horizontalLayout_5 = QHBoxLayout(self.GROUPPKGConf)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame = QFrame(self.GROUPPKGConf)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.LABELPKGAment = QLabel(self.frame)
        self.LABELPKGAment.setObjectName(u"LABELPKGAment")
        sizePolicy1.setHeightForWidth(self.LABELPKGAment.sizePolicy().hasHeightForWidth())
        self.LABELPKGAment.setSizePolicy(sizePolicy1)
        self.LABELPKGAment.setWordWrap(True)

        self.horizontalLayout_7.addWidget(self.LABELPKGAment)

        self.CBPKGAment = QComboBox(self.frame)
        self.CBPKGAment.addItem("")
        self.CBPKGAment.addItem("")
        self.CBPKGAment.addItem("")
        self.CBPKGAment.setObjectName(u"CBPKGAment")
        self.CBPKGAment.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        if not arrow_down_icon.isNull() and not arrow_up_icon.isNull():
            self.CBPKGAment.setStyleSheet(f"""
                QComboBox::down-arrow {{ image: url({_resolve_icon(icon_dirs, os.path.join('arrows', 'down.svg'))}); }}
                QComboBox::up-arrow {{ image: url({_resolve_icon(icon_dirs, os.path.join('arrows', 'up.svg'))}); }}
            """)
        sizePolicy2.setHeightForWidth(self.CBPKGAment.sizePolicy().hasHeightForWidth())
        self.CBPKGAment.setSizePolicy(sizePolicy2)

        self.horizontalLayout_7.addWidget(self.CBPKGAment)


        self.verticalLayout_5.addLayout(self.horizontalLayout_7)

        self.INFOPKGAment = QLabel(self.frame)
        self.INFOPKGAment.setObjectName(u"INFOPKGAment")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.INFOPKGAment.sizePolicy().hasHeightForWidth())
        self.INFOPKGAment.setSizePolicy(sizePolicy8)
        font = QFont()
        font.setItalic(True)
        self.INFOPKGAment.setFont(font)
        self.INFOPKGAment.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.INFOPKGAment)


        self.horizontalLayout_5.addWidget(self.frame)

        self.frame_2 = QFrame(self.GROUPPKGConf)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.LABELProjectVer = QLabel(self.frame_2)
        self.LABELProjectVer.setObjectName(u"LABELProjectVer")
        sizePolicy3.setHeightForWidth(self.LABELProjectVer.sizePolicy().hasHeightForWidth())
        self.LABELProjectVer.setSizePolicy(sizePolicy3)
        self.LABELProjectVer.setWordWrap(True)

        self.horizontalLayout_6.addWidget(self.LABELProjectVer)

        self.EDITProjectVer = QLineEdit(self.frame_2)
        self.EDITProjectVer.setObjectName(u"EDITProjectVer")

        self.horizontalLayout_6.addWidget(self.EDITProjectVer)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)

        self.INFOProjectVer = QLabel(self.frame_2)
        self.INFOProjectVer.setObjectName(u"INFOProjectVer")
        sizePolicy3.setHeightForWidth(self.INFOProjectVer.sizePolicy().hasHeightForWidth())
        self.INFOProjectVer.setSizePolicy(sizePolicy3)
        self.INFOProjectVer.setFont(font)
        self.INFOProjectVer.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.INFOProjectVer)


        self.horizontalLayout_5.addWidget(self.frame_2)


        self.verticalLayout_2.addWidget(self.GROUPPKGConf)

        self.GROUPMainteiner = QGroupBox(self.scrollAreaWidgetContents)
        self.GROUPMainteiner.setObjectName(u"GROUPMainteiner")
        sizePolicy6.setHeightForWidth(self.GROUPMainteiner.sizePolicy().hasHeightForWidth())
        self.GROUPMainteiner.setSizePolicy(sizePolicy6)
        self.verticalLayout_12 = QVBoxLayout(self.GROUPMainteiner)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.LABELMAINTName = QLabel(self.GROUPMainteiner)
        self.LABELMAINTName.setObjectName(u"LABELMAINTName")
        self.LABELMAINTName.setWordWrap(True)

        self.horizontalLayout_11.addWidget(self.LABELMAINTName)

        self.EDITMAINTName = QLineEdit(self.GROUPMainteiner)
        self.EDITMAINTName.setObjectName(u"EDITMAINTName")

        self.horizontalLayout_11.addWidget(self.EDITMAINTName)

        self.LABELMAINTEmail = QLabel(self.GROUPMainteiner)
        self.LABELMAINTEmail.setObjectName(u"LABELMAINTEmail")
        self.LABELMAINTEmail.setWordWrap(True)

        self.horizontalLayout_11.addWidget(self.LABELMAINTEmail)

        self.EDITMAINTEmail = QLineEdit(self.GROUPMainteiner)
        self.EDITMAINTEmail.setObjectName(u"EDITMAINTEmail")

        self.horizontalLayout_11.addWidget(self.EDITMAINTEmail)


        self.verticalLayout_12.addLayout(self.horizontalLayout_11)


        self.verticalLayout_2.addWidget(self.GROUPMainteiner)

        self.GROUPConf = QGroupBox(self.scrollAreaWidgetContents)
        self.GROUPConf.setObjectName(u"GROUPConf")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.GROUPConf.sizePolicy().hasHeightForWidth())
        self.GROUPConf.setSizePolicy(sizePolicy9)
        self.verticalLayout_8 = QVBoxLayout(self.GROUPConf)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.LABELPKGDir = QLabel(self.GROUPConf)
        self.LABELPKGDir.setObjectName(u"LABELPKGDir")
        sizePolicy1.setHeightForWidth(self.LABELPKGDir.sizePolicy().hasHeightForWidth())
        self.LABELPKGDir.setSizePolicy(sizePolicy1)
        self.LABELPKGDir.setWordWrap(True)

        self.horizontalLayout_12.addWidget(self.LABELPKGDir)

        self.EDITPKGDir = QLineEdit(self.GROUPConf)
        self.EDITPKGDir.setObjectName(u"EDITPKGDir")
        sizePolicy4.setHeightForWidth(self.EDITPKGDir.sizePolicy().hasHeightForWidth())
        self.EDITPKGDir.setSizePolicy(sizePolicy4)

        self.horizontalLayout_12.addWidget(self.EDITPKGDir)


        self.verticalLayout_8.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.LABELPKGApts = QLabel(self.GROUPConf)
        self.LABELPKGApts.setObjectName(u"LABELPKGApts")
        sizePolicy6.setHeightForWidth(self.LABELPKGApts.sizePolicy().hasHeightForWidth())
        self.LABELPKGApts.setSizePolicy(sizePolicy6)
        self.LABELPKGApts.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.LABELPKGApts.setWordWrap(True)

        self.horizontalLayout_13.addWidget(self.LABELPKGApts)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.EDITPKGApts = QLineEdit(self.GROUPConf)
        self.EDITPKGApts.setObjectName(u"EDITPKGApts")

        self.horizontalLayout_13.addWidget(self.EDITPKGApts)

        self.verticalLayout_8.addLayout(self.horizontalLayout_13)


        self.verticalLayout_2.addWidget(self.GROUPConf)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.GROUPNode = QGroupBox(self.TAB_my_pkg)
        self.GROUPNode.setObjectName(u"GROUPNode")
        sizePolicy12 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.GROUPNode.sizePolicy().hasHeightForWidth())
        self.GROUPNode.setSizePolicy(sizePolicy12)
        self.verticalLayout_10 = QVBoxLayout(self.GROUPNode)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.EDITNODENew = QLineEdit(self.GROUPNode)
        self.EDITNODENew.setObjectName(u"EDITNODENew")
        sizePolicy2.setHeightForWidth(self.EDITNODENew.sizePolicy().hasHeightForWidth())
        self.EDITNODENew.setSizePolicy(sizePolicy2)
        self.EDITNODENew.setPlaceholderText("new_node")

        self.horizontalLayout_16.addWidget(self.EDITNODENew)

        self.CBNODENew = QComboBox(self.GROUPNode)
        self.CBNODENew.addItem("")
        self.CBNODENew.addItem("")
        self.CBNODENew.setObjectName(u"CBNODENew")
        self.CBNODENew.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        if not arrow_down_icon.isNull() and not arrow_up_icon.isNull():
            self.CBNODENew.setStyleSheet(f"""
                QComboBox::down-arrow {{ image: url({_resolve_icon(icon_dirs, os.path.join('arrows', 'down.svg'))}); }}
                QComboBox::up-arrow {{ image: url({_resolve_icon(icon_dirs, os.path.join('arrows', 'up.svg'))}); }}
            """)

        self.horizontalLayout_16.addWidget(self.CBNODENew)

        self.BTNNODENew = QPushButton(self.GROUPNode)
        self.BTNNODENew.setObjectName(u"BTNNODENew")
        self.BTNNODENew.setIcon(icon1)
        self.BTNNODENew.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_16.addWidget(self.BTNNODENew)


        self.verticalLayout_10.addLayout(self.horizontalLayout_16)

        self.FRAMENODEAdded = QScrollArea(self.GROUPNode)
        self.FRAMENODEAdded.setObjectName(u"FRAMENODEAdded")
        sizePolicy4.setHeightForWidth(self.FRAMENODEAdded.sizePolicy().hasHeightForWidth())
        self.FRAMENODEAdded.setSizePolicy(sizePolicy4)
        self.FRAMENODEAdded.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 340, 101))
        sizePolicy12 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.scrollAreaWidgetContents_2.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_2.setSizePolicy(sizePolicy12)
        self.verticalLayout_16 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setSpacing(0)
        self.FRAMENODEAdded.setProperty('role', 'node-list')
        self.FRAMENODEAdded.setProperty('variant', 'default')
        self.FRAMENODEAdded.setProperty('state', 'normal')
        self.scrollAreaWidgetContents_2.setProperty('role', 'node-scroll')
        self.scrollAreaWidgetContents_2.setProperty('variant', 'default')
        self.scrollAreaWidgetContents_2.setProperty('state', 'normal')
        # try RemovableItemWidget for node entries
        try:
            self.LAYOUTNODEAdded = QHBoxLayout()
            self.LAYOUTNODEAdded.setObjectName(u"LAYOUTNODEAdded")
        except Exception:
            self.LAYOUTNODEAdded = QHBoxLayout()
            self.LAYOUTNODEAdded.setObjectName(u"LAYOUTNODEAdded")
            self.LABELNODEAdded = QLabel(self.scrollAreaWidgetContents_2)
            self.LABELNODEAdded.setObjectName(u"LABELNODEAdded")
            sizePolicy11.setHeightForWidth(self.LABELNODEAdded.sizePolicy().hasHeightForWidth())
            self.LABELNODEAdded.setSizePolicy(sizePolicy11)

            self.LAYOUTNODEAdded.addWidget(self.LABELNODEAdded)

            self.BTNNODEAdded = QPushButton(self.scrollAreaWidgetContents_2)
            self.BTNNODEAdded.setObjectName(u"BTNNODEAdded")
            self.BTNNODEAdded.setIcon(icon3)
            self.BTNNODEAdded.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

            self.LAYOUTNODEAdded.addWidget(self.BTNNODEAdded)

            self.verticalLayout_16.addLayout(self.LAYOUTNODEAdded)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_2)

        self.FRAMENODEAdded.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_10.addWidget(self.FRAMENODEAdded)


        self.horizontalLayout_26.addWidget(self.GROUPNode)

        self.GROUPLaunch = QGroupBox(self.TAB_my_pkg)
        self.GROUPLaunch.setObjectName(u"GROUPLaunch")
        self.verticalLayout_15 = QVBoxLayout(self.GROUPLaunch)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.EDITLAUNCHNew = QLineEdit(self.GROUPLaunch)
        self.EDITLAUNCHNew.setObjectName(u"EDITLAUNCHNew")
        sizePolicy2.setHeightForWidth(self.EDITLAUNCHNew.sizePolicy().hasHeightForWidth())
        self.EDITLAUNCHNew.setSizePolicy(sizePolicy2)
        self.EDITLAUNCHNew.setPlaceholderText("new_launch")

        self.horizontalLayout_17.addWidget(self.EDITLAUNCHNew)

        self.CBLAUNCHNew = QComboBox(self.GROUPLaunch)
        self.CBLAUNCHNew.addItem("")
        self.CBLAUNCHNew.addItem("")
        self.CBLAUNCHNew.addItem("")
        self.CBLAUNCHNew.setObjectName(u"CBLAUNCHNew")
        self.CBLAUNCHNew.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        if not arrow_down_icon.isNull() and not arrow_up_icon.isNull():
            self.CBLAUNCHNew.setStyleSheet(f"""
                QComboBox::down-arrow {{ image: url({_resolve_icon(icon_dirs, os.path.join('arrows', 'down.svg'))}); }}
                QComboBox::up-arrow {{ image: url({_resolve_icon(icon_dirs, os.path.join('arrows', 'up.svg'))}); }}
            """)

        self.horizontalLayout_17.addWidget(self.CBLAUNCHNew)

        self.BTNLAUNCHNew = QPushButton(self.GROUPLaunch)
        self.BTNLAUNCHNew.setObjectName(u"BTNLAUNCHNew")
        self.BTNLAUNCHNew.setIcon(icon1)
        self.BTNLAUNCHNew.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_17.addWidget(self.BTNLAUNCHNew)


        self.verticalLayout_15.addLayout(self.horizontalLayout_17)

        self.FRAMELAUNCHAdd = QScrollArea(self.GROUPLaunch)
        self.FRAMELAUNCHAdd.setObjectName(u"FRAMELAUNCHAdd")
        sizePolicy4.setHeightForWidth(self.FRAMELAUNCHAdd.sizePolicy().hasHeightForWidth())
        self.FRAMELAUNCHAdd.setSizePolicy(sizePolicy4)
        self.FRAMELAUNCHAdd.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 340, 101))
        sizePolicy12.setHeightForWidth(self.scrollAreaWidgetContents_3.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_3.setSizePolicy(sizePolicy12)
        self.verticalLayout_13 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(0)
        self.FRAMELAUNCHAdd.setProperty('role', 'node-list')
        self.FRAMELAUNCHAdd.setProperty('variant', 'default')
        self.FRAMELAUNCHAdd.setProperty('state', 'normal')
        self.scrollAreaWidgetContents_3.setProperty('role', 'node-scroll')
        self.scrollAreaWidgetContents_3.setProperty('variant', 'default')
        self.scrollAreaWidgetContents_3.setProperty('state', 'normal')
        # try RemovableItemWidget for launch entries
        try:
            self.LAYOUTLAUNCHAdded = QHBoxLayout()
            self.LAYOUTLAUNCHAdded.setObjectName(u"LAYOUTLAUNCHAdded")
        except Exception:
            self.LAYOUTLAUNCHAdded = QHBoxLayout()
            self.LAYOUTLAUNCHAdded.setObjectName(u"LAYOUTLAUNCHAdded")
            self.LABELLAUNCHAdded = QLabel(self.scrollAreaWidgetContents_3)
            self.LABELLAUNCHAdded.setObjectName(u"LABELLAUNCHAdded")
            sizePolicy11.setHeightForWidth(self.LABELLAUNCHAdded.sizePolicy().hasHeightForWidth())
            self.LABELLAUNCHAdded.setSizePolicy(sizePolicy11)

            self.LAYOUTLAUNCHAdded.addWidget(self.LABELLAUNCHAdded)

            self.BTNLAUNCHAdded = QPushButton(self.scrollAreaWidgetContents_3)
            self.BTNLAUNCHAdded.setObjectName(u"BTNLAUNCHAdded")
            self.BTNLAUNCHAdded.setIcon(icon3)
            self.BTNLAUNCHAdded.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

            self.LAYOUTLAUNCHAdded.addWidget(self.BTNLAUNCHAdded)

            self.verticalLayout_13.addLayout(self.LAYOUTLAUNCHAdded)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_3)

        self.FRAMELAUNCHAdd.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_15.addWidget(self.FRAMELAUNCHAdd)


        self.horizontalLayout_26.addWidget(self.GROUPLaunch)


        self.verticalLayout_4.addLayout(self.horizontalLayout_26)

        #self.TABPKGNew.addTab(self.TAB_my_pkg, "")

        self.verticalLayout_17.addWidget(self.TABPKGNew)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_2)

        self.BTNMake = QPushButton(Widget)
        self.BTNMake.setObjectName(u"BTNMake")
        self.BTNMake.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_19.addWidget(self.BTNMake)

        self.BTNCancell = QPushButton(Widget)
        self.BTNCancell.setObjectName(u"BTNCancell")
        self.BTNCancell.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_19.addWidget(self.BTNCancell)


        self.verticalLayout_17.addLayout(self.horizontalLayout_19)


        self.retranslateUi(Widget)

        self.TABPKGNew.setCurrentIndex(0)

        # store icon dirs for runtime handlers
        self._icon_dirs = icon_dirs or []

        try:
            self.EDITWSNew.textChanged.connect(self._on_ws_name_changed)
        except Exception:
            pass

        # connect add buttons for nodes and launches to runtime handlers
        try:
            self.BTNNODENew.clicked.connect(self._on_add_node)
        except Exception:
            pass
        try:
            self.BTNLAUNCHNew.clicked.connect(self._on_add_launch)
        except Exception:
            pass
        try:
            self.BTNPKGNew.clicked.connect(self._on_add_pkg)
        except Exception:
            pass
        try:
            self.EDITPKGNew.returnPressed.connect(self._on_add_pkg)
        except Exception:
            pass
        # connect delete-package button to remove its tab from the tabwidget
        try:
            self.BTNDel_my_pkg.clicked.connect(self._on_delete_my_pkg_tab)
        except Exception:
            pass

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"RQTLL IDE / Nuevo espacio de trabajo", None))
        self.LABELWSNew.setText(QCoreApplication.translate("Widget", u"Nombre para el nuevo espacio de trabajo:", None))
        self.EDITWSNew.setPlaceholderText(QCoreApplication.translate("Widget", u"ros2_ws", None))
        self.LABELPKGNew.setText(QCoreApplication.translate("Widget", u"Nombre del paquete a incluir:", None))
        self.EDITPKGNew.setPlaceholderText(QCoreApplication.translate("Widget", u"my_pkg", None))
        self.BTNPKGNew.setText(QCoreApplication.translate("Widget", u"Paquete", None))
        self.LABELPKGInfo.setText(QCoreApplication.translate("Widget", u"Sobre el nuevo paquete", None))
        self.BTNDel_my_pkg.setText("")
        self.LABELPKGDescription.setText(QCoreApplication.translate("Widget", u"Descripci\u00f3n:", None))
        self.EDITPKGDescription.setPlaceholderText(QCoreApplication.translate("Widget", u"Proposito del nuevo paquete de ROS2.", None))
        self.LABELPKGLicense.setText(QCoreApplication.translate("Widget", u"Licencia:", None))
        self.CBPKGLicense.setItemText(0, QCoreApplication.translate("Widget", u"Apache-2.0", None))
        self.CBPKGLicense.setItemText(1, QCoreApplication.translate("Widget", u"BSL-1.0", None))
        self.CBPKGLicense.setItemText(2, QCoreApplication.translate("Widget", u"MIT", None))
        self.CBPKGLicense.setItemText(3, QCoreApplication.translate("Widget", u"MIT-0", None))
        self.CBPKGLicense.setItemText(4, QCoreApplication.translate("Widget", u"GPL-3.0-only", None))
        self.CBPKGLicense.setItemText(5, QCoreApplication.translate("Widget", u"LGPL-3.0-only", None))
        self.CBPKGLicense.setItemText(6, QCoreApplication.translate("Widget", u"BSD-2.0", None))
        self.CBPKGLicense.setItemText(7, QCoreApplication.translate("Widget", u"BSD-2.Clause", None))
        self.CBPKGLicense.setItemText(8, QCoreApplication.translate("Widget", u"BSD-3.Clause", None))

        self.GROUPPKGConf.setTitle(QCoreApplication.translate("Widget", u"Configuraci\u00f3n del paquete", None))
        self.LABELPKGAment.setText(QCoreApplication.translate("Widget", u"Tipo de construcci\u00f3n:", None))
        self.CBPKGAment.setItemText(0, QCoreApplication.translate("Widget", u"Python [ament_python]", None))
        self.CBPKGAment.setItemText(1, QCoreApplication.translate("Widget", u"CMake [ament_cmake]", None))
        self.CBPKGAment.setItemText(2, QCoreApplication.translate("Widget", u"Rust [ament_cargo]", None))

        self.INFOPKGAment.setText(QCoreApplication.translate("Widget", u"Sistema de compilaci\u00f3n del nuevo paquete.", None))
        self.LABELProjectVer.setText(QCoreApplication.translate("Widget", u"Versi\u00f3n del proyecto:", None))
        self.EDITProjectVer.setPlaceholderText(QCoreApplication.translate("Widget", u"0.0.0", None))
        self.INFOProjectVer.setText(QCoreApplication.translate("Widget", u"Versi\u00f3n del nuevo proyecto/paquete (por ejemplo, alpha, 1.0.0, A).", None))
        self.GROUPMainteiner.setTitle(QCoreApplication.translate("Widget", u"Sobre el responsable del paquete", None))
        self.LABELMAINTName.setText(QCoreApplication.translate("Widget", u"Nombre: ", None))
        self.LABELMAINTEmail.setText(QCoreApplication.translate("Widget", u"Correo:", None))
        self.GROUPConf.setTitle(QCoreApplication.translate("Widget", u"Conexiones", None))
        self.LABELPKGDir.setText(QCoreApplication.translate("Widget", u"Ubicaci\u00f3n de instalaci\u00f3n", None))
        self.EDITPKGDir.setPlaceholderText(QCoreApplication.translate("Widget", u"ros2_ws/src/", None))
        self.LABELPKGApts.setText(QCoreApplication.translate("Widget", u"Dependencias:", None))
        self.EDITPKGApts.setPlaceholderText(QCoreApplication.translate("Widget", u"separados por espacios", None))
        self.GROUPNode.setTitle(QCoreApplication.translate("Widget", u"Nodos", None))
        self.CBNODENew.setItemText(0, QCoreApplication.translate("Widget", u".py", None))
        self.CBNODENew.setItemText(1, QCoreApplication.translate("Widget", u".cpp", None))

        #self.LABELNODEAdded.setText(QCoreApplication.translate("Widget", u"my_node.py", None))
        self.GROUPLaunch.setTitle(QCoreApplication.translate("Widget", u"Lanzadores", None))
        self.CBLAUNCHNew.setItemText(0, QCoreApplication.translate("Widget", u".launch.py", None))
        self.CBLAUNCHNew.setItemText(1, QCoreApplication.translate("Widget", u".yaml", None))
        self.CBLAUNCHNew.setItemText(2, QCoreApplication.translate("Widget", u".xml", None))

        #self.LABELLAUNCHAdded.setText(QCoreApplication.translate("Widget", u"my_launcher.python.py", None))
        self.TABPKGNew.setTabText(self.TABPKGNew.indexOf(self.TAB_my_pkg), QCoreApplication.translate("Widget", u"my_pkg", None))
        self.BTNMake.setText(QCoreApplication.translate("Widget", u"Crear", None))
        self.BTNCancell.setText(QCoreApplication.translate("Widget", u"Cancelar", None))
        self.LABELDir.setText(QCoreApplication.translate("Widget", u"Ubicaci\u00f3n del nuevo espacio de trabajo:", None))
        self.EDITDir.setPlaceholderText(QCoreApplication.translate("Widget", u"~/", None))
    # retranslateUi

    def _remove_item(self, widget, parent_layout):
        try:
            parent_layout.removeWidget(widget)
        except Exception:
            pass
        try:
            widget.setParent(None)
            widget.deleteLater()
        except Exception:
            pass

    def _on_add_node(self):
        # determine active tab and corresponding controls/layouts
        target_tab = None
        try:
            target_tab = self.TABPKGNew.currentWidget()
        except Exception:
            target_tab = None

        # prefer controls inside the active tab, fallback to the ones on self
        edit_widget = None
        combo_widget = None
        node_container = None
        target_layout = None
        try:
            if target_tab is not None:
                edit_widget = target_tab.findChild(QLineEdit, 'EDITNODENew')
                combo_widget = target_tab.findChild(QComboBox, 'CBNODENew')
                node_container = target_tab.findChild(QWidget, 'scrollAreaWidgetContents_2')
                if node_container is not None:
                    target_layout = node_container.layout()
        except Exception:
            edit_widget = None
            combo_widget = None

        if edit_widget is None:
            edit_widget = getattr(self, 'EDITNODENew', None)
        if combo_widget is None:
            combo_widget = getattr(self, 'CBNODENew', None)
        if target_layout is None:
            target_layout = getattr(self, 'verticalLayout_16', None)
            node_container = getattr(self, 'scrollAreaWidgetContents_2', None)

        try:
            if target_layout is not None:
                target_layout.setContentsMargins(0, 0, 0, 0)
                target_layout.setSpacing(0)
        except Exception:
            pass

        raw = (edit_widget.text() if edit_widget is not None else '') or ''
        ext = (combo_widget.currentText() if combo_widget is not None else '') or ''

        name = sanitize_item_name(raw, ext=ext, default_base='new_node')

        # ensure uniqueness in the node list
        exists = False
        if target_layout is not None:
            for i in range(target_layout.count()):
                it = target_layout.itemAt(i)
                w = it.widget()
                if w is not None:
                    if hasattr(w, 'label'):
                        if (w.label.text() or '') == name:
                            exists = True
                            break
                    if isinstance(w, QLabel):
                        if (w.text() or '') == name:
                            exists = True
                            break
                else:
                    l = it.layout()
                    if l is not None and l.count() > 0:
                        first = l.itemAt(0).widget()
                        if first is not None and isinstance(first, QLabel):
                            if (first.text() or '') == name:
                                exists = True
                                break
        if exists:
            return

        # attempt to create a RemovableItemWidget
        try:

            widget = RemovableItemWidget(text=name, parent=(node_container or self.scrollAreaWidgetContents_2),
                                         icon_path=_resolve_icon(self._icon_dirs, os.path.join('close', 'default.svg'), theme=self.theme))
            # insert before the spacer (last item)
            if target_layout is not None:
                target_layout.insertWidget(max(0, target_layout.count()-1), widget)
                try:
                    widget.removed.connect(lambda w=widget: self._remove_item(w, target_layout))
                except Exception:
                    pass
        except Exception:
            # fallback: create simple layout with label + button
            layout = QHBoxLayout()
            parent_widget = node_container or self.scrollAreaWidgetContents_2
            lbl = QLabel(parent_widget)
            lbl.setText(name)
            sp = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
            lbl.setSizePolicy(sp)
            btn = QPushButton(parent_widget)
            btn.setText('x')
            btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            layout.addWidget(lbl)
            layout.addWidget(btn)
            # insert before spacer
            if target_layout is not None:
                target_layout.insertLayout(max(0, target_layout.count()-1), layout)
                btn.clicked.connect(lambda _, l=layout: (l.setParent(None)))

    def _on_add_launch(self):
        # determine active tab and corresponding controls/layouts
        target_tab = None
        try:
            target_tab = self.TABPKGNew.currentWidget()
        except Exception:
            target_tab = None

        edit_widget = None
        combo_widget = None
        launch_container = None
        target_layout = None
        try:
            if target_tab is not None:
                edit_widget = target_tab.findChild(QLineEdit, 'EDITLAUNCHNew')
                combo_widget = target_tab.findChild(QComboBox, 'CBLAUNCHNew')
                launch_container = target_tab.findChild(QWidget, 'scrollAreaWidgetContents_3')
                if launch_container is not None:
                    target_layout = launch_container.layout()
        except Exception:
            edit_widget = None
            combo_widget = None

        if edit_widget is None:
            edit_widget = getattr(self, 'EDITLAUNCHNew', None)
        if combo_widget is None:
            combo_widget = getattr(self, 'CBLAUNCHNew', None)
        if target_layout is None:
            target_layout = getattr(self, 'verticalLayout_13', None)
            launch_container = getattr(self, 'scrollAreaWidgetContents_3', None)

        try:
            if target_layout is not None:
                target_layout.setContentsMargins(0, 0, 0, 0)
                target_layout.setSpacing(0)
        except Exception:
            pass

        raw = (edit_widget.text() if edit_widget is not None else '') or ''
        ext = (combo_widget.currentText() if combo_widget is not None else '') or ''

        name = sanitize_item_name(raw, ext=ext, default_base='new_launch')

        # ensure uniqueness in launch list
        exists = False
        if target_layout is not None:
            for i in range(target_layout.count()):
                it = target_layout.itemAt(i)
                w = it.widget()
                if w is not None:
                    if hasattr(w, 'label'):
                        if (w.label.text() or '') == name:
                            exists = True
                            break
                    if isinstance(w, QLabel):
                        if (w.text() or '') == name:
                            exists = True
                            break
                else:
                    l = it.layout()
                    if l is not None and l.count() > 0:
                        first = l.itemAt(0).widget()
                        if first is not None and isinstance(first, QLabel):
                            if (first.text() or '') == name:
                                exists = True
                                break
        if exists:
            return

        try:

            widget = RemovableItemWidget(text=name, parent=(launch_container or self.scrollAreaWidgetContents_3),
                                         icon_path=_resolve_icon(self._icon_dirs, os.path.join('close', 'default.svg'), theme=self.theme))
            if target_layout is not None:
                target_layout.insertWidget(max(0, target_layout.count()-1), widget)
                try:
                    widget.removed.connect(lambda w=widget: self._remove_item(w, target_layout))
                except Exception:
                    pass
        except Exception:
            layout = QHBoxLayout()
            parent_widget = launch_container or self.scrollAreaWidgetContents_3
            lbl = QLabel(parent_widget)
            lbl.setText(name)
            sp = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
            lbl.setSizePolicy(sp)
            btn = QPushButton(parent_widget)
            btn.setText('x')
            btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            layout.addWidget(lbl)
            layout.addWidget(btn)
            if target_layout is not None:
                target_layout.insertLayout(max(0, target_layout.count()-1), layout)
                btn.clicked.connect(lambda _, l=layout: (l.setParent(None)))

    def _on_delete_my_pkg_tab(self):
        try:
            # find the index of the tab that contains TAB_my_pkg
            idx = -1
            try:
                idx = self.TABPKGNew.indexOf(self.TAB_my_pkg)
            except Exception:
                idx = -1
            if idx is not None and idx >= 0:
                try:
                    self.TABPKGNew.removeTab(idx)
                except Exception:
                    pass
        except Exception:
            pass

    def _on_add_pkg(self):
        raw = (self.EDITPKGNew.text() or '')
        # packages typically don't have an extension here
        name = sanitize_item_name(raw, ext='', default_base='my_pkg')

        # ensure uniqueness among tab texts
        for i in range(self.TABPKGNew.count()):
            try:
                if (self.TABPKGNew.tabText(i) or '') == name:
                    return
            except Exception:
                continue

        try:
            # instantiate a temporary Ui_Widget to reuse the TAB_my_pkg template
            temp_root = QWidget()
            temp_ui = type(self)()
            temp_ui.setupUi(temp_root, icon_dirs=self._icon_dirs, theme=self.theme)

            # grab the template tab widget
            try:
                template_tab = temp_ui.TAB_my_pkg
            except Exception:
                template_tab = None

            if template_tab is None:
                return

            # find the original delete button on the template (before renaming)
            try:
                orig_del_btn = template_tab.findChild(QPushButton, 'BTNDel_my_pkg')
            except Exception:
                orig_del_btn = None

            # rename objectNames that include '_my_pkg' to use the new package id
            pkg_id = name
            try:
                for obj in template_tab.findChildren(QObject):
                    try:
                        on = obj.objectName()
                        if on and '_my_pkg' in on:
                            obj.setObjectName(on.replace('_my_pkg', '_' + pkg_id))
                    except Exception:
                        continue
            except Exception:
                pass

            # detach from the temporary root and add as a new tab
            try:
                template_tab.setParent(None)
                idx = self.TABPKGNew.addTab(template_tab, pkg_id)
            except Exception:
                return

            # set package install dir placeholder based on current workspace name
            try:
                ws_raw = (getattr(self, 'EDITWSNew', None).text() or '')
            except Exception:
                ws_raw = ''
            try:
                ws_sanit = sanitize_item_name(ws_raw, ext='', default_base='ros2_ws')
                ws_placeholder = ws_sanit.rstrip('/') + '/src/'
            except Exception:
                ws_placeholder = 'ros2_ws/src/'
            try:
                for le in template_tab.findChildren(QLineEdit):
                    on = le.objectName() or ''
                    if on.startswith('EDITPKGDir'):
                        try:
                            le.setPlaceholderText(ws_placeholder)
                        except Exception:
                            pass
            except Exception:
                pass

            # connect the delete button (use the original reference if found)
            try:
                btn = orig_del_btn if orig_del_btn is not None else None
                if btn is None:
                    # fallback: try to find renamed delete button
                    btn = template_tab.findChild(QPushButton, 'BTNDel_' + pkg_id)
                if btn is not None:
                    def _remove_this_tab():
                        try:
                            ix = self.TABPKGNew.indexOf(template_tab)
                            if ix is not None and ix >= 0:
                                self.TABPKGNew.removeTab(ix)
                        except Exception:
                            pass
                    try:
                        btn.clicked.connect(_remove_this_tab)
                    except Exception:
                        pass
            except Exception:
                pass
            # connect cloned add-node and add-launch buttons to operate on this tab
            try:
                node_btn = template_tab.findChild(QPushButton, 'BTNNODENew')
                if node_btn is not None:
                    node_btn.clicked.connect(lambda _, tb=template_tab: (self.TABPKGNew.setCurrentWidget(tb), self._on_add_node()))
                # also connect returnPressed of EDITNODENew inside the tab if present
                edit_node = template_tab.findChild(QLineEdit, 'EDITNODENew')
                if edit_node is not None:
                    edit_node.returnPressed.connect(lambda tb=template_tab: (self.TABPKGNew.setCurrentWidget(tb), self._on_add_node()))
            except Exception:
                pass
            try:
                launch_btn = template_tab.findChild(QPushButton, 'BTNLAUNCHNew')
                if launch_btn is not None:
                    launch_btn.clicked.connect(lambda _, tb=template_tab: (self.TABPKGNew.setCurrentWidget(tb), self._on_add_launch()))
                edit_launch = template_tab.findChild(QLineEdit, 'EDITLAUNCHNew')
                if edit_launch is not None:
                    edit_launch.returnPressed.connect(lambda tb=template_tab: (self.TABPKGNew.setCurrentWidget(tb), self._on_add_launch()))
            except Exception:
                pass
        except Exception:
            pass

    def _on_ws_name_changed(self, text: str):
        try:
            ws = (text or '')
            sanitized = sanitize_item_name(ws, ext='', default_base='ros2_ws')
            new_placeholder = sanitized.rstrip('/') + '/src/'
        except Exception:
            new_placeholder = 'ros2_ws/src/'

        # update the main EDITPKGDir if present
        try:
            if hasattr(self, 'EDITPKGDir') and self.EDITPKGDir is not None:
                try:
                    self.EDITPKGDir.setPlaceholderText(new_placeholder)
                except Exception:
                    pass
        except Exception:
            pass

        # update EDITPKGDir inside every tab (including cloned ones)
        try:
            for i in range(self.TABPKGNew.count()):
                tab = self.TABPKGNew.widget(i)
                if tab is None:
                    continue
                try:
                    # find all QLineEdit children and update those named like EDITPKGDir
                    for le in tab.findChildren(QLineEdit):
                        on = le.objectName() or ''
                        if on.startswith('EDITPKGDir'):
                            try:
                                le.setPlaceholderText(new_placeholder)
                            except Exception:
                                pass
                except Exception:
                    continue
        except Exception:
            pass

    def _on_maint_changed(self, _=None):
        return

