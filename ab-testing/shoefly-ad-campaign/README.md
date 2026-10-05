# ShoeFly.com — Ad Campaign & A/B Test

**Question:** Which traffic sources (Google, Facebook, Twitter, email) drive the most ad views and clicks, and which of two ad creatives (A vs B) should ShoeFly run?

## Approach
- Flag clicks from `ad_click_timestamp`, then build click-through-rate tables with `groupby` + pivot.
- Compare CTR by **traffic source**, by **ad variant**, and by **variant × weekday** to spot day-of-week effects.

## Skills
pandas aggregation & pivoting · funnel metrics · A/B test reporting

## Run
```bash
python analysis.py   # expects data/ad_clicks.csv
```
