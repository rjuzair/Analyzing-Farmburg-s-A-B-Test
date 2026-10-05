"""FarmBurg pricing experiment.

Three groups were offered an in-game upgrade at different price points
(A = $0.99, B = $1.99, C = $4.99). The goal is to find which price point
reliably clears a $1,000/week revenue target.

Data: data/clicks.csv with columns user_id, group, is_purchase ('Yes'/'No').
"""
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

DATA = Path(__file__).parent / "data" / "clicks.csv"
WEEKLY_TARGET = 1000
PRICES = {"A": 0.99, "B": 1.99, "C": 4.99}
ALPHA = 0.05


def main():
    abdata = pd.read_csv(DATA)

    # 1. Is purchase rate associated with group? (chi-square test of independence)
    xtab = pd.crosstab(abdata.group, abdata.is_purchase)
    print(xtab, "\n")
    _, pval, _, _ = stats.chi2_contingency(xtab)
    print(f"Chi-square p-value: {pval:.3g} -> "
          f"{'significant' if pval < ALPHA else 'not significant'} difference in purchase rate\n")

    # 2. A higher purchase rate does not mean higher revenue. For each price,
    #    test whether the observed purchase rate beats the rate needed to hit
    #    the weekly revenue target (one-sided binomial test).
    num_visits = len(abdata)
    print(f"Weekly visitors: {num_visits}\n")

    viable = []
    for group, price in PRICES.items():
        sales_needed = np.ceil(WEEKLY_TARGET / price)
        p_needed = sales_needed / num_visits

        in_group = abdata.group == group
        samp_size = int(in_group.sum())
        sales = int((in_group & (abdata.is_purchase == "Yes")).sum())

        result = stats.binomtest(sales, n=samp_size, p=p_needed, alternative="greater")
        print(f"Group {group} (${price}): needs {p_needed:.2%} conversion, "
              f"observed {sales / samp_size:.2%}, p = {result.pvalue:.4f}")
        if result.pvalue < ALPHA:
            viable.append((group, price))

    print()
    if viable:
        best = max(viable, key=lambda gp: gp[1])
        print(f"Price points significantly above break-even: {[g for g, _ in viable]}")
        print(f"Recommendation: charge ${best[1]} (group {best[0]}), the highest viable price")
    else:
        print("No price point is significantly above the break-even conversion rate.")


if __name__ == "__main__":
    main()
