from .models import Font


def font_css_url(font_family: str) -> str:
    """
    Shortcut function to generate URL of font-css from font-family

    :param font: font-family or Font instance
    :returns: Font CSS URL
    """
    font = Font(family_name=font_family)
    return font.css_url()
