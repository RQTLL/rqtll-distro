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
    QSize, QTime, QUrl, Qt, QAbstractTableModel, QModelIndex)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QScrollArea, QSizePolicy, QSpacerItem, QTabWidget,
    QVBoxLayout, QWidget, QTableView, QHeaderView)

import os
try:
    from ..utils.icon_loader import load_qicon, load_qpixmap, _resolve_icon
except (ImportError, ValueError):
    import sys
    _parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if _parent not in sys.path:
        sys.path.insert(0, _parent)
    from utils.icon_loader import load_qicon, load_qpixmap, _resolve_icon

try:
    from ..utils.frame_option_button import FrameOptionButtonWidget
except (ImportError, ValueError):
    import sys
    _parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if _parent not in sys.path:
        sys.path.insert(0, _parent)
    from utils.frame_option_button import FrameOptionButtonWidget

class WizardPackageTableModel(QAbstractTableModel):
    HEADERS = ["Nombre", "Acción"]

    def __init__(self, packages=None, parent=None):
        super().__init__(parent)
        self._data = packages or []

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)

    def columnCount(self, parent=QModelIndex()):
        return len(self.HEADERS)

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if role != Qt.ItemDataRole.DisplayRole:
            return None
        if orientation == Qt.Orientation.Horizontal:
            return self.HEADERS[section]
        return section + 1

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return None
        row = index.row()
        col = index.column()
        pkg = self._data[row]
        if role == Qt.ItemDataRole.DisplayRole:
            if col == 0:
                return pkg.get("name")
            if col == 1:
                if pkg.get("installed"):
                    return "Instalado"
                if pkg.get("pending"):
                    return "Pendiente"
                return "Solicitar"
        return None

    def flags(self, index):
        if not index.isValid():
            return Qt.ItemFlag.NoItemFlags
        return Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable

    def set_packages(self, packages):
        self.beginResetModel()
        self._data = []
        for p in packages:
            item = {
                'name': p.get('name', ''),
                'installed': bool(p.get('installed', False)),
                'pending': False,
            }
            self._data.append(item)
        self.endResetModel()

    def request_toggle_pending(self, row: int):
        if row < 0 or row >= len(self._data):
            return
        if not self._data[row].get('installed'):
            self._data[row]['pending'] = not self._data[row].get('pending', False)
            left = self.index(row, 1)
            right = self.index(row, 1)
            self.dataChanged.emit(left, right, [Qt.ItemDataRole.DisplayRole])
        return sum(1 for it in self._data if it.get('pending'))

class Ui_Widget(object):
    def setupUi(self, Widget, icon_dirs=None, theme: str = "default.qss"):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(630, 393)
        Widget.setMinimumSize(QSize(630, 393))
        Widget.setMaximumSize(QSize(630, 393))
        self.theme = theme

        icon = QIcon()
        icon_path = _resolve_icon(icon_dirs, os.path.join('logo.svg'), theme=self.theme)
        icon.addFile(icon_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Widget.setWindowIcon(icon)
        self.gridLayout = QGridLayout(Widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(Widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setProperty('role', 'in-tab')
        self.tab.setProperty('variant', 'default')
        self.tab.setProperty('state', 'normal')
        self.tab.setObjectName(u"tab")
        
        self.verticalLayout_tab = QVBoxLayout(self.tab)
        self.verticalLayout_tab.setObjectName(u"verticalLayout_tab")
        self.verticalLayout_tab.setContentsMargins(0, 0, 0, 0)
        
        self.scrollAreaOptions = QScrollArea(self.tab)
        self.scrollAreaOptions.setObjectName(u"scrollAreaOptions")
        self.scrollAreaOptions.setWidgetResizable(True)
        self.scrollAreaOptions.setStyleSheet("QScrollArea#scrollAreaOptions { background: transparent; border: none; }")
        
        self.scrollAreaWidgetContentsOptions = QWidget()
        self.scrollAreaWidgetContentsOptions.setObjectName(u"scrollAreaWidgetContentsOptions")
        self.scrollAreaWidgetContentsOptions.setStyleSheet("QWidget#scrollAreaWidgetContentsOptions { background: transparent; }")
        
        self.gridLayout_options = QGridLayout(self.scrollAreaWidgetContentsOptions)
        self.gridLayout_options.setObjectName(u"gridLayout_options")
        self.gridLayout_options.setSpacing(10)
        self.gridLayout_options.setContentsMargins(10, 10, 10, 10)

        self.FRAMECore1 = FrameOptionButtonWidget(
            icon_path=_resolve_icon(icon_dirs, os.path.join('ros-core', 'default.svg'), theme=self.theme), 
            title="", info="", parent=self.scrollAreaWidgetContentsOptions, theme=theme, button_id="core")
        self.FRAMECore1.setObjectName(u"FRAMECore1")
        self.ICONCore1 = self.FRAMECore1.icon
        self.LABELTitleCore1 = self.FRAMECore1.title
        self.LABELInfoCore1 = self.FRAMECore1.info
        self.gridLayout_options.addWidget(self.FRAMECore1, 0, 0, 1, 1)

        self.FRAMEDesktop1 = FrameOptionButtonWidget(
            icon_path=_resolve_icon(icon_dirs, os.path.join('ros-desktop', 'default.svg'), theme=self.theme), 
            title="", info="", parent=self.scrollAreaWidgetContentsOptions, theme=theme, button_id="desktop")
        self.FRAMEDesktop1.setObjectName(u"FRAMEDesktop1")
        self.ICONDesktop1 = self.FRAMEDesktop1.icon
        self.LABELTitleDesktop1 = self.FRAMEDesktop1.title
        self.LABELInfoDesktop1 = self.FRAMEDesktop1.info
        self.gridLayout_options.addWidget(self.FRAMEDesktop1, 0, 1, 1, 1)

        self.FRAMEFull1 = FrameOptionButtonWidget(
            icon_path=_resolve_icon(icon_dirs, os.path.join('ros-full', 'default.svg'), theme=self.theme), 
            title="", info="", parent=self.scrollAreaWidgetContentsOptions, theme=theme, button_id="full")
        self.FRAMEFull1.setObjectName(u"FRAMEFull1")
        self.ICONFull1 = self.FRAMEFull1.icon
        self.LABELTitleFull1 = self.FRAMEFull1.title
        self.LABELInfoFull1 = self.FRAMEFull1.info
        self.gridLayout_options.addWidget(self.FRAMEFull1, 0, 2, 1, 1)

        self.FRAMECore2 = FrameOptionButtonWidget(
            icon_path=_resolve_icon(icon_dirs, os.path.join('ros-core', 'default.svg'), theme=self.theme), 
            title="", info="", parent=self.scrollAreaWidgetContentsOptions, theme=theme, button_id="core")
        self.FRAMECore2.setObjectName(u"FRAMECore")
        self.ICONCore2 = self.FRAMECore2.icon
        self.LABELTitleCore2 = self.FRAMECore2.title
        self.LABELInfoCore2 = self.FRAMECore2.info
        self.gridLayout_options.addWidget(self.FRAMECore2, 1, 0, 1, 1)

        self.FRAMEDesktop2 = FrameOptionButtonWidget(
            icon_path=_resolve_icon(icon_dirs, os.path.join('ros-desktop', 'default.svg'), theme=self.theme), 
            title="", info="", parent=self.scrollAreaWidgetContentsOptions, theme=theme, button_id="desktop")
        self.FRAMEDesktop2.setObjectName(u"FRAMEDesktop")
        self.ICONDesktop2 = self.FRAMEDesktop2.icon
        self.LABELTitleDesktop2 = self.FRAMEDesktop2.title
        self.LABELInfoDesktop2 = self.FRAMEDesktop2.info
        self.gridLayout_options.addWidget(self.FRAMEDesktop2, 1, 1, 1, 1)

        self.FRAMEFull2 = FrameOptionButtonWidget(
            icon_path=_resolve_icon(icon_dirs, os.path.join('ros-full', 'default.svg'), theme=self.theme), 
            title="", info="", parent=self.scrollAreaWidgetContentsOptions, theme=theme, button_id="full")
        self.FRAMEFull2.setObjectName(u"FRAMEFull")
        self.ICONFull2 = self.FRAMEFull2.icon
        self.LABELTitleFull2 = self.FRAMEFull2.title
        self.LABELInfoFull2 = self.FRAMEFull2.info
        self.gridLayout_options.addWidget(self.FRAMEFull2, 1, 2, 1, 1)

        self.scrollAreaOptions.setWidget(self.scrollAreaWidgetContentsOptions)
        self.verticalLayout_tab.addWidget(self.scrollAreaOptions)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setProperty('role', 'in-tab')
        self.tab_2.setProperty('variant', 'default')
        self.tab_2.setProperty('state', 'normal')
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout = QVBoxLayout(self.tab_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.LABELSearch = QLabel(self.tab_2)
        self.LABELSearch.setObjectName(u"LABELSearch")

        self.horizontalLayout_2.addWidget(self.LABELSearch)

        self.EDITSearch = QLineEdit(self.tab_2)
        self.EDITSearch.setObjectName(u"EDITSearch")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EDITSearch.sizePolicy().hasHeightForWidth())
        self.EDITSearch.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.EDITSearch)

        self.CBOPT1Search = QCheckBox(self.tab_2)
        self.CBOPT1Search.setObjectName(u"CBOPT1Search")
        self.CBOPT1Search.setChecked(True)

        self.horizontalLayout_2.addWidget(self.CBOPT1Search)

        self.CBOPT2Search = QCheckBox(self.tab_2)
        self.CBOPT2Search.setObjectName(u"CBOPT2Search")
        self.CBOPT2Search.setChecked(True)

        self.horizontalLayout_2.addWidget(self.CBOPT2Search)

        self.CBRti = QCheckBox(self.tab_2)
        self.CBRti.setObjectName(u"CBRti")
        self.CBRti.setChecked(True)

        self.horizontalLayout_2.addWidget(self.CBRti)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.scrollArea = QScrollArea(self.tab_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 532, 198))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        
        self.pkg_view = QTableView(self.scrollAreaWidgetContents)
        self.pkg_view.setObjectName(u"pkgView")
        self.pkg_model = WizardPackageTableModel(parent=Widget)
        self.pkg_view.setModel(self.pkg_model)
        header = self.pkg_view.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        self.verticalLayout_3.addWidget(self.pkg_view)

        def _on_pkg_clicked(index):
            try:
                if index.column() == 1:
                    self.pkg_model.request_toggle_pending(index.row())
            except Exception:
                pass

        self.pkg_view.clicked.connect(_on_pkg_clicked)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

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


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)


        # Connect shared toggled signals to manage a property on the top-level Widget
        def _on_option_toggled(checked, btn_id):
            if checked:
                try:
                    Widget.setProperty("selected_ros_option", btn_id)
                except Exception:
                    pass

        self.FRAMECore1.toggled.connect(lambda checked: _on_option_toggled(checked, "core1"))
        self.FRAMEDesktop1.toggled.connect(lambda checked: _on_option_toggled(checked, "desktop1"))
        self.FRAMEFull1.toggled.connect(lambda checked: _on_option_toggled(checked, "full1"))

        self.FRAMECore2.toggled.connect(lambda checked: _on_option_toggled(checked, "core2"))
        self.FRAMEDesktop2.toggled.connect(lambda checked: _on_option_toggled(checked, "desktop2"))
        self.FRAMEFull2.toggled.connect(lambda checked: _on_option_toggled(checked, "full2"))

        self.FRAMECore1.setChecked(True)
        self.retranslateUi(Widget)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"RQTLL IDE / Versión de ROS2", None))
        
        self.LABELTitleCore1.setText(QCoreApplication.translate("Widget", u"$install_opt_core_title", None))
        self.LABELInfoCore1.setText(QCoreApplication.translate("Widget", u"$install_opt_core_desc", None))
        self.LABELTitleDesktop1.setText(QCoreApplication.translate("Widget", u"$install_opt_desktop_title", None))
        self.LABELInfoDesktop1.setText(QCoreApplication.translate("Widget", u"$install_opt_desktop_desc", None))
        self.LABELTitleFull1.setText(QCoreApplication.translate("Widget", u"$install_opt_full_title", None))
        self.LABELInfoFull1.setText(QCoreApplication.translate("Widget", u"$install_opt_full_desc", None))

        self.LABELTitleCore2.setText(QCoreApplication.translate("Widget", u"$install_opt_core_title", None))
        self.LABELInfoCore2.setText(QCoreApplication.translate("Widget", u"$install_opt_core_desc", None))
        self.LABELTitleDesktop2.setText(QCoreApplication.translate("Widget", u"$install_opt_desktop_title", None))
        self.LABELInfoDesktop2.setText(QCoreApplication.translate("Widget", u"$install_opt_desktop_desc", None))
        self.LABELTitleFull2.setText(QCoreApplication.translate("Widget", u"$install_opt_full_title", None))
        self.LABELInfoFull2.setText(QCoreApplication.translate("Widget", u"$install_opt_full_desc", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Widget", u"Versi\u00f3n de ROS2", None))
        self.LABELSearch.setText(QCoreApplication.translate("Widget", u"Buscar", None))
        self.CBOPT1Search.setText(QCoreApplication.translate("Widget", u"ROS2", None))
        self.CBOPT2Search.setText(QCoreApplication.translate("Widget", u"Python", None))
        self.CBRti.setText(QCoreApplication.translate("Widget", u"rti", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Widget", u"Paquetes extra", None))
        self.BTNBack.setText(QCoreApplication.translate("Widget", u"Regresar", None))
        self.BTNNext.setText(QCoreApplication.translate("Widget", u"Siguiente", None))
        self.BTNCancel.setText(QCoreApplication.translate("Widget", u"Cancelar", None))
    # retranslateUi

