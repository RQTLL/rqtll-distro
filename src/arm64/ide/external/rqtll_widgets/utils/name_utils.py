import re


def sanitize_item_name(raw: str, ext: str = "", default_base: str = "new_item") -> str:
    if raw is None:
        raw = ""
    combined = raw.strip()
    combined = combined.replace(' ', '_')
    base = re.sub(r'[^A-Za-z0-9._-]', '', combined)
    base = (base or '').lower().rstrip('.')
    if not base:
        base = default_base
    if not base[0].isalpha():
        base = 'a' + base
    if ext and not base.endswith(ext):
        return base + ext
    return base
