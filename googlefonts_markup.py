from urllib.parse import urlencode

from pydantic import BaseModel

API_URL = "https://fonts.googleapis.com/css2"


class Font(BaseModel):
    """
    Font spec of Google Fonts
    """

    family_name: str

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
