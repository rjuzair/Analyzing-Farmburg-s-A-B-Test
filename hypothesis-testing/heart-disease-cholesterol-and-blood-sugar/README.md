# Heart Disease Research I — Cholesterol & Fasting Blood Sugar

Data: patients evaluated for heart disease at the Cleveland Clinic Foundation ([UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/45/heart+disease)).

| Question | Test |
|---|---|
| Is mean cholesterol above the 240 mg/dl "high" threshold for patients **with** heart disease? | One-sample t-test (one-sided) |
| …and for patients **without** heart disease? | One-sample t-test (one-sided) |
| Is the share of patients with fasting blood sugar > 120 mg/dl higher than the ~8% US diabetes prevalence (1988)? | Binomial test (one-sided) |

## Run
```bash
python analysis.py   # expects data/heart_disease.csv
```
See also: [Heart Disease Research II](../heart-disease-risk-factors).
