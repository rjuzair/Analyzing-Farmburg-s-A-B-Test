"""FetchMaker - hypothesis tests on adoptable dog data.

1. Are whippets more or less likely than the 8% average to be rescues?
2. Do whippets, terriers and pitbulls differ in average weight? Which pairs?
3. Do poodles and shih tzus come in different colour distributions?

Data: data/dog_data.csv with columns breed, weight, tail_length, age,
color, is_rescue.
"""
from pathlib import Path

import pandas as pd
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd

DATA = Path(__file__).parent / "data" / "dog_data.csv"
ALPHA = 0.05


def verdict(pval):
    return "significant" if pval < ALPHA else "not significant"


def main():
    dogs = pd.read_csv(DATA)
    print(dogs.head(), "\n")

    # 1. Binomial test: whippet rescue rate vs 8%
    whippet_rescue = dogs.is_rescue[dogs.breed == "whippet"]
    num_rescues = int(whippet_rescue.sum())
    num_whippets = len(whippet_rescue)
    pval = stats.binomtest(num_rescues, num_whippets, 0.08).pvalue
    print(f"Whippet rescues: {num_rescues}/{num_whippets} "
          f"({num_rescues / num_whippets:.1%}) vs 8%: p = {pval:.4f} ({verdict(pval)})\n")

    # 2. ANOVA + Tukey HSD on mid-sized breed weights
    dogs_wtp = dogs[dogs.breed.isin(["whippet", "terrier", "pitbull"])]
    weights = [dogs_wtp.weight[dogs_wtp.breed == b] for b in ("whippet", "terrier", "pitbull")]
    _, pval = stats.f_oneway(*weights)
    print(f"ANOVA (whippet, terrier, pitbull weights): p = {pval:.3g} ({verdict(pval)})")
    print(pairwise_tukeyhsd(dogs_wtp.weight, dogs_wtp.breed, alpha=ALPHA), "\n")

    # 3. Chi-square: colour vs breed for poodles and shih tzus
    dogs_ps = dogs[dogs.breed.isin(["poodle", "shihtzu"])]
    xtab = pd.crosstab(dogs_ps.color, dogs_ps.breed)
    print(xtab)
    _, pval, _, _ = stats.chi2_contingency(xtab)
    print(f"Colour vs breed: p = {pval:.4f} ({verdict(pval)} association)")


if __name__ == "__main__":
    main()
