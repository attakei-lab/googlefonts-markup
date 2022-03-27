from typing import List, Literal, Optional, Tuple, Union
from urllib.parse import urlencode

from pydantic import BaseModel, validator

API_URL = "https://fonts.googleapis.com/css2"

FontDisplayValue = Literal["auto", "block", "swap", "fallback", "optional"]


class Axis(BaseModel):
    """
    Axis range definition
    """

    italic: bool = False
    """Using Italic style"""

    weight: Union[int, Tuple[int, int]] = 400

    def value(self) -> str:
        weight = (
            f"{self.weight[0]}..{self.weight[1]}"
            if isinstance(self.weight, tuple)
            else self.weight
        )
        return f"{1 if self.italic else 0},{weight}"

    @validator("weight")
    def check_weight_range(cls, v: Union[int, Tuple[int, int]]):
        if isinstance(v, int):
            assert 100 <= v <= 900, "Axis weight must be between 100 and 900"
            return v
        min_v, max_v = v
        assert 100 <= min_v <= 900, "Axis weight must be between 100 and 900"
        assert 100 <= max_v <= 900, "Axis weight must be between 100 and 900"
        assert (
            min_v < max_v
        ), "If axis weight is range, weight[0] must be less than weight[1]"
        return v


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
