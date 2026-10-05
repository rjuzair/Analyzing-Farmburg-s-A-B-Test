"""ShoeFly.com - ad campaign funnel and A/B test.

Which traffic source drives the most ad views and clicks, and does Ad A or
Ad B earn a higher click-through rate across the week?

Data: data/ad_clicks.csv with columns user_id, utm_source, day,
ad_click_timestamp, experimental_group.
"""
from pathlib import Path

import pandas as pd

DATA = Path(__file__).parent / "data" / "ad_clicks.csv"


def click_rate(df, by):
    """Return clicks, views and click-through rate (%) grouped by `by`."""
    pivot = (df.groupby([by, "is_click"]).user_id.count()
               .unstack("is_click", fill_value=0))
    pivot["views"] = pivot[True] + pivot[False]
    pivot["percent_clicked"] = pivot[True] / pivot["views"] * 100
    return pivot.rename(columns={True: "clicked", False: "not_clicked"})


def main():
    ad_clicks = pd.read_csv(DATA)
    ad_clicks["is_click"] = ad_clicks.ad_click_timestamp.notnull()

    print("Views by traffic source:")
    print(ad_clicks.groupby("utm_source").user_id.count().sort_values(ascending=False), "\n")

    print("Click-through rate by traffic source:")
    print(click_rate(ad_clicks, "utm_source").round(2), "\n")

    print("Users per experimental group:")
    print(ad_clicks.groupby("experimental_group").user_id.count(), "\n")

    print("Click-through rate by ad:")
    print(click_rate(ad_clicks, "experimental_group").round(2), "\n")

    for group in ("A", "B"):
        print(f"Ad {group} click-through rate by day:")
        print(click_rate(ad_clicks[ad_clicks.experimental_group == group], "day").round(2), "\n")


if __name__ == "__main__":
    main()
