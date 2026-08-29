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
    QSize, QTime, QUrl, Qt, QAbstractTableModel, QModelIndex)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget, QCheckBox, QLineEdit,
    QScrollArea, QTableView, QHeaderView, QLabel)
import os
import urllib.request

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
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        # Content of f4_ui_package_manager.py placed inside self.frame
        self.verticalLayout_frame = QVBoxLayout(self.frame)
        self.verticalLayout_frame.setObjectName(u"verticalLayout_frame")
        self.verticalLayout_frame.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_frame.setSpacing(6)

        self.horizontalLayout_frame = QHBoxLayout()
        self.horizontalLayout_frame.setObjectName(u"horizontalLayout_frame")
        self.LABELSearch = QLabel(self.frame)
        self.LABELSearch.setObjectName(u"LABELSearch")

        self.horizontalLayout_frame.addWidget(self.LABELSearch)

        self.EDITSearch = QLineEdit(self.frame)
        self.EDITSearch.setObjectName(u"EDITSearch")
        sizePolicy_search = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy_search.setHorizontalStretch(0)
        sizePolicy_search.setVerticalStretch(0)
        sizePolicy_search.setHeightForWidth(self.EDITSearch.sizePolicy().hasHeightForWidth())
        self.EDITSearch.setSizePolicy(sizePolicy_search)

        self.horizontalLayout_frame.addWidget(self.EDITSearch)

        self.CBOPT1Search = QCheckBox(self.frame)
        self.CBOPT1Search.setObjectName(u"CBOPT1Search")
        self.CBOPT1Search.setChecked(True)

        self.horizontalLayout_frame.addWidget(self.CBOPT1Search)

        self.CBOPT2Search = QCheckBox(self.frame)
        self.CBOPT2Search.setObjectName(u"CBOPT2Search")
        self.CBOPT2Search.setChecked(True)

        self.horizontalLayout_frame.addWidget(self.CBOPT2Search)

        self.CBRti = QCheckBox(self.frame)
        self.CBRti.setObjectName(u"CBRti")
        self.CBRti.setChecked(True)

        self.horizontalLayout_frame.addWidget(self.CBRti)

        self.verticalLayout_frame.addLayout(self.horizontalLayout_frame)

        self.scrollArea = QScrollArea(self.frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 555, 262))
        self.verticalLayout_scroll = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_scroll.setObjectName(u"verticalLayout_scroll")

        self.pkg_view = QTableView(self.scrollAreaWidgetContents)
        self.pkg_view.setObjectName(u"pkgView")
        self.pkg_model = PackageTableModel(parent=Widget)
        self.pkg_view.setModel(self.pkg_model)
        header = self.pkg_view.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        self.verticalLayout_scroll.addWidget(self.pkg_view)

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
        self.verticalLayout_frame.addWidget(self.scrollArea)

        self.horizontalLayout_buttons = QHBoxLayout()
        self.horizontalLayout_buttons.setObjectName(u"horizontalLayout_buttons")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_buttons.addItem(self.horizontalSpacer)

        self.BTNApply = QPushButton(self.frame)
        self.BTNApply.setObjectName(u"BTNApply")
        self.BTNApply.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_buttons.addWidget(self.BTNApply)
        try:
            self.BTNApply.clicked.connect(lambda: getattr(self, '_on_apply_packages', lambda: None)())
        except Exception:
            pass

        self.BTNAccept = QPushButton(self.frame)
        self.BTNAccept.setObjectName(u"BTNAccept")
        self.BTNAccept.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_buttons.addWidget(self.BTNAccept)

        self.BTNCancell = QPushButton(self.frame)
        self.BTNCancell.setObjectName(u"BTNCancell")
        self.BTNCancell.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_buttons.addWidget(self.BTNCancell)

        self.verticalLayout_frame.addLayout(self.horizontalLayout_buttons)

        self.verticalLayout_3.addWidget(self.frame)

        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"RQTLL IDE / Gestor de paquetes", None))
        self.LABELSearch.setText(QCoreApplication.translate("Widget", u"Buscar", None))
        self.CBOPT1Search.setText(QCoreApplication.translate("Widget", u"ROS2", None))
        self.CBOPT2Search.setText(QCoreApplication.translate("Widget", u"Python", None))
        self.CBRti.setText(QCoreApplication.translate("Widget", u"rti", None))
        self.BTNApply.setText(QCoreApplication.translate("Widget", u"Aplicar", None))
        self.BTNAccept.setText(QCoreApplication.translate("Widget", u"Aceptar", None))
        self.BTNCancell.setText(QCoreApplication.translate("Widget", u"Cancelar", None))
    # retranslateUi

    def _on_apply_packages(self):
        try:
            ops = self.pkg_model.apply_requests()
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
