import pytest
from pydantic import ValidationError

from googlefonts_markup.models import Axis


def test_invalid_weight():
    with pytest.raises(ValidationError):
        Axis(weight=1)


def test_italic():
    axis = Axis(italic=True)
    assert axis.value() == "1,400"


def test_multiple_weight():
    axis = Axis(weight=(100, 900))
    assert axis.value() == "0,100..900"
