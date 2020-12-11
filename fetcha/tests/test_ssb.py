import random
import time

import fetcha as fetcha


def test_fetch_n_pivot_lst_months_no():
    time.sleep(random.randint(1, 5))
    ssb_10948 = fetcha.SSB("10948")
    periods = ["2019M12", "2020M01"]
    df = ssb_10948.fetch(periods)
    df = ssb_10948.pivot(df)
    assert df.shape[1] == 3
    assert list(df.index.names) == ["eiersektor", "statistikkvariabel", "måned"]
    assert df.index.get_level_values("måned").unique().to_list() == periods


def test_fetch_n_pivot_lst_months_en():
    time.sleep(random.randint(1, 5))
    ssb_10948 = fetcha.SSB("10948", language="en")
    periods = ["2019M12", "2020M01"]
    df = ssb_10948.fetch(periods)
    df = ssb_10948.pivot(df)
    assert df.shape[1] == 3
    assert list(df.index.names) == ["holding sector", "contents", "month"]
    assert df.index.get_level_values("month").unique().to_list() == periods


def test_fetch_n_pivot_lst_year_no():
    time.sleep(random.randint(1, 5))
    ssb_10948 = fetcha.SSB("10948")
    periods = "2019"
    df = ssb_10948.fetch(periods)
    df = ssb_10948.pivot(df)
    assert df.shape[1] == 3
    assert list(df.index.names) == ["eiersektor", "statistikkvariabel", "måned"]
    assert df.index.get_level_values("måned").unique().to_list() == [
        "2019M" + str(i).zfill(2) for i in range(1, 13)
    ]
