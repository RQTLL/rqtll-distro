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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget, QTableView, QHeaderView)
from PySide6.QtCore import QAbstractTableModel, QModelIndex, QTimer
import urllib.request
import io
import os
from PySide6 import QtWidgets as _qtw

try:
    from ..utils.icon_loader import load_qicon, load_qpixmap, _resolve_icon
except (ImportError, ValueError):
    import sys
    _parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if _parent not in sys.path:
        sys.path.insert(0, _parent)
    from utils.icon_loader import load_qicon, load_qpixmap, _resolve_icon

placeholder = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'icons', 'placeholder.svg'))


# Lightweight table model for packages used by the package manager UI.
class PackageTableModel(QAbstractTableModel):
    HEADERS = ["Nombre", "Estado", "Acción"]

    def __init__(self, packages=None, parent=None):
        super().__init__(parent)
        # each item: {'name':str, 'link':str, 'installed':bool, 'pending':bool}
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
                # three-state: Installed / Uninstalled / Pending
                if pkg.get("pending"):
                    return "Pendiente"
                return "Instalado" if pkg.get("installed") else "Desinstalado"
            if col == 2:
                # action shows request/ cancel
                return "Solicitar" if not pkg.get("pending") else "Cancelar"
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
        self._data[row]['pending'] = not self._data[row].get('pending', False)
        left = self.index(row, 1)
        right = self.index(row, 2)
        self.dataChanged.emit(left, right, [Qt.ItemDataRole.DisplayRole])
        # return number of pending items after the toggle
        return sum(1 for it in self._data if it.get('pending'))

    def apply_requests(self):
        # Apply requested operations: flip installed for pending items
        ops = []
        for i, item in enumerate(self._data):
            if item.get('pending'):
                # simulate install/uninstall by toggling installed
                prev = item.get('installed', False)
                item['installed'] = not prev
                item['pending'] = False
                ops.append((item['name'], 'install' if item['installed'] else 'uninstall'))
                left = self.index(i, 1)
                right = self.index(i, 2)
                self.dataChanged.emit(left, right, [Qt.ItemDataRole.DisplayRole])
        return ops

    def load_from_url(self, url: str, max_items: int = 500):
        try:
            with urllib.request.urlopen(url, timeout=15) as resp:
                raw = resp.read().decode('utf-8', errors='ignore')
        except Exception:
            return
        # parse Debian Packages format: split by blank line
        records = [r for r in raw.split('\n\n') if r.strip()]
        pkgs = []
        for rec in records:
            name = None
            for line in rec.splitlines():
                if line.startswith('Package:'):
                    name = line.split(':', 1)[1].strip()
                    break
            if name:
                pkgs.append({'name': name, 'installed': False})
            if len(pkgs) >= max_items:
                break
        self.set_packages(pkgs)

class Ui_Widget(object):
    def setupUi(self, Widget, icon_dirs=None, theme: str = "default.qss"):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(575, 350)
        Widget.setMinimumSize(QSize(575, 350))
        icon = QIcon()
        icon_path = _resolve_icon(icon_dirs, os.path.join('logo.svg'))
        icon.addFile(icon_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Widget.setWindowIcon(icon)
        self.verticalLayout = _qtw.QVBoxLayout(Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.LABELSearch = QLabel(Widget)
        self.LABELSearch.setObjectName(u"LABELSearch")

        self.horizontalLayout.addWidget(self.LABELSearch)

        self.EDITSearch = QLineEdit(Widget)
        self.EDITSearch.setObjectName(u"EDITSearch")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EDITSearch.sizePolicy().hasHeightForWidth())
        self.EDITSearch.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.EDITSearch)

        self.CBOPT1Search = QCheckBox(Widget)
        self.CBOPT1Search.setObjectName(u"CBOPT1Search")
        self.CBOPT1Search.setChecked(True)

        self.horizontalLayout.addWidget(self.CBOPT1Search)

        self.CBOPT2Search = QCheckBox(Widget)
        self.CBOPT2Search.setObjectName(u"CBOPT2Search")
        self.CBOPT2Search.setChecked(True)

        self.horizontalLayout.addWidget(self.CBOPT2Search)

        self.CBRti = QCheckBox(Widget)
        self.CBRti.setObjectName(u"CBRti")
        self.CBRti.setChecked(True)

        self.horizontalLayout.addWidget(self.CBRti)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.scrollArea = QScrollArea(Widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 555, 262))
        self.verticalLayout_3 = _qtw.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        # Replace grid-based package list with a model/view table for scalability
        self.pkg_view = QTableView(self.scrollAreaWidgetContents)
        self.pkg_view.setObjectName(u"pkgView")
        # model parent must be a QObject (use the actual Widget, not the Ui object)
        self.pkg_model = PackageTableModel(parent=Widget)
        self.pkg_view.setModel(self.pkg_model)
        # configure header: name column should expand, others fit contents
        header = self.pkg_view.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        self.verticalLayout_3.addWidget(self.pkg_view)

        # clicking the Action column toggles the 'pending' state (does not apply changes)
        #self.pkg_model.load_from_url("http://packages.ros.org/ros2/ubuntu/dists/noble/main/binary-amd64/Packages")
        def _on_pkg_clicked(index):
            try:
                if index.column() == 2:
                    self.pkg_model.request_toggle_pending(index.row())
                    try:
                        self._update_apply_button()
                    except Exception:
                        pass
            except Exception:
                pass

        self.pkg_view.clicked.connect(_on_pkg_clicked)


        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.BTNApply = QPushButton(Widget)
        self.BTNApply.setObjectName(u"BTNApply")
        self.BTNApply.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.BTNApply)
        try:
            # connect apply to model apply_requests
            self.BTNApply.clicked.connect(lambda: getattr(self, '_on_apply_packages', lambda: None)())
        except Exception:
            pass

        self.BTNAccept = QPushButton(Widget)
        self.BTNAccept.setObjectName(u"BTNAccept")
        self.BTNAccept.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.BTNAccept)

        self.BTNCancell = QPushButton(Widget)
        self.BTNCancell.setObjectName(u"BTNCancell")
        self.BTNCancell.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.BTNCancell)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"RQTLL IDE / Gestor de paquetes", None))
        self.LABELSearch.setText(QCoreApplication.translate("Widget", u"Buscar", None))
        #self.EDITSearch.setText(QCoreApplication.translate("Widget", u"*", None))
        self.CBOPT1Search.setText(QCoreApplication.translate("Widget", u"ROS2", None))
        self.CBOPT2Search.setText(QCoreApplication.translate("Widget", u"Python", None))
        self.CBRti.setText(QCoreApplication.translate("Widget", u"rti", None))
        #self.BUTTONInstall0.setText(QCoreApplication.translate("Widget", u"Instalar", None))
        # links text for first package row
        #self.PKGName0.setText(QCoreApplication.translate("Widget", u"ros2-jazzy", None))
        self.BTNApply.setText(QCoreApplication.translate("Widget", u"Aplicar", None))
        self.BTNAccept.setText(QCoreApplication.translate("Widget", u"Aceptar", None))
        self.BTNCancell.setText(QCoreApplication.translate("Widget", u"Cancelar", None))
    # retranslateUi

    def _on_apply_packages(self):
        try:
            ops = self.pkg_model.apply_requests()
            # simple feedback: print operations; real implementation should
            # perform installation/uninstallation via backend
            if ops:
                for name, op in ops:
                    print(f"Requested {op} for {name}")
            try:
                self._update_apply_button()
            except Exception:
                pass
        except Exception:
            pass

    def _update_apply_button(self):
        try:
            pending = 0
            if hasattr(self, 'pkg_model'):
                pending = sum(1 for it in self.pkg_model._data if it.get('pending'))
            if pending:
                self.BTNApply.setText(f"Aplicar ({pending} pendientes)")
            else:
                self.BTNApply.setText(QCoreApplication.translate("Widget", u"Aplicar", None))
        except Exception:
            pass

