from __future__ import annotations

import os
from typing import List, Optional

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QPixmap, QCursor, QIcon, QFont
from PySide6.QtWidgets import QLabel, QFrame, QVBoxLayout, QApplication, QSizePolicy

try:
    from .scaled_icon_label import ScaledIconLabel
except Exception:
    import importlib.util as _il, os as _os
    _spec = _il.spec_from_file_location("scaled_icon_label", _os.path.join(_os.path.dirname(__file__), "scaled_icon_label.py"))
    _mod = _il.module_from_spec(_spec)
    _spec.loader.exec_module(_mod)
    ScaledIconLabel = _mod.ScaledIconLabel

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


class FrameOptionButtonWidget(QFrame):
    clicked = Signal()
    toggled = Signal(bool)

    def __init__(self, icon_path: Optional[str] = None, title: str = "", info: str = "",
                 parent=None, icon_dirs: Optional[List[str]] = None,
                 apply_theme_from_palette: bool = True, theme: str = 'default.qss',
                 button_id: str = ""):
        super().__init__(parent)
        self.button_id = button_id
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setObjectName("FrameOptionButtonWidget")
        self.setProperty('role', 'frame-button')
        self.setProperty('variant', 'default')
        self.setProperty('state', 'normal')
        self.icon_dirs = icon_dirs or []
        self.max_size = 46
        self._checked = False

        self.icon = ScaledIconLabel(max_size=self.max_size, parent=self, base_size=self.max_size, scale_power=1.0)
        self.icon.setMinimumSize(self.max_size, self.max_size)
        self.icon.setStyleSheet("background: transparent;")
        
        # Title and Info/Subtitle
        self.title = QLabel(title, parent=self)
        self.title.setProperty('role', 'title')
        self.title.setStyleSheet("background: transparent;")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_font = self.title.font()
        title_font.setBold(True)
        self.title.setFont(title_font)
        
        self.info = QLabel(info, parent=self)
        self.info.setProperty('role', 'info')
        self.info.setStyleSheet("background: transparent;")
        self.info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.info.setWordWrap(True)
        info_font = self.info.font()
        info_font.setBold(False)
        self.info.setFont(info_font)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(8, 8, 8, 8)
        layout.setSpacing(6)
        layout.addWidget(self.icon, 1, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.title, 0, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.info, 0, Qt.AlignmentFlag.AlignCenter)

        if icon_path:
            self._icon_path = icon_path
            pix = self._load_pix(icon_path, theme=theme)
            if pix and not pix.isNull():
                self.icon.setPixmap(pix)
        else:
            self._icon_path = None

        if _theme_manager is not None:
            _theme_manager.themeChanged.connect(self._on_theme_changed)

    def _on_theme_changed(self, theme: str):
        try:
            if getattr(self, '_icon_path', None):
                pix = self._load_pix(self._icon_path, theme=theme)
                if pix and not pix.isNull():
                    self.icon.setPixmap(pix)
        except Exception:
            pass

    def enterEvent(self, event):
        super().enterEvent(event)
        try:
            self.setProperty('hover', True)
            self.style().unpolish(self)
            self.style().polish(self)
            self.update()
        except Exception:
            pass

    def leaveEvent(self, event):
        super().leaveEvent(event)
        try:
            self.setProperty('hover', False)
            self.style().unpolish(self)
            self.style().polish(self)
            self.update()
        except Exception:
            pass

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        try:
            if not self.isChecked():
                self.setProperty('state', 'pressed')
                self.style().unpolish(self)
                self.style().polish(self)
                self.update()
        except Exception:
            pass

    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)
        try:
            if not self.isChecked():
                self.setChecked(True)
            else:
                self.setProperty('state', 'checked')
                self.style().unpolish(self)
                self.style().polish(self)
                self.update()
        except Exception:
            pass
        self.clicked.emit()

    def setVariant(self, variant: str):
        """Set visual variant used by QSS selectors (e.g. 'primary')."""
        try:
            self.setProperty('variant', variant)
            self.style().unpolish(self)
            self.style().polish(self)
            self.update()
        except Exception:
            pass

    def isChecked(self) -> bool:
        return getattr(self, '_checked', False)

    def setChecked(self, checked: bool):
        if getattr(self, '_checked', False) == checked:
            return
        self._checked = checked
        self.setProperty('state', 'checked' if checked else 'normal')
        self.style().unpolish(self)
        self.style().polish(self)
        self.update()
        
        self.toggled.emit(checked)
        
        if checked and self.parent():
            for sibling in self.parent().findChildren(FrameOptionButtonWidget):
                if sibling is not self:
                    if sibling.isChecked():
                        sibling.setChecked(False)

    def _load_pix(self, rel_path: str, theme: str = 'default.qss') -> QPixmap:
        base = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))

        try:
            if hasattr(icon_loader, 'recolor_svg_to_temp'):
                temp_svg = icon_loader.recolor_svg_to_temp(rel_path, theme=theme)
            else:
                temp_svg = rel_path
            if temp_svg and os.path.exists(temp_svg):
                pm = QPixmap(temp_svg)
                if pm and not pm.isNull():
                    return pm
                try:
                    ico = QIcon(temp_svg)
                    pm2 = ico.pixmap(min(self.max_size or 256, 512), min(self.max_size or 256, 512))
                    if pm2 and not pm2.isNull():
                        return pm2
                except Exception:
                    pass
        except Exception as e:
            print(f"[FrameOptionButtonWidget] _resolve_icon error: {e}")

        resolved = None
        try:
            if hasattr(icon_loader, 'resolve_icon_path'):
                resolved = icon_loader.resolve_icon_path(self.icon_dirs, rel_path)
                if resolved and os.path.exists(resolved):
                    pm = QPixmap(resolved)
                    if pm and not pm.isNull():
                        return pm
                    try:
                        ico = QIcon(resolved)
                        pm2 = ico.pixmap(min(self.max_size or 256, 512), min(self.max_size or 256, 512))
                        if pm2 and not pm2.isNull():
                            return pm2
                    except Exception:
                        pass
        except Exception as e:
            print(f"[FrameOptionButtonWidget] resolve_icon_path error: {e}")

        try:
            pix = icon_loader.load_qpixmap(rel_path, icon_dirs=self.icon_dirs)
            if pix and not pix.isNull():
                return pix
        except Exception as e:
            print(f"[FrameOptionButtonWidget] load_qpixmap error: {e}")

        if os.path.isabs(rel_path) and os.path.exists(rel_path):
            return QPixmap(rel_path)

        candidates = [
            os.path.normpath(os.path.join(base, 'icons', rel_path)),
            os.path.normpath(os.path.join(base, '..', 'rqtll_components', 'assets', 'branding', rel_path)),
            os.path.normpath(os.path.join(base, '..', 'rqtll_components', 'assets', 'icons', rel_path)),
            os.path.normpath(os.path.join(base, '..', 'rqtll-components', 'assets', 'branding', rel_path)),
            os.path.normpath(os.path.join(base, '..', 'rqtll-components', 'assets', 'icons', rel_path)),
            os.path.normpath(rel_path),
        ]
        for p in candidates:
            if os.path.exists(p):
                try:
                    return QPixmap(p)
                except Exception:
                    pass

        placeholder = os.path.join(base, 'icons', 'placeholder.svg')
        if os.path.exists(placeholder):
            print(f"[FrameOptionButtonWidget] icon not found: {rel_path!r}. Using placeholder. Candidates checked: {candidates}")
            return QPixmap(placeholder)

        print(f"[FrameOptionButtonWidget] icon not found: {rel_path!r}. Candidates checked: {candidates}")
        return QPixmap()

    def setTitle(self, text: str):
        self.title.setText(text)

    def setInfo(self, text: str):
        self.info.setText(text)

    def setIcon(self, path: str, theme: str = 'default.qss'):
        pix = self._load_pix(path, theme=theme)
        if pix and not pix.isNull():
            self.icon.setPixmap(pix)
