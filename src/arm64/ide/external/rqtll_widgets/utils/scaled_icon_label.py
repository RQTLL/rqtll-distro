from typing import Optional

from PySide6.QtWidgets import QLabel, QSizePolicy
from PySide6.QtCore import Qt, QSize, QTimer
from PySide6.QtGui import QPixmap


class ScaledIconLabel(QLabel):
    def __init__(self, parent=None, max_size: Optional[int] = 256, base_size: int = 128, scale_power: float = 1.0,
                 window_influence: float = 0.9, window_scale_factor: float = 0.45):
        super().__init__(parent)
        self._original = QPixmap()
        self.max_size = max_size or 0
        self.base_size = max(1, int(base_size))
        self.scale_power = float(scale_power)
        self.window_influence = float(window_influence)
        self.window_scale_factor = float(window_scale_factor)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred))

    def set_icon(self, path_or_pixmap):
        if isinstance(path_or_pixmap, QPixmap):
            self._original = path_or_pixmap
        else:
            self._original = QPixmap(path_or_pixmap)
        self._rescale()
        QTimer.singleShot(0, self._rescale)

    def setPixmap(self, pixmap: QPixmap):
        self._original = QPixmap(pixmap)
        self._rescale()
        QTimer.singleShot(0, self._rescale)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._rescale()

    def _rescale(self):
        if self._original.isNull():
            super().setPixmap(QPixmap())
            return
        w = max(1, self.width())
        h = max(1, self.height())
        local_avail = float(min(w, h))

        win = self.window()
        win_avail = 0.0
        try:
            ww = max(1, win.width())
            wh = max(1, win.height())
            win_avail = float(min(ww, wh)) * float(self.window_scale_factor)
        except Exception:
            win_avail = local_avail

        avail = (1.0 - self.window_influence) * local_avail + self.window_influence * win_avail

        override_target = None
        try:
            tw = win.width()
            th = win.height()
            if tw < 1200 and th < 680:
                override_target = 96
            elif 1200 <= tw <= 1500 and 680 <= th <= 750:
                override_target = 256
            elif tw > 1500 and th > 750:
                override_target = 384
        except Exception:
            override_target = None

        bs = float(self.base_size)
        ms = float(self.max_size) if (self.max_size and self.max_size > 0) else max(bs * 4.0, bs)

        span = max(1.0, ms - bs)
        norm = (avail - bs) / span
        if norm > 1.0:
            norm = 1.0
        if norm < -1.0:
            norm = -1.0

        if norm >= 0.0:
            factor = (norm ** self.scale_power)
        else:
            factor = -((abs(norm)) ** self.scale_power)

        scaled_size = int(round(bs + factor * span))

        if override_target is not None:
            scaled_size = int(override_target)

        min_allowed = max(8, int(bs // 4))
        if scaled_size < min_allowed:
            scaled_size = min_allowed

        if ms and ms > 0:
            scaled_size = min(scaled_size, int(ms))

        scaled = self._original.scaled(QSize(scaled_size, scaled_size), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        super().setPixmap(scaled)

    def set_max_size(self, max_size: int):
        self.max_size = max_size
        self._rescale()
