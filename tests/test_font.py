from googlefonts_markup import Font


def test_name():
    font = Font(family_name="Noto Sans JP")
    assert "family=Noto+Sans+JP" in font.css_url()
