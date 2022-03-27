from googlefonts_markup import Axis, Font


def test_name():
    font = Font(family_name="Noto Sans JP")
    assert "family=Noto+Sans+JP" in font.css_url()


def test_with_single_axis():
    axis_list = [
        Axis(weight=100),
    ]
    font = Font(family_name="Noto Sans JP", axis_list=axis_list)
    assert "family=Noto+Sans+JP:ital,wght@0,100" in font.css_url()


def test_with_multiple_axis():
    axis_list = [
        Axis(weight=100),
        Axis(italic=True, weight=100),
    ]
    font = Font(family_name="Noto Sans JP", axis_list=axis_list)
    assert "family=Noto+Sans+JP:ital,wght@0,100;1,100" in font.css_url()
