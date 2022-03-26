from typing import List, Literal, Optional
from urllib.parse import urlencode

from pydantic import BaseModel

API_URL = "https://fonts.googleapis.com/css2"

FontDisplayValue = Literal["auto", "block", "swap", "fallback", "optional"]


class Font(BaseModel):
    """
    Font spec of Google Fonts
    """

    family_name: str

    def spec(self):
        return self.family_name

    def css_url(self) -> str:
        """
        Build and return URL for using itself by Google Fonts.
        """
        query = {
            "family": self.family_name,
        }
        return f"{API_URL}?{urlencode(query)}"

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
        return f"{API_URL}?{urlencode(query)}"

    def css_tag(self) -> str:
        """
        Return HTML element with ``self.css_url()``.
        """
        return f'<link href="{self.css_url()}" rel="stylesheet">'
