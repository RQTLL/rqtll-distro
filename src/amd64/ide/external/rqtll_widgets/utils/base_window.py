import os
from PySide6.QtWidgets import QWidget, QVBoxLayout, QFrame, QSizePolicy
from PySide6.QtCore import Qt, QEvent, Signal, QTimer
from PySide6.QtGui import QIcon, QPixmap

try:
    from .titlebar import TitleBar
except ImportError:
    try:
        from titlebar import TitleBar
    except ImportError:
        import importlib.util as _il, os as _os
        _spec = _il.spec_from_file_location("titlebar", _os.path.join(_os.path.dirname(__file__), "titlebar.py"))
        _mod = _il.module_from_spec(_spec)
        _spec.loader.exec_module(_mod)
        TitleBar = _mod.TitleBar

try:
    from .icon_loader import update_cached_icons_color
except ImportError:
    try:
        from icon_loader import update_cached_icons_color
    except ImportError:
        def update_cached_icons_color(theme):
            pass

class DemoWindow(QWidget):
    uiReinitialized = Signal()
    def __init__(self, ui_class, title: str = None, icon_dirs: list = None, parent=None, 
                 logo_variant: str = "color", show_daemon: bool = False, 
                 show_tab: bool = False, theme: str = "default.qss"):
        super().__init__(parent)
        
        self.setMouseTracking(True)
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(3, 3, 3, 3)
        layout.setSpacing(0)
        
        self.main_container = QFrame(self)
        self.main_container.setObjectName("MainContainer")
        self.main_container.setProperty("state", "normal")
        self.main_container.setCursor(Qt.CursorShape.ArrowCursor)
        container_layout = QVBoxLayout(self.main_container)
        container_layout.setContentsMargins(0, 0, 0, 0)
        container_layout.setSpacing(0)

        self.titlebar = TitleBar(self, show_daemon=show_daemon, logo_variant=logo_variant,
                                 show_tab=show_tab, icon_dirs=icon_dirs, theme=theme)
        if title:
            self.titlebar.setTitle(title)

        self.titlebar.minimizeRequested.connect(self.showMinimized)
        self.titlebar.maximizeRequested.connect(self._toggle_maximize)
        self.titlebar.closeRequested.connect(self.close)

        self.content = QWidget(self)
        self.content.setObjectName("Content")
        self.ui = ui_class()
        
        try:
            self.ui.setupUi(self.content, icon_dirs=icon_dirs, theme=theme)
        except TypeError:
            self.ui.setupUi(self.content)

        self._ui_class = ui_class
        self._initial_icon_dirs = icon_dirs
        self._initial_theme = theme

        try:
            try:
                from .theme_manager import get_theme_manager
            except ImportError:
                try:
                    from theme_manager import get_theme_manager
                except ImportError:
                    import importlib.util as _il, os as _os
                    _spec = _il.spec_from_file_location("theme_manager", _os.path.join(_os.path.dirname(__file__), "theme_manager.py"))
                    _mod = _il.module_from_spec(_spec)
                    _spec.loader.exec_module(_mod)
                    get_theme_manager = _mod.get_theme_manager
            
            tm = get_theme_manager()
            if tm is not None:
                tm.themeChanged.connect(self._on_theme_changed)
        except Exception:
            pass

        container_layout.addWidget(self.titlebar)
        container_layout.addWidget(self.content)
        layout.addWidget(self.main_container)

        content_min = self.content.minimumSize()
        content_max = self.content.maximumSize()
        if content_min.isValid() and content_max.isValid() and content_min == content_max and content_min.width() > 0:
            title_height = 40
            fixed_width = content_min.width() + 16
            fixed_height = content_min.height() + 16 + title_height
            self.setFixedSize(fixed_width, fixed_height)
            try:
                self.titlebar._btn_max.setVisible(False)
            except Exception:
                pass

        self._drag_pos = None
        self._resizing = False
        self._resize_edge = None
        self.titlebar.installEventFilter(self)

    def _get_resize_edge_and_cursor(self, pos):
        margin = 3
        rect = self.rect()
        
        on_left = pos.x() < margin
        on_right = pos.x() > rect.width() - margin
        on_top = pos.y() < margin
        on_bottom = pos.y() > rect.height() - margin
        
        edge = None
        cursor = Qt.CursorShape.ArrowCursor
        
        if on_top and on_left:
            edge = Qt.TopEdge | Qt.LeftEdge
            cursor = Qt.CursorShape.SizeFDiagCursor
        elif on_top and on_right:
            edge = Qt.TopEdge | Qt.RightEdge
            cursor = Qt.CursorShape.SizeBDiagCursor
        elif on_bottom and on_left:
            edge = Qt.BottomEdge | Qt.LeftEdge
            cursor = Qt.CursorShape.SizeBDiagCursor
        elif on_bottom and on_right:
            edge = Qt.BottomEdge | Qt.RightEdge
            cursor = Qt.CursorShape.SizeFDiagCursor
        elif on_left:
            edge = Qt.LeftEdge
            cursor = Qt.CursorShape.SizeHorCursor
        elif on_right:
            edge = Qt.RightEdge
            cursor = Qt.CursorShape.SizeHorCursor
        elif on_top:
            edge = Qt.TopEdge
            cursor = Qt.CursorShape.SizeVerCursor
        elif on_bottom:
            edge = Qt.BottomEdge
            cursor = Qt.CursorShape.SizeVerCursor
            
        return edge, cursor

    def mousePressEvent(self, event):
        if self.minimumSize() == self.maximumSize():
            return
        if event.button() == Qt.LeftButton:
            pos = event.position().toPoint()
            edge, _ = self._get_resize_edge_and_cursor(pos)
            if edge is not None:
                window_handle = self.window().windowHandle()
                if window_handle:
                    window_handle.startSystemResize(edge)
                    event.accept()
                    return

    def mouseMoveEvent(self, event):
        if self.minimumSize() == self.maximumSize():
            self.setCursor(Qt.CursorShape.ArrowCursor)
            return
        pos = event.position().toPoint()
        _, cursor = self._get_resize_edge_and_cursor(pos)
        self.setCursor(cursor)

    def mouseReleaseEvent(self, event):
        self.setCursor(Qt.CursorShape.ArrowCursor)

    def _toggle_maximize(self):
        if self.minimumSize() == self.maximumSize():
            return
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def eventFilter(self, obj, event):
        if obj is self.titlebar:
            if event.type() == QEvent.MouseButtonPress:
                if event.button() == Qt.LeftButton:
                    self._drag_pos = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
                    self.titlebar.setCursor(Qt.CursorShape.ClosedHandCursor)
                    window_handle = self.window().windowHandle()
                    if window_handle:
                        window_handle.startSystemMove()
                        return True
                    return True
            elif event.type() == QEvent.MouseMove:
                if event.buttons() & Qt.LeftButton and self._drag_pos is not None:
                    self.titlebar.setCursor(Qt.CursorShape.ClosedHandCursor)
                    self.move(event.globalPosition().toPoint() - self._drag_pos)
                    return True
                else:
                    self.titlebar.unsetCursor()
            elif event.type() == QEvent.MouseButtonRelease:
                self.titlebar.unsetCursor()
                if self._drag_pos is not None:
                    self._drag_pos = None
                    return True
            elif event.type() == QEvent.Leave:
                self.titlebar.unsetCursor()
            elif event.type() == QEvent.MouseButtonDblClick:
                self._toggle_maximize()
                return True
        return super().eventFilter(obj, event)

    def changeEvent(self, event):
        if event.type() == QEvent.WindowStateChange:
            state = "maximized" if self.isMaximized() else "normal"
            self.main_container.setProperty("state", state)
            
            if self.isMaximized():
                self.layout().setContentsMargins(0, 0, 0, 0)
            else:
                self.layout().setContentsMargins(3, 3, 3, 3)
                
            self.main_container.style().unpolish(self.main_container)
            self.main_container.style().polish(self.main_container)
        super().changeEvent(event)

    def _on_theme_changed(self, theme: str):
        try:
            update_cached_icons_color(theme)
            self.style().unpolish(self)
            self.style().polish(self)
            for widget in self.findChildren(QWidget):
                if hasattr(widget, "_rqtll_icon_path"):
                    widget.setIcon(QIcon(widget._rqtll_icon_path))
                if hasattr(widget, "_rqtll_pixmap_path"):
                    ico = QIcon(widget._rqtll_pixmap_path)
                    if hasattr(widget, "_rqtll_pixmap_size") and widget._rqtll_pixmap_size.width() > 0:
                        pix = ico.pixmap(widget._rqtll_pixmap_size)
                    else:
                        pix = ico.pixmap(32, 32)
                    widget.setPixmap(pix)
                if hasattr(widget, "topLevelItemCount"):
                    def traverse_tree(item):
                        if hasattr(item, "_rqtll_icon_paths"):
                            for col, path in item._rqtll_icon_paths.items():
                                item.setIcon(col, QIcon(path))
                        for i in range(item.childCount()):
                            traverse_tree(item.child(i))
                    for i in range(widget.topLevelItemCount()):
                        traverse_tree(widget.topLevelItem(i))
                if hasattr(widget, "count") and hasattr(widget, "item"):
                    for i in range(widget.count()):
                        item = widget.item(i)
                        if item and hasattr(item, "_rqtll_icon_path"):
                            item.setIcon(QIcon(item._rqtll_icon_path))
                if hasattr(widget, "rowCount") and hasattr(widget, "item"):
                    for r in range(widget.rowCount()):
                        for c in range(widget.columnCount()):
                            item = widget.item(r, c)
                            if item and hasattr(item, "_rqtll_icon_path"):
                                item.setIcon(QIcon(item._rqtll_icon_path))
                for action in widget.actions():
                    if hasattr(action, "_rqtll_icon_path"):
                        action.setIcon(QIcon(action._rqtll_icon_path))
                widget.style().unpolish(widget)
                widget.style().polish(widget)
            try:
                self.uiReinitialized.emit()
            except Exception:
                pass
        except Exception:
            pass
