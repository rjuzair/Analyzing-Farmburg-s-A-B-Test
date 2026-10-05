"""Familiar - does a blood-transfusion subscription affect health outcomes?

1. Do Vein Pack subscribers live longer than the average of 73 years?
2. Is there a lifespan difference between Vein Pack and Artery Pack subscribers?
3. Is the subscription pack associated with iron levels?

Data: data/familiar_lifespan.csv (pack, lifespan) and
      data/familiar_iron.csv (pack, iron).
"""
from pathlib import Path

import pandas as pd
from scipy import stats

DATA_DIR = Path(__file__).parent / "data"
ALPHA = 0.05


def verdict(pval):
    return "significant" if pval < ALPHA else "not significant"


def main():
    lifespans = pd.read_csv(DATA_DIR / "familiar_lifespan.csv")
    iron = pd.read_csv(DATA_DIR / "familiar_iron.csv")

    vein = lifespans.lifespan[lifespans.pack == "vein"]
    artery = lifespans.lifespan[lifespans.pack == "artery"]

    # One-sample t-test against the population average of 73 years
    _, pval = stats.ttest_1samp(vein, 73, alternative="greater")
    print(f"Vein Pack mean lifespan: {vein.mean():.2f} years")
    print(f"H1 mean > 73: p = {pval:.4f} ({verdict(pval)})\n")

    # Two-sample t-test between packs
    _, pval = stats.ttest_ind(artery, vein)
    print(f"Artery Pack mean lifespan: {artery.mean():.2f} years")
    print(f"Vein vs Artery: p = {pval:.4f} ({verdict(pval)})\n")

    # Chi-square test of independence: pack vs iron level
    xtab = pd.crosstab(iron.pack, iron.iron)
    print(xtab)
    _, pval, _, _ = stats.chi2_contingency(xtab)
    print(f"Pack vs iron level: p = {pval:.4f} ({verdict(pval)} association)")


if __name__ == "__main__":
    main()
