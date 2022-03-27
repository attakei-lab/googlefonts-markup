"""
Sphinx extension source for googlefonts-markup
"""
import logging

try:
    from sphinx.application import Sphinx
    from sphinx.config import Config
except ImportError as err:
    logging.error(f"To use {__name__}, you must install sphinx")
    raise (err)

from ..models import Font, FontSet


def convert_googlefonts(app: Sphinx, config: Config):
    font_obj = None
    if not config.googlefonts_font:
        return
    elif isinstance(config.googlefonts_font, Font):
        font_obj = config.googlefonts_font
    elif isinstance(config.googlefonts_font, str):
        font_obj = Font(family_name=config.googlefonts_font)
    elif isinstance(config.googlefonts_font, dict):
        font_obj = Font.parse_obj(config.googlefonts_font)
    else:
        raise ValueError("Invalid format googlefonts_font")
    config.googlefonts_font = font_obj


def add_fontset_url(app: Sphinx, env):
    if not app.config.googlefonts_font:
        return
    if not app.config.googlefonts_add_css_url:
        return
    fontset = FontSet(
        fonts=[app.config.googlefonts_font], display=app.config.googlefonts_display
    )
    app.add_css_file(fontset.css_url())


def setup(app: Sphinx):
    app.add_config_value("googlefonts_add_css_url", False, True)
    app.add_config_value("googlefonts_font", None, True)
    app.add_config_value("googlefonts_display", "auto", True)
    app.connect("config-inited", convert_googlefonts)
    app.connect("env-updated", add_fontset_url)
