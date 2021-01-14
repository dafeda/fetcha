import random
import time

import fetcha as fetcha
from pyjstat import pyjstat


def test_against_ssb_made_data():
    df_ssb = pyjstat.Dataset.read(
        "https://data.ssb.no/api/v0/dataset/934513.json?lang=no"
    )
    df_ssb = df_ssb.write("dataframe")
    df_ssb = df_ssb.pivot(index="år", columns="statistikkvariabel", values="value")

    ssb_12880 = fetcha.SSB("12880", language="no")
    periods = ssb_12880.periods()
    df_fetcha = ssb_12880.fetch(periods)
    df_fetcha = df_fetcha.reset_index().pivot(
        index="år", columns="statistikkvariabel", values="value"
    )
    assert df_ssb.equals(df_fetcha)
