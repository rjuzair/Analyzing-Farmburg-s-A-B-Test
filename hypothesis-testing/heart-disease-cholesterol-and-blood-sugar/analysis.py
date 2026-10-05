"""Heart disease research - cholesterol and fasting blood sugar.

Data from patients evaluated for heart disease at the Cleveland Clinic
Foundation (UCI Machine Learning Repository).

1. Do patients with / without heart disease have mean cholesterol above
   the 240 mg/dl "high" threshold?
2. Is the share of patients with fasting blood sugar > 120 mg/dl higher than
   the ~8% diabetes prevalence in the 1988 US population?

Data: data/heart_disease.csv
"""
from pathlib import Path

import pandas as pd
from scipy import stats

DATA = Path(__file__).parent / "data" / "heart_disease.csv"
HIGH_CHOLESTEROL = 240
DIABETES_RATE = 0.08
ALPHA = 0.05


def verdict(pval):
    return "significant" if pval < ALPHA else "not significant"


def main():
    heart = pd.read_csv(DATA)

    for label, status in (("with", "presence"), ("without", "absence")):
        chol = heart.chol[heart.heart_disease == status]
        _, pval = stats.ttest_1samp(chol, HIGH_CHOLESTEROL, alternative="greater")
        print(f"Patients {label} heart disease: mean cholesterol {chol.mean():.1f} mg/dl, "
              f"H1 mean > {HIGH_CHOLESTEROL}: p = {pval:.4f} ({verdict(pval)})")

    num_patients = len(heart)
    num_high_fbs = int((heart.fbs == 1).sum())
    expected = num_patients * DIABETES_RATE
    print(f"\nPatients: {num_patients}, fasting blood sugar > 120 mg/dl: {num_high_fbs} "
          f"(expected at 8% prevalence: {expected:.0f})")

    pval = stats.binomtest(num_high_fbs, n=num_patients, p=DIABETES_RATE,
                           alternative="greater").pvalue
    print(f"H1 rate > 8%: p = {pval:.4f} ({verdict(pval)})")


if __name__ == "__main__":
    main()
