from pathlib import Path

import tomli

prj = tomli.loads((Path(__file__).parent.parent / "pyproject.toml").read_text())[
    "tool"
]["poetry"]

project = prj["name"]
copyright = "2022, Kazuya Takei"
author = "Kazuya Takei"
release = prj["version"]

extensions = [
    "googlefonts_markup.ext.sphinx",
]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "alabaster"
html_theme_options = {
    "caption_font_family": "'Noto Sans JP', sans-serif",
    "head_font_family": "'Noto Sans JP', sans-serif",
    "font_family": "'Noto Sans JP', sans-serif",
}
html_static_path = ["_static"]
googlefonts_font = {
    "family_name": "Noto Sans JP",
    "axis_list": [
        {
            "italic": True,
        }
    ],
}
googlefonts_add_css_url = True
