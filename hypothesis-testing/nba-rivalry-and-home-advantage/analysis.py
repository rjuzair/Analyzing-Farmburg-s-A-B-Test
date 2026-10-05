"""NBA trends - Knicks vs Nets and home-court advantage.

1. Did the Knicks and Nets score differently in 2010 vs 2014?
2. How do points scored vary by franchise?
3. Is game result associated with home/away location?
4. Do FiveThirtyEight's pre-game win forecasts correlate with point differential?

Data: data/nba_games.csv (FiveThirtyEight NBA Elo data, subset)
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.stats import chi2_contingency, pearsonr

DATA = Path(__file__).parent / "data" / "nba_games.csv"


def compare_knicks_nets(season, year):
    knicks = season.pts[season.fran_id == "Knicks"]
    nets = season.pts[season.fran_id == "Nets"]
    print(f"{year}: Knicks - Nets mean points = {knicks.mean() - nets.mean():.2f}")

    plt.hist(knicks, alpha=0.7, density=True, label="Knicks")
    plt.hist(nets, alpha=0.7, density=True, label="Nets")
    plt.title(f"Points per game, {year}")
    plt.xlabel("Points")
    plt.legend()
    plt.show()


def main():
    np.set_printoptions(suppress=True, precision=2)
    nba = pd.read_csv(DATA)
    nba_2010 = nba[nba.year_id == 2010]
    nba_2014 = nba[nba.year_id == 2014]

    compare_knicks_nets(nba_2010, 2010)
    compare_knicks_nets(nba_2014, 2014)

    sns.boxplot(data=nba_2010, x="fran_id", y="pts")
    plt.title("Points per game by franchise, 2010")
    plt.show()

    location_results = pd.crosstab(nba_2010.game_result, nba_2010.game_location)
    print("\nGame result by location (% of games):")
    print((location_results / len(nba_2010) * 100).round(1))
    chi2, pval, _, _ = chi2_contingency(location_results)
    print(f"Chi-square = {chi2:.2f}, p = {pval:.3g}")

    r, pval = pearsonr(nba_2010.forecast, nba_2010.point_diff)
    print(f"\nForecast vs point differential: r = {r:.2f}, p = {pval:.3g}")

    plt.scatter(nba_2010.forecast, nba_2010.point_diff, alpha=0.5)
    plt.title("Win forecast vs point differential, 2010")
    plt.xlabel("Forecast win probability")
    plt.ylabel("Point differential")
    plt.show()


if __name__ == "__main__":
    main()
