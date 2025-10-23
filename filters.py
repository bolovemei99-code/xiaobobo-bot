# filters.py
def filter_message(text, filters, replacements):
    if not text:
        return None
    for word in filters:
        if word in text:
            return None
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text
