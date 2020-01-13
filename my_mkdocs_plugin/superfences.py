def _escape(txt):
    """Basic html escaping."""

    txt = txt.replace('&', '&amp;')
    txt = txt.replace('<', '&lt;')
    txt = txt.replace('>', '&gt;')
    return txt


def fence_div_format(source, language, css_class, options, md):
    """Format source as div."""

    return '<div class="%s" match-brackets="true" highlight-on-fly="true" data-autocomplete="true" auto-indent="true">%s</div>' % (
        css_class, _escape(source))
