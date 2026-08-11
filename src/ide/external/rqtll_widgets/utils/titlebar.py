from __future__ import annotations

import os
from typing import Optional, List

from PySide6.QtCore import Qt, Signal, QSize
from PySide6.QtGui import QPixmap, QIcon, QCursor
from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout, QSizePolicy, QSpacerItem


try:
    from . import icon_loader
except Exception:
    import importlib.util as _il, os as _os
    _spec = _il.spec_from_file_location("icon_loader", _os.path.join(_os.path.dirname(__file__), "icon_loader.py"))
    _mod = _il.module_from_spec(_spec)
    _spec.loader.exec_module(_mod)
    icon_loader = _mod
try:
    from .theme_manager import get_theme_manager
    _theme_manager = get_theme_manager()
except Exception:
    _theme_manager = None
    try:
        from rqtll_widgets.utils.theme_manager import get_theme_manager as _gm
        _theme_manager = _gm()
    except Exception:
        try:
            from external.rqtll_widgets.utils.theme_manager import get_theme_manager as _gm2
            _theme_manager = _gm2()
        except Exception:
            _theme_manager = None


class TitleBar(QWidget):
    restartDaemonRequested = Signal()
    splitTerminalRequested = Signal()
    minimizeRequested = Signal()
    maximizeRequested = Signal()
    closeRequested = Signal()

    def __init__(self, parent=None, show_daemon: bool = False, show_tab: bool = False,
                 logo_variant: str = "color", icon_dirs: Optional[List[str]] = None, theme: str = "default.qss"):
        super().__init__(parent)
        self.setObjectName("TitleBar")
        self.setProperty('role', 'titlebox')
        self.setProperty('variant', 'default')
        self.setProperty('state', 'normal')
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.setFixedHeight(40)

        self.icon_dirs = icon_dirs or []

        self._logo = QLabel(self)
        self._logo.setText("")
        self._logo.setFixedSize(28, 28)
        self._logo.setScaledContents(True)

        self._title = QLabel(self)
        self._title.setText("")
        self._title.setProperty('role', 'title')
        self._title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        self._spacer = QSpacerItem(8, 8, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self._btn_min = self._make_button('minimize/default.svg', 'Minimize', theme=theme)
        self._btn_max = self._make_button('maximize/default.svg', 'Maximize', theme=theme)
        self._btn_close = self._make_button('close/default.svg', 'Close', theme=theme)
        self._btn_close.setProperty('role', 'close')
        self._btn_close.setProperty('variant', 'default')
        self._btn_close.setProperty('state', 'normal')

        layout = QHBoxLayout(self)
        layout.setContentsMargins(8, 4, 8, 4)
        layout.setSpacing(6)
        layout.addWidget(self._logo)
        layout.addWidget(self._title)
        layout.addItem(self._spacer)

        self._btn_daemon = self._make_button('daemon/default.svg', 'Restart daemon', theme=theme)
        layout.addWidget(self._btn_daemon)
        self._btn_daemon.clicked.connect(self.restartDaemonRequested.emit)
        self._btn_daemon.setVisible(show_daemon)

        self._btn_tab = self._make_button('tab/default.svg', 'Split terminal', theme=theme)
        layout.addWidget(self._btn_tab)
        self._btn_tab.clicked.connect(self.splitTerminalRequested.emit)
        self._btn_tab.setVisible(show_tab)

        layout.addWidget(self._btn_min)
        layout.addWidget(self._btn_max)
        layout.addWidget(self._btn_close)

        self._btn_min.clicked.connect(self.minimizeRequested.emit)
        self._btn_max.clicked.connect(self.maximizeRequested.emit)
        self._btn_close.clicked.connect(self.closeRequested.emit)

        self.setLogoVariant(logo_variant)

        if _theme_manager is not None:
            _theme_manager.themeChanged.connect(self._on_theme_changed)

    def _on_theme_changed(self, theme: str):
        try:
            self._apply_icon_to_button(self._btn_min, 'minimize/default.svg', theme)
            self._apply_icon_to_button(self._btn_max, 'maximize/default.svg', theme)
            self._apply_icon_to_button(self._btn_close, 'close/default.svg', theme)
            if hasattr(self, '_btn_daemon'):
                self._apply_icon_to_button(self._btn_daemon, 'daemon/default.svg', theme)
            if hasattr(self, '_btn_tab'):
                self._apply_icon_to_button(self._btn_tab, 'tab/default.svg', theme)
            self.setLogoVariant('color')
        except Exception:
            pass

    def _apply_icon_to_button(self, btn: QPushButton, rel_icon_path: str, theme: str = 'default.qss'):
        try:
            ico = QIcon()
            p = None
            if hasattr(icon_loader, 'resolve_icon_path'):
                p = icon_loader.resolve_icon_path(self.icon_dirs, rel_icon_path)
            if p and os.path.exists(p) and p.lower().endswith('.svg') and hasattr(icon_loader, 'recolor_svg_to_temp'):
                try:
                    p2 = icon_loader.recolor_svg_to_temp(p, theme=theme)
                    if p2 and os.path.exists(p2):
                        ico.addFile(p2)
                except Exception:
                    pass
            if ico.isNull():
                if hasattr(icon_loader, 'load_qicon'):
                    ico = icon_loader.load_qicon(rel_icon_path, icon_dirs=self.icon_dirs)
                elif p and os.path.exists(p):
                    ico.addFile(p)
            if not ico.isNull():
                btn.setIcon(ico)
                btn.setIconSize(QSize(18, 18))
        except Exception:
            pass

    def _make_button(self, rel_icon_path: str, tooltip: str, theme: str = "default.qss") -> QPushButton:
        btn = QPushButton(self)
        btn.setToolTip(tooltip)
        btn.setFlat(True)
        btn.setCursor(QCursor(Qt.PointingHandCursor))
        btn.setFixedSize(28, 28)
        try:
            ico = QIcon()
            p = None
            if hasattr(icon_loader, 'resolve_icon_path'):
                p = icon_loader.resolve_icon_path(self.icon_dirs, rel_icon_path)
            
            if p and os.path.exists(p) and p.lower().endswith('.svg') and hasattr(icon_loader, 'recolor_svg_to_temp'):
                try:
                    p2 = icon_loader.recolor_svg_to_temp(p, theme=theme)
                    if p2 and os.path.exists(p2):
                        ico.addFile(p2)
                except Exception:
                    pass

            if ico.isNull():
                if hasattr(icon_loader, 'load_qicon'):
                    ico = icon_loader.load_qicon(rel_icon_path, icon_dirs=self.icon_dirs)
                elif p and os.path.exists(p):
                    ico.addFile(p)

            if not ico.isNull():
                btn.setIcon(ico)
                btn.setIconSize(QSize(18, 18))
        except Exception:
            pass
        return btn

    def setTitle(self, text: str):
        self._title.setText(text)

    def setLogoVariant(self, variant: str):
        fname = f"logo-main-{variant}.svg"
        pm = None
        try:
            if hasattr(icon_loader, 'resolve_icon_path'):
                p = icon_loader.resolve_icon_path(self.icon_dirs, fname)
                if p and os.path.exists(p):
                    pm = QPixmap(p)
                else:
                    rel = os.path.join('branding', fname)
                    p2 = icon_loader.resolve_icon_path(self.icon_dirs, rel)
                    if p2 and os.path.exists(p2):
                        pm = QPixmap(p2)
        except Exception:
            pm = None

        if pm and not pm.isNull():
            self._logo.setPixmap(pm.scaled(self._logo.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def showDaemonButton(self, show: bool):
        self._btn_daemon.setVisible(show)

    def showTabButton(self, show: bool):
        self._btn_tab.setVisible(show)
