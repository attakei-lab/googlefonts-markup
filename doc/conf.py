# -- Path setup
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent / "libs"))

# -- Project information
project = "googlefonts-markup"
copyright = "2022, Kazuya Takei"
author = "Kazuya Takei"
release = "0.4.0"

# -- General configuration
extensions = [
    "sphinx_pyscript",
]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output
html_theme = "haiku"
html_static_path = ["_static"]
