from .start import soma


def test_soma():
    """testing soma"""

    result = soma(2, 5)
    assert result == 7
