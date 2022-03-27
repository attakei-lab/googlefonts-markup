from typing import List, Literal, Optional
from urllib.parse import urlencode

from pydantic import BaseModel

API_URL = "https://fonts.googleapis.com/css2"

FontDisplayValue = Literal["auto", "block", "swap", "fallback", "optional"]


class Axis(BaseModel):
    """
    Axis range definition
    """

    italic: bool = False
    """Using Italic style"""

    weight: int = 400

    def value(self) -> str:
        return f"{1 if self.italic else 0},{self.weight}"


class Font(BaseModel):
    """
    Font spec of Google Fonts
    """

    family_name: str

    axis_list: List[Axis] = []

    def spec(self):
        if len(self.axis_list) == 0:
            return self.family_name
        axis_range = "ital,wght@" + ";".join([axis.value() for axis in self.axis_list])
        return f"{self.family_name}:{axis_range}"

    def css_url(self) -> str:
        """
        Build and return URL for using itself by Google Fonts.
        """
        query = {
            "family": self.spec(),
        }
        return f"{API_URL}?{urlencode(query, safe=':@,;')}"

    def css_tag(self) -> str:
        """
        Return HTML element with ``self.css_url()``.
        """
        return f'<link href="{self.css_url()}" rel="stylesheet">'


class FontSet(BaseModel):
    """
    Fonts spec to use Google Fonts.
    """

    fonts: List[Font]

    text: Optional[str]

    display: FontDisplayValue = "auto"

    def css_url(self) -> str:
        """
        Build and return URL for using itself by Google Fonts.
        """
        query = [("family", font.spec()) for font in self.fonts]
        if self.text:
            query.append(("text", self.text))
        query.append(("display", self.display))
        return f"{API_URL}?{urlencode(query, safe=',@:;')}"

    def css_tag(self) -> str:
        """
        Return HTML element with ``self.css_url()``.
        """
        return f'<link href="{self.css_url()}" rel="stylesheet">'
