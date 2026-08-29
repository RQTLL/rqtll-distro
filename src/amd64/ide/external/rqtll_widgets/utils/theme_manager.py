from PySide6.QtCore import QObject, Signal

class ThemeManager(QObject):
    themeChanged = Signal(str)

_instance = None

def get_theme_manager():
    global _instance
    if _instance is None:
        _instance = ThemeManager()
    return _instance
