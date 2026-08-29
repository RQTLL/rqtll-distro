import os
import tempfile
import xml.etree.ElementTree as ET
from typing import Iterable, Optional

from PySide6.QtGui import QIcon, QPixmap


def resolve_icon_path(icon_dirs: Optional[Iterable[str]], rel_path: str) -> str:
    if not icon_dirs:
        return rel_path

    if isinstance(icon_dirs, str):
        icon_dirs = [icon_dirs]

    for base in icon_dirs:
        try:
            cand = os.path.normpath(os.path.join(base, rel_path))
        except Exception:
            continue
        if os.path.exists(cand):
            return cand
        parts = rel_path.replace('\\', '/').lstrip('/').split('/')
        if parts and parts[0] == 'icons':
            tail = '/'.join(parts[1:])
            try:
                cand2 = os.path.normpath(os.path.join(base, tail))
            except Exception:
                cand2 = None
            if cand2 and os.path.exists(cand2):
                return cand2

    return rel_path


def load_qicon(rel_path: str, icon_dirs: Optional[Iterable[str]] = None, fallback: Optional[str] = None) -> QIcon:
    path = resolve_icon_path(icon_dirs, rel_path)
    ico = QIcon()
    if os.path.exists(path):
        ico.addFile(path)
        return ico
    if fallback and os.path.exists(fallback):
        ico.addFile(fallback)
        return ico
    return ico


def load_qpixmap(rel_path: str, icon_dirs: Optional[Iterable[str]] = None, fallback: Optional[str] = None) -> QPixmap:
    path = resolve_icon_path(icon_dirs, rel_path)
    pix = QPixmap()
    if os.path.exists(path):
        pix.load(path)
        return pix
    if fallback and os.path.exists(fallback):
        pix.load(fallback)
        return pix
    return pix


_svg_cache = {}


def _parse_qss_palette(qss_paths):
    for q in qss_paths:
        try:
            if not os.path.exists(q):
                continue
            data = open(q, 'r', encoding='utf-8').read()
            start = data.find('/* @palette')
            if start < 0:
                continue
            end = data.find('*/', start)
            if end < 0:
                continue
            block = data[start:end]
            for line in block.splitlines()[1:]:
                line = line.strip().lstrip('/*').strip()
                if not line or ':' not in line:
                    continue
                k, v = line.split(':', 1)
                if k.strip() == 'color':
                    return v.strip()
        except Exception:
            continue
    return None


def _recolor_svg_tree(tree, color):
    root = tree.getroot()
    changed = False
    for el in root.iter():
        style = el.get('style')
        if style:
            parts = [p.strip() for p in style.split(';') if p.strip()]
            d = {}
            for p in parts:
                if ':' in p:
                    kk, vv = p.split(':', 1)
                    d[kk.strip()] = vv.strip()
            if d.get('fill') != color or d.get('stroke') != color:
                d['fill'] = color
                d['stroke'] = color
                new_style = ';'.join(f"{k}:{v}" for k, v in d.items()) + ';'
                el.set('style', new_style)
                changed = True

        for attr in ('fill', 'stroke'):
            v = el.get(attr)
            if v and v.strip() and v.strip() != color:
                el.set(attr, color)
                changed = True

    root_style = root.get('style')
    if not root_style:
        root.set('style', f'fill:{color};stroke:{color};')
        changed = True
    else:
        if 'fill:' not in root_style or 'stroke:' not in root_style:
            parts = [p.strip() for p in root_style.split(';') if p.strip()]
            keys = {p.split(':',1)[0].strip() for p in parts if ':' in p}
            if 'fill' not in keys:
                parts.append(f'fill:{color}')
            if 'stroke' not in keys:
                parts.append(f'stroke:{color}')
            root.set('style', ';'.join(parts) + ';')
            changed = True
    return changed


def _resolve_icon(icon_dirs: Optional[Iterable[str]], rel_path: str, theme: str = 'default.qss') -> str:
    path = resolve_icon_path(icon_dirs, rel_path)
    if not path or not os.path.exists(path):
        return path

    if not path.lower().endswith('.svg'):
        return path

    qss_paths = [
        os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '..', 'rqtll_components', 'styles', theme)),
        os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '..', 'rqtll_components', 'styles', 'themes', theme)),
        os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '..', 'rqtll-components', 'styles', theme)),
        os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '..', 'rqtll-components', 'styles', 'themes', theme)),
    ]
    color = _parse_qss_palette(qss_paths)
    if not color:
        color = '#000000'

    key = (os.path.abspath(path), color)
    if key in _svg_cache and os.path.exists(_svg_cache[key]):
        return _svg_cache[key]

    try:
        tree = ET.parse(path)
    except Exception:
        return path

    changed = _recolor_svg_tree(tree, color)

    if not changed:
        return path

    try:
        tf = tempfile.NamedTemporaryFile(delete=False, suffix='.svg', prefix='rqtll_icon_')
        tf.close()
        tree.write(tf.name, encoding='utf-8', xml_declaration=True)
        _svg_cache[key] = tf.name
        return tf.name
    except Exception:
        return path


def recolor_svg_to_temp(src_path: str, color: Optional[str] = None, theme: str = 'default.qss') -> str:
    if not src_path or not os.path.exists(src_path):
        return src_path

    if not src_path.lower().endswith('.svg'):
        return src_path

    qss_paths = [
        os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '..', 'rqtll_components', 'styles', theme)),
        os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '..', 'rqtll_components', 'styles', 'themes', theme)),
        os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '..', 'rqtll-components', 'styles', theme)),
        os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '..', 'rqtll-components', 'styles', 'themes', theme)),
    ]
    if color is None:
        color = _parse_qss_palette(qss_paths) or '#000000'

    key = (os.path.abspath(src_path), color)
    if key in _svg_cache and os.path.exists(_svg_cache[key]):
        return _svg_cache[key]

    try:
        tree = ET.parse(src_path)
    except Exception:
        return src_path

    changed = _recolor_svg_tree(tree, color)

    if not changed:
        return src_path

    try:
        tf = tempfile.NamedTemporaryFile(delete=False, suffix='.svg', prefix='rqtll_icon_')
        tf.close()
        tree.write(tf.name, encoding='utf-8', xml_declaration=True)
        _svg_cache[key] = tf.name
        return tf.name
    except Exception:
        return src_path


def update_cached_icons_color(theme_name: str):
    qss_paths = [
        os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '..', 'rqtll_components', 'styles', theme_name)),
        os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '..', 'rqtll_components', 'styles', 'themes', theme_name)),
        os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '..', 'rqtll-components', 'styles', theme_name)),
        os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '..', 'rqtll-components', 'styles', 'themes', theme_name)),
    ]
    color = _parse_qss_palette(qss_paths)
    if not color:
        return

    for (src_path, _), temp_path in list(_svg_cache.items()):
        if os.path.exists(temp_path) and os.path.exists(src_path):
            try:
                tree = ET.parse(src_path)
                if _recolor_svg_tree(tree, color):
                    tree.write(temp_path, encoding='utf-8', xml_declaration=True)
            except Exception as e:
                print(f"Error updating cached SVG: {e}")
