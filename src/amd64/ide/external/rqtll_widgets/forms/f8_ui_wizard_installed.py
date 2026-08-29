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
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

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
        self.LABELInstallProgress = QLabel(Widget)
        self.LABELInstallProgress.setObjectName(u"LABELInstallProgress")

        self.verticalLayout_2.addWidget(self.LABELInstallProgress)

        self.progressBar = QProgressBar(Widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(5)
        self.progressBar.setTextVisible(False)

        self.verticalLayout_2.addWidget(self.progressBar)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.CBLoadRosShell = QCheckBox(Widget)
        self.CBLoadRosShell.setObjectName(u"CBLoadRosShell")
        self.CBLoadRosShell.setChecked(True)

        self.verticalLayout.addWidget(self.CBLoadRosShell)

        self.CBConfigDomainId = QCheckBox(Widget)
        self.CBConfigDomainId.setObjectName(u"CBConfigDomainId")

        self.verticalLayout.addWidget(self.CBConfigDomainId)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.LABELDomainId = QLabel(Widget)
        self.LABELDomainId.setObjectName(u"LABELDomainId")

        self.horizontalLayout_2.addWidget(self.LABELDomainId)

        self.spinBox = QSpinBox(Widget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximum(232)
        arrow_down_icon = load_qicon(os.path.join('arrows', 'down.svg'), icon_dirs)
        arrow_up_icon = load_qicon(os.path.join('arrows', 'up.svg'), icon_dirs)
        if not arrow_down_icon.isNull() and not arrow_up_icon.isNull():
            self.spinBox.setStyleSheet(f"""
                QSpinBox::down-arrow {{ image: url({_resolve_icon(icon_dirs, os.path.join('arrows', 'down.svg'))}); }}
                QSpinBox::up-arrow {{ image: url({_resolve_icon(icon_dirs, os.path.join('arrows', 'up.svg'))}); }}
            """)

        self.horizontalLayout_2.addWidget(self.spinBox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        # Connect CBConfigDomainId toggled signal to show/hide domain ID configuration widgets
        self.LABELDomainId.setVisible(self.CBConfigDomainId.isChecked())
        self.spinBox.setVisible(self.CBConfigDomainId.isChecked())
        if not self.CBConfigDomainId.isChecked():
            self.spinBox.setValue(0)
        self.CBConfigDomainId.toggled.connect(lambda checked: (
            self.LABELDomainId.setVisible(checked),
            self.spinBox.setVisible(checked),
            self.spinBox.setValue(0) if not checked else None
        ))


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.LABELConfigProgress = QLabel(Widget)
        self.LABELConfigProgress.setObjectName(u"LABELConfigProgress")

        self.verticalLayout_2.addWidget(self.LABELConfigProgress)

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
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"RQTLL IDE / Progreso de Instalación", None))
        self.LABELInstallProgress.setText(QCoreApplication.translate("Widget", u"Instalando ROS2", None))
        self.CBLoadRosShell.setText(QCoreApplication.translate("Widget", u"Cargar ROS2 con la shell", None))
        self.CBConfigDomainId.setText(QCoreApplication.translate("Widget", u"Configurar ROS_DAMAIN_ID (+ufw allow)", None))
        self.LABELDomainId.setText(QCoreApplication.translate("Widget", u"ROS_DAMAIN_ID:", None))
        self.BTNBack.setText(QCoreApplication.translate("Widget", u"Regresar", None))
        self.BTNNext.setText(QCoreApplication.translate("Widget", u"Siguiente", None))
        self.BTNCancel.setText(QCoreApplication.translate("Widget", u"Cancelar", None))
    # retranslateUi

