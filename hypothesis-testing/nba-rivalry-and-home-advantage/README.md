# NBA Trends — Rivalries, Home Advantage & Forecast Accuracy

Data: [FiveThirtyEight NBA Elo](https://github.com/fivethirtyeight/data/tree/master/nba-elo) game records (2010 and 2014 seasons).

| Question | Method |
|---|---|
| Did the Knicks and Nets score differently in 2010 vs 2014? | Mean difference + overlapping histograms |
| How do points per game vary by franchise? | Side-by-side box plots |
| Is winning associated with playing at home? | Contingency table + chi-square test |
| Do pre-game win forecasts track the final point differential? | Pearson correlation + scatter plot |

## Run
```bash
python analysis.py   # expects data/nba_games.csv
```
