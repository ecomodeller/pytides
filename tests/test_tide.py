from pytides.constituent import noaa


def test_noaa():

    names = [c.name for c in noaa]
    assert "Mm" in names
