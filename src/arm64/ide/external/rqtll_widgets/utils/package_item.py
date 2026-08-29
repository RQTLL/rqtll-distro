from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout, QSizePolicy
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QCursor

class PackageItemWidget(QWidget):
    install_requested = Signal(str)

    def __init__(self, name: str = "", link: str = "", parent=None):
        super().__init__(parent)
        self._name = name
        self._link = link

        self.label_name = QLabel(name)
        self.label_link = QLabel(link)
        self.btn_action = QPushButton("Instalar")
        self.btn_action.clicked.connect(self._on_clicked)

        layout = QHBoxLayout(self)
        layout.addWidget(self.label_name)
        layout.addWidget(self.label_link)
        layout.addWidget(self.btn_action)

    def _on_clicked(self):
        self.install_requested.emit(self._name)

    def setName(self, name: str):
        self._name = name
        self.label_name.setText(name)

    def setLink(self, link: str):
        self._link = link
        self.label_link.setText(link)

    def setButtonText(self, text: str):
        self.btn_action.setText(text)


def add_package_row(grid_layout, grid_row: int, idx: int, name: str, link: str, button_text: str = "Instalar", parent=None):

    lbl_name = QLabel(parent)
    lbl_name.setObjectName(f"PKGName{idx}")
    sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
    sizePolicy.setHeightForWidth(lbl_name.sizePolicy().hasHeightForWidth())
    lbl_name.setSizePolicy(sizePolicy)
    lbl_name.setText(name)

    lbl_link = QLabel(parent)
    lbl_link.setObjectName(f"PKGLINKS{idx}")
    lbl_link.setText(link)
    lbl_link.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

    btn = QPushButton(parent)
    btn.setObjectName(f"BUTTONInstall{idx}")
    btn.setText(button_text)

    grid_layout.addWidget(lbl_name, grid_row, 0, 1, 1)
    grid_layout.addWidget(lbl_link, grid_row, 1, 1, 1)
    grid_layout.addWidget(btn, grid_row, 3, 1, 1)

    return lbl_name, lbl_link, btn
