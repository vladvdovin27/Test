from engine import calc


def test_primary():
    assert calc('1 * 2 - 3 + 1') == 0
