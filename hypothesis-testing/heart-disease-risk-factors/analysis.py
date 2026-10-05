"""Heart disease research - risk factors.

Explores how maximum heart rate (thalach), age and chest-pain type relate to
a heart disease diagnosis using t-tests, ANOVA, Tukey HSD and chi-square tests.

Data: data/heart_disease.csv
"""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd

DATA = Path(__file__).parent / "data" / "heart_disease.csv"
ALPHA = 0.05


def verdict(pval):
    return "significant" if pval < ALPHA else "not significant"


def compare_by_diagnosis(heart, column, title):
    sns.boxplot(data=heart, x="heart_disease", y=column)
    plt.title(title)
    plt.show()

    with_hd = heart[column][heart.heart_disease == "presence"]
    without_hd = heart[column][heart.heart_disease == "absence"]
    _, pval = stats.ttest_ind(with_hd, without_hd)
    print(f"{column}: mean difference {without_hd.mean() - with_hd.mean():.2f}, "
          f"median difference {without_hd.median() - with_hd.median():.2f}, "
          f"p = {pval:.3g} ({verdict(pval)})")


def main():
    heart = pd.read_csv(DATA)
    print(heart.head(), "\n")

    compare_by_diagnosis(heart, "thalach", "Max heart rate and heart disease")
    compare_by_diagnosis(heart, "age", "Age and heart disease")

    # Max heart rate across chest-pain types
    sns.boxplot(data=heart, x="cp", y="thalach")
    plt.title("Max heart rate by chest pain type")
    plt.show()

    groups = [g.thalach for _, g in heart.groupby("cp")]
    _, pval = stats.f_oneway(*groups)
    print(f"\nANOVA thalach ~ chest pain type: p = {pval:.3g} ({verdict(pval)})")
    print(pairwise_tukeyhsd(endog=heart.thalach, groups=heart.cp, alpha=ALPHA))

    # Association between chest-pain type and diagnosis
    xtab = pd.crosstab(heart.cp, heart.heart_disease)
    print(f"\n{xtab}")
    _, pval, _, _ = stats.chi2_contingency(xtab)
    print(f"Chest pain type vs heart disease: p = {pval:.3g} ({verdict(pval)} association)")


if __name__ == "__main__":
    main()
