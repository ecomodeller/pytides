import pandas as pd
from pytides.constituent import noaa
from pytides.tide import Tide


def test_noaa():

    names = [c.name for c in noaa]
    assert "Mm" in names


def test_decompose():

    df = pd.read_csv("tests/testdata/wl.csv", parse_dates=True, index_col=0)

    my_tide = Tide.decompose(heights=df.heights, t=df.index)

    assert len(my_tide.model) == 43