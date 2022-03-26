from googlefonts_markup import Font, FontSet


def test_single_font_only():
    font = Font(family_name="Noto Sans JP")
    fontset = FontSet(fonts=[font])
    assert "family=Noto+Sans+JP" in fontset.css_url()


def test_with_display():
    font = Font(family_name="Noto Sans JP")
    fontset = FontSet(fonts=[font], display="swap")
    assert "family=Noto+Sans+JP" in fontset.css_url()
    assert "display=swap" in fontset.css_url()
    assert "text=" not in fontset.css_url()


def test_with_text():
    font = Font(family_name="Noto Sans JP")
    fontset = FontSet(fonts=[font], text="Hello world")
    assert "family=Noto+Sans+JP" in fontset.css_url()
    assert "text=Hello+world" in fontset.css_url()
